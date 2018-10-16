
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
    alph = 'abcdefghijklmnopqrstuvwxyzI. '
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

# SECRET = gur.chmmyr.uhag.pbagvahrf.gur.lrne.vf.zpzkpvvv (ROT13 to avoid spoilers)

################################################################################
### Running
################################################################################

if __name__ == "__main__":

    decrypt_bf()
