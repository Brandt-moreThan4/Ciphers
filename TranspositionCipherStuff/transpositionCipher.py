import math
import random as rd
import sys


def encrypt_message(message, key):
    cipher_text = ['' for x in range(key)]
    for col in range(key):
        pointer = col

        while pointer < len(message):
            cipher_text[col] += message[pointer]
            pointer += key
    return ''.join(cipher_text)


def decrypt_message(secret_message, key):
    """Decrypt a Transposition Cipher given the key."""
    num_of_columns = math.ceil(len(secret_message) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_rows * num_of_columns) - len(secret_message)
    decrypted_grid = [''] * num_of_columns

    col = 0
    row = 0

    for letter in secret_message:
        decrypted_grid[col] += letter
        col += 1

        if col == num_of_columns or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(decrypted_grid)


def main():
    pass


if __name__ == '__main__':
    main()
