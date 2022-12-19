from util.constants import NONCE_LIMIT
from util.func import readFile, writeEncoding, getEncoding
from components.estimator import randomString, hasIrrationalSquareRoot

def convertToAscii(text: str) -> int:
        res = []
        for ele in text:
                res.append(ord(ele))
        
        asciiCode = "1" + "".join(str(x if len(str(x)) == 3 else f"0{x}") for x in res)
        return int(asciiCode)

def encode(fileName: str) -> None:
        # file contents
        FC = readFile(fileName)
        asciiFC = convertToAscii(FC)

        # encode file
        lcd = 1
        nonce = 1

        for i in range(1, NONCE_LIMIT):
                BE = randomString(i)

                scalar = asciiFC / BE

                if (len(str(scalar)) < len(str(lcd)) or lcd == 1) and scalar > 1:
                        lcd = scalar
                        nonce = i

                        print(getEncoding(nonce, lcd))
        
        # end of program, the encoding is found
        encodedFileName = fileName + ".ILOE"

        print(f"Encoded File for: {asciiFC}")
        writeEncoding(encodedFileName, nonce, lcd)
        print(getEncoding(nonce, lcd))
