from setuptools import setup, find_packages


# find version 
with open('raia/__init__.py') as f:
    info = {}
    for line in f:
        if line.startswith('__version__'):
            exec(line, info)
            break


setup_info = dict(
    name='raia',
    version=info['__version__'],
    author='Alexandros Stratoudakis',
    long_description_content_type='text/markdown',
    author_email='alexstrat4@gmail.com',
    url='https://github.com/AlexStratou/raia',
    download_url='https://github.com/AlexStratou/raia/archive/refs/tags/v0.1.0.zip',
    description='Simplistic python package to print colored and/or styled text with a user friendly API.',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # Package info
    packages =  find_packages()

)

setup(**setup_info)