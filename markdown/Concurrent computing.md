# Concurrent computing

## Task Link
[Rosetta Code - Concurrent computing](https://rosettacode.org/wiki/Concurrent_computing)

## Java Code
### java_code_1.txt
```java
Thread[] threads = new Thread[3];
threads[0] = new Thread(() -> System.out.println("enjoy"));
threads[1] = new Thread(() -> System.out.println("rosetta"));
threads[2] = new Thread(() -> System.out.println("code"));
Collections.shuffle(Arrays.asList(threads));
for (Thread thread : threads)
    thread.start();

```

### java_code_2.txt
```java
import java.util.concurrent.CyclicBarrier;

public class Threads
{
  public static class DelayedMessagePrinter implements Runnable
  {
    private CyclicBarrier barrier;
    private String msg;
    
    public DelayedMessagePrinter(CyclicBarrier barrier, String msg)
    {
      this.barrier = barrier;
      this.msg = msg;
    }
    
    public void run()
    {
      try
      {  barrier.await();  }
      catch (Exception e)
      {  }
      System.out.println(msg);
    }
  }
  
  public static void main(String[] args)
  {
    CyclicBarrier barrier = new CyclicBarrier(3);
    new Thread(new DelayedMessagePrinter(barrier, "Enjoy")).start();
    new Thread(new DelayedMessagePrinter(barrier, "Rosetta")).start();
    new Thread(new DelayedMessagePrinter(barrier, "Code")).start();
  }
}

```

## Python Code
### python_code_1.txt
```python
let words = ["Enjoy", "Rosetta", "Code"]

for word in words:
    (word) |> async (w) =>
        sleep(random())
        print(w)

```

### python_code_2.txt
```python
import asyncio


async def print_(string: str) -> None:
    print(string)


async def main():
    strings = ['Enjoy', 'Rosetta', 'Code']
    coroutines = map(print_, strings)
    await asyncio.gather(*coroutines)


if __name__ == '__main__':
    asyncio.run(main())

```

### python_code_3.txt
```python
Python 3.2 (r32:88445, Feb 20 2011, 21:30:00) [MSC v.1500 64 bit (AMD64)] on win 32
Type "help", "copyright", "credits" or "license" for more information.
>>> from concurrent import futures
>>> with futures.ProcessPoolExecutor() as executor:
...   _ = list(executor.map(print, 'Enjoy Rosetta Code'.split()))
...
Enjoy
Rosetta
Code
>>>

```

### python_code_4.txt
```python
import threading
import random
 
def echo(text):
    print(text)
 
threading.Timer(random.random(), echo, ("Enjoy",)).start()
threading.Timer(random.random(), echo, ("Rosetta",)).start()
threading.Timer(random.random(), echo, ("Code",)).start()

```

### python_code_5.txt
```python
import threading
import random

def echo(text):
    print(text)

for text in ["Enjoy", "Rosetta", "Code"]:
    threading.Timer(random.random(), echo, (text,)).start()

```

### python_code_6.txt
```python
import random, sys, time
import threading

lock = threading.Lock()

def echo(s):
    time.sleep(1e-2*random.random())
    # use `.write()` with lock due to `print` prints empty lines occasionally
    with lock:
        sys.stdout.write(s)
        sys.stdout.write('\n')

for line in 'Enjoy Rosetta Code'.split():
    threading.Thread(target=echo, args=(line,)).start()

```

### python_code_7.txt
```python
from __future__ import print_function
from multiprocessing import Pool

def main():
    p = Pool()
    p.map(print, 'Enjoy Rosetta Code'.split())

if __name__=="__main__":
    main()

```

### python_code_8.txt
```python
import random
from twisted.internet    import reactor, task, defer
from twisted.python.util import println

delay = lambda: 1e-4*random.random()
d = defer.DeferredList([task.deferLater(reactor, delay(), println, line)
                        for line in 'Enjoy Rosetta Code'.split()])
d.addBoth(lambda _: reactor.stop())
reactor.run()

```

### python_code_9.txt
```python
from __future__ import print_function
import random
import gevent

delay = lambda: 1e-4*random.random()
gevent.joinall([gevent.spawn_later(delay(), print, line)
               for line in 'Enjoy Rosetta Code'.split()])

```

