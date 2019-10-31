from neo4jPythonDriver import neo4jPythonDriver
import credentials


def test1():

    driver = neo4jPythonDriver(credentials.URI, credentials.USER_NAME, credentials.PASSWORD)
    session = driver.getSession()

    allNodes = session.runNeo4jSession("match (n) WHERE n.age = {age} return n", {"age":24})
    session.closeNeo4jSession()

    for node in allNodes:
        print(node)








if __name__ == "__main__":

    test1()