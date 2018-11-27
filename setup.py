from setuptools import setup

setup(
	name = 'enckey',
	version = '0.0.1',
	description = 'a tools to encrypt personal private keys',
	packages = ['enckey'],
	package_data = {'enckey':['resource/keys.txt']},
	include_package_data = True,
	license = 'LICENSE.txt',
	author = 'mozhiyan',
	author_email = 'mozhiyan@gmail.com',
	url = ''
)