from util.func import throwError, printHelp
from components.encoder.encoder import encode
from components.decoder.decoder import decode

import sys

encoding = False

if __name__ == "__main__":
        encoding = False
        fileName = ""

        if len(sys.argv) < 2:
                throwError("Expected Argument 1 to be file name")
                printHelp()

        fileName = sys.argv[1]

        if len(sys.argv) >= 3:
                actionArgument = sys.argv[2]
                if actionArgument == "encode" or actionArgument == "e":
                                encoding = True

        # program entry point for encoding / decoding
        encode(fileName) if encoding else decode(fileName)
