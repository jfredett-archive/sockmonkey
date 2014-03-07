from distutils.core import setup

setup(
        name='sockmonkey',
        version='0.0.0',
        author='Joe Fredette',
        author_email='jfredett@gmail.com',
        packages=['sockmonkey'],
        scripts=[],
        url='http://pypi.python.org/pypi/sockmonkey/',
        license='LICENSE',
        description='A tool for identifying potential sockpuppet reddit accounts',
        long_description=open('README.txt').read(),
        install_requires=[
            "nltk == 2.0.4",
            "numpy == 1.8.0",
            "pyyaml == 3.10"
        ]
)
