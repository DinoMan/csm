from setuptools import setup

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='csm',
    version='0.1.0',
    py_modules=['generator', 'models', 'watermarking'],
    install_requires=requirements,
)
