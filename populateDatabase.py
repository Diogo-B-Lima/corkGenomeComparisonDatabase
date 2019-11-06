import sys, os
FAA_PARSER_RELATIVE_PATH = "../../bigBlast/big-blast-parser-python"
sys.path.append(os.path.join(sys.path[0], FAA_PARSER_RELATIVE_PATH))
from FaaParser import FaaParser
from nodeEntityFactory import nodeEntityFactory
from edgeRelationshipFactory import edgeRelationshipFactory
from datetime import datetime
from neo4jPythonDriver import neo4jPythonDriver
import credentials as crd
from tqdm import tqdm
import scpManager




class populateDatabase:


    def __init__(self):

        self.__faaFile = ""


    def loadFaaGenomeToDatabase(self, faaFile):

        self.__faaFile = faaFile
        faaParser = FaaParser()
        faaParser.readFaa(self.__faaFile)
        nod = nodeEntityFactory()
        edg = edgeRelationshipFactory()
        driver = neo4jPythonDriver(crd.URI, crd.USER_NAME, crd.PASSWORD)

        session = driver.initSession()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        genomeVersionNodeProperties = {"GenomeVersion":self.__faaFile.split("/")[-1].replace("faa",""), "OrganismTaxonomyID":"58331", "Timestamp":timestamp}
        genomeVersionID = nod.createNodeAndProperties("GenomeVersion", genomeVersionNodeProperties, session)

        faaContents = faaParser.getFaaContents()

        for geneIdentifier in tqdm(faaContents):

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            geneIdentifierNodeProperties = {"GeneIdentifier":geneIdentifier, "Timestamp":timestamp}
            geneIdentifierID = nod.createNodeAndProperties("GeneIdentifier", geneIdentifierNodeProperties, session)

            productNodeProperties = {"Product": faaContents[geneIdentifier]["Product"].replace("'", ""), "Timestamp":timestamp}
            sequenceNodeProperties = {"Sequence": faaContents[geneIdentifier]["Sequence"], "Timestamp":timestamp}

            productID = nod.createNodeAndProperties("Product", productNodeProperties, session)
            sequenceID = nod.createNodeAndProperties("Sequence", sequenceNodeProperties, session)

            edg.createEdgeAndProperties("GENE_IDENTIFIER_IN_GENOME_VERSION", {"Timestamp":timestamp}, geneIdentifierID, genomeVersionID, session)
            edg.createEdgeAndProperties("PRODUCT_IN_GENOME_VERSION", {"Timestamp":timestamp}, productID, genomeVersionID, session)
            edg.createEdgeAndProperties("SEQUENCE_IN_GENOME_VERSION", {"Timestamp":timestamp}, sequenceID, genomeVersionID, session)

            edg.createEdgeAndProperties("GENE_IDENTIFIER_HAS_PRODUCT", {"Timestamp":timestamp}, geneIdentifierID, productID, session)
            edg.createEdgeAndProperties("GENE_IDENTIFIER_HAS_SEQUENCE", {"Timestamp":timestamp}, geneIdentifierID, sequenceID, session)


        session.close()



    def moveFiletoNeo4jDockerImport(self, file, host, port, serverUserName, serverPassword, dockerContainerID):

        fileName = file.split("/")[-1]
        destination = "/home/dlima/cork_2019/files"
        ssh = scpManager.createSSHClient(host, port, serverUserName, serverPassword)
        self.moveFileToRemoteServer(ssh, file, destination)
        command = "docker cp " + destination + "/" + fileName + " " + dockerContainerID + ":/var/lib/neo4j/import/" + fileName
        ssh.exec_command(command)
        ssh.close()



    def moveFileToRemoteServer(self, sshClient, file, destination):

        try:

            scp = scpManager.SCPClient(sshClient.get_transport())
            scp.put(file, destination)
            print("File moved successfully to " + destination)

        except Exception as e:
            print(e)


    def batchMergeFaaGenomeFromCSV(self, faaGenomeCsvFileName, organismTaxonomyID, ):

        # THE CSV FILE MUST BE IN THE neo4j/import directory of the docker in the server

        driver = neo4jPythonDriver(crd.URI, crd.USER_NAME, crd.PASSWORD)
        session = driver.initSession()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        constraints =  ["CREATE CONSTRAINT ON (gv:GenomeVersion) ASSERT gv.Version IS UNIQUE " ,
                       "CREATE CONSTRAINT ON (giden:GeneIdentifier) ASSERT giden.Identifier IS UNIQUE " ,
                       "CREATE CONSTRAINT ON (produc:Product) ASSERT produc.Description IS UNIQUE "]

        query = "USING PERIODIC COMMIT 5000 " \
                "LOAD CSV WITH HEADERS FROM 'file:///" + faaGenomeCsvFileName +"' " \
                "AS row WITH row, {timestamp} as time " \
                "MERGE (g:GenomeVersion {Version:{version}, OrganismTaxonomyID:{taxid}}) " \
                "ON CREATE SET g.Timestamp = time " \
                "MERGE (gid:GeneIdentifier {Identifier:row.GeneIdentifier}) " \
                "ON CREATE SET gid.Timestamp = time " \
                "MERGE (prod:Product {Description:row.Product}) " \
                "ON CREATE SET prod.Timestamp = time " \
                "MERGE (seq:Sequence {Sequence:row.Sequence, SequenceType:'Protein'}) " \
                "ON CREATE SET seq.Timestamp = time " \
                "MERGE (gid)-[:GENE_IDENTIFIER_IN_GENOME_VERSION]->(g) " \
                "MERGE (prod)-[:PRODUCT_IN_GENOME_VERSION]->(g) " \
                "MERGE (seq)-[:SEQUENCE_IN_GENOME_VERSION]->(g) " \
                "MERGE (prod)-[:GENE_IDENTIFIER_HAS_PRODUCT]->(gid) " \
                "MERGE (seq)-[:GENE_IDENTIFIER_HAS_SEQUENCE]->(gid) "


        queryProperties = {"version":faaGenomeCsvFileName.replace(".csv",""), "taxid":str(organismTaxonomyID), "timestamp":timestamp}

        for c in constraints:
            session.run(c, {})

        session.run(query, queryProperties)

        # the query auto commits, it is not necessary to close the session








