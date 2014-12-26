#Set 1 Les 1
import base64
import binascii

hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base64String = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
hexRawByte = binascii.unhexlify(hexString)

print hexRawByte
stringToBase64 = str(hexRawByte).encode('base64').rstrip()
print stringToBase64 == base64String
