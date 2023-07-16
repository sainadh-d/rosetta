# Extend your language

## Task Link
[Rosetta Code - Extend your language](https://rosettacode.org/wiki/Extend_your_language)

## Java Code
### java_code_1.txt
```java
public class If2 {

    public static void if2(boolean firstCondition, boolean secondCondition,
                           Runnable bothTrue, Runnable firstTrue, Runnable secondTrue, Runnable noneTrue) {
        if (firstCondition)
            if (secondCondition)
                bothTrue.run();
            else firstTrue.run();
        else if (secondCondition)
            secondTrue.run();
        else noneTrue.run();
    }
}

```

### java_code_2.txt
```java
import static If2.if2;
class Main {
    private static void print(String s) {
        System.out.println(s);
    }

    public static void main(String[] args) {
        // prints "both true"
        if2(true, true,
                () -> print("both true"),
                () -> print("first true"),
                () -> print("second true"),
                () -> print("none true"));
    }
}

```

### java_code_3.txt
```java
public class If2 {
    private final boolean firstCondition;
    private final boolean secondCondition;

    public If2(boolean firstCondition, boolean secondCondition) {
        this.firstCondition = firstCondition;
        this.secondCondition = secondCondition;
    }

    public static If2 if2(boolean firstCondition, boolean secondCondition) {
        return new If2(firstCondition, secondCondition);
    }

    public If2 then(Runnable runnable) {
        if (firstCondition && secondCondition) {
            runnable.run();
        }
        return this;
    }

    public If2 elseNone(Runnable runnable) {
        if (!firstCondition && !secondCondition) {
            runnable.run();
        }
        return this;
    }

    public If2 elseIfFirst(Runnable runnable) {
        if (firstCondition && !secondCondition) {
            runnable.run();
        }
        return this;
    }

    public If2 elseIfSecond(Runnable runnable) {
        if (!firstCondition && secondCondition) {
            runnable.run();
        }
        return this;
    }
}

```

### java_code_4.txt
```java
// prints "both true"
if2(true, true)
    .then(() -> print("both true"))
    .elseIfFirst(() -> print("first true"))
    .elseIfSecond(() -> print("second true"))
    .elseNone(() -> print("none true"));

// if we only care about both true and none true...
// prints "none true"
if2(false, false)
    .then(() -> print("both true"))
    .elseNone(() -> { // a lambda can have a block body
        print("none true");
    });

```

## Python Code
### python_code_1.txt
```python
a, b = 1, 0

if (c1 := a == 1) and (c2 := b == 3):
  print('a = 1 and b = 3')
elif c1:
  print('a = 1 and b <> 3')
elif c2:
  print('a <> 1 and b = 3')
else:
  print('a <> 1 and b <> 3')

```

