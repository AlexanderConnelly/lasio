'''Setup script for lasio'''

from setuptools import setup

from os import path

from lasio import __version__


with open(path.join(path.dirname(__file__), "requirements.txt"), "r") as f:
    requirements = f.read().splitlines()

setup(name='lasio',
      version=__version__,
      description="Read/write well data from Log ASCII Standard (LAS) files",
      long_description=(
          'This is a Python 2/3 package to read and write Log ASCII Standard '
          '(LAS) files, used for borehole data such as geophysical, geological, '
          'or petrophysical logs. It\'s compatible with versions 1.2 and 2.0 of '
          'the LAS file specification, published by the Canadian Well Logging '
          'Society (http://www.cwls.org/las). In principle it is designed to read '
          'as many types of LAS files as possible, including ones containing '
          'common errors or non-compliant formatting.\n\n'
          'See http://github.com/kinverarity1/lasio for more details.'),
      url="https://github.com/kinverarity1/lasio",
      author="Kent Inverarity",
      author_email="kinverarity@hotmail.com",
      license="MIT",
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: Customer Service",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: End Users/Desktop",
          "Intended Audience :: Other Audience",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Topic :: Scientific/Engineering",
          "Topic :: System :: Filesystems",
          "Topic :: Scientific/Engineering :: Information Analysis",
      ],
      keywords="science geophysics io",
      packages=["lasio", ],
      install_requires=requirements,
      entry_points={
          'console_scripts': [
              'las2excel = lasio.excel:main',
              'las2excelbulk = lasio.excel:main_bulk'
          ],
      }
      )
