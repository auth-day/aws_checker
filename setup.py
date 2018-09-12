from setuptools import setup, find_packages
from os.path import join, dirname
from distutils.core import setup

class register(register_orig):

    def _get_rc_file(self):
        return os.path.join('.', '/opt/.pypirc')

class upload(upload_orig):

    def _get_rc_file(self):
        return os.path.join('.', '/opt/.pypirc')

setup(
    name = 'aws_checker',
    packages = find_packages(),
    version = '0.1',
    description = 'List AWS resources',
    author = 'diboan',
    author_email = 'diboan@yandex.ru',
    include_package_data=True,
    url = 'https://github.com/diboanches/aws_checker',
    download_url = 'https://github.com/diboanches/aws_checker',
    cmdclass={
        'register': register,
        'upload': upload,
    }
)
