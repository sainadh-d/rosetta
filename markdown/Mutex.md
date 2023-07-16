# Mutex

## Task Link
[Rosetta Code - Mutex](https://rosettacode.org/wiki/Mutex)

## Java Code
### java_code_1.txt
```java
import java.util.concurrent.Semaphore;

public class VolatileClass{
   public Semaphore mutex = new Semaphore(1); //also a "fair" boolean may be passed which,
                                              //when true, queues requests for the lock
   public void needsToBeSynched(){
      //...
   }
   //delegate methods could be added for acquiring and releasing the mutex
}

```

### java_code_2.txt
```java
public class TestVolitileClass throws Exception{
   public static void main(String[] args){
      VolatileClass vc = new VolatileClass();
      vc.mutex.acquire(); //will wait automatically if another class has the mutex
                          //can be interrupted similarly to a Thread
                          //use acquireUninterruptibly() to avoid that
      vc.needsToBeSynched();
      vc.mutex.release();
   }
}

```

### java_code_3.txt
```java
public class Main {
    static Object mutex = new Object();
    static int i = 0;

    public void addAndPrint()
    {
        System.out.print("" + i + " + 1 = ");
        i++;
        System.out.println("" + i);
    }

    public void subAndPrint()
    {
        System.out.print("" + i + " - 1 = ");
        i--;
        System.out.println("" + i);
    }


    public static void main(String[] args){
        final Main m = new Main();
        new Thread() {
            public void run()
            {
                while (true) { synchronized(m.mutex) { m.addAndPrint(); } }
            }
        }.start();
        new Thread() {
            public void run()
            {
                while (true) { synchronized(m.mutex) { m.subAndPrint(); } }
            }
        }.start();
    }
}

```

## Python Code
### python_code_1.txt
```python
import threading
from time import sleep

# res: max number of resources. If changed to 1, it functions
# identically to a mutex/lock object
res = 2
sema = threading.Semaphore(res)

class res_thread(threading.Thread):
    def run(self):
        global res
        n = self.getName()
        for i in range(1, 4):
            # acquire a resource if available and work hard
            # for 2 seconds.  if all res are occupied, block
            # and wait
            sema.acquire()
            res = res - 1
            print n, "+  res count", res
            sleep(2)

                        # after done with resource, return it to pool and flag so
            res = res + 1
            print n, "-  res count", res
            sema.release()

# create 4 threads, each acquire resorce and work
for i in range(1, 5):
    t = res_thread()
    t.start()

```

