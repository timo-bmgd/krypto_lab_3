import argparse
import re
from bs4 import BeautifulSoup

alphabet_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

KEYWORD = "ENIGMA"
CIPHER = "ÄSGUG TLVVQ ORCCB USREC PEUSX UMGZS ARZZA YSHZV DOFYM SFHIA GUGDS ABQZO AJPGF YSHZV DOFYM SUSHD"

HARD_CIPHER = "GIKGE LEGHR OIGDQ PRNDL ORXMO ERLDM XEGUM QEGDV OVXQW MHETI CSXKX ONMDB DAERY OBNMK CANEK KBXFI CTXKP DDBDW DUWDR DEGRM XDUDM WDXJS NIXQI XVXQD GEBEI VTWZH ORMDB DZNJY BZPZV NAPHV NEGRG RLNDW CEEUI BLHQI XUGCH ONDKE BTXWX XIVGX KUYFI CCAQM OBXML KTMDR UOGMX ONPHV KUVGO OIGDP YELTR QPKZI CEGSM ORXMH SELDV DEQSM CTGTR ROYEI XTEHG RNBBL DZNJY BZCDH ONYZP VSDNR XTXDV WIMCI WIFJY BSONV QELSI VLMDR ZRHFV KMFDR DSVGP EELRI VTPDV NEG"

def cleanse(input):
    cleaned_string = re.sub(r'[^a-zA-Z]', '', input)
    uppercase_string = cleaned_string.upper()
    return uppercase_string

def load_input():
    with open('texts.xml', 'r') as f:
        data = f.read()
    Bs_data = BeautifulSoup(data, "xml")
    text1 = str(Bs_data.find('text1').text)
    text2 = str(Bs_data.find('text2').text)
    key1 = str(Bs_data.find('key1').text)
    key2 = str(Bs_data.find('key2').text)
    return text1,text2,key1,key2


def strip_whitespaces(cipher_string):
    return stripped_string

def char_to_num(char):
    char_index = alphabet_list.index(char.upper())
    return char_index

def num_to_char(num):
    char = alphabet_list[num]
    return char

def decode(cipher, keyword):
    solved_string = ""
    for i in range(0, len(cipher)):
        key_index = char_to_num(keyword[i % len(keyword)])
        cipher_index = char_to_num(cipher[i])

        shifted_index = (cipher_index - key_index) % len(alphabet_list)

        shifted_char = num_to_char(shifted_index)
        solved_string += shifted_char
        
    return solved_string

def encode(cipher, keyword):
    solved_string = ""
    for i in range(0, len(cipher)):
        key_index = char_to_num(keyword[i % len(keyword)])
        cipher_index = char_to_num(cipher[i])

        shifted_index = (cipher_index + key_index) % len(alphabet_list)

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
                

if __name__ == "__main__":

    text1,text2,key1,key2 = load_input()
    text1,text2 = cleanse(text1),cleanse(text2)
    encoded1,encoded2 = encode(text1,key1),encode(text2,key2)
    decoded1,decoded2 = decode(encoded1,key1),decode(encoded2,key2)
    print(decoded1,decoded2)