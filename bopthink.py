import sys
given_string = input('Enter the original line: ')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher_key = input('Enter the cipher key (take a note: "0" cipher key equals to print non-encrypted line): ')
alph = 0
#cant really think of variable's name for this one
test = 0
encrypted_string = ''
if not cipher_key.isnumeric():
 print('Error: Key value only accepts numeric')
 sys.exit()
cipher_key = int(cipher_key)
if cipher_key > 25:
    print('Error: Key value must be 25 or less')
    sys.exit()
for letter in given_string:
    if letter.isalpha():
        #print(letter.isupper())
        if letter.isupper():
            letter = letter.swapcase()
            for i in range(len(alphabet)):
                if alphabet[i] == letter:
                    test = i
            test = test + cipher_key
            #print(letter)
            if test > 25:
                test = abs(26 - test)
            letter = letter.swapcase()
            encrypted_string = encrypted_string + alphabet[test].swapcase()
            #print(alphabet[test].swapcase())
        else:
            for i in range(len(alphabet)):
                if alphabet[i] == letter:
                    test = i
            test = test + cipher_key
            #print(letter)
            if test > 25:
                test = abs(26 - test)
            encrypted_string = encrypted_string + alphabet[test]
    else:
        encrypted_string = encrypted_string + letter
print(f"The encrypted string is '{encrypted_string}' using '{cipher_key}' as a key")