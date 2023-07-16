# Doubly-linked list/Element definition

## Task Link
[Rosetta Code - Doubly-linked list/Element definition](https://rosettacode.org/wiki/Doubly-linked_list/Element_definition)

## Java Code
### java_code_1.txt
```java
public class Node<T> {
   private T element;
   private Node<T> next, prev;

   public Node<T>(){
      next = prev = element = null;
   }

   public Node<T>(Node<T> n, Node<T> p, T elem){
      next = n;
      prev = p;
      element = elem;
   }

   public void setNext(Node<T> n){
      next = n;
   }

   public Node<T> getNext(){
      return next;
   }

   public void setElem(T elem){
      element = elem;
   }

   public T getElem(){
      return element;
   }

   public void setNext(Node<T> n){
      next = n;
   }

   public Node<T> setPrev(Node<T> p){
      prev = p;
   }

   public getPrev(){
      return prev;
   }
}

```

## Python Code
### python_code_1.txt
```python
class Node(object):
     def __init__(self, data = None, prev = None, next = None):
         self.prev = prev
         self.next = next
         self.data = data
     def __str__(self):
         return str(self.data)
     def __repr__(self):
         return repr(self.data)
     def iter_forward(self):
         c = self
         while c != None:
             yield c
             c = c.next
     def iter_backward(self):
         c = self
         while c != None:
             yield c
             c = c.prev

```

