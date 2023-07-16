# 100 doors

## Task Link
[Rosetta Code - 100 doors](https://rosettacode.org/wiki/100_doors)

## Java Code
### java_code_2.txt
```java
class HundredDoors {
    public static void main(String[] args) {
        boolean[] doors = new boolean[101];

        for (int i = 1; i < doors.length; i++) {
            for (int j = i; j < doors.length; j += i) {
                doors[j] = !doors[j];
            }
        }

        for (int i = 1; i < doors.length; i++) {
            if (doors[i]) {
                System.out.printf("Door %d is open.%n", i);
            }
        }
    }
}

```

### java_code_3.txt
```java
import java.util.BitSet;

public class HundredDoors {
    public static void main(String[] args) {
        final int n = 100;
        var a = new BitSet(n);
        for (int i = 1; i <= n; i++) {
            for (int j = i - 1; j < n; j += i) {
                a.flip(j);
            }
        }
        a.stream().map(i -> i + 1).forEachOrdered(System.out::println);
    }
}

```

### java_code_4.txt
```java
class HundredDoors {
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++)
            System.out.printf("Door %d is open.%n", i * i);
    }
}

```

### java_code_5.txt
```java
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class HundredDoors {
    public static void main(String args[]) {
        String openDoors = IntStream.rangeClosed(1, 100)
                .filter(i -> Math.pow((int) Math.sqrt(i), 2) == i)
                .mapToObj(Integer::toString)
                .collect(Collectors.joining(", "));
        System.out.printf("Open doors: %s%n", openDoors);
    }
}

```

## Python Code
### python_code_1.txt
```python
var doors = falses(100)

for a in 1..100: for b in a..a..100:
    doors[b] = not doors[b]

for a in 1..100:
    print "Door $a is ${(doors[a]) ? 'open.': 'closed.'}"

```

### python_code_2.txt
```python
doors = [False] * 100
for i in range(100):
   for j in range(i, 100, i+1):
       doors[j] = not doors[j]
   print("Door %d:" % (i+1), 'open' if doors[i] else 'close')

```

### python_code_3.txt
```python
for i in xrange(1, 101):
    root = i ** 0.5
    print "Door %d:" % i, 'open' if root == int(root) else 'close'

```

### python_code_4.txt
```python
print '\n'.join(['Door %s is %s' % (i, ('closed', 'open')[(i**0.5).is_integer()]) for i in xrange(1, 101)])

```

### python_code_5.txt
```python
print '\n'.join('Door %s is %s' % (i, 'closed' if i**0.5 % 1 else 'open') for i in range(1, 101))

```

### python_code_6.txt
```python
for i in range(1, 101):
    if i**0.5 % 1:
        state='closed'
    else:
        state='open'
    print("Door {}:{}".format(i, state))

```

### python_code_7.txt
```python
for i in range(1,101): print("Door %s is open" % i**2)

```

