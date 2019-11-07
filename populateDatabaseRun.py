from populateDatabase import populateDatabase
import credentials as crd


DATA_DIRECTORY = "../../bigBlast/big-blast-results/genome-comparison-refseq-vs-genbank/"
NEW_GENOME_GCF = DATA_DIRECTORY + "GCF_002906115.1_CorkOak1.0_protein.faa"
OLD_GENOME_GCA = DATA_DIRECTORY + "GCA_002906115.1_CorkOak1.0_protein.faa"
OLD_GENOME_GCA_CSV = "../../bigBlast/big-blast-parser-python/GCA_002906115.1_CorkOak1.0_protein.csv"
NEW_GENOME_GCF_CSV = "../../bigBlast/big-blast-parser-python/GCF_002906115.1_CorkOak1.0_protein.csv"
MATCHED_GENES = "../data/MatchedGeneID.csv"




if __name__ == "__main__":

    pop = populateDatabase()
    # pop.loadFaaGenomeToDatabase(NEW_GENOME_GCF)
    # pop.moveFiletoNeo4jDockerImport(OLD_GENOME_GCA_CSV, crd.WCRED_NAME, "22", "root", crd.WCRED, "a826ed4ee5aa")
    # pop.MergeFaaGenomeFromCSV(OLD_GENOME_GCA_CSV.split("/")[-1], "58331")
    #
    # pop.moveFiletoNeo4jDockerImport(NEW_GENOME_GCF_CSV, crd.WCRED_NAME, "22", "root", crd.WCRED, "a826ed4ee5aa")
    # pop.MergeFaaGenomeFromCSV(NEW_GENOME_GCF_CSV.split("/")[-1], "58331")
    #
    # pop.moveFiletoNeo4jDockerImport(MATCHED_GENES, crd.WCRED_NAME, "22", "root", crd.WCRED, "069cc9149f83")
    # pop.ConnectGenesWithSameSequenceFromCSV(MATCHED_GENES.split("/")[-1])
    # pop.SetGenesWithSameSequenceAndSameGenome()


