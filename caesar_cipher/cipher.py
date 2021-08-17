
import re

# from corpus_loader import word_list, name_list
import nltk

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

#creation of encrypt function
def encrypt(plain_text, key):

    encrypted_string = ""

    for character in plain_text:
        num = ord(character)
        if num == 32:
            encrypted_string = encrypted_string + character
        if num in range(97,123):
            shifted_num = num + key % 26
            if shifted_num > ord('z'):
                shifted_num = ord('z') - 26  + key % 26
            encrypted_string = encrypted_string + chr(shifted_num)
        elif num in range(65,91):
            shifted_num = num + key % 26
            if shifted_num > ord('Z'):
                shifted_num = ord('Z') - 26  + key % 26
            encrypted_string = encrypted_string + chr(shifted_num)
        
        

    return encrypted_string

def decrypt(encrypted, key):

    encrypted_string = ""
    for character in encrypted:
        num = ord(character)
        if num == 32:
            encrypted_string = encrypted_string + character
        if num in range(97,123):
            shifted_num = num - key % 26
            if shifted_num > ord('z'):
                shifted_num = ord('z') - 26  - key % 26
            encrypted_string = encrypted_string + chr(shifted_num)
        elif num in range(65,91):
            shifted_num = num - key % 26
            if shifted_num > ord('Z'):
                shifted_num = ord('Z') - 26  - key % 26
            encrypted_string = encrypted_string + chr(shifted_num)

    return encrypted_string

def crack(encrypted):

    candidates = []

    for key in range(0,27):
       candidates.append(decrypt(encrypted,key))
    
    for candidate in candidates:
        candidate_words = candidate.split()

        word_count = 0

        for pseudo_word in candidate_words:
            word = re.sub(r'[^A-Za-z]+','', pseudo_word)
            if word.lower() in word_list or word in name_list:
                # print("english word", word)
                word_count += 1
            else:
                pass
                # print('not english word or name', word)

         
        percentage = int(word_count / len(candidate_words) * 100)
        if percentage > 80:
            return candidate
            

    



if __name__=="__main__":
    # print(ord('A'))
    # print(ord(' '))
    # print(ord('Z'))
    print(ord(' '))
    # print(encrypt('$b ',1))
    # print(ord('a'))
    # print(ord('z'))
    # print(chr(98))
    # print(chr(65))
    print(encrypt('It was the best of times, it was the worst of times',4))
    print(crack('Kv ycu vjg dguv qh vkogu kv ycu vjg yqtuv qh vkogu'))
    # print(encrypt('abc',1)) #bcd
    # print(encrypt('ABC',1)) # BCD
    # print(decrypt('bcd',1)) #abc
    # print(encrypt('abc',10)) #klm
    # print(encrypt('abc',26)) #abc
    # print(encrypt('abc',27)) #bcd
    # print(encrypt("ABC",27)) #BCD
    # print(encrypt('zzz',1)) #aaa
    # print(encrypt('zzz',2)) #bbb
    # print(encrypt('ZZZ',1)) #AAA
