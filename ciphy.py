"""Cipher stuff"""


def reverse(string_input):
    """Reverses a string"""

    letter_count = len(string_input)
    backwards = ''
    x = 1
    while x <= letter_count:
        backwards += string_input[-x]
        x += 1
    return backwards


def caesar_encrypt(message, key):
    """Encrypt a message with the provided key using Caesar Cipher method."""
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper()
    encrypted_message = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num += key
            if num > len(LETTERS) - 1:
                num -= len(LETTERS)
            encrypted_message += LETTERS[num]
        else:
            encrypted_message += symbol
    return encrypted_message
