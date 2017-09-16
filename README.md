
# PyArchy

Implementation of the popular node-archy tool in python.
Draws good looking trees and lists on the command line.

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

