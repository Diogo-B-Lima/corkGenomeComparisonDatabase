import pandas as pd



def JSON2CSV(jsonContent, header, outputDirectory):

    # keys must be convertable to Strings and values must be an Array of objects convertable to Strings

    data = []

    for key in jsonContent:
        rows = []
        for listItem in jsonContent[key]:
            rows.append([key, listItem])
        data += rows

    dataframe = pd.DataFrame(data = data, columns = header)


    if not outputDirectory.endswith(".csv"):
        outputDirectory += ".csv"

    dataframe.to_csv(outputDirectory, index = False)



def JSON2CSV_VALUES_ONLY(jsonContent, header, outputDirectory):

    # keys must be convertable to Strings and values must be an Array of objects convertable to Strings

    data = []

    for key in jsonContent:
        for listItemIndex in range(len(jsonContent[key])):

            listSize = len(jsonContent[key])
            rows = []
            if listItemIndex != listSize -1 :
                for comparedListItemIndex in range(listItemIndex +1, listSize):
                    item = jsonContent[key][listItemIndex]
                    comparedItem = jsonContent[key][comparedListItemIndex]
                    rows.append([item, comparedItem])
            data += rows


    dataframe = pd.DataFrame(data = data, columns = header)


    if not outputDirectory.endswith(".csv"):
        outputDirectory += ".csv"

    dataframe.to_csv(outputDirectory, index = False)
