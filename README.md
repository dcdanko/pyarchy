
# PyArchy

Implementation of the popular node-archy tool in python.
Draws good looking trees and lists on the command line.

[![PyPI](https://img.shields.io/pypi/v/nine.svg)](https://pypi.python.org/pypi?name=py_archy&version=1.0.0&:action=display)

[The original Archy on NPM](https://www.npmjs.com/package/archy)

* Free software: MIT license

### Input:

```
from pyarchy import pyarchy

tree = { 'nodes' : [{ 'nodes' : ['a','b','c'], 'label' : 'bar'}, 'bizz'], 'label' : 'foo'}
pyarchy(tree, unicode=False)
```
### Output:
With Unicode
```
foo
└─┬ bar 
  ├── a
  ├── b
  └── c
└── bizz
```
With ASCII
```
foo
+-- bar
    +-- a
    +-- b
    `-- c
`-- bizz
```

### Credits
This package was created with Cookiecutter.

