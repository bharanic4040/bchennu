from setuptools import setup

setup(
    name='bchennu',
    version='3.0.0',
    packages=['bchennu'],
    entry_points = {
        "console_scripts": ['bchennu = bchennu.bchennu:main']
        },
    url='https://github.com/bharanic4040/bchennu/',
    license='Open Source',
    author='bharani chennu',
    author_email='bharanic404@gmail.com',
    description='',
    setup_requires=['wheel']
)
