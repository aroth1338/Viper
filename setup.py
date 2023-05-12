from setuptools import setup
import re
import ast

#Only change __version__ in data_visualization/__init__.py file
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('vipervis/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    # Needed to silence warnings 
    name='ViperVis',
    url='https://github.com/aroth1338/ViperViz',
    download_url = 'https://github.com/aroth1338/ViperViz',
    author='Adam Roth',
    author_email='aroth1338@gmail.com',
    # Needed to actually package something
    packages=['viperviz', 'viperviz.ColorWheel'],
    # Needed for dependencies
    install_requires=['numpy', 'matplotlib >= 3.5.0', 'pillow'],
    # *strongly* suggested for sharing
    version=version,
    # The license can be anything you like
    license='MIT',
    description='Supplemental package to assist with data visualization in Python.',
    long_description=open('README.md').read(),
    include_package_data=True,
)
