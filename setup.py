import os, json
from setuptools import setup, find_packages

filename = './alias.json'
name = json.load(open(filename))[0]
src_dir = 'chat4free'

if name != src_dir: os.system(f'mv {src_dir} {name}')
setup(
    name = name,
    packages = find_packages(exclude=['examples']),
    version = '0.0.0',
    license = 'GPL-2.0',
    description = 'Chat for Free',
    author = 'JiauZhang',
    author_email = 'jiauzhang@163.com',
    url = 'https://github.com/JiauZhang/chat4free',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type = 'text/markdown',
    keywords = [
        'ChatBot',
    ],
    install_requires=[
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3.8',
    ],
)
if src_dir != name: os.system(f'mv {name} {src_dir}')