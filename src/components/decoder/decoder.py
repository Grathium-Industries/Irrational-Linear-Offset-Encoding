from util.func import writeDecoding, readFile
from components.estimator import randomString

def decode(fileName: str) -> None:
        fileNameOut = fileName.replace(".ILOE", "")
        decodedFile = "Error Decoding ILOE file"

        fileContents = readFile(fileName)
        nonce = int(fileContents.split(":")[0])
        scalar = float(fileContents.split(":")[1])

        BE = randomString(nonce)
        decodedDecimal = BE * scalar
        print(decodedDecimal)

        writeDecoding(fileNameOut, str(decodedDecimal))
