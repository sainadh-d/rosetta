# Doubly-linked list/Traversal

## Task Link
[Rosetta Code - Doubly-linked list/Traversal](https://rosettacode.org/wiki/Doubly-linked_list/Traversal)

## Java Code
### java_code_1.txt
```java
package com.rosettacode;

import java.util.LinkedList;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class DoubleLinkedListTraversing {

  public static void main(String[] args) {

    final LinkedList<String> doubleLinkedList =
        IntStream.range(1, 10)
            .mapToObj(String::valueOf)
            .collect(Collectors.toCollection(LinkedList::new));

    doubleLinkedList.iterator().forEachRemaining(System.out::print);
    System.out.println();
    doubleLinkedList.descendingIterator().forEachRemaining(System.out::print);
  }
}

```

## Python Code
### python_code_1.txt
```python
class List:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def append(self, data):
        if self.next == None:
            self.next = List(data, None, self)
            return self.next
        else:
            return self.next.append(data)

# Build the list
tail = head = List(10)
for i in [ 20, 30, 40 ]:
    tail = tail.append(i)

# Traverse forwards
node = head
while node != None:
    print(node.data)
    node = node.next

# Traverse Backwards
node = tail
while node != None:
    print(node.data)
    node = node.prev

```

### python_code_2.txt
```python
l = [ 10, 20, 30, 40 ]
for i in l:
    print(i)
for i in reversed(l):    # reversed produces an iterator, so only O(1) memory is used
    print(i)

```

