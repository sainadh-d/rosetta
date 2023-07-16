# Time a function

## Task Link
[Rosetta Code - Time a function](https://rosettacode.org/wiki/Time_a_function)

## Java Code
### java_code_1.txt
```java
long start = System.currentTimeMillis();
/* code you want to time, here */
long duration = System.currentTimeMillis() - start;

```

### java_code_2.txt
```java
import java.lang.management.ManagementFactory;
import java.lang.management.ThreadMXBean;

public class TimeIt {
	public static void main(String[] args) {
		final ThreadMXBean threadMX = ManagementFactory.getThreadMXBean();
		assert threadMX.isCurrentThreadCpuTimeSupported();
		threadMX.setThreadCpuTimeEnabled(true);
		
		long start, end;
		start = threadMX.getCurrentThreadCpuTime();
		countTo(100000000);
		end = threadMX.getCurrentThreadCpuTime();
		System.out.println("Counting to 100000000 takes "+(end-start)/1000000+"ms");
		start = threadMX.getCurrentThreadCpuTime();
		countTo(1000000000L);
		end = threadMX.getCurrentThreadCpuTime();
		System.out.println("Counting to 1000000000 takes "+(end-start)/1000000+"ms");
 
	}
 
	public static void countTo(long x){
		System.out.println("Counting...");
		for(long i=0;i<x;i++);
		System.out.println("Done!");
	}
}

```

### java_code_3.txt
```java
	public static void main(String[] args){
		long start, end;
		start = System.currentTimeMillis();
		countTo(100000000);
		end = System.currentTimeMillis();
		System.out.println("Counting to 100000000 takes "+(end-start)+"ms");
		start = System.currentTimeMillis();
		countTo(1000000000L);
		end = System.currentTimeMillis();
		System.out.println("Counting to 1000000000 takes "+(end-start)+"ms");

	}

```

## Python Code
### python_code_1.txt
```python
import sys, timeit
def usec(function, arguments):
    modname, funcname = __name__, function.__name__
    timer = timeit.Timer(stmt='%(funcname)s(*args)' % vars(),
                         setup='from %(modname)s import %(funcname)s; args=%(arguments)r' % vars())
    try:
        t, N = 0, 1
        while t < 0.2:            
            t = min(timer.repeat(repeat=3, number=N))            
            N *= 10
        microseconds = round(10000000 * t / N, 1) # per loop
        return microseconds 
    except:
        timer.print_exc(file=sys.stderr)
        raise

from math import pow
def nothing(): pass
def identity(x): return x

```

### python_code_2.txt
```python
time 1+1
30000/1000000  # in microseconds
=> 2

```

