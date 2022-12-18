from util.constants import HELP_TEXT

def closeProgram() -> None:
        exit()

def throwError(errorMessage: str) -> None:
        print("Application Error...")
        print(errorMessage)
        closeProgram()

def readFile(fileName: str) -> str:
        fp = open(fileName, "r")
        return fp.readlines()[0]

def writeToFile(fileName: str, fileContents: str) -> None:
        with open(fileName, "w") as file:
                file.write(fileContents)
                file.close()

def printHelp() -> None:
        print()
        print(HELP_TEXT)

def isWholeNumber(num: int) -> bool:
        return "." in str(num)

def writeEncoding(fileName: str, nonce: int, scalar: int) -> None:
        encodedFile = getEncoding(nonce, scalar)
        writeToFile(fileName, encodedFile)

def getEncoding(nonce: int, scalar: int) -> str:
        return f"{nonce}:{scalar}"

def writeDecoding(fileName: str, fileContents: str) -> None:
        writeToFile(fileName, fileContents)
