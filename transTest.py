import transpositionCipher
import unittest
import random as rd

class MyTestCase(unittest.TestCase):
    def test_encrypt(self):
        message = 'Fuck you bro'
        correct_encrypted = 'Fouuc kb ryo'
        test_encrypted = transpositionCipher.encrypt_message(message, key=6)
        self.assertEqual(test_encrypted, correct_encrypted)


if __name__ == '__main__':
    unittest.main()
