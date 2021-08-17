
from caesar_cipher.cipher import encrypt,decrypt,crack
#encrypt a string with a given key

def test_encrypt():
    #Arrange
    expected = 'Kv ycu vjg dguv qh vkogu kv ycu vjg yqtuv qh vkogu'

    #Act
    actual = encrypt('It was the best of times it was the worst of times',2)

    #Assert
    assert actual == expected

def test_decrypt():
    #Arrange
    expected = 'It was the best of times it was the worst of times'

    #Act
    actual = decrypt('Kv ycu vjg dguv qh vkogu kv ycu vjg yqtuv qh vkogu',2)

    #Assert
    assert actual == expected

def test_crack():
    #Arrange
    expected = 'It was the best of times it was the worst of times'

    #Act
    actual = crack('Kv ycu vjg dguv qh vkogu kv ycu vjg yqtuv qh vkogu')

    #Assert
    assert actual == expected