from util.constants import NONCE_LIMIT
from util.func import readFile, writeEncoding, getEncoding
from components.estimator import randomString, hasIrrationalSquareRoot

def encode(fileName: str) -> None:
        # file contents
        FC = readFile(fileName)
        decimalFC = int("".join([hex(ord(x))[2:] for x in FC]), 16)

        # encode file
        lcd = 1
        nonce = 1

        for i in range(1, NONCE_LIMIT):
                BE = randomString(i)

                scalar = decimalFC / BE

                if (len(str(scalar)) < len(str(lcd)) or lcd == 1) and scalar > 1:
                        lcd = scalar
                        nonce = i

                        print(getEncoding(nonce, lcd))
        
        # end of program, the encoding is found
        encodedFileName = fileName + ".ILOE"

        print(f"Encoded File for: {decimalFC}")        
        writeEncoding(encodedFileName, nonce, lcd)
        print(getEncoding(nonce, lcd))
