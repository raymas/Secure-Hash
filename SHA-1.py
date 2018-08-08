#
#
#
#
#
#
import multiprocessing


class SHA1(object):
    """Python implementation of SHA-1 hashing algorithm"""

    # useful sizes in bits
    messageSize = pow(2, 64)
    blockSize = 512
    wordSize = 32

    #    0 < t < 19  20 < t < 39 40 < t < 59 60 < t < 79
    K = [0x5a827999, 0x6ed9eba1, 0x8f1bbcdc, 0xca62c1d6]

    def __init__(self):
        """Constructor for SHA-1"""
        return super(SHA1, self).__init__()

    def addPadding(buffer):
        pass

    @staticmethod
    def leftShift(bites):
        pass

    @staticmethod
    def rightShift(bites):
        pass
