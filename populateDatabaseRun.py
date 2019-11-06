from populateDatabase import populateDatabase
import credentials as crd

DATA_DIRECTORY = "../../bigBlast/big-blast-results/genome-comparison-refseq-vs-genbank/"
OLD_GENOME_GCF = DATA_DIRECTORY + "GCF_002906115.1_CorkOak1.0_protein.faa"
NEW_GENOME_GCA = DATA_DIRECTORY + "GCA_002906115.1_CorkOak1.0_protein.faa"
NEW_GENOME_GCA_CSV = "../../bigBlast/big-blast-parser-python/GCA_002906115.1_CorkOak1.0_protein.csv"
OLD_GENOME_GCF_CSV = "../../bigBlast/big-blast-parser-python/GCF_002906115.1_CorkOak1.0_protein.csv"




if __name__ == "__main__":

    pop = populateDatabase()
    #pop.loadFaaGenomeToDatabase(OLD_GENOME_GCF)
    #pop.moveFiletoNeo4jDockerImport(NEW_GENOME_GCA_CSV, crd.WCRED_NAME, "22", "root", crd.WCRED, "65e0f6255235")
    #pop.batchMergeFaaGenomeFromCSV(NEW_GENOME_GCA_CSV.split("/")[-1], "58331")

    #pop.moveFiletoNeo4jDockerImport(OLD_GENOME_GCF_CSV, crd.WCRED_NAME, "22", "root", crd.WCRED, "65e0f6255235")
    #pop.batchMergeFaaGenomeFromCSV(OLD_GENOME_GCF_CSV.split("/")[-1], "58331")
