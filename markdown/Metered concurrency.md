# Metered concurrency

## Task Link
[Rosetta Code - Metered concurrency](https://rosettacode.org/wiki/Metered_concurrency)

## Java Code
### java_code_1.txt
```java
public class CountingSemaphore{
   private int lockCount = 0;
   private int maxCount;

   CountingSemaphore(int Max){
      maxCount = Max;
   }
  
   public synchronized void acquire() throws InterruptedException{
      while( lockCount >= maxCount){
         wait();
      }
      lockCount++;
   }
   public synchronized void release(){
      if (lockCount > 0)
      {
         lockCount--;
         notifyAll();
      }
   }
   public synchronized int getCount(){
      return lockCount;
   }
}

public class Worker extends Thread{
   private CountingSemaphore lock;
   private int id;

   Worker(CountingSemaphore coordinator, int num){
      lock = coordinator;
      id = num;
   }
   Worker(){
   }
   public void run(){
      try{
         lock.acquire();
         System.out.println("Worker " + id + " has acquired the lock.");
         sleep(2000);
      }
      catch (InterruptedException e){
      }
      finally{
         lock.release();
      }
   }
   public static void main(String[] args){
      CountingSemaphore lock = new CountingSemaphore(3);
      Worker crew[];
      crew = new Worker[5];
      for (int i = 0; i < 5; i++){
         crew[i] = new Worker(lock, i);
         crew[i].start();
      }

   }
}

```

## Python Code
### python_code_1.txt
```python
import time
import threading

# Only 4 workers can run in the same time
sem = threading.Semaphore(4)

workers = []
running = 1


def worker():
    me = threading.currentThread()
    while 1:
        sem.acquire()
        try:
            if not running:
                break
            print '%s acquired semaphore' % me.getName()
            time.sleep(2.0)
        finally:
            sem.release()
        time.sleep(0.01) # Let others acquire

# Start 10 workers
for i in range(10):
    t = threading.Thread(name=str(i), target=worker)
    workers.append(t)
    t.start()

# Main loop
try:
    while 1:
        time.sleep(0.1)
except KeyboardInterrupt:
    running = 0
    for t in workers:
        t.join()

```

