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
| [Milestone 1](../master/README.md) | Project Proposal |

## Package Overview

This project provides several tools to manipulate lists in Python.  
For example, a user search through a list for a certain kind of item
The repository includes the following functions:

## Functions

|ID|Function|Description|
|--|--|--|
|1|binary_search(x, list)|Search if the value `x` exists in the `list`, and return a list contains: `TRUE/FALSE` depends on whether the `x` value has been found, `x` value, and `x` position indice in `list`|
|2|flatten_list_prime(list)|This function takes an input list and returns a flat list that contains only prime numbers.  For example, the list `[[1, 2], [3, 4]]` would be flattened to the list `[3]`.|
|3|find_prime(list)| Return the largest prime number for a given list.|

## Python Environment

1. binary_search(x, list): In the Python environment, there is [bisect](https://docs.python.org/2/library/bisect.html) that give similar functionality as binary_search, but is not automated and requires extra coding. The binary_search presented here is able to return a list contains whether `x` is in the `list`, `x` value, `x` position indice in `list`.

2. flatten_list_prime(list): In the Python environment, there is a library called [Itertool functions](https://docs.python.org/2/library/itertools.html#itertools.chain) that allows for flattening list, but it does not select for prime numbers.

3. find_prime(list): There is no function that find the largest prime within a list in the Python environment.

## Dependencies

- Python 3 or higher
