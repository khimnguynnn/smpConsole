from setuptools import setup, find_packages

setup(
    name='smpconsole',
    version='1.0.2',
    author='khiemndd',
    description='best console experience',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url = 'https://github.com/khimnguynnn/smpConsole',
    install_requires=[
        'colorama'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',
)