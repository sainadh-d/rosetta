# Handle a signal

## Task Link
[Rosetta Code - Handle a signal](https://rosettacode.org/wiki/Handle_a_signal)

## Java Code
### java_code_1.txt
```java
import sun.misc.Signal;
import sun.misc.SignalHandler;

public class ExampleSignalHandler {
    public static void main(String... args) throws InterruptedException {
        final long start = System.nanoTime();
        Signal.handle(new Signal("INT"), new SignalHandler() {
            public void handle(Signal sig) {
                System.out.format("\nProgram execution took %f seconds\n", (System.nanoTime() - start) / 1e9f);
                System.exit(0);
            }
        });
        int counter = 0;
        while(true) {
            System.out.println(counter++);
            Thread.sleep(500);
        }
    }
}

```

### java_code_2.txt
```java
public class ExampleSignalHandler {
    public static void main(String... args) throws InterruptedException {
        final long start = System.nanoTime();
        Runtime.getRuntime().addShutdownHook(new Thread(new Runnable() {
            public void run() {
                System.out.format("\nProgram execution took %f seconds\n", (System.nanoTime() - start) / 1e9f);
            }
        }));
        int counter = 0;
        while(true) {
            System.out.println(counter++);
            Thread.sleep(500);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import time

def counter():
    n = 0
    t1 = time.time()
    while True:
        try:
            time.sleep(0.5)
            n += 1
            print n
        except KeyboardInterrupt, e:
            print 'Program has run for %5.3f seconds.' % (time.time() - t1)
            break

counter()

```

### python_code_2.txt
```python
import time

def intrptWIN():
   procDone = False
   n = 0

   while not procDone:
      try:
         time.sleep(0.5)
         n += 1
         print n
      except KeyboardInterrupt, e:
         procDone = True

t1 = time.time()
intrptWIN()
tdelt = time.time() - t1
print 'Program has run for %5.3f seconds.' % tdelt

```

### python_code_3.txt
```python
import signal, time, threading
done = False
n = 0

def counter():
   global n, timer
   n += 1
   print n
   timer = threading.Timer(0.5, counter)
   timer.start()

def sigIntHandler(signum, frame):
   global done
   timer.cancel()
   done = True

def intrptUNIX():
   global timer
   signal.signal(signal.SIGINT, sigIntHandler)

   timer = threading.Timer(0.5, counter)
   timer.start()
   while not done:
      signal.pause()

t1 = time.time()
intrptUNIX()
tdelt = time.time() - t1
print 'Program has run for %5.3f seconds.' % tdelt

```

### python_code_4.txt
```python
import time, signal

class WeAreDoneException(Exception):
    pass

def sigIntHandler(signum, frame):
    signal.signal(signal.SIGINT, signal.SIG_DFL) # resets to default handler
    raise WeAreDoneException

t1 = time.time()

try:
    signal.signal(signal.SIGINT, sigIntHandler)
    n = 0
    while True:
        time.sleep(0.5)
        n += 1
        print n
except WeAreDoneException:
    pass

tdelt = time.time() - t1
print 'Program has run for %5.3f seconds.' % tdelt

```

