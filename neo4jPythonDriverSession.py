
class neo4jPythonDriverSession:

    ###### CONSTRUCTOR ######


    def __init__(self, driver):

        self.__driver = driver
        self.__session = driver.session()



    def runNeo4jSession(self, query, attributesDictionary = ""):

        return self.__session.run(query, attributesDictionary)


    def closeNeo4jSession(self):

        self.__session.close()


    def __getSession(self):

        return self.__session


    def __getDriver(self):

        return self.__driver


    def __setSession(self, session):

        self.__session = session


    def __setDriver(self, driver):

        self.__driver = driver


