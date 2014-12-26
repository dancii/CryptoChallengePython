#Set 1 les 3
#import string
import collections
import binascii

englishPlainText ="In a cryptosystem, weaknesses can be introduced through insecure handling of plaintext, allowing an attacker to bypass the cryptography altogether. Plaintext is vulnerable in use and in storage, whether in electronic or paper format. Physical security deals with methods of securing information and its storage media from local, physical, attacks. For instance, an attacker might enter a poorly secured building and attempt to open locked desk drawers or safes. An attacker can also engage in dumpster diving, and may be able to reconstruct shredded information if it is sufficiently valuable to be worth the effort. One countermeasure is to burn or thoroughly crosscut shred discarded printed plaintexts or storage media; NSA is infamous for its disposal security precautions."
hexEncodedString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


''' //"Harder way"
englishAlphabet = list(string.ascii_lowercase)
alphabetScoring = [0] * len(englishAlphabet)

for x in englishPlainText:
    i = 0
    for y in englishAlphabet:
        if x == y:
            alphabetScoring[i] += 1
        i+=1

print alphabetScoring
'''

#print(collections.Counter(englishPlainText).most_common(2)[0])
#Answer 'e'

print binascii.unhexlify(hexEncodedString)
xoredSingleChar = hex(int(hexEncodedString,16) ^ int("e",16))

print xoredSingleChar

xored = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3738"

print binascii.unhexlify(xored)
