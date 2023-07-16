# Stack

## Task Link
[Rosetta Code - Stack](https://rosettacode.org/wiki/Stack)

## Java Code
### java_code_1.txt
```java
import java.util.Stack;

public class StackTest {
    public static void main( final String[] args ) {
        final Stack<String> stack = new Stack<String>();

        System.out.println( "New stack empty? " + stack.empty() );

        stack.push( "There can be only one" );
        System.out.println( "Pushed stack empty? " + stack.empty() );
        System.out.println( "Popped single entry: " + stack.pop() );

        stack.push( "First" );
        stack.push( "Second" );
        System.out.println( "Popped entry should be second: " + stack.pop() );

        // Popping an empty stack will throw...
        stack.pop();
        stack.pop();
    }
}

```

### java_code_2.txt
```java
public class Stack{
    private Node first = null;
    public boolean isEmpty(){
        return first == null;
    }
    public Object Pop(){
        if(isEmpty()) 
            throw new Exception("Can't Pop from an empty Stack.");
        else{
            Object temp = first.value;
            first = first.next;
            return temp;
        }
    }
    public void Push(Object o){
        first = new Node(o, first);
    }
    class Node{
        public Node next;
        public Object value;
        public Node(Object value){
            this(value, null); 
        }
        public Node(Object value, Node next){
            this.next = next;
            this.value = value;
        }
    }
}

```

### java_code_3.txt
```java
public class Stack<T>{
    private Node first = null;
    public boolean isEmpty(){
        return first == null;
    }
    public T Pop(){
        if(isEmpty()) 
            throw new Exception("Can't Pop from an empty Stack.");
        else{
            T temp = first.value;
            first = first.next;
            return temp;
        }
    }
    public void Push(T o){
        first = new Node(o, first);
    }
    class Node{
        public Node next;
        public T value;
        public Node(T value){
            this(value, null); 
        }
        public Node(T value, Node next){
            this.next = next;
            this.value = value;
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import deque
stack = deque()
stack.append(value) # pushing
value = stack.pop()
not stack # is empty?

```

### python_code_2.txt
```python
from collections import deque

class Stack:
    def __init__(self):
        self._items = deque()
    def append(self, item):
        self._items.append(item)
    def pop(self):
        return self._items.pop()
    def __nonzero__(self):
        return bool(self._items)

```

### python_code_3.txt
```python
class Stack:
    def __init__(self):
        self._first = None
    def __nonzero__(self):
        return self._first is not None 
    def append(self, value):
        self._first = (value, self._first)
    def pop(self):
        if self._first is None:
            raise IndexError, "pop from empty stack"
        value, self._first = self._first
        return value

```

### python_code_4.txt
```python
while not stack.empty():

```

### python_code_5.txt
```python
while stack:

```

