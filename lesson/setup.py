'''Execution method

    terminal : python setup.py sdist

    create   : MANIFEST, tar.gz
'''

from distutils.core import setup


setup(
    name='udemy',
    version='1.0.0',
    packages=['package','package.talk','package.tools'],
    url='',
    license='Free',
    author='hibikon',
    author_email='hibikon.asr.mac@gmail.com',
    description='Sample package'
)