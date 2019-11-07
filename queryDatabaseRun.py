from queryDatabase import queryDatabase
import utilities


OUTPUT_DIRECTORY = "../data/"








if __name__ == "__main__":

    query = queryDatabase()
    #results = query.getSetofNodeWithMultipleRelationships_Generic("GeneIdentifier", "Sequence", "GENE_IDENTIFIER_HAS_SEQUENCE", 1)
    #header = ["SequenceID", "GeneIdentifierID"]
    #utilities.JSON2CSV(results, header, OUTPUT_DIRECTORY + "sequencesAndAssociatedGeneIdentifiers.csv")

    #utilities.JSON2CSV_VALUES_ONLY(results, ["ID1", "ID2"], OUTPUT_DIRECTORY + "MatchedGeneID.csv")


    #output = OUTPUT_DIRECTORY + "sequencesAndAssociatedGeneIdentifiers.json"
    #query.getSetofNodeWithMultipleRelationships_Genome("GeneIdentifier", "Sequence", "GENE_IDENTIFIER_HAS_SEQUENCE", 0, output)
    #oldGenomeRepeatedSequences = OUTPUT_DIRECTORY + "sequencesWithAssociatedGenesOldGenome.json"
    #newGenomeRepeatedSequences = OUTPUT_DIRECTORY + "sequencesWithAssociatedGenesNewGenome.json"

    #query.getSetofNodeWithMultipleRelationships_SpecificGenome("GeneIdentifier", "Sequence", "GENE_IDENTIFIER_HAS_SEQUENCE", 1, oldGenomeRepeatedSequences, "GCF_002906115.1_CorkOak1.0_protein")
    #query.getSetofNodeWithMultipleRelationships_SpecificGenome("GeneIdentifier", "Sequence", "GENE_IDENTIFIER_HAS_SEQUENCE", 1, newGenomeRepeatedSequences, "GCA_002906115.1_CorkOak1.0_protein")

    #query.printGenesWithSharedSequenceStatistics()
    query.getMatchedGenesAcrossGenomesBySequence(OUTPUT_DIRECTORY + "matchedGenesAcrossOldAndNewGenomeBySequence.csv")