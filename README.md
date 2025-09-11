[![PyPI](https://img.shields.io/pypi/v/zpic)](https://pypi.org/project/zpic)

# ZPIC

A fork of the https://github.com/zpic-plasma/zpic project which attempts to integrate the python functionality as a standalone pip package for convenience. Installation instructions are present [here](#installation). Information about **zpic** itself is present at the origin repository and documentation page.

> Particle-in-Cell (PIC) codes are used in almost all areas of plasma physics, such as fusion energy research, plasma accelerators, space physics, ion propulsion, and plasma processing, and many other areas. Leveraging on our expertise and experience from the development and use of the OSIRIS PIC code, we have developed a suite of 1D/2D fully relativistic electromagnetic PIC codes, as well as 1D electrostatic. These codes are self-contained and require only a standard laptop/desktop computer with a C compiler to be run. The output files are written in a new file format called ZDF that can be easily read using the supplied routines in a number of languages, such as Python, and IDL. The code suite also includes a number of example problems that can be used to illustrate several textbook and advanced plasma mechanisms, including instructions for parameter space exploration. We also invite contributions to this repository of test problems that will be made freely available to the community provided the input files comply with the format defined by the ZPIC team.

## Documentation

The project now has its own dedicated website on GitHub pages. You can find all the documentation at [https://zpic-plasma.github.io](https://zpic-plasma.github.io)

## Installation

**zpic** may be installed with 
```
pip install zpic
```
The compilation process from the documentation is run for multiple OSes and platform specific wheels are provided. More details can be found on the PyPI page. 

| OS      | Compatibility |
| ------- | ------------- |
| Linux   | >= python3.10 |
| MacOS   | >= python3.10 |