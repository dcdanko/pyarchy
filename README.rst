===============================
py_archy
===============================


.. image:: https://img.shields.io/pypi/v/py_archy.svg
        :target: https://pypi.python.org/pypi/py_archy


Implementation of the popular node-archy tool in python.

Draws good looking trees and lists on the command line.

* Free software: MIT license
* Documentation: https://py-archy.readthedocs.io.

Input:

```
from pyarchy import pyarchy

tree = { 'nodes' : [{ 'nodes' : ['a','b','c'], 'label' : 'bar'}, 'bizz'], 'label' : 'foo'}
pyarchy(tree, unicode=False)
```
Output:

foo
+-- bar
    +-- a
    +-- b
    `-- c
`-- bizz

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

