#monoalpha
monoalpha = "9$)(/72:$719#98(+2#9$$9#!-2-:7$(4)2=2$2:?/69#$2#93=6(9!-$)(/72:$2-$)9$7:3&9$692:(8#6&/$7?69/)(6#9:$(33.)($)(69?2*(:93?762$)+2--(#56(76:7$$)(95$)76719:93?762$)+-9&-+&#2/)(62--(#56(,9:8$65-$+(29+9:(4/(6$9$$)2-9:8$7/67*($)9$29+96(93?778(4/(6$2#)933(:?(7$)(6(4/(6$-$712:8(*(:$)(+7-$2+/69#$2#939#98(+2#139.2:+&#2/)(6"

freq_chars_german = {
    "E": 0.1740,
    "N": 0.0978,
    "I": 0.0755,
    "S": 0.0727,
    "R": 0.0700,
    "A": 0.0651,
    "T": 0.0615,
    "D": 0.0508,
    "H": 0.0476,
    "U": 0.0435,
    "L": 0.0344,
    "C": 0.0306,
    "G": 0.0301,
    "M": 0.0253,
    "O": 0.0251,
    "B": 0.0189,
    "W": 0.0189,
    "F": 0.0166,
    "K": 0.0121,
    "Z": 0.0113,
    "P": 0.0079,
    "V": 0.0067,
    "ß": 0.0031,
    "J": 0.0027,
    "Y": 0.0004,
    "X": 0.0003,
    "Q": 0.0002
}

freq_chars_english = {
    "e": 0.12702,
    "t": 0.09056,
    "a": 0.08167,
    "o": 0.07507,
    "i": 0.06966,
    "n": 0.06749,
    "s": 0.06327,
    "h": 0.06094,
    "r": 0.05987,
    "d": 0.04253,
    "l": 0.04025,
    "c": 0.02782,
    "u": 0.02758,
    "m": 0.02406,
    "w": 0.02360,
    "f": 0.02228,
    "g": 0.02015,
    "y": 0.01974,
    "p": 0.01929,
    "b": 0.01492,
    "v": 0.00978,
    "k": 0.00772,
    "j": 0.00153,
    "x": 0.00150,
    "q": 0.00095,
    "z": 0.00074
}

freq_bigrams_english = {
    "th": 0.0356,
    "he": 0.0307,
    "in": 0.0243,
    "er": 0.0205,
    "an": 0.0199,
    "re": 0.0185,
    "on": 0.0176,
    "at": 0.0149,
    "en": 0.0145,
    "nd": 0.0135,
    "ti": 0.0134,
    "es": 0.0134,
    "or": 0.0128,
    "te": 0.0120,
    "of": 0.0117,
    "ed": 0.0117,
    "is": 0.0113,
    "it": 0.0112,
    "al": 0.0109,
    "ar": 0.0107,
    "st": 0.0105,
    "to": 0.0105,
    "nt": 0.0104,
    "ng": 0.0095,
    "se": 0.0093,
    "ha": 0.0093,
    "as": 0.0087,
    "ou": 0.0087,
    "io": 0.0083,
    "le": 0.0083,
    "ve": 0.0083,
    "co": 0.0079,
    "me": 0.0079,
    "de": 0.0076,
    "hi": 0.0076,
    "ri": 0.0073,
    "ro": 0.0073,
    "ic": 0.0070,
    "ne": 0.0069,
    "ea": 0.0069,
    "ra": 0.0069,
    "ce": 0.0065,
}

freq_bigrams_german = {
    "er": 0.0400,
    "en": 0.040,
    "ch": 0.02400,
    "de": 0.0220,
    "ei": 0.0190,
    "nd": 0.01870,
    "ie": 0.0185,
    "ge": 0.0200,
    "te": 0.0190,
    "un": 0.0180,
    "st": 0.0170,
    "be": 0.0160,
    "es": 0.0150,
    "he": 0.0140,
    "se": 0.0130,
    "in": 0.0125,
    "ng": 0.0120,
    "au": 0.0115,
    "ar": 0.0110,
    "an": 0.0105,
    "sc": 0.0100,
    "ne": 0.0095,
    "zu": 0.0090,
    "ht": 0.0085,
    "it": 0.0080,
    "is": 0.0070,
    "tr": 0.0065,
    "ra": 0.0060,
    "si": 0.0055,
    "ri": 0.0050,
    "so": 0.0045,
    "la": 0.0040,
    "me": 0.0035,
    "li": 0.0030,
    "ot": 0.0025,
    "um": 0.0020,
    "el": 0.0020,
    "or": 0.0020,
    "di": 0.0020,
    "ll": 0.0020,
    "da": 0.0020,
}


manual_dict = {
    "$": "t",
    ")": "h",
    "(": "e",
    "9": "o",
    "2": "a",
    "/": "r"
}


def count_frequency_of_chars(string):
    all_freq = {}
 
    for i in string:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    
    relative_frequency = {}
    
    for key, value in all_freq.items():
        freq = value / len(string)
        relative_frequency.update({key:freq})
    
    return relative_frequency

def count_frequency_of_bigrams(string):
    all_freq = {}
    relative_freq = {}

    for i in range(0, len(string) - 1):

        bigram = string[i] + string[i+1]
        if bigram in all_freq:
            all_freq[bigram] += 1

        else:
            all_freq[bigram] = 1
            
    for key, value in all_freq.items():
        freq = value / len(all_freq)
        relative_freq.update({key:freq})

    return relative_freq

def sort_frequencies(freq_dict, reverse):
    sorted_by_values = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=reverse))
    return sorted_by_values

def swap_key_value(dict_1, dict_2):
    swapped_dict_1 = {}
    swapped_dict_2 = {}
    for key, value in dict_1.items():
        swapped_dict_1.update({value:key})
        
    for key, value in dict_2.items():
        swapped_dict_2.update({value:key})

    """

    print(f"THIS IS THE SWAPPED WIKI DICT \n its lenths is: {len(swapped_dict_1)}: \n {swapped_dict_1}")
    
    print(f"THIS IS THE SWAPPED MONO DICT \n its lenths is: {len(swapped_dict_2)}: \n {swapped_dict_2}")
    """

    return swapped_dict_1, swapped_dict_2


def match_frequencies(wiki_dict, mono_dict):

    wiki_list = list(wiki_dict.keys())
    mono_list = list(mono_dict.keys())
    
    match_dict = {}

    max_list_length = min(len(wiki_list), len(mono_list))
    print(max_list_length)

    for i in range(0, max_list_length):
        match_dict[mono_list[i]] = wiki_list[i]
                
    return match_dict

def match_keys_values(wiki_dict, mono_dict):
    match_dict = {}

    wiki_list = list(wiki_dict.keys())
    mono_list = list(mono_dict.keys())

    if len(wiki_list) > len(mono_list):
        shorter_list = mono_list
    else:
        shorter_list = wiki_list
    
    print(f"Length of wiki_list: {len(wiki_list)}")
    print(f"Length of mono_list: {len(mono_list)}")

    for i in range(0, len(shorter_list)):
        match_dict.update({mono_list[i] : wiki_list[i]})

    return match_dict

def solve_monoalpha(string, match_dict):

    solved_string = ""
    for char in string:
        solved_string += match_dict.get(char, char)

    return solved_string.lower()

def solve_monoalpha_bigram(string, match_dict):
    
    solved_string = string
    for key, value in match_dict.items():
        solved_string = solved_string.replace(key, value)
        
    return solved_string.lower()

def update_english_dict(char_dict, bigram_match_dict):
    temp_char_dict = char_dict.copy()
    temp_string = ""

    for v in bigram_match_dict.values():
        temp_string += v
        
    char_list = list(temp_string)
    char_list = list(dict.fromkeys(char_list))

    for char in char_list:
        if char in temp_char_dict.keys():
            
            print(f"DELETING {char} from dict")
            
            del temp_char_dict[char]

    return temp_char_dict

def update_char_dict(char_dict, bigram_match_dict):
    temp_char_dict = char_dict.copy()
    temp_string = ""

    for k in bigram_match_dict.keys():
        temp_string += k.lower()
        
    char_list = list(temp_string)
    char_list = list(dict.fromkeys(char_list))

    for char in char_list:
        
        print(f"DELETING {char} from dict")
        
        del temp_char_dict[char]

    return temp_char_dict
        
if __name__ == "__main__":

    bigram_slice_factor = 20
    char_slice_factor = 20

    cypher_char_dict = count_frequency_of_chars(monoalpha)
    
    #sort for ascending frequencies
    sorted_cypher_char_dict = sort_frequencies(cypher_char_dict, True)

    #sort bigram frequencies
    bigram_dict = count_frequency_of_bigrams(monoalpha)
    sorted_cypher_bigram_dict = sort_frequencies(bigram_dict, True)
    sliced_cypher_bigram_dict = dict(list(sorted_cypher_bigram_dict.items())[:bigram_slice_factor])
    
    char_match_dict = match_frequencies(freq_chars_english, sorted_cypher_char_dict)
    print(char_match_dict)

    bigram_match_dict = match_frequencies(freq_bigrams_english, sorted_cypher_bigram_dict)
    print(bigram_match_dict)
    """
    solved_string_with_bigrams = solve_monoalpha_bigram(monoalpha, bigram_match_dict)
    print(solved_string_with_bigrams)
    """
    char_match_dict.update(manual_dict)
    print("UPDATED CHAR DICT:")
    print(char_match_dict)
    solved_string_with_chars = solve_monoalpha(monoalpha, char_match_dict)
    
    solved_string_with_bigrams = solve_monoalpha_bigram(monoalpha, bigram_match_dict)
    print(solved_string_with_bigrams)

    complete_solved_string = solve_monoalpha_bigram(solved_string_with_bigrams, char_match_dict)
    print(complete_solved_string)

    
    
    """

    # FREQUENCIES FOR CHARS AND BIGRAMS IN ENGLISH LANGUAGE
    english_char_dict = freq_chars_english
    english_bigram_dict = freq_bigrams_english
    
    """
    
        
