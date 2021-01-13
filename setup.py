
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))


def get_long_description(rel_path):
    with open(path.join(here, rel_path)) as file:
        return file.read()


def get_version(rel_path):
    with open(path.join(here, rel_path)) as file:
        lines = file.read().splitlines()
    for line in lines:
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(name='tol_colors',
      version=get_version('tol_colors.py'),

      description="Color schemes for lines and maps, color-blind safe",
      long_description=get_long_description('README.md'),
      long_description_content_type='text/markdown',

      keywords='visualization colormap colorset',

      url='https://personal.sron.nl/~pault',
      project_urls={
          'Source': 'https://github.com/Descanonge/tol_colors',
      },
      author="Clément Haëck",
      author_email='clement.haeck@posteo.net',

      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Visualization'
      ],

      py_modules=['tol_colors'],

      install_requires=['numpy', 'matplotlib'])
