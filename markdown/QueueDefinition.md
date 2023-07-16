# Queue/Definition

## Task Link
[Rosetta Code - Queue/Definition](https://rosettacode.org/wiki/Queue/Definition)

## Java Code
### java_code_1.txt
```java
public class Queue<E>{
    Node<E> head = null, tail = null;

    static class Node<E>{
        E value;
        Node<E> next;

        Node(E value, Node<E> next){
            this.value= value;
            this.next= next;
        }

    }

    public Queue(){
    }

    public void enqueue(E value){ //standard queue name for "push"
        Node<E> newNode= new Node<E>(value, null);
        if(empty()){
            head= newNode;
        }else{
            tail.next = newNode;
        }
        tail= newNode;
    }

    public E dequeue() throws java.util.NoSuchElementException{//standard queue name for "pop"
        if(empty()){
            throw new java.util.NoSuchElementException("No more elements.");
        }
        E retVal= head.value;
        head= head.next;
        return retVal;
    } 

    public boolean empty(){
        return head == null;
    }
}

```

## Python Code
### python_code_1.txt
```python
   class FIFO(object):
       def __init__(self, *args):
           self.contents = list(args)
       def __call__(self):
           return self.pop()
       def __len__(self):
           return len(self.contents)
       def pop(self):
           return self.contents.pop(0)
       def push(self, item):
           self.contents.append(item)
       def extend(self,*itemlist):
           self.contents += itemlist
       def empty(self):
           return bool(self.contents)
       def __iter__(self):
           return self
       def next(self):
           if self.empty():
               raise StopIteration
           return self.pop()

if __name__ == "__main__":
    # Sample usage:
    f = FIFO()
    f.push(3)
    f.push(2)
    f.push(1)
    while not f.empty():
        print f.pop(),
    # >>> 3 2 1
    # Another simple example gives the same results:
    f = FIFO(3,2,1)
    while not f.empty():
        print f(),
    # Another using the default "truth" value of the object
    # (implicitly calls on the length() of the object after
    # checking for a __nonzero__ method
    f = FIFO(3,2,1)
    while f:
        print f(),
    # Yet another, using more Pythonic iteration:
    f = FIFO(3,2,1)
    for i in f:
        print i,

```

### python_code_2.txt
```python
class FIFO:  ## NOT a new-style class, must not derive from "object"
   def __init__(self,*args):
       self.contents = list(args)
   def __call__(self):
       return self.pop()
   def empty(self):
       return bool(self.contents)
   def pop(self):
       return self.contents.pop(0)
   def __getattr__(self, attr):
       return getattr(self.contents,attr)
   def next(self):
       if not self:
           raise StopIteration
       return self.pop()

```

### python_code_3.txt
```python
from collections import deque
fifo = deque()
fifo. appendleft(value) # push
value = fifo.pop()
not fifo # empty
fifo.pop() # raises IndexError when empty

```

