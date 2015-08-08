from distutils.core import setup

setup(
    name='connect4',
    version='0.0.1',
    author='Ross Meikleham',
    author_email='RossMeikleham@hotmail.co.uk',
    packages=['connect4'],
    url='https://github.com/RossMeikleham/Connect4',
    license='MIT',
    description='Connect 4 clone',
    package_dir={'connect4':'src'},
    long_description=open('README.md').read()
)

