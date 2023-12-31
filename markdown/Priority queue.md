# Priority queue

## Task Link
[Rosetta Code - Priority queue](https://rosettacode.org/wiki/Priority_queue)

## Java Code
### java_code_1.txt
```java
import java.util.PriorityQueue;

class Task implements Comparable<Task> {
    final int priority;
    final String name;

    public Task(int p, String n) {
        priority = p;
        name = n;
    }

    public String toString() {
        return priority + ", " + name;
    }

    public int compareTo(Task other) {
        return priority < other.priority ? -1 : priority > other.priority ? 1 : 0;
    }

    public static void main(String[] args) {
        PriorityQueue<Task> pq = new PriorityQueue<Task>();
        pq.add(new Task(3, "Clear drains"));
        pq.add(new Task(4, "Feed cat"));
        pq.add(new Task(5, "Make tea"));
        pq.add(new Task(1, "Solve RC tasks"));
        pq.add(new Task(2, "Tax return"));

        while (!pq.isEmpty())
            System.out.println(pq.remove());
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> import queue
>>> pq = queue.PriorityQueue()
>>> for item in ((3, "Clear drains"), (4, "Feed cat"), (5, "Make tea"), (1, "Solve RC tasks"), (2, "Tax return")):
  pq.put(item)

  
>>> while not pq.empty():
  print(pq.get_nowait())

  
(1, 'Solve RC tasks')
(2, 'Tax return')
(3, 'Clear drains')
(4, 'Feed cat')
(5, 'Make tea')
>>>

```

### python_code_2.txt
```python
>>> import queue
>>> help(queue.PriorityQueue)
Help on class PriorityQueue in module queue:

class PriorityQueue(Queue)
 |  Variant of Queue that retrieves open entries in priority order (lowest first).
 |  
 |  Entries are typically tuples of the form:  (priority number, data).
 |  
 |  Method resolution order:
 |      PriorityQueue
 |      Queue
 |      builtins.object
 |  
 |  Methods inherited from Queue:
 |  
 |  __init__(self, maxsize=0)
 |  
 |  empty(self)
 |      Return True if the queue is empty, False otherwise (not reliable!).
 |      
 |      This method is likely to be removed at some point.  Use qsize() == 0
 |      as a direct substitute, but be aware that either approach risks a race
 |      condition where a queue can grow before the result of empty() or
 |      qsize() can be used.
 |      
 |      To create code that needs to wait for all queued tasks to be
 |      completed, the preferred technique is to use the join() method.
 |  
 |  full(self)
 |      Return True if the queue is full, False otherwise (not reliable!).
 |      
 |      This method is likely to be removed at some point.  Use qsize() >= n
 |      as a direct substitute, but be aware that either approach risks a race
 |      condition where a queue can shrink before the result of full() or
 |      qsize() can be used.
 |  
 |  get(self, block=True, timeout=None)
 |      Remove and return an item from the queue.
 |      
 |      If optional args 'block' is true and 'timeout' is None (the default),
 |      block if necessary until an item is available. If 'timeout' is
 |      a positive number, it blocks at most 'timeout' seconds and raises
 |      the Empty exception if no item was available within that time.
 |      Otherwise ('block' is false), return an item if one is immediately
 |      available, else raise the Empty exception ('timeout' is ignored
 |      in that case).
 |  
 |  get_nowait(self)
 |      Remove and return an item from the queue without blocking.
 |      
 |      Only get an item if one is immediately available. Otherwise
 |      raise the Empty exception.
 |  
 |  join(self)
 |      Blocks until all items in the Queue have been gotten and processed.
 |      
 |      The count of unfinished tasks goes up whenever an item is added to the
 |      queue. The count goes down whenever a consumer thread calls task_done()
 |      to indicate the item was retrieved and all work on it is complete.
 |      
 |      When the count of unfinished tasks drops to zero, join() unblocks.
 |  
 |  put(self, item, block=True, timeout=None)
 |      Put an item into the queue.
 |      
 |      If optional args 'block' is true and 'timeout' is None (the default),
 |      block if necessary until a free slot is available. If 'timeout' is
 |      a positive number, it blocks at most 'timeout' seconds and raises
 |      the Full exception if no free slot was available within that time.
 |      Otherwise ('block' is false), put an item on the queue if a free slot
 |      is immediately available, else raise the Full exception ('timeout'
 |      is ignored in that case).
 |  
 |  put_nowait(self, item)
 |      Put an item into the queue without blocking.
 |      
 |      Only enqueue the item if a free slot is immediately available.
 |      Otherwise raise the Full exception.
 |  
 |  qsize(self)
 |      Return the approximate size of the queue (not reliable!).
 |  
 |  task_done(self)
 |      Indicate that a formerly enqueued task is complete.
 |      
 |      Used by Queue consumer threads.  For each get() used to fetch a task,
 |      a subsequent call to task_done() tells the queue that the processing
 |      on the task is complete.
 |      
 |      If a join() is currently blocking, it will resume when all items
 |      have been processed (meaning that a task_done() call was received
 |      for every item that had been put() into the queue).
 |      
 |      Raises a ValueError if called more times than there were items
 |      placed in the queue.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Queue:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

>>>

```

### python_code_3.txt
```python
>>> from heapq import heappush, heappop, heapify
>>> items = [(3, "Clear drains"), (4, "Feed cat"), (5, "Make tea"), (1, "Solve RC tasks"), (2, "Tax return")]
>>> heapify(items)
>>> while items:
  print(heappop(items))

  
(1, 'Solve RC tasks')
(2, 'Tax return')
(3, 'Clear drains')
(4, 'Feed cat')
(5, 'Make tea')
>>>

```

### python_code_4.txt
```python
>>> help('heapq')
Help on module heapq:

NAME
    heapq - Heap queue algorithm (a.k.a. priority queue).

DESCRIPTION
    Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
    all k, counting elements from 0.  For the sake of comparison,
    non-existing elements are considered to be infinite.  The interesting
    property of a heap is that a[0] is always its smallest element.
    
    Usage:
    
    heap = []            # creates an empty heap
    heappush(heap, item) # pushes a new item on the heap
    item = heappop(heap) # pops the smallest item from the heap
    item = heap[0]       # smallest item on the heap without popping it
    heapify(x)           # transforms list into a heap, in-place, in linear time
    item = heapreplace(heap, item) # pops and returns smallest item, and adds
                                   # new item; the heap size is unchanged
    
    Our API differs from textbook heap algorithms as follows:
    
    - We use 0-based indexing.  This makes the relationship between the
      index for a node and the indexes for its children slightly less
      obvious, but is more suitable since Python uses 0-based indexing.
    
    - Our heappop() method returns the smallest item, not the largest.
    
    These two make it possible to view the heap as a regular Python list
    without surprises: heap[0] is the smallest item, and heap.sort()
    maintains the heap invariant!

FUNCTIONS
    heapify(...)
        Transform list into a heap, in-place, in O(len(heap)) time.
    
    heappop(...)
        Pop the smallest item off the heap, maintaining the heap invariant.
    
    heappush(...)
        Push item onto heap, maintaining the heap invariant.
    
    heappushpop(...)
        Push item on the heap, then pop and return the smallest item
        from the heap. The combined action runs more efficiently than
        heappush() followed by a separate call to heappop().
    
    heapreplace(...)
        Pop and return the current smallest value, and add the new item.
        
        This is more efficient than heappop() followed by heappush(), and can be
        more appropriate when using a fixed-size heap.  Note that the value
        returned may be larger than item!  That constrains reasonable uses of
        this routine unless written as part of a conditional replacement:
        
            if item > heap[0]:
                item = heapreplace(heap, item)
    
    merge(*iterables)
        Merge multiple sorted inputs into a single sorted output.
        
        Similar to sorted(itertools.chain(*iterables)) but returns a generator,
        does not pull the data into memory all at once, and assumes that each of
        the input streams is already sorted (smallest to largest).
        
        >>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
        [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]
    
    nlargest(n, iterable, key=None)
        Find the n largest elements in a dataset.
        
        Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]
    
    nsmallest(n, iterable, key=None)
        Find the n smallest elements in a dataset.
        
        Equivalent to:  sorted(iterable, key=key)[:n]

DATA
    __about__ = 'Heap queues\n\n[explanation by François Pinard]\n\nH... t...
    __all__ = ['heappush', 'heappop', 'heapify', 'heapreplace', 'merge', '...

FILE
    c:\python32\lib\heapq.py


>>>

```

