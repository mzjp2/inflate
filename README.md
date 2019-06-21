# inflate

![PyPI](https://img.shields.io/pypi/v/inflate.svg?style=flat-square)
![License](https://img.shields.io/github/license/mzjp2/inflation.svg?style=flat-square)
[![Code Style: Black](https://img.shields.io/badge/code-black-black.svg?style=flat-square)](https://github.com/ambv/black)

inflate is a Python built command line interface that lets you quickly compute how inflation affects a sum of money in an intuitive and visually pleasing package.

## Installation

Run ``pip install inflate``. Verify that the latest version is installed by running ``inflate --version``.

## Usage

```shell
>>> inflate [OPTIONS] START END [AMOUNT]
    [AMOUNT] in [START] is worth [INFLATED AMOUNT] in [END] ([INCLUSIVE/EXCLUSIVE])
```
The options are

```
  -c, --country TEXT  Country [either US/UK], default is UK
  -i, --inclusive     Include ending year, default no
  --version           Show the version and exit.
  --help              Show this message and exit.
```

**Example**: 

```shell
>>> inflate -c US -i 1998 1999 50
    $50.0 in 1998 is worth $51.51 in 1999 (inclusive).
```

## Current features

- Able to work "backwards", that is, if you want to know how much $10 in 2018 was worth in 2000, you can do so via ``inflate -c US 2018 2000 10``

## Future features/work

- [ ] Add in a more detailed analytics view, showing average inflation across time period.
- [ ] Flesh out the testing modules
- [ ] Package and publish on PyPI.
