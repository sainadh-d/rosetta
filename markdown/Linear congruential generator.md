# Linear congruential generator

## Task Link
[Rosetta Code - Linear congruential generator](https://rosettacode.org/wiki/Linear_congruential_generator)

## Java Code
### java_code_1.txt
```java
import java.util.stream.IntStream;
import static java.util.stream.IntStream.iterate;

public class LinearCongruentialGenerator {
    final static int mask = (1 << 31) - 1;

    public static void main(String[] args) {
        System.out.println("BSD:");
        randBSD(0).limit(10).forEach(System.out::println);

        System.out.println("\nMS:");
        randMS(0).limit(10).forEach(System.out::println);
    }

    static IntStream randBSD(int seed) {
        return iterate(seed, s -> (s * 1_103_515_245 + 12_345) & mask).skip(1);
    }

    static IntStream randMS(int seed) {
        return iterate(seed, s -> (s * 214_013 + 2_531_011) & mask).skip(1)
                .map(i -> i >> 16);
    }
}

```

## Python Code
### python_code_1.txt
```python
def bsd_rand(seed):
   def rand():
      rand.seed = (1103515245*rand.seed + 12345) & 0x7fffffff
      return rand.seed
   rand.seed = seed
   return rand

def msvcrt_rand(seed):
   def rand():
      rand.seed = (214013*rand.seed + 2531011) & 0x7fffffff
      return rand.seed >> 16
   rand.seed = seed
   return rand

```

### python_code_2.txt
```python
def bsd_rand(seed):
   def rand():
      nonlocal seed
      seed = (1103515245*seed + 12345) & 0x7fffffff
      return seed
   return rand

def msvcrt_rand(seed):
   def rand():
      nonlocal seed
      seed = (214013*seed + 2531011) & 0x7fffffff
      return seed >> 16
   return rand

```

