from copy import deepcopy
from datetime import datetime



class nodeEntityFactory:

    def __init__(self):

        self.__nodeEntities = []


    def createNodeAndProperties(self, nodeLabel, nodePropertiesDictionary, session):

        if "Timestamp" not in nodePropertiesDictionary:
            nodePropertiesDictionary["Timestamp"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        auxDict = deepcopy(nodePropertiesDictionary)
        del auxDict["Timestamp"]
        queryProperties = "{"
        if(nodeLabel and len(nodePropertiesDictionary)>0):

            for dictKey in auxDict:
                queryProperties += dictKey + ":" + "'" + str(auxDict[dictKey]) + "'" + ","

            if("," in queryProperties):
                queryProperties = queryProperties[:-1] + "}"
            else:
                queryProperties = queryProperties+"}"

            timestamp = nodePropertiesDictionary["Timestamp"]

            query = "MERGE (x:" +nodeLabel+ queryProperties+") ON CREATE SET x.Timestamp = " + "'" + timestamp + "' RETURN ID(x)"
            res = session.run(query, nodePropertiesDictionary)
            for i in res:
                return i[0]


        else:
            raise Exception("node label or node properties dictionary might be empty")


    def getNodeEntities(self):

        return self.__nodeEntities






