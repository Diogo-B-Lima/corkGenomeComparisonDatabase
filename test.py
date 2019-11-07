from neo4jPythonDriver import neo4jPythonDriver
import credentials


def test1():

    driver = neo4jPythonDriver(credentials.URI, credentials.USER_NAME, credentials.PASSWORD)
    session = driver.initSession()

    allNodes = session.run("match (s:Sequence) WHERE s.Sequence STARTS WITH({seq}) return s", {"seq":"MRVN"})
    session.close()

    for node in allNodes:
        print(node["s"]["Sequence"])








if __name__ == "__main__":

    test1()