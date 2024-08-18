from setuptools import setup, find_packages
import sys

# ensure compatible python version
if sys.version_info <= (3, 10):
    raise Exception('Python must be at least on version 3.10.0')

# find version
with open('raia/__init__.py') as f:
    info = {}
    for line in f:
        if line.startswith('__version__'):
            exec(line, info)
            break


setup_info = dict(
    name='raia',
    python_requires=">=3.10",
    version=info['__version__'],
    author='Alexandros Stratoudakis',
    long_description_content_type='text/markdown',
    long_description=open('README.md', 'r').read(),
    author_email='alexstrat4@gmail.com',
    url='https://github.com/AlexStratou/raia',
    download_url='https://github.com/AlexStratou/raia/archive/refs/tags/v' +
        info['__version__']+'.zip',
    description='Simplistic python package to print colored and/or styled text with a user friendly API.',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # Package info
    packages=find_packages()

)

setup(**setup_info)
