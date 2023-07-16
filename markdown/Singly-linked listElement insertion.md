# Singly-linked list/Element insertion

## Task Link
[Rosetta Code - Singly-linked list/Element insertion](https://rosettacode.org/wiki/Singly-linked_list/Element_insertion)

## Java Code
### java_code_1.txt
```java
void insertNode(Node<T> anchor_node, Node<T> new_node)
{
    new_node.next = anchor_node.next;
    anchor_node.next = new_node;
}

```

## Python Code
### python_code_1.txt
```python
def chain_insert(lst, at, item):
    while lst is not None:
        if lst[0] == at:
            lst[1] = [item, lst[1]]
            return
        else:
            lst = lst[1]
    raise ValueError(str(at) + " not found")

chain = ['A', ['B', None]]
chain_insert(chain, 'A', 'C')
print chain

```

### python_code_2.txt
```python
['A', ['C', ['B', None]]]

```

