# Primality by trial division

## Task Link
[Rosetta Code - Primality by trial division](https://rosettacode.org/wiki/Primality_by_trial_division)

## Java Code
### java_code_1.txt
```java
public static boolean prime(long a){
   if(a == 2){
      return true;
   }else if(a <= 1 || a % 2 == 0){
      return false;
   }
   long max = (long)Math.sqrt(a);
   for(long n= 3; n <= max; n+= 2){
      if(a % n == 0){ return false; }
   }
   return true;
}

```

### java_code_2.txt
```java
public static boolean prime(int n) {
    return !new String(new char[n]).matches(".?|(..+?)\\1+");
}

```

## Python Code
### python_code_1.txt
```python
def prime(a):
    return not (a < 2 or any(a % x == 0 for x in xrange(2, int(a**0.5) + 1)))

```

### python_code_2.txt
```python
def prime2(a):
    if a == 2: return True
    if a < 2 or a % 2 == 0: return False
    return not any(a % x == 0 for x in xrange(3, int(a**0.5) + 1, 2))

```

### python_code_3.txt
```python
def prime3(a):
    if a < 2: return False
    if a == 2 or a == 3: return True # manually test 2 and 3   
    if a % 2 == 0 or a % 3 == 0: return False # exclude multiples of 2 and 3

    maxDivisor = a**0.5
    d, i = 5, 2
    while d <= maxDivisor:
        if a % d == 0: return False
        d += i 
        i = 6 - i # this modifies 2 into 4 and viceversa

    return True

```

### python_code_4.txt
```python
>>> import re
>>> def isprime(n):
    return not re.match(r'^1?$|^(11+?)\1+$', '1' * n)

>>> # A quick test
>>> [i for i in range(40) if isprime(i)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

```

