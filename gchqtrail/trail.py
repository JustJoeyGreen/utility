################################################################################
### Imports
################################################################################

import wordlist
import enchant
import re

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
### Running
################################################################################

if __name__ == "__main__":

    print hangman()
