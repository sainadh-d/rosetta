# Atomic updates

## Task Link
[Rosetta Code - Atomic updates](https://rosettacode.org/wiki/Atomic_updates)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

public class AtomicUpdates {

    private static final int NUM_BUCKETS = 10;

    public static class Buckets {
        private final int[] data;

        public Buckets(int[] data) {
            this.data = data.clone();
        }

        public int getBucket(int index) {
            synchronized (data) {
                return data[index];
            }
        }

        public int transfer(int srcIndex, int dstIndex, int amount) {
            if (amount < 0)
                throw new IllegalArgumentException("negative amount: " + amount);
            if (amount == 0)
                return 0;

            synchronized (data) {
                if (data[srcIndex] - amount < 0)
                    amount = data[srcIndex];
                if (data[dstIndex] + amount < 0)
                    amount = Integer.MAX_VALUE - data[dstIndex];
                if (amount < 0)
                    throw new IllegalStateException();
                data[srcIndex] -= amount;
                data[dstIndex] += amount;
                return amount;
            }
        }

        public int[] getBuckets() {
            synchronized (data) {
                return data.clone();
            }
        }
    }

    private static long getTotal(int[] values) {
        long total = 0;
        for (int value : values) {
            total += value;
        }
        return total;
    }

    public static void main(String[] args) {
        ThreadLocalRandom rnd = ThreadLocalRandom.current();

        int[] values = new int[NUM_BUCKETS];
        for (int i = 0; i < values.length; i++)
            values[i] = rnd.nextInt() & Integer.MAX_VALUE;
        System.out.println("Initial Array: " + getTotal(values) + " " + Arrays.toString(values));

        Buckets buckets = new Buckets(values);
        new Thread(() -> equalize(buckets), "equalizer").start();
        new Thread(() -> transferRandomAmount(buckets), "transferrer").start();
        new Thread(() -> print(buckets), "printer").start();
    }

    private static void transferRandomAmount(Buckets buckets) {
        ThreadLocalRandom rnd = ThreadLocalRandom.current();
        while (true) {
            int srcIndex = rnd.nextInt(NUM_BUCKETS);
            int dstIndex = rnd.nextInt(NUM_BUCKETS);
            int amount = rnd.nextInt() & Integer.MAX_VALUE;
            buckets.transfer(srcIndex, dstIndex, amount);
        }
    }

    private static void equalize(Buckets buckets) {
        ThreadLocalRandom rnd = ThreadLocalRandom.current();
        while (true) {
            int srcIndex = rnd.nextInt(NUM_BUCKETS);
            int dstIndex = rnd.nextInt(NUM_BUCKETS);
            int amount = (buckets.getBucket(srcIndex) - buckets.getBucket(dstIndex)) / 2;
            if (amount >= 0)
                buckets.transfer(srcIndex, dstIndex, amount);
        }
    }

    private static void print(Buckets buckets) {
        while (true) {
            long nextPrintTime = System.currentTimeMillis() + 3000;
            long now;
            while ((now = System.currentTimeMillis()) < nextPrintTime) {
                try {
                    Thread.sleep(nextPrintTime - now);
                } catch (InterruptedException e) {
                    return;
                }
            }

            int[] bucketValues = buckets.getBuckets();
            System.out.println("Current values: " + getTotal(bucketValues) + " " + Arrays.toString(bucketValues));
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import with_statement # required for Python 2.5
import threading
import random
import time

terminate = threading.Event()

class Buckets:
    def __init__(self, nbuckets):
        self.nbuckets = nbuckets
        self.values = [random.randrange(10) for i in range(nbuckets)]
        self.lock = threading.Lock()

    def __getitem__(self, i):
        return self.values[i]

    def transfer(self, src, dst, amount):
        with self.lock:
            amount = min(amount, self.values[src])
            self.values[src] -= amount
            self.values[dst] += amount

    def snapshot(self):
        # copy of the current state (synchronized)
        with self.lock:
            return self.values[:]

def randomize(buckets):
    nbuckets = buckets.nbuckets
    while not terminate.isSet():
        src = random.randrange(nbuckets)
        dst = random.randrange(nbuckets)
        if dst!=src:
            amount = random.randrange(20)
            buckets.transfer(src, dst, amount)

def equalize(buckets):
    nbuckets = buckets.nbuckets
    while not terminate.isSet():
        src = random.randrange(nbuckets)
        dst = random.randrange(nbuckets)
        if dst!=src:
            amount = (buckets[src] - buckets[dst]) // 2
            if amount>=0: buckets.transfer(src, dst, amount)
            else: buckets.transfer(dst, src, -amount)

def print_state(buckets):
    snapshot = buckets.snapshot()
    for value in snapshot:
        print '%2d' % value,
    print '=', sum(snapshot)

# create 15 buckets
buckets = Buckets(15)

# the randomize thread
t1 = threading.Thread(target=randomize, args=[buckets])
t1.start()

# the equalize thread
t2 = threading.Thread(target=equalize, args=[buckets])
t2.start()

# main thread, display
try:
    while True:
        print_state(buckets)
        time.sleep(1)
except KeyboardInterrupt: # ^C to finish
    terminate.set()

# wait until all worker threads finish
t1.join()
t2.join()

```

