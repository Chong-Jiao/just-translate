import unittest

from just_translate.read_configure import encode, decode, write_configure, read_configure

class TestREADConfigure(unittest.TestCase):

    def test_encode_decode(self):
        appid = 'uxddgx'
        secretKey = 'jjigelg'
        encoded_appid, encoded_secretKey = encode(appid, secretKey)
        decoded_appid, decoded_secretKey = decode(encoded_appid, encoded_secretKey)
        self.assertEqual(appid, decoded_appid, 'The decoded key should be consistent with the original key')
        self.assertEqual(secretKey, decoded_secretKey, 'The decoded key should be consistent with the original key')
    def test_read_write(self):
        appid = 'uxddgx'
        secretKey = 'jjigelg'
        write_configure(appid, secretKey)
        x, y = read_configure()
        self.assertEqual(appid, x, 'The decoded key should be consistent with the original key')
        self.assertEqual(secretKey, y, 'The decoded key should be consistent with the original key')