# Delegates

## Task Link
[Rosetta Code - Delegates](https://rosettacode.org/wiki/Delegates)

## Java Code
### java_code_1.txt
```java
interface Thingable {
    String thing();
}

class Delegator {
    public Thingable delegate;

    public String operation() {
        if (delegate == null)
            return "default implementation";
        else
            return delegate.thing();
    }
}

class Delegate implements Thingable {
    public String thing() {
        return "delegate implementation";
    }
}

// Example usage
// Memory management ignored for simplification
public class DelegateExample {
    public static void main(String[] args) {
        // Without a delegate:
        Delegator a = new Delegator();
        assert a.operation().equals("default implementation");

        // With a delegate:
        Delegate d = new Delegate();
        a.delegate = d;
        assert a.operation().equals("delegate implementation");

        // Same as the above, but with an anonymous class:
        a.delegate = new Thingable() {
                public String thing() {
                    return "anonymous delegate implementation";
                }
            };
        assert a.operation().equals("anonymous delegate implementation");
    }
}

```

### java_code_2.txt
```java
package delegate;

@FunctionalInterface
public interface Thingable {
  public String thing();
}

```

### java_code_3.txt
```java
package delegate;

import java.util.Optional;

public interface Delegator {
  public Thingable delegate();
  public Delegator delegate(Thingable thingable);

  public static Delegator new_() {
    return $Delegator.new_();
  }
 
  public default String operation() {
    return Optional.ofNullable(delegate())
      .map(Thingable::thing)
      .orElse("default implementation")
    ;
  }
}

```

### java_code_4.txt
```java
package delegate;

@FunctionalInterface
/* package */ interface $Delegator extends Delegator {
  @Override
  public default Delegator delegate(Thingable thingable) {
    return new_(thingable);
  }

  public static $Delegator new_() {
    return new_(() -> null);
  }

  public static $Delegator new_(Thingable thingable) {
    return () -> thingable;
  }
}

```

### java_code_5.txt
```java
package delegate;

public final class Delegate implements Thingable {
  @Override
  public String thing() {
    return "delegate implementation";
  }
}

```

### java_code_6.txt
```java
package delegate;

// Example usage
// Memory management ignored for simplification
public interface DelegateTest {
  public static String thingable() {
    return "method reference implementation";
  }

  public static void main(String... arguments) {
    // Without a delegate:
    Delegator d1 = Delegator.new_();
    assert d1.operation().equals("default implementation");

    // With a delegate:
    Delegator d2 = d1.delegate(new Delegate());
    assert d2.operation().equals("delegate implementation");

    // Same as the above, but with an anonymous class:
    Delegator d3 = d2.delegate(new Thingable() {
      @Override
      public String thing() {
        return "anonymous delegate implementation";
      }
    });
    assert d3.operation().equals("anonymous delegate implementation");

    // Same as the above, but with a method reference:
    Delegator d4 = d3.delegate(DelegateTest::thingable);
    assert d4.operation().equals("method reference implementation");

    // Same as the above, but with a lambda expression:
    Delegator d5 = d4.delegate(() -> "lambda expression implementation");
    assert d5.operation().equals("lambda expression implementation");
  }
}

```

## Python Code
### python_code_1.txt
```python
class Delegator:
   def __init__(self):
      self.delegate = None
   def operation(self):
       if hasattr(self.delegate, 'thing') and callable(self.delegate.thing):
          return self.delegate.thing()
       return 'default implementation'

class Delegate:
   def thing(self):
      return 'delegate implementation'

if __name__ == '__main__':

   # No delegate
   a = Delegator()
   assert a.operation() == 'default implementation'

   # With a delegate that does not implement "thing"
   a.delegate = 'A delegate may be any object'
   assert a.operation() == 'default implementation'

   # With delegate that implements "thing"
   a.delegate = Delegate()
   assert a.operation() == 'delegate implementation'

```

