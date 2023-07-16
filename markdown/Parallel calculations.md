# Parallel calculations

## Task Link
[Rosetta Code - Parallel calculations](https://rosettacode.org/wiki/Parallel_calculations)

## Java Code
### java_code_1.txt
```java
import static java.lang.System.out; 
import static java.util.Arrays.stream;
import static java.util.Comparator.comparing;
 
public interface ParallelCalculations {
    public static final long[] NUMBERS = {
      12757923,
      12878611,
      12878893,
      12757923,
      15808973,
      15780709,
      197622519
    };
 
    public static void main(String... arguments) {
      stream(NUMBERS)
        .unordered()
        .parallel()
        .mapToObj(ParallelCalculations::minimalPrimeFactor)
        .max(comparing(a -> a[0]))
        .ifPresent(res -> out.printf(
          "%d has the largest minimum prime factor: %d%n",
          res[1],
          res[0]
        ));
    }
 
    public static long[] minimalPrimeFactor(long n) {
      for (long i = 2; n >= i * i; i++) {
        if (n % i == 0) {
          return new long[]{i, n};
        }
      }
      return new long[]{n, n};
    }
}

```

## Python Code
### python_code_1.txt
```python
from concurrent import futures
from math import floor, sqrt
 
NUMBERS = [
    112272537195293,
    112582718962171,
    112272537095293,
    115280098190773,
    115797840077099,
    1099726829285419]
# NUMBERS = [33, 44, 55, 275]
 
def lowest_factor(n, _start=3):
    if n % 2 == 0:
        return 2
    search_max = int(floor(sqrt(n))) + 1
    for i in range(_start, search_max, 2):
        if n % i == 0:
            return i
    return n

def prime_factors(n, lowest):
    pf = []
    while n > 1:
        pf.append(lowest)
        n //= lowest
        lowest = lowest_factor(n, max(lowest, 3))
    return pf

def prime_factors_of_number_with_lowest_prime_factor(NUMBERS):
    with futures.ProcessPoolExecutor() as executor:
        low_factor, number = max( (l, f) for l, f in zip(executor.map(lowest_factor, NUMBERS), NUMBERS) )
        all_factors = prime_factors(number, low_factor)
        return number, all_factors

 
def main():
    print('For these numbers:')
    print('\n  '.join(str(p) for p in NUMBERS))
    number, all_factors = prime_factors_of_number_with_lowest_prime_factor(NUMBERS)
    print('    The one with the largest minimum prime factor is {}:'.format(number))
    print('      All its prime factors in order are: {}'.format(all_factors))
 
if __name__ == '__main__':
    main()

```

### python_code_2.txt
```python
import multiprocessing

# ========== #Python3 - concurrent
from math import floor, sqrt
 
numbers = [
    112272537195293,
    112582718962171,
    112272537095293,
    115280098190773,
    115797840077099,
    1099726829285419]
# numbers = [33, 44, 55, 275]
 
def lowest_factor(n, _start=3):
    if n % 2 == 0:
        return 2
    search_max = int(floor(sqrt(n))) + 1
    for i in range(_start, search_max, 2):
        if n % i == 0:
            return i
    return n
 
def prime_factors(n, lowest):
    pf = []
    while n > 1:
        pf.append(lowest)
        n //= lowest
        lowest = lowest_factor(n, max(lowest, 3))
    return pf
# ========== #Python3 - concurrent

def prime_factors_of_number_with_lowest_prime_factor(numbers):
    pool = multiprocessing.Pool(processes=5)
    factors = pool.map(lowest_factor,numbers)
    
    low_factor,number = max((l,f) for l,f in zip(factors,numbers))
    all_factors = prime_factors(number,low_factor)
    return number,all_factors
 
if __name__ == '__main__':
    print('For these numbers:')
    print('\n  '.join(str(p) for p in numbers))
    number, all_factors = prime_factors_of_number_with_lowest_prime_factor(numbers)
    print('    The one with the largest minimum prime factor is {}:'.format(number))
    print('      All its prime factors in order are: {}'.format(all_factors))

```

