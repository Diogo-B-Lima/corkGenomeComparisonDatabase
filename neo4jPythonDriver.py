from neo4j.v1 import GraphDatabase
from neo4jPythonDriverSession import neo4jPythonDriverSession


class neo4jPythonDriver:

    ###### CONSTRUCTOR ######

    def __init__(self, uri, user, password):

        self.__uri = uri
        self.__user = user
        self.__password = password
        self.__driver = self.__initDriver()
        self.__session = neo4jPythonDriverSession(self.__driver)


    def __initDriver(self):

        return GraphDatabase.driver(self.__getUri(), auth=(self.__getUser(), self.__getPassword()))


    def __getUri(self):

        return self.__uri


    def __getUser(self):

        return self.__user


    def __getPassword(self):

        return self.__password


    def __getDriver(self):

        return self.__driver

    def getSession(self):

        return self.__session


    def __setUri(self, value):

        self.__uri = value


    def __setUser(self, value):

        self.__user = value


    def __setPassword(self, value):

        self.__password = value


    def __setDriver(self, value):

        self.__driver = value


    def __setSession(self, session):

        self.__session = session





