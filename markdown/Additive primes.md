# Additive primes

## Task Link
[Rosetta Code - Additive primes](https://rosettacode.org/wiki/Additive_primes)

## Java Code
### java_code_1.txt
```java
public class additivePrimes {

    public static void main(String[] args) {
        int additive_primes = 0;
        for (int i = 2; i < 500; i++) {
            if(isPrime(i) && isPrime(digitSum(i))){
                additive_primes++;
                System.out.print(i + " ");
            }
        }
        System.out.print("\nFound " + additive_primes + " additive primes less than 500");
    }

    static boolean isPrime(int n) {
        int counter = 1;
        if (n < 2 || (n != 2 && n % 2 == 0) || (n != 3 && n % 3 == 0)) {
            return false;
        }
        while (counter * 6 - 1 <= Math.sqrt(n)) {
            if (n % (counter * 6 - 1) == 0 || n % (counter * 6 + 1) == 0) {
                return false;
            } else {
                counter++;
            }
        }
        return true;
    }

    static int digitSum(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}

```

## Python Code
### python_code_1.txt
```python
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def digit_sum(n: int) -> int:
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def main() -> None:
    additive_primes = 0
    for i in range(2, 500):
        if is_prime(i) and is_prime(digit_sum(i)):
            additive_primes += 1
            print(i, end=" ")
    print(f"\nFound {additive_primes} additive primes less than 500")

if __name__ == "__main__":
    main()

```

