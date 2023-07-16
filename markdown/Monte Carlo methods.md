# Monte Carlo methods

## Task Link
[Rosetta Code - Monte Carlo methods](https://rosettacode.org/wiki/Monte_Carlo_methods)

## Java Code
### java_code_1.txt
```java
public class MC {
	public static void main(String[] args) {
		System.out.println(getPi(10000));
		System.out.println(getPi(100000));
		System.out.println(getPi(1000000));
		System.out.println(getPi(10000000));
		System.out.println(getPi(100000000));
		
	}
	public static double getPi(int numThrows){
		int inCircle= 0;
		for(int i= 0;i < numThrows;i++){
			//a square with a side of length 2 centered at 0 has 
			//x and y range of -1 to 1
			double randX= (Math.random() * 2) - 1;//range -1 to 1
			double randY= (Math.random() * 2) - 1;//range -1 to 1
			//distance from (0,0) = sqrt((x-0)^2+(y-0)^2)
			double dist= Math.sqrt(randX * randX + randY * randY);
			//^ or in Java 1.5+: double dist= Math.hypot(randX, randY);
			if(dist < 1){//circle with diameter of 2 has radius of 1
				inCircle++;
			}
		}
		return 4.0 * inCircle / numThrows;
	}
}

```

### java_code_2.txt
```java
package montecarlo;

import java.util.stream.IntStream;
import java.util.stream.DoubleStream;

import static java.lang.Math.random;
import static java.lang.Math.hypot;
import static java.lang.System.out;

public interface MonteCarlo {
  public static void main(String... arguments) {
    IntStream.of(
      10000,
      100000,
      1000000,
      10000000,
      100000000
    )
      .mapToDouble(MonteCarlo::pi)
      .forEach(out::println)
    ;
  }

  public static double range() {
    //a square with a side of length 2 centered at 0 has 
    //x and y range of -1 to 1
    return (random() * 2) - 1;
  }

  public static double pi(int numThrows){
    long inCircle = DoubleStream.generate(
      //distance from (0,0) = hypot(x, y)
      () -> hypot(range(), range())
    )
      .limit(numThrows)
      .unordered()
      .parallel()
      //circle with diameter of 2 has radius of 1
      .filter(d -> d < 1)
      .count()
    ;
    return (4.0 * inCircle) / numThrows;
  }
}

```

## Python Code
### python_code_1.txt
```python
>>> import random, math
>>> throws = 1000
>>> 4.0 * sum(math.hypot(*[random.random()*2-1
	                 for q in [0,1]]) < 1
              for p in xrange(throws)) / float(throws)
3.1520000000000001
>>> throws = 1000000
>>> 4.0 * sum(math.hypot(*[random.random()*2-1
	                 for q in [0,1]]) < 1
              for p in xrange(throws)) / float(throws)
3.1396359999999999
>>> throws = 100000000
>>> 4.0 * sum(math.hypot(*[random.random()*2-1
	                 for q in [0,1]]) < 1
              for p in xrange(throws)) / float(throws)
3.1415666400000002

```

### python_code_2.txt
```python
from random import random
from math import hypot
try:
    import psyco
    psyco.full()
except:
    pass

def pi(nthrows):
    inside = 0
    for i in xrange(nthrows):
        if hypot(random(), random()) < 1:
            inside += 1
    return 4.0 * inside / nthrows

for n in [10**4, 10**6, 10**7, 10**8]:
    print "%9d: %07f" % (n, pi(n))

```

### python_code_3.txt
```python
import numpy as np

n = input('Number of samples: ')
print np.sum(np.random.rand(n)**2+np.random.rand(n)**2<1)/float(n)*4

```

