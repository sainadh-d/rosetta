# Möbius function

## Task Link
[Rosetta Code - Möbius function](https://rosettacode.org/wiki/M%C3%B6bius_function)

## Java Code
### java_code_1.txt
```java
public class MöbiusFunction {

    public static void main(String[] args) {
        System.out.printf("First 199 terms of the möbius function are as follows:%n    ");
        for ( int n = 1 ; n < 200 ; n++ ) {
            System.out.printf("%2d  ", möbiusFunction(n));
            if ( (n+1) % 20 == 0 ) {
                System.out.printf("%n");
            }
        }
    }
    
    private static int MU_MAX = 1_000_000;
    private static int[] MU = null;
    
    //  Compute mobius function via sieve
    private static int möbiusFunction(int n) {
        if ( MU != null ) {
            return MU[n];
        }
        
        //  Populate array
        MU = new int[MU_MAX+1];
        int sqrt = (int) Math.sqrt(MU_MAX);
        for ( int i = 0 ; i < MU_MAX ; i++ ) {
            MU[i] = 1;
        }
        
        for ( int i = 2 ; i <= sqrt ; i++ ) {
            if ( MU[i] == 1 ) {
                //  for each factor found, swap + and -
                for ( int j = i ; j <= MU_MAX ; j += i ) {
                    MU[j] *= -i;
                }
                //  square factor = 0
                for ( int j = i*i ; j <= MU_MAX ; j += i*i ) {
                    MU[j] = 0;
                }
            }
        }
        
        for ( int i = 2 ; i <= MU_MAX ; i++ ) {
            if ( MU[i] == i ) {
                MU[i] = 1;
            }
            else if ( MU[i] == -i ) {
                MU[i] = -1;
            }
            else if ( MU[i] < 0 ) {
                MU[i] = 1;               
            }
            else if ( MU[i] > 0 ) {
                MU[i] = -1;
            }
        }
        return MU[n];
    }

}

```

## Python Code
### python_code_1.txt
```python
# Python Program to evaluate
# Mobius def M(N) = 1 if N = 1
# M(N) = 0 if any prime factor
# of N is contained twice
# M(N) = (-1)^(no of distinct
# prime factors)
# Python Program to
# evaluate Mobius def
# M(N) = 1 if N = 1
# M(N) = 0 if any
# prime factor of
# N is contained twice
# M(N) = (-1)^(no of
# distinct prime factors)
 
# def to check if
# n is prime or not
def isPrime(n) :
 
    if (n < 2) :
        return False
    for i in range(2, n + 1) :
        if (i * i <= n and n % i == 0) :
            return False
    return True
 
def mobius(N) :
     
    # Base Case
    if (N == 1) :
        return 1
 
    # For a prime factor i
    # check if i^2 is also
    # a factor.
    p = 0
    for i in range(1, N + 1) :
        if (N % i == 0 and
                isPrime(i)) :
 
            # Check if N is
            # divisible by i^2
            if (N % (i * i) == 0) :
                return 0
            else :
 
                # i occurs only once,
                # increase f
                p = p + 1
 
    # All prime factors are
    # contained only once
    # Return 1 if p is even
    # else -1
    if(p % 2 != 0) :
        return -1
    else :
        return 1
 
# Driver Code
print("Mobius numbers from 1..99:")
      
for i in range(1, 100):
  print(f"{mobius(i):>4}", end = '')

  if i % 20 == 0: print()
# This code is contributed by
# Manish Shaw(manishshaw1)

```

### python_code_2.txt
```python
# Python Program to evaluate
# Mobius def M(N) = 1 if N = 1
# M(N) = 0 if any prime factor
# of N is contained twice
# M(N) = (-1)^(no of distinct
# prime factors)
import math
 
# def to check if n
# is prime or not
def isPrime(n) :
 
    if (n < 2) :
        return False
    for i in range(2, n + 1) :
        if (n % i == 0) :
            return False
        i = i * i
    return True
 
def mobius(n) :
 
    p = 0
 
    # Handling 2 separately
    if (n % 2 == 0) :
     
        n = int(n / 2)
        p = p + 1
 
        # If 2^2 also
        # divides N
        if (n % 2 == 0) :
            return 0
     
 
    # Check for all
    # other prime factors
    for i in range(3, int(math.sqrt(n)) + 1) :
     
        # If i divides n
        if (n % i == 0) :
         
            n = int(n / i)
            p = p + 1
 
            # If i^2 also
            # divides N
            if (n % i == 0) :
                return 0
        i = i + 2   
     
    if(p % 2 == 0) :
        return -1
    else :
        return 1
 
# Driver Code
print("Mobius numbers from 1..99:")
      
for i in range(1, 100):
  print(f"{mobius(i):>4}", end = '')
# This code is contributed by
# Manish Shaw(manishshaw1)

```

