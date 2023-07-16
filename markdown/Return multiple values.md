# Return multiple values

## Task Link
[Rosetta Code - Return multiple values](https://rosettacode.org/wiki/Return_multiple_values)

## Java Code
### java_code_1.txt
```java
Point getPoint() {
    return new Point(1, 2);
}

static class Point {
    int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

```

### java_code_2.txt
```java
Values<String, OutputStream> getValues() {
    return new Values<>("Rosetta Code", System.out);
}

static class Values<X, Y> {
    X x;
    Y y;

    public Values(X x, Y y) {
        this.x = x;
        this.y = y;
    }
}

```

### java_code_3.txt
```java
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

// =============================================================================
public class RReturnMultipleVals {
  public static final String K_lipsum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
  public static final Long   K_1024   = 1024L;
  public static final String L        = "L";
  public static final String R        = "R";

  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  public static void main(String[] args) throws NumberFormatException{
    Long nv_;
    String sv_;
    switch (args.length) {
      case 0:
        nv_ = K_1024;
        sv_ = K_lipsum;
        break;
      case 1:
        nv_ = Long.parseLong(args[0]);
        sv_ = K_lipsum;
        break;
      case 2:
        nv_ = Long.parseLong(args[0]);
        sv_ = args[1];
        break;
      default:
        nv_ = Long.parseLong(args[0]);
        sv_ = args[1];
        for (int ix = 2; ix < args.length; ++ix) {
          sv_ = sv_ + " " + args[ix];
        }
        break;
    }

    RReturnMultipleVals lcl = new RReturnMultipleVals();

    Pair<Long, String> rvp = lcl.getPairFromPair(nv_, sv_); // values returned in a bespoke object
    System.out.println("Results extracted from a composite object:");
    System.out.printf("%s, %s%n%n", rvp.getLeftVal(), rvp.getRightVal());

    List<Object> rvl = lcl.getPairFromList(nv_, sv_); // values returned in a Java Collection object
    System.out.println("Results extracted from a Java Colections \"List\" object:");
    System.out.printf("%s, %s%n%n", rvl.get(0), rvl.get(1));

    Map<String, Object> rvm = lcl.getPairFromMap(nv_, sv_); // values returned in a Java Collection object
    System.out.println("Results extracted from a Java Colections \"Map\" object:");
    System.out.printf("%s, %s%n%n", rvm.get(L), rvm.get(R));
  }
  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  // Return a bespoke object.
  // Permits any number and type of value to be returned
  public <T, U> Pair<T, U> getPairFromPair(T vl_, U vr_) {
    return new Pair<T, U>(vl_, vr_);
  }
  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  // Exploit Java Collections classes to assemble a collection of results.
  // This example uses java.util.List
  public List<Object> getPairFromList(Object nv_, Object sv_) {
    List<Object> rset = new ArrayList<Object>();
    rset.add(nv_);
    rset.add(sv_);
    return rset;
  }
  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  // Exploit Java Collections classes to assemble a collection of results.
  // This example uses java.util.Map
  public Map<String, Object> getPairFromMap(Object nv_, Object sv_) {
    Map<String, Object> rset = new HashMap<String, Object>();
    rset.put(L, nv_);
    rset.put(R, sv_);
    return rset;
  }

  // ===========================================================================
  private static class Pair<L, R> {
    private L leftVal;
    private R rightVal;

    public Pair(L nv_, R sv_) {
      setLeftVal(nv_);
      setRightVal(sv_);
    }
    public void setLeftVal(L nv_) {
      leftVal = nv_;
    }
    public L getLeftVal() {
      return leftVal;
    }
    public void setRightVal(R sv_) {
      rightVal = sv_;
    }
    public R getRightVal() {
      return rightVal;
    }
  }
}

```

### java_code_4.txt
```java
public class Values {
	private final Object[] objects;
	public Values(Object ... objects) {
		this.objects = objects;
	}
	public <T> T get(int i) {
		return (T) objects[i];
	}
	public Object[] get() {
		return objects;
	}
	
	// to test
	public static void main(String[] args) {
		Values v = getValues();
		int i = v.get(0);
		System.out.println(i);
		printValues(i, v.get(1));
		printValues(v.get());
	}
	private static Values getValues() {
		return new Values(1, 3.8, "text");
	}
	private static void printValues(int i, double d) {
		System.out.println(i + ", " + d);
	}
	private static void printValues(Object ... objects) {
		for (int i=0; i<objects.length; i+=1) System.out.print((i==0 ? "": ", ") + objects[i]);
		System.out.println();
	}
}

```

## Python Code
### python_code_1.txt
```python
def addsub(x, y):
  return x + y, x - y

```

### python_code_2.txt
```python
sum, difference = addsub(33, 12)
print "33 + 12 = %s" % sum
print "33 - 12 = %s" % difference

```

