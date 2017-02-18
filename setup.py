from setuptools import setup

__version__ = '0.1'

setup(
    name='tcx2dict',
    version=__version__,
    author='Xaris Arvanitis.',
    author_email='xaris@gmx.com',
    py_modules=[''],
    url='',
    license='MIT',
    description='Module that reads data from tcx and stores them in dictionary',
    long_description=open('README.md').read(),
    keywords = "xml tcx parser python garmin",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        "python-tcxparser",
     ]
)
