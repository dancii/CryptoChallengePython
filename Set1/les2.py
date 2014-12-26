#Set 1 les 2

hexDecodeFirstStr = "1c0111001f010100061a024b53535009181c"
hexDecodeSecStr = "686974207468652062756c6c277320657965"


def xorGrind(firstStr, secStr):
    correctAnswer = "746865206b696420646f6e277420706c6179"

    xored=hex(int(firstStr,16) ^ int(secStr,16))
    print hex(int(correctAnswer,16)) == xored

xorGrind(hexDecodeFirstStr, hexDecodeSecStr)
