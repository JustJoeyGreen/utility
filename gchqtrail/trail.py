################################################################################
### Imports
################################################################################

import wordlist
import enchant
import re
from pycipher import ColTrans as ct
from itertools import permutations
from collections import OrderedDict

alphabet = 'abcdefghijklmnopqrstuvwxyz'

################################################################################
### Obfusated code
################################################################################

def encrypt(a, debug = False):
    A = "nymphsblitzquIckvexdwarfjog."
    b = A
    n = 28
    i = 0
    z = 0
    c = ""
    if debug:
        print "* Encrypting Message: {}".format(a)
    while (i < len(a)):
        x = A.find(a[i])            # Find position of ith letter in A
        y = A.find(b[i % len(b)])   # Find position of ith letter in b, wrapping round b (might be small)
        z = (x + y) % n             # Add the two positions together mod 28
        c += A[z]                   # Add this character in A to the output
        if (x + 1) == n:            # If the position of ith letter in A is 27 (the full stop), then
            b = c                   # Make b the current output c
        if debug:
            print "i: {}, x: {}, y: {}, z: {}, c: {}\n> (x+1) == n: {}, so b: {}".format(i, x, y, z, c, (x + 1) == n, b)
        i += 1                      # Increment loop counter
    return c

def decrypt_bf(debug = True):
    alph = alphabet + 'I. '
    ciphertext = 'tsdmueyuvrxIedqqfmdqweIyaaxtiyzrujqezxqdawgotw'
    plaintext = ''
    i = 0

    while len(plaintext) != len(ciphertext):

        temp_plaintext = plaintext + alph[i] # Add alph to temp
        out = encrypt(temp_plaintext)
        if ciphertext[:len(out)] == out:
            # Correct!
            plaintext = temp_plaintext
            i = 0
            if debug:
                print "Plaintext: {}".format(plaintext)
        else:
            # Incorrect
            i += 1
            if i == len(alph):
                print "! Error: Failed"

    return plaintext

''' Answer: gur.chmmyr.uhag.pbagvahrf.gur.lrne.vf.zpzkpvvv (ROT13 to avoid spoilers) '''

################################################################################
### Hangman
################################################################################

def hangman():
    english_dict = enchant.Dict('en_GB')
    our_alphabet = re.sub('[anordpwuyigt]', '', alphabet)
    wordgen = wordlist.Generator(our_alphabet)
    possible_words = list()
    for poss in wordgen.generate_with_pattern('@@ig@t'):
        if english_dict.check(poss):
            possible_words.append(poss)
    return possible_words

''' Answer: urvtug. cbffvoyr jbeqf ner oyvtug, syvtug, fyvtug, naq urvtug.
vs y jnf vapbeerpg gura pbhyq bayl or urvtug (ROT13 to avoid spoilers) '''

################################################################################
### Back Cover
################################################################################

def cover_decrypt_bf(debug = True):
    # Pattern: PGLSS, PMXPY, PACS, PI, PLAMD
    # Pattern: ABCDD, AEFAG, AHID, AJ, ACHEK
    english_dict = enchant.Dict('en_GB')
    wordgen = wordlist.Generator(alphabet)
    possible_words = list()
    # First word ABCDD:
    for poss_1 in wordgen.generate_with_pattern('@@@@@'):
        # Make sure last two letters the same, and no other letters the same, and it's a word
        if (poss_1[3] == poss_1[4]) and (len(set(poss_1)) == 4) and english_dict.check(poss_1):
            # Next word!
            for poss_2 in wordgen.generate_with_pattern('{}@@{}@'.format(poss_1[0], poss_1[0])):
                if (len(set(poss_1 + poss_2)) == 7) and english_dict.check(poss_2):
                    # Next word!
                    for poss_3 in wordgen.generate_with_pattern('{}@@{}'.format(poss_1[0], poss_1[4])):
                        if (len(set(poss_1 + poss_2 + poss_3)) == 9) and english_dict.check(poss_3):
                            # Next word!
                            for poss_4 in wordgen.generate_with_pattern('{}@'.format(poss_1[0])):
                                if (len(set(poss_1 + poss_2 + poss_3 + poss_4)) == 10) and english_dict.check(poss_4):
                                    # Next word!
                                    for poss_5 in wordgen.generate_with_pattern('{}{}{}{}@'.format(poss_1[0], poss_1[2], poss_3[1], poss_2[1])):
                                        if (len(set(poss_1 + poss_2 + poss_3 + poss_4 + poss_5)) == 11) and english_dict.check(poss_5):
                                            possible_words.append((poss_1, poss_2, poss_3, poss_4, poss_5))
                                            if debug:
                                                print 'Found: {}'.format((poss_1, poss_2, poss_3, poss_4, poss_5))
    return possible_words

''' Answer: LRNE AVARGRRA FVKGL GUERR GNXR CHMMYR GENVY GB BOSHFPNGRQ PBQR (ROT13 to avoid spoilers) '''
''' Ciphetext: AQKLFGHNOPJRISDTUMECBVWXYZ '''

################################################################################
### Games
################################################################################

def games_bf(debug = True):
    # We know: B1, D5, H8, F4
    # 8 letter word?
    english_dict = enchant.Dict('en_GB')
    wordgen = wordlist.Generator(alphabet)
    possible_words = list()
    for poss in wordgen.generate_with_pattern('be@fd@@h'):
        if english_dict.check(poss):
            possible_words.append(poss)
    return possible_words


################################################################################
### Transpositional Cipher
################################################################################

def trans_bf(debug = True):
    ciphertext = 'RUWDEHMUNHTWNARUGTOETRUNCNASEELRIEEIHMESOACPAEQOIANLENTUMOTSSOOMATRENTHEIHE'
    phrases = ['TRAIL','THOUSAND','GCHQ','QUESTION','CHRISTMAS','NINETEEN','UNDER']

    for i in range(2, 12):
        if debug:
            print "> Trying key length {}".format(i)
        for key in permutations(alphabet[:i]):
            mykey = ''.join(key)
            plaintext = ct(mykey).decipher(ciphertext)
            if any(word in plaintext for word in phrases):
                print "+ Key {}: {}".format(mykey, plaintext)

""" Shamelessly nicked from https://stackoverflow.com/questions/28777219/basic-program-to-convert-integer-to-roman-numerals """
def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])

def key_bf(debug = True):
    ciphertext = 'RUWDEHMUNHTWNARUGTOETRUNCNASEELRIEEIHMESOACPAEQOIANLENTUMOTSSOOMATRENTHEIHE'
    plaintext = '!!! GET THIS FROM ROT13 OF THE SPOILER !!!'
    possible_numerals = list()
    for number in range(1900, 2100):
        roman = write_roman(number)
        if ct(roman).decipher(ciphertext) == plaintext:
            possible_numerals.append((number, roman))
    return possible_numerals


'''Answer: NEBZNAAHZRENYJNFHFRQGBTRARENGRGURPBYHZACREZHGNGVBAURERGURDHRFGVBAVFJUVPUBAR'''

################################################################################
### Running
################################################################################

if __name__ == "__main__":

    print games_bf()
