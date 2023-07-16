# Euler method

## Task Link
[Rosetta Code - Euler method](https://rosettacode.org/wiki/Euler_method)

## Java Code
### java_code_1.txt
```java
public class Euler {
  private static void euler (Callable f, double y0, int a, int b, int h) {
    int t = a;
    double y = y0;
    while (t < b) {
      System.out.println ("" + t + " " + y);
      t += h;
      y += h * f.compute (t, y);
    }
    System.out.println ("DONE");
  }

  public static void main (String[] args) {
    Callable cooling = new Cooling ();
    int[] steps = {2, 5, 10};
    for (int stepSize : steps) {
      System.out.println ("Step size: " + stepSize);
      euler (cooling, 100.0, 0, 100, stepSize);
    }
  }
}

// interface used so we can plug in alternative functions to Euler
interface Callable {
  public double compute (int time, double t);
}

// class to implement the newton cooling equation
class Cooling implements Callable {
  public double compute (int time, double t) {
    return -0.07 * (t - 20);
  }
}

```

## Python Code
### python_code_1.txt
```python
def euler(f,y0,a,b,h):
	t,y = a,y0
	while t <= b:
		print "%6.3f %6.3f" % (t,y)
		t += h
		y += h * f(t,y)

def newtoncooling(time, temp):
	return -0.07 * (temp - 20)

euler(newtoncooling,100,0,100,10)

```

