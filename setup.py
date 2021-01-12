
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))


def get_long_description(rel_path):
    with open(path.join(here, rel_path)) as file:
        return file.read()


setup(name='tol_colors',
      version=1.0,

      description="Color schemes for lines and maps, color-blind safe",
      long_description=get_long_description('README.md'),
      long_description_content_type='text/markdown',

      keywords='color schemes palette color-blind',

      url='https://personal.sron.nl/~pault',
      project_urls={
          'Source': 'https://github.com/Descanonge/tol_colors',
      },
      author="Clément Haëck",
      author_email='clement.haeck@posteo.net',

      classifiers=[
          'Programming Language :: Python :: 3',
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Science/Research'
      ],

      py_modules="tol_colors")
