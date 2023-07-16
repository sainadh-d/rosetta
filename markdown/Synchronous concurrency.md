# Synchronous concurrency

## Task Link
[Rosetta Code - Synchronous concurrency](https://rosettacode.org/wiki/Synchronous_concurrency)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicLong;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

class SynchronousConcurrency
{
  public static void main(String[] args) throws Exception
  {
    final AtomicLong lineCount = new AtomicLong(0);
    final BlockingQueue<String> queue = new LinkedBlockingQueue<String>();
    final String EOF = new String();
    
    final Thread writerThread = new Thread(new Runnable() {
        public void run()
        {
          long linesWrote = 0;
          while (true)
          {
            try
            {
              String line = queue.take();
              // Reference equality
              if (line == EOF)
                break;
              System.out.println(line);
              linesWrote++;
            }
            catch (InterruptedException ie)
            {  }
          }
          lineCount.set(linesWrote);
        }
      }
    );
    writerThread.start();
    
    // No need to start a third thread for the reader, just use this thread
    BufferedReader br = new BufferedReader(new FileReader("input.txt"));
    String line;
    while ((line = br.readLine()) != null)
      queue.put(line);
    br.close();
    queue.put(EOF);
    writerThread.join();
    // AtomicLong is not needed here due to memory barrier created by thread join, but still need a mutable long since lineCount must be final to access it from an anonymous class
    System.out.println("Line count: " + lineCount.get());
    return;
  }
}

```

## Python Code
### python_code_1.txt
```python
import sys
from Queue import Queue
from threading import Thread

lines = Queue(1)
count = Queue(1)

def read(file):
    try:
        for line in file:
            lines.put(line)
    finally:
        lines.put(None)
    print count.get()

def write(file):
    n = 0
    while 1:
        line = lines.get()
        if line is None:
            break
        file.write(line)
        n += 1
    count.put(n)

reader = Thread(target=read, args=(open('input.txt'),))
writer = Thread(target=write, args=(sys.stdout,))
reader.start()
writer.start()
reader.join()
writer.join()

```

### python_code_2.txt
```python
count = 0

def reader():
    for line in open('input.txt'):
        yield line.rstrip()
    print('Printed %d lines.' % count)

r = reader() 
# printer
for line in r:
    print(line)
    count += 1

```

### python_code_3.txt
```python
def reader():
    for line in open('input.txt'):
        yield line.rstrip()
    count = yield None
    print('Printed %d lines.' % count)
 
r = reader() 

# printer
for count, line in enumerate(r):
    if line is None:
        break
    print(line)
try: 
    r.send(count)
except StopIteration: 
    pass

```

