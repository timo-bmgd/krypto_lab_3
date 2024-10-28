import argparse

alphabet_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

KEYWORD = "ENIGMA"
CIPHER = "ÄSGUG TLVVQ ORCCB USREC PEUSX UMGZS ARZZA YSHZV DOFYM SFHIA GUGDS ABQZO AJPGF YSHZV DOFYM SUSHD"

HARD_CIPHER = "GIKGE LEGHR OIGDQ PRNDL ORXMO ERLDM XEGUM QEGDV OVXQW MHETI CSXKX ONMDB DAERY OBNMK CANEK KBXFI CTXKP DDBDW DUWDR DEGRM XDUDM WDXJS NIXQI XVXQD GEBEI VTWZH ORMDB DZNJY BZPZV NAPHV NEGRG RLNDW CEEUI BLHQI XUGCH ONDKE BTXWX XIVGX KUYFI CCAQM OBXML KTMDR UOGMX ONPHV KUVGO OIGDP YELTR QPKZI CEGSM ORXMH SELDV DEQSM CTGTR ROYEI XTEHG RNBBL DZNJY BZCDH ONYZP VSDNR XTXDV WIMCI WIFJY BSONV QELSI VLMDR ZRHFV KMFDR DSVGP EELRI VTPDV NEG"

def strip_whitespaces(cipher_string):
    stripped_string = cipher_string.replace(" ", "")
    return stripped_string

def char_to_num(char):
    char_index = alphabet_list.index(char.upper())
    return char_index

def num_to_char(num):
    char = alphabet_list[num]
    return char

def solve_vignere_with_key(cipher, keyword):
    solved_string = ""
    for i in range(0, len(cipher)):
        key_index = char_to_num(keyword[i % len(keyword)])
        cipher_index = char_to_num(cipher[i])

        shifted_index = (cipher_index - key_index) % len(alphabet_list)

        shifted_char = num_to_char(shifted_index)
        solved_string += shifted_char
        
    return solved_string


def find_trigrams(cipher):
    trigrams = {}
    for i in range(0, len(cipher) - 4):
        trigram = cipher[i:i+3]
        for j in range(i + 3, len(cipher) - 4):
            if cipher[j: j + 3] == trigram:
                if trigram not in trigrams:
                    trigrams[trigram] = []
                trigrams[trigram].append(j-i)
    print(trigrams)
                

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("counter", help="An integer will be increased by 1 and printed.", type=int)
args = parser.parse_args()
print(args.counter + 1)