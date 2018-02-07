from pyarchy import archy

tree = { 'nodes' : [{ 'nodes' : ['a','b','c'], 'label' : 'bar'}, 'bizz'], 'label' : 'foo'}

print(archy(tree))
print(archy(tree, unicode=False))
