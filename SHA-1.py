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
    maxMessageSize = pow(2, 64)
    blockSize = 512
    wordSize = 32

    #    0 < t < 19  20 < t < 39 40 < t < 59 60 < t < 79
    K = [0x5a827999, 0x6ed9eba1, 0x8f1bbcdc, 0xca62c1d6]
    # default hash value
    H = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]

    def __init__(self):
        """Constructor for SHA-1"""
        return super(SHA1, self).__init__()

    def parseBuffer(self, buffer):
        """preparing buffer for cuts"""
        listOfBytes = []
        if isinstance(buffer, basestring):
            for i in range(0, len(buffer), 2):
                listOfBytes.append(int(str(buffer[i] + buffer[i+1]), 16))
        elif isinstance(buffer, list):
            listOfBytes = buffer

        # add padding
        print(len(listOfBytes))
        listOfBytes = self.addPadding(listOfBytes)

        # parsed is a list of 32 bits block
        parsed = []
        for i in range(0, len(listOfBytes), SHA1.blockSize / 8):
            word = []
            for j in range(i, (i + SHA1.wordSize), 1):
                word.append(listOfBytes[j])
            parsed.append(word)

        return parsed

    def preprocessing(self, buffer):
        pass

    def addPadding(self, buffer):
        """Ending a 512 bits block"""
        # padding must not change SHA1
        # so we must find the solution to this equation
        # adding a binary 1
        # solve k = 448 - (size(buffer) + 1)
        # add k 0
        # add the size of message
        if (len(buffer) % 512 != 0):
            buffer.append(1)

        return buffer

    @staticmethod
    def leftShift(bites):
        pass

    @staticmethod
    def rightShift(bites):
        pass


def main():
    s = """4d6975736f762c2061732061206d616e206d616e206f66206272656564696e6720616e64206465696c636163792c20636f756c64206e6f7420627574206665656c20736f6d6520696e777264207175616c6d732c207768656e20686520726561636865642074686520466174686572205375706572696f7227732077697468204976616e3a2068652066656c7420617368616d6564206f6620686176696e206c6f7374206869732074656d7065722e2048652066656c742074686174206865206f7567687420746f2068617665206469736461696d656420746861742064657370696361626c65207772657463682c2046796f646f72205061766c6f76697463682c20746f6f206d75636820746f2068617665206265656e2075707365742062792068696d20696e20466174686572205a6f7373696d6127732063656c6c2c20616e6420736f20746f206861766520666f72676f7474656e2068696d73656c662e20546568206d6f6e6b732077657265206e6f7420746f20626c616d652c20696e20616e7920636173652c206865207265666c63657465642c206f6e207468652073746570732e20416e64206966207468657927726520646563656e742070656f706c6520686572652028616e642074686520466174686572205375706572696f722c204920756e6465727374616e642c2069732061206e6f626c656d616e2920776879206e6f7420626520667269656e646c7920616e6420636f757274656f757320776974687468656d3f204920776f6e27742061726775652c2049276c6c2066616c6c20696e20776974682065766572797468696e672c2049276c6c2077696e207468656d20627920706f6c69746e6573732c20616e642073686f77207468656d20746861742049277665206e6f7468696e6720746f20646f20776974682074686174204165736f702c207468746120627566666f6f6e2c20746861742050696572726f742c20616e642068617665206d6572656c79206265656e2074616b6b656e20696e206f7665722074686973206166666169722c206a757374206173207468657920686176652e"""

    sha = SHA1()
    print(sha.parseBuffer(s))


if __name__ == "__main__":
    main()
