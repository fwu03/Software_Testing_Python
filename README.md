# mlist

## Contributors

|Name|Github.com User Id|
|--|--|
|Bailey Lei (baileyle)|[blei7](https://github.com/blei7)|
|Daniel Lin (dglin)|[danielglin](https://github.com/danielglin)|
|Fan Wu (fwu03)|[fwu03](https://github.com/fwu03)|

## Versions
| Document | Description |
|-|-|
| [Milestone 1](https://github.com/UBC-MDS/mlist_Python/tree/v1.0) | Project Proposal |
| [Milestone 2](../master/README.md) | Milestone 2|

## Package Overview

Python provides lots of tools to manipulate lists. In this package, we will implement several list manipulating functions, including `binary_search()`, `flatten_list_prime()`, and `find_prime()`.

## Functions

|ID|Function|Description|Arguments|Example|
|--|--|--|--|--|
|1|binary_search(x, lst)|Search if the value `x` exists in the `lst`, and return a list contains: `TRUE/FALSE` depends on whether the `x` value has been found, `x` value, and `x` position indices in `lst`.|x: numeric, lst: sorted list of numerics|binary_search(4, [1,2,3,4,5,6])|
|2|flatten_list_prime(l)|This function takes an input list and returns a flat list that contains only prime numbers.|l: a list of integers|flatten_list_prime([[2, 3, 4, 5], 19, [131, 127]])|
|3|find_prime(x)| Return the largest prime number for a given list.|x : a list of integer|find_prime([0,1,2,3,4,5])|

## Python Environment

1. binary_search(x, list): In the Python environment, there is [bisect](https://docs.python.org/2/library/bisect.html) that give similar functionality as binary_search, but is not automated and requires extra coding. The binary_search presented here is able to return a list contains whether `x` is in the `list`, `x` value, `x` position indices in `list`.

2. flatten_list_prime(list): In the Python environment, there is a library called [Itertool functions](https://docs.python.org/2/library/itertools.html#itertools.chain) that allows for flattening list, but it does not select for prime numbers.

3. find_prime(list): There is no function that find the largest prime within a list in the Python environment.

## Installation
The `mlist` package can be installed through `pip` by running the following command in Terminal:

```
pip install git+https://github.com/UBC-MDS/mlist_Python.git
```

For further updates of the package, please enter the following command:

```
pip install --upgrade git+https://github.com/UBC-MDS/mlist_Python.git
```

## Usage
To import the package using:

```
import mlist
```

To import the functions using:

```
from mlist.<function name> import <function name>
```
For examples:

```
from mlist.binary_search import binary_search
from mlist.flatten_list_prime import flatten_list_prime
from mlist.find_prime import find_prime
```

## Dependencies

- Python version 3.6.5
- Python packages:
  + pytest
