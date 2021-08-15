
import os

class TokenLoader:
    
    def __init__(self):
        self.TOKEN_FILE_NAME = "/res/token.txt"

    def getToken(self):

        currentPath = os.getcwd()
        filePath = currentPath + self.TOKEN_FILE_NAME

        file = open(filePath, 'r')
        token = str(file.readline())
        
        file.close()

        return token