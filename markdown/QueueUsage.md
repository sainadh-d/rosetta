# Queue/Usage

## Task Link
[Rosetta Code - Queue/Usage](https://rosettacode.org/wiki/Queue/Usage)

## Java Code
### java_code_1.txt
```java
import java.util.LinkedList;
import java.util.Queue;
...
Queue<Integer> queue = new LinkedList<Integer>();
System.out.println(queue.isEmpty());      // empty test - true
// queue.remove();       // would throw NoSuchElementException
queue.add(1);
queue.add(2);
queue.add(3);
System.out.println(queue);                // [1, 2, 3]
System.out.println(queue.remove());       // 1
System.out.println(queue);                // [2, 3]
System.out.println(queue.isEmpty());      // false

```

### java_code_2.txt
```java
import java.util.LinkedList;
...
LinkedList queue = new LinkedList();
System.out.println(queue.isEmpty());      // empty test - true
queue.add(new Integer(1));
queue.add(new Integer(2));
queue.add(new Integer(3));
System.out.println(queue);                // [1, 2, 3]
System.out.println(queue.removeFirst());  // 1
System.out.println(queue);                // [2, 3]
System.out.println(queue.isEmpty());      // false

```

## Python Code
### python_code_1.txt
```python
let my_queue = Queue()

my_queue.push!('foo')
my_queue.push!('bar')
my_queue.push!('baz')

print my_queue.pop!() # 'foo'
print my_queue.pop!() # 'bar'
print my_queue.pop!() # 'baz'

```

### python_code_2.txt
```python
import Queue
my_queue = Queue.Queue()
my_queue.put("foo")
my_queue.put("bar")
my_queue.put("baz")
print my_queue.get()  # foo
print my_queue.get()  # bar
print my_queue.get()  # baz

```

