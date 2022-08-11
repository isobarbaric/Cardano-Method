from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = "A basic cubic equation solver"
LONG_DESCRIPTION = "An implementation of Cardano's Method of solving cubic equations"

setup(
    name="CardanoMethod",
    version=VERSION,
    author="Krish Shah",
    author_email="shahkrish2016@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['algebra', 'cardano', 'cardano-method', 'coefficients', 'complex', 'complex numbers', 'cubic', 'cubic equation', 'depressed cubic', 'equation', 'imaginary', 'method', 'polynomial', 'quadratic equation', 'real', 'roots', 'square root', 'zeroes'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
