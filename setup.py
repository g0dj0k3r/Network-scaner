from setuptools import setup,find_packages
setup(
    name='Network-Scaner',
    version='2.0',
    author='Godjoker',
    
    url='github.com/g0dj0k3r',

    packages=find_packages(),
    py_modules=['scan','osdiscovery', 'scaners', 'getip', 'pingscan', 'scriptscan'],
    install_requires=[
        'python-nmap',
        'colorama',
        'pyfiglet',
        
    ],
    entry_points={
        'console_scripts': [
            'net-scan=scan:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
    license='open source',
    description='A comprehensive network scanning tool using Nmap.'
    )
