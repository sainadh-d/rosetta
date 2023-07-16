# Twin primes

## Task Link
[Rosetta Code - Twin primes](https://rosettacode.org/wiki/Twin_primes)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.Scanner;

public class twinPrimes {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Search Size: ");
        BigInteger max = input.nextBigInteger();
        int counter = 0;
        for(BigInteger x = new BigInteger("3"); x.compareTo(max) <= 0; x = x.add(BigInteger.ONE)){
            BigInteger sqrtNum = x.sqrt().add(BigInteger.ONE);
            if(x.add(BigInteger.TWO).compareTo(max) <= 0) {
                counter += findPrime(x.add(BigInteger.TWO), x.add(BigInteger.TWO).sqrt().add(BigInteger.ONE)) && findPrime(x, sqrtNum) ? 1 : 0;
            }
        }
        System.out.println(counter + " twin prime pairs.");
    }
    public static boolean findPrime(BigInteger x, BigInteger sqrtNum){
        for(BigInteger divisor = BigInteger.TWO; divisor.compareTo(sqrtNum) <= 0; divisor = divisor.add(BigInteger.ONE)){
            if(x.remainder(divisor).compareTo(BigInteger.ZERO) == 0){
                return false;
            }
        }
        return true;
    }
}

```

## Python Code
### python_code_1.txt
```python
primes = [2, 3, 5, 7, 11, 13, 17, 19]


def count_twin_primes(limit: int) -> int:
    global primes
    if limit > primes[-1]:
        ram_limit = primes[-1] + 90000000 - len(primes)
        reasonable_limit = min(limit, primes[-1] ** 2, ram_limit) - 1

        while reasonable_limit < limit:
            ram_limit = primes[-1] + 90000000 - len(primes)
            if ram_limit > primes[-1]:
                reasonable_limit = min(limit, primes[-1] ** 2, ram_limit)
            else:
                reasonable_limit = min(limit, primes[-1] ** 2)

            sieve = list({x for prime in primes for x in
                          range(primes[-1] + prime - (primes[-1] % prime), reasonable_limit, prime)})
            primes += [x - 1 for i, x in enumerate(sieve) if i and x - 1 != sieve[i - 1] and x - 1 < limit]

    count = len([(x, y) for (x, y) in zip(primes, primes[1:]) if x + 2 == y])

    return count


def test(limit: int):
    count = count_twin_primes(limit)
    print(f"Number of twin prime pairs less than {limit} is {count}\n")


test(10)
test(100)
test(1000)
test(10000)
test(100000)
test(1000000)
test(10000000)
test(100000000)

```

