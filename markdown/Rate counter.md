# Rate counter

## Task Link
[Rosetta Code - Rate counter](https://rosettacode.org/wiki/Rate_counter)

## Java Code
### java_code_1.txt
```java
import java.util.function.Consumer;

public class RateCounter {

    public static void main(String[] args) {
        for (double d : benchmark(10, x -> System.out.print(""), 10))
            System.out.println(d);
    }

    static double[] benchmark(int n, Consumer<Integer> f, int arg) {
        double[] timings = new double[n];
        for (int i = 0; i < n; i++) {
            long time = System.nanoTime();
            f.accept(arg);
            timings[i] = System.nanoTime() - time;
        }
        return timings;
    }
}

```

### java_code_2.txt
```java
import java.util.function.IntConsumer;
import java.util.stream.DoubleStream;

import static java.lang.System.nanoTime;
import static java.util.stream.DoubleStream.generate;

import static java.lang.System.out;

public interface RateCounter {
  public static void main(final String... arguments) {
    benchmark(
      10,
      x -> out.print(""),
      10
    )
      .forEach(out::println)
    ;
  }

  public static DoubleStream benchmark(
    final int n,
    final IntConsumer consumer,
    final int argument
  ) {
    return generate(() -> {
      final long time = nanoTime();
      consumer.accept(argument);
      return nanoTime() - time;
    })
      .limit(n)
    ;
  }
}

```

## Python Code
### python_code_1.txt
```python
import subprocess
import time

class Tlogger(object):
    def __init__(self):
        self.counts = 0
        self.tottime = 0.0
        self.laststart = 0.0
        self.lastreport = time.time()

    def logstart(self):
        self.laststart = time.time()

    def logend(self):
        self.counts +=1
        self.tottime += (time.time()-self.laststart)
        if (time.time()-self.lastreport)>5.0:   # report once every 5 seconds
           self.report()

    def report(self):
        if ( self.counts > 4*self.tottime):
            print "Subtask execution rate: %f times/second"% (self.counts/self.tottime);
        else:
            print "Average execution time: %f seconds"%(self.tottime/self.counts);
        self.lastreport = time.time()


def taskTimer( n, subproc_args ):
    logger = Tlogger()

    for x in range(n):
        logger.logstart()
        p = subprocess.Popen(subproc_args)
        p.wait()
        logger.logend()
    logger.report()


import timeit
import sys

def main( ):

    # for accurate timing of code segments 
    s = """j = [4*n for n in range(50)]"""
    timer = timeit.Timer(s)
    rzlts = timer.repeat(5, 5000)
    for t in rzlts:
        print "Time for 5000 executions of statement = ",t
    
    # subprocess execution timing
    print "#times:",sys.argv[1]
    print "Command:",sys.argv[2:]
    print ""
    for k in range(3):
       taskTimer( int(sys.argv[1]), sys.argv[2:])

main()

```

