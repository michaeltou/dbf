try:
    import setuptools
    setuptools
except ImportError:
    pass
from distutils.core import setup

#html_docs = glob('dbfdm/html/*')

long_desc="""
Currently supports dBase III, Clipper, FoxPro, and Visual FoxPro tables. Text is returned as unicode, and codepage settings in tables are honored. Memos and Null fields are supported.  Documentation needs work, but author is very responsive to e-mails.

Not supported: index files (but can create tempory non-file indexes), auto-incrementing fields, and Varchar fields.

Installation:  `pip install dbfdm`
"""

py2_only = ()
py3_only = ()
make = []

data = dict(
        name='dbfdm',
        version='0.99.11a1',
        license='BSD License',
        description='Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbfdm files (including memos)',
        long_description=long_desc,
        url='https://github.com/ethanfurman/dbf',
        packages=['dbfdm', ],
        package_data={
           'dbfdm' : [
               'LICENSE',
               'README.md',
               'WHATSNEW',
               ]
           },
        provides=['dbfdm'],
        install_requires=['aenum'],
        author='Ethan Furman',
        author_email='ethan@stoneleaf.us',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Topic :: Database',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Programming Language :: Python :: 3.13',
            ],
        )

if __name__ == '__main__':
    setup(**data)
