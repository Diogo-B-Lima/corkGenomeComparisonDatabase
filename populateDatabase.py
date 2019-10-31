import sys

FAA_PARSER_RELATIVE_PATH = "../../bigBlast/big-blast-parser-python"
sys.path.append(sys.path.join(sys.path[0], FAA_PARSER_RELATIVE_PATH))

from FaaParser import FaaParser
print(sys.path)






class populateDatabase:

    def __init__(self):

        self.__faaParsedContents = {}

