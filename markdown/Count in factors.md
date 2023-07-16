# Count in factors

## Task Link
[Rosetta Code - Count in factors](https://rosettacode.org/wiki/Count_in_factors)

## Java Code
### java_code_1.txt
```java
public class CountingInFactors{ 
    public static void main(String[] args){
        for(int i = 1; i<= 10; i++){
            System.out.println(i + " = "+ countInFactors(i));
        }
 
        for(int i = 9991; i <= 10000; i++){
        	System.out.println(i + " = "+ countInFactors(i));
        }
    }
 
    private static String countInFactors(int n){
        if(n == 1) return "1";
 
        StringBuilder sb = new StringBuilder();
 
        n = checkFactor(2, n, sb);
        if(n == 1) return sb.toString();
 
        n = checkFactor(3, n, sb);
        if(n == 1) return sb.toString();
 
        for(int i = 5; i <= n; i+= 2){
            if(i % 3 == 0)continue;
 
            n = checkFactor(i, n, sb);
            if(n == 1)break;
        }
 
        return sb.toString();
    }
 
    private static int checkFactor(int mult, int n, StringBuilder sb){
        while(n % mult == 0 ){
            if(sb.length() > 0) sb.append(" x ");
            sb.append(mult);
            n /= mult;
        }
        return n;
    }
}

```

## Python Code
### python_code_1.txt
```python
from functools import lru_cache

primes = [2, 3, 5, 7, 11, 13, 17]    # Will be extended

@lru_cache(maxsize=2000)
def pfactor(n):
    if n == 1:
        return [1]
    n2 = n // 2 + 1
    for p in primes:
        if p <= n2:
            d, m = divmod(n, p)
            if m == 0:
                if d > 1:
                    return [p] + pfactor(d)
                else:
                    return [p]
        else:
            if n > primes[-1]:
                primes.append(n)
            return [n]
        
if __name__ == '__main__':
    mx = 5000
    for n in range(1, mx + 1):
        factors = pfactor(n)
        if n <= 10 or n >= mx - 20:
            print( '%4i %5s %s' % (n,
                                   '' if factors != [n] or n == 1 else 'prime',
                                   'x'.join(str(i) for i in factors)) )
        if n == 11:
            print('...')
            
    print('\nNumber of primes gathered up to', n, 'is', len(primes))
    print(pfactor.cache_info())

```

### python_code_2.txt
```python
def count_in_factors(n):
    if is_prime(n) or n == 1: 
        print(n,end="")
        return
    while n != 1:
        p = next_prime(1)
        while n % p != 0:
            p = next_prime(p)
        print(p,end="")
        n = n / p
        if n != 1: print(" x",end=" ")

for i in range(1, 101):
    print(i,"=",end=" ")
    count_in_factors(i)
    print("")

```

