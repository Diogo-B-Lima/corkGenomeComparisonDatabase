from neo4jPythonDriver import neo4jPythonDriver
import credentials as crd
import json
import pandas as pd


class queryDatabase:


    def __init__(self):

        self.__query = ""



    def getSetofNodeWithMultipleRelationships_Generic(self, originNodeLabel, destinationNodeLabel, relationshipLabel, size):

        driver = neo4jPythonDriver(crd.URI, crd.USER_NAME, crd.PASSWORD)
        session = driver.initSession()

        query = "MATCH (x:" + originNodeLabel+")-[oldRel:"+relationshipLabel+"]->(y:"+destinationNodeLabel+") " \
                "WITH size((y)<--()) as cnt, y as yy, x as xx " \
                "WHERE cnt>toInt("+str(size)+") " \
                "return ID(yy), collect(ID(xx))"

        result = session.run(query)
        session.close()

        output = {}
        for r in result:
            destinationNodeID = r[0]
            originNodeIDs = r[1]
            output[destinationNodeID] = originNodeIDs

        return output



    def getSetofNodeWithMultipleRelationships_Genome(self, originNodeLabel, destinationNodeLabel, relationshipLabel, size, outputDirectory):

        driver = neo4jPythonDriver(crd.URI, crd.USER_NAME, crd.PASSWORD)
        session = driver.initSession()

        query = "MATCH (x:" + originNodeLabel+")-[oldRel:"+relationshipLabel+"]->(y:"+destinationNodeLabel+") " \
                "WITH size((y)<--()) as cnt, y as yy, x as xx " \
                "WHERE cnt>toInt("+str(size)+") " \
                "return yy.Sequence, collect(xx.Identifier)"

        result = session.run(query)
        session.close()

        output = {}
        for r in result:
            destinationNodeID = r[0]
            originNodeIDs = r[1]
            output[destinationNodeID] = originNodeIDs

        if not outputDirectory.endswith(".json"):
            outputDirectory += ".json"

        with open(outputDirectory, "w") as file:
            json.dump(output, file)





    def getSetofNodeWithMultipleRelationships_SpecificGenome(self, originNodeLabel, destinationNodeLabel, relationshipLabel, size, outputDirectory, genomeVersion):

        driver = neo4jPythonDriver(crd.URI, crd.USER_NAME, crd.PASSWORD)
        session = driver.initSession()

        query = "MATCH (v:GenomeVersion)<-[]-(x:" + originNodeLabel+")-[oldRel:"+relationshipLabel+"]->(y:"+destinationNodeLabel+")-[]->(v)" \
                "WITH size((y)<--()) as cnt, y as yy, x as xx, v as vv " \
                "WHERE vv.Version='"+genomeVersion+"' AND cnt>toInt("+str(size)+") " \
                "return yy.Sequence, collect(xx.Identifier)"

        result = session.run(query)
        session.close()

        output = {}
        for r in result:
            destinationNodeID = r[0]
            originNodeIDs = r[1]
            output[destinationNodeID] = originNodeIDs

        if not outputDirectory.endswith(".json"):
            outputDirectory += ".json"

        with open(outputDirectory, "w") as file:
            json.dump(output, file)


    def printGenesWithSharedSequenceStatistics(self):

        driver = neo4jPythonDriver(crd.URI, crd.USER_NAME, crd.PASSWORD)
        session = driver.initSession()

        query1 = "match (v1:GenomeVersion)<-[:GENE_IDENTIFIER_IN_GENOME_VERSION]-(g1:GeneIdentifier)-[rel:GENES_SHARE_SEQUENCE]->() where rel.SameGenome = False and v1.Version = 'GCF_002906115.1_CorkOak1.0_protein' return count(distinct(g1))"
        query2 = "match (v1:GenomeVersion)<-[:GENE_IDENTIFIER_IN_GENOME_VERSION]-(g1:GeneIdentifier)-[rel:GENES_SHARE_SEQUENCE]->() where rel.SameGenome = True and v1.Version = 'GCF_002906115.1_CorkOak1.0_protein' return count(distinct(g1))"
        query3 = "match (v1:GenomeVersion)<-[:GENE_IDENTIFIER_IN_GENOME_VERSION]-(g1:GeneIdentifier)-[rel:GENES_SHARE_SEQUENCE]->() where rel.SameGenome = False and v1.Version = 'GCA_002906115.1_CorkOak1.0_protein' return count(distinct(g1))"
        query4 = "match (v1:GenomeVersion)<-[:GENE_IDENTIFIER_IN_GENOME_VERSION]-(g1:GeneIdentifier)-[rel:GENES_SHARE_SEQUENCE]->() where rel.SameGenome = True and v1.Version = 'GCA_002906115.1_CorkOak1.0_protein' return count(distinct(g1))"

        print("Number of genes in the new genome which match (same sequence) the old genome", [res[0] for res in session.run(query1)])
        print("Number of genes in the new genome which share the same sequence", [res[0] for res in session.run(query2)])
        print("Number of genes in the old genome which match (same sequence) the new genome", [res[0] for res in session.run(query3)])
        print("Number of genes in the old genome which share the same sequence", [res[0] for res in session.run(query4)])

        session.close()


    def getMatchedGenesAcrossGenomesBySequence(self, outputFileName):

        driver = neo4jPythonDriver(crd.URI, crd.USER_NAME, crd.PASSWORD)
        session = driver.initSession()

        query = "match (g1:GeneIdentifier)-[rel:GENES_SHARE_SEQUENCE]->(g2:GeneIdentifier) where rel.SameGenome = false return distinct(g1.Identifier),g2.Identifier"


        results = session.run(query)
        session.close()

        data = []

        for r in results:

            data.append([r[0], r[1]])

        dataframe = pd.DataFrame(data = data, columns = ["Identifier1", "Identifier2"])

        if not outputFileName.endswith(".csv"):
            outputFileName += ".csv"

        dataframe.to_csv(outputFileName, index = False)








