import setuptools


# Package setup

setuptools.setup(

name='mypkg',

version="1.0.0",

author="Yusud",

author_email="yusuf.abdurrasheed@outlook.com",

description="This is my app",

packages=setuptools.find_packages(),

setup_requires=['flask']
)