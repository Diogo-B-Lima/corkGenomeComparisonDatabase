from copy import deepcopy
from datetime import datetime


class edgeRelationshipFactory:

    def __init__(self):

        self.__faaParsedContents = {}


    def createEdgeAndProperties(self, edgeLabel, edgePropertiesDictionary, originNodeID, destinationNodeID, session):

        if "Timestamp" not in edgePropertiesDictionary:
            edgePropertiesDictionary["Timestamp"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        auxDict = deepcopy(edgePropertiesDictionary)
        del auxDict["Timestamp"]
        queryProperties = "{"
        if(edgeLabel and len(edgePropertiesDictionary)>0):

            for dictKey in auxDict:
                queryProperties += dictKey + ":" + "'" + str(auxDict[dictKey]) + "'" + ","

            if("," in queryProperties):
                queryProperties = queryProperties[:-1] + "}"
            else:
                queryProperties = queryProperties+"}"

            timestamp = edgePropertiesDictionary["Timestamp"]

            query = "MATCH (x),(y) where ID(x) = " + str(originNodeID) + " and ID(y) = " + str(destinationNodeID) + \
                    " MERGE (x)-[z:" +edgeLabel+ queryProperties+"]->(y) ON CREATE SET z.Timestamp = " + "'" + timestamp + "' RETURN ID(z)"
            session.run(query, edgePropertiesDictionary)

        else:
            raise Exception("node label or node properties dictionary might be empty")



    def getFaaParsedContents(self):

        return self.__faaParsedContents