import unittest
from enckey.enckey import Enckey

class EnckeyTestCase(unittest.TestCase):

	def setUp(self):
		self.client = Enckey()
		self.client.set_keys_file('/home/victor/tmp/keys.txt')

	@unittest.skip('Not test')
	def test_encrypt(self):
		self.client.encrypt('test value', 'my key')

	@unittest.skip('Not test')
	def test_print_cipher(self):
		ciphers = self.client.load_cipher()

	@unittest.skip('Not test')
	def test_decrypt(self):
		ciphers = self.client.load_cipher()
		ciphers_txt = ciphers[0].get_cipher()
		print('Cipher key is : ' + ciphers_txt)
		plain_txt = self.client.decrypt(ciphers_txt)
		print('Plain key is : ' + plain_txt)

	def test_change_key(self):
		self.client.load_cipher()
		self.client.change_key('88888888')
		ciphers = self.client.load_cipher()
		ciphers_txt = ciphers[0].get_cipher()
		print('Cipher key is : ' + ciphers_txt)
		plain_txt = self.client.decrypt(ciphers_txt)
		print('Plain key is : ' + plain_txt)

if __name__ == '__main__':
	unittest.main()