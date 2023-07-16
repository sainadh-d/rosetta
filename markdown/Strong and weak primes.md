# Strong and weak primes

## Task Link
[Rosetta Code - Strong and weak primes](https://rosettacode.org/wiki/Strong_and_weak_primes)

## Java Code
### java_code_1.txt
```java
public class StrongAndWeakPrimes {

    private static int MAX = 10_000_000 + 1000;
    private static boolean[] primes = new boolean[MAX];

    public static void main(String[] args) {
        sieve();
        System.out.println("First 36 strong primes:");        
        displayStrongPrimes(36);
        for ( int n : new int[] {1_000_000, 10_000_000}) {
            System.out.printf("Number of strong primes below %,d = %,d%n", n, strongPrimesBelow(n));
        }
        System.out.println("First 37 weak primes:");        
        displayWeakPrimes(37);
        for ( int n : new int[] {1_000_000, 10_000_000}) {
            System.out.printf("Number of weak primes below %,d = %,d%n", n, weakPrimesBelow(n));
        }
    }

    private static int weakPrimesBelow(int maxPrime) {
        int priorPrime = 2;
        int currentPrime = 3;
        int count = 0;
        while ( currentPrime < maxPrime ) {
            int nextPrime = getNextPrime(currentPrime);
            if ( currentPrime * 2 < priorPrime + nextPrime ) {
                count++;
            }
            priorPrime = currentPrime;
            currentPrime = nextPrime;
        }
        return count;
    }

    private static void displayWeakPrimes(int maxCount) {
        int priorPrime = 2;
        int currentPrime = 3;
        int count = 0;
        while ( count < maxCount ) {
            int nextPrime = getNextPrime(currentPrime);
            if ( currentPrime * 2 < priorPrime + nextPrime) {
                count++;
                System.out.printf("%d ", currentPrime);
            }
            priorPrime = currentPrime;
            currentPrime = nextPrime;
        }
        System.out.println();
    }

    private static int getNextPrime(int currentPrime) {
        int nextPrime = currentPrime + 2;
        while ( ! primes[nextPrime] ) {
            nextPrime += 2;
        }
        return nextPrime;
    }
    
    private static int strongPrimesBelow(int maxPrime) {
        int priorPrime = 2;
        int currentPrime = 3;
        int count = 0;
        while ( currentPrime < maxPrime ) {
            int nextPrime = getNextPrime(currentPrime);
            if ( currentPrime * 2 > priorPrime + nextPrime ) {
                count++;
            }
            priorPrime = currentPrime;
            currentPrime = nextPrime;
        }
        return count;
    }
    
    private static void displayStrongPrimes(int maxCount) {
        int priorPrime = 2;
        int currentPrime = 3;
        int count = 0;
        while ( count < maxCount ) {
            int nextPrime = getNextPrime(currentPrime);
            if ( currentPrime * 2 > priorPrime + nextPrime) {
                count++;
                System.out.printf("%d ", currentPrime);
            }
            priorPrime = currentPrime;
            currentPrime = nextPrime;
        }
        System.out.println();
    }

    private static final void sieve() {
        //  primes
        for ( int i = 2 ; i < MAX ; i++ ) {
            primes[i] = true;            
        }
        for ( int i = 2 ; i < MAX ; i++ ) {
            if ( primes[i] ) {
                for ( int j = 2*i ; j < MAX ; j += i ) {
                    primes[j] = false;
                }
            }
        }
    }

}

```

## Python Code
### python_code_1.txt
```python
import numpy as np

def primesfrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)//3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

p = primes10m   = primesfrom2to(10_000_000)
s = strong10m   = [t for s, t, u in zip(p, p[1:], p[2:]) 
                   if t > (s + u) / 2]
w = weak10m     = [t for s, t, u in zip(p, p[1:], p[2:]) 
                   if t < (s + u) / 2]
b = balanced10m = [t for s, t, u in zip(p, p[1:], p[2:]) 
                   if t == (s + u) / 2]

print('The first   36   strong primes:', s[:36])
print('The   count   of the strong primes below   1,000,000:',
      sum(1 for p in s if p < 1_000_000))
print('The   count   of the strong primes below  10,000,000:', len(s))
print('\nThe first   37   weak primes:', w[:37])
print('The   count   of the weak   primes below   1,000,000:',
      sum(1 for p in w if p < 1_000_000))
print('The   count   of the weak   primes below  10,000,000:', len(w))
print('\n\nThe first   10 balanced primes:', b[:10])
print('The   count   of balanced   primes below   1,000,000:',
      sum(1 for p in b if p < 1_000_000))
print('The   count   of balanced   primes below  10,000,000:', len(b))
print('\nTOTAL primes below   1,000,000:',
      sum(1 for pr in p if pr < 1_000_000))
print('TOTAL primes below  10,000,000:', len(p))

```

