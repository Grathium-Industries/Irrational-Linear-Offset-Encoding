from util.func import writeDecoding, readFile
from components.estimator import randomString

def convertFromAscii(code: str) -> list[int]:
        print(code)
        code = str(code).replace(".", "")[1:]
        code = code[:code.index("e+")]

        n = 3
        value = [code[index : index + n] for index in range(0, len(code), n)]

        returnValue = list(map(int, value))

        print(returnValue)
        return returnValue

def deStructAsciiCode(code: list[int]) -> str:
        result = ""

        for ele in code:
                result += chr(ele)
        
        return result

def decode(fileName: str) -> None:
        fileNameOut = fileName.replace(".ILOE", "")
        decodedFile = "Error Decoding ILOE file"

        fileContents = readFile(fileName)
        nonce = int(fileContents.split(":")[0])
        scalar = float(fileContents.split(":")[1])

        BE = randomString(nonce)
        decodedAscii = BE * scalar

        splitAscii = convertFromAscii(decodedAscii)
        decodedFile = deStructAsciiCode(splitAscii)

        print(decodedFile)
        # writeDecoding(fileNameOut, decodedFile)
