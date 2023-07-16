# Truncatable primes

## Task Link
[Rosetta Code - Truncatable primes](https://rosettacode.org/wiki/Truncatable_primes)

## Java Code
### java_code_1.txt
```java
import java.util.BitSet;

public class Main {

	public static void main(String[] args){

		final int MAX = 1000000;

		//Sieve of Eratosthenes (using BitSet only for odd numbers)
		BitSet primeList = new BitSet(MAX>>1); 
		primeList.set(0,primeList.size(),true); 

		int sqroot = (int) Math.sqrt(MAX); 
		primeList.clear(0); 
		for(int num = 3; num <= sqroot; num+=2) 
		{ 
			if( primeList.get(num >> 1) ) 
			{ 
				int inc = num << 1;
				for(int factor = num * num; factor < MAX; factor += inc) 
				{ 
					//if( ((factor) & 1) == 1) 
					//{ 
					primeList.clear(factor >> 1); 
					//} 
				} 
			} 
		}
		//Sieve ends...

		//Find Largest Truncatable Prime. (so we start from 1000000 - 1
		int rightTrunc = -1, leftTrunc = -1;
		for(int prime = (MAX - 1) | 1; prime >= 3; prime -= 2)
		{
			if(primeList.get(prime>>1))
			{
				//Already found Right Truncatable Prime?
				if(rightTrunc == -1)
				{
					int right = prime;
					while(right > 0 && right % 2 != 0 && primeList.get(right >> 1)) right /= 10;
					if(right == 0) rightTrunc = prime;
				}

				//Already found Left Truncatable Prime?
				if(leftTrunc == -1 )
				{
					//Left Truncation
					String left = Integer.toString(prime);
					if(!left.contains("0"))
					{
						while( left.length() > 0 ){
							int iLeft = Integer.parseInt(left);
							if(!primeList.get( iLeft >> 1)) break;
							left = left.substring(1);
						}
						if(left.length() == 0) leftTrunc = prime;
					}
				}
				if(leftTrunc != -1 && rightTrunc != -1) //Found both? then Stop loop
				{
					break;
				}
			}
		}
		System.out.println("Left  Truncatable : " + leftTrunc);
		System.out.println("Right Truncatable : " + rightTrunc);
	}
}

```

## Python Code
### python_code_1.txt
```python
maxprime = 1000000

def primes(n):
    multiples = set()
    prime = []
    for i in range(2, n+1):
        if i not in multiples:
            prime.append(i)
            multiples.update(set(range(i*i, n+1, i)))
    return prime

def truncatableprime(n):
    'Return a longest left and right truncatable primes below n'
    primelist = [str(x) for x in primes(n)[::-1]]
    primeset = set(primelist)
    for n in primelist:
        # n = 'abc'; [n[i:] for i in range(len(n))] -> ['abc', 'bc', 'c']
        alltruncs = set(n[i:] for i in range(len(n)))
        if alltruncs.issubset(primeset):
            truncateleft = int(n)
            break
    for n in primelist:
        # n = 'abc'; [n[:i+1] for i in range(len(n))] -> ['a', 'ab', 'abc']
        alltruncs = set([n[:i+1] for i in range(len(n))])
        if alltruncs.issubset(primeset):
            truncateright = int(n)
            break
    return truncateleft, truncateright

print(truncatableprime(maxprime))

```

