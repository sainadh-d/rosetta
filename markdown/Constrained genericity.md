# Constrained genericity

## Task Link
[Rosetta Code - Constrained genericity](https://rosettacode.org/wiki/Constrained_genericity)

## Java Code
### java_code_1.txt
```java
interface Eatable
{
    void eat();
}

```

### java_code_2.txt
```java
import java.util.List;

class FoodBox<T extends Eatable>
{
    public List<T> food;
}

```

### java_code_3.txt
```java
public <T extends Eatable> void foo(T x) { }
// although in this case this is no more useful than just "public void foo(Eatable x)"

```

### java_code_4.txt
```java
public class Test{
   public <T extends Eatable> void bar(){ }
}

```

### java_code_5.txt
```java
test.<EatableClass>bar();

```

## Python Code
