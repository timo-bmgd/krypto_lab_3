import argparse
import re
from bs4 import BeautifulSoup
from math import gcd
from mono_alpha import count_frequency_of_chars as count_frequency_of_chars
from mono_alpha import solve_monoalpha as solve_monoalpha
from mono_alpha import count_frequency_of_chars as count_frequency_of_chars


alphabet_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

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
    crypttext = str(Bs_data.find('crypttext').text)
    return text1,text2,key1,key2,crypttext

def char_to_num(char):
    char_index = alphabet_list.index(char.upper())
    return char_index

def num_to_char(num):
    char = alphabet_list[num]
    return char

def decode(cipher, keyword):
    cipher = cleanse(cipher)
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
    counter = 0

    for i in range(0, len(cipher)):
        counter += 1
        key_index = char_to_num(keyword[i % len(keyword)])
        cipher_index = char_to_num(cipher[i])

        shifted_index = (cipher_index + key_index) % len(alphabet_list)

        shifted_char = num_to_char(shifted_index)
        solved_string += shifted_char
        if counter == 5:
            solved_string += " "
            counter = 0
        
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


def get_substrings(crypttext: str):
    crypttext = cleanse(crypttext)
    substrings = []
    for index in enumerate(crypttext):
        for length in range(4,10):
            substrings.append(crypttext[index[0]:index[0]+length])
    substrings = list(set(substrings))
    return substrings

def count_occurances(crypttext: str, substrings: list):
    occurances = list()
    for substring in enumerate(substrings):
        frequency,indices,distances = count(substring[1],crypttext)
        results = tuple((substring[1],frequency,indices,distances))
        occurances.append(results)
    for occurance in occurances:
        print(occurance)
    return occurances

def count(search, text):
    start = 0
    frequency = 0
    indices = []
    distances = []
    while start != -1:
        start = text.find(search, start)
        if start != -1:
            print(f"Found at index: {start}")
            frequency += 1
            indices.append(start)
            start += len(search)  # Move past the last found occurrence
    if len(indices) >= 2:
        for i in range(0, len(indices)-1):
            distances.append(indices[i+1]-indices[i])
    return frequency,indices,distances


# def guess_keyword(crypt_text):


if __name__ == "__main__":

    text1,text2,key1,key2,crypttext = load_input()
    text1,text2 = cleanse(text1),cleanse(text2)
    encoded1,encoded2 = encode(text1,key1),encode(text2,key2)
    decoded1,decoded2 = decode(encoded1,key1),decode(encoded2,key2)
    # print(decode(crypttext,"FOSTERTHEPEOPLE"))

    crypttext = cleanse(crypttext)
    print(get_substrings(crypttext))
    occurances = count_occurances(crypttext,get_substrings(crypttext))
    occurances = sorted(occurances, key=lambda i: i[1])
    for occurance in occurances:
        print(occurance[3],occurance[0])
    
    print(gcd(638, 319, 154, 429, 22))

    # count_frequency_of_chars()


    print(encode("THISISTHESECRETMESSAGE","KEY"))


    