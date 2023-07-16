# Singly-linked list/Element definition

## Task Link
[Rosetta Code - Singly-linked list/Element definition](https://rosettacode.org/wiki/Singly-linked_list/Element_definition)

## Java Code
### java_code_1.txt
```java
class Link
{
    Link next;
    int data;
}

```

### java_code_2.txt
```java
class Link
{
    Link next;
    int data;
    Link(int a_data, Link a_next) { next = a_next; data = a_data; }
}

```

### java_code_3.txt
```java
 Link small_primes = new Link(2, new Link(3, new Link(5, new Link(7, null))));

```

### java_code_4.txt
```java
class Link<T>
{
  Link<T> next;
  T data;
  Link(T a_data, Link<T> a_next) { next = a_next; data = a_data; }
}

```

## Python Code
### python_code_1.txt
```python
class LinkedList(object):
     """USELESS academic/classroom example of a linked list implemented in Python.
        Don't ever consider using something this crude!  Use the built-in list() type!
     """
	class Node(object):
		def __init__(self, item):
			self.value  = item
			self.next = None
	def __init__(self, item=None):
		if item is not None:
			self.head = Node(item); self.tail = self.head
		else:
			self.head = None; self.tail = None
	def append(self, item):
		if not self.head:
			self.head = Node(item)
			self.tail = self.head
		elif self.tail:
			self.tail.next = Node(item)
			self.tail = self.tail.next
		else:
			self.tail = Node(item)
	def __iter__(self):
		cursor = self.head
		while cursor:
			yield cursor.value
			cursor = cursor.next

```

