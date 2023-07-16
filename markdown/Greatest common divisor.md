# Greatest common divisor

## Task Link
[Rosetta Code - Greatest common divisor](https://rosettacode.org/wiki/Greatest_common_divisor)

## Java Code
### java_code_1.txt
```java
/* recursive */
int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

```

### java_code_2.txt
```java
public static long gcd(long a, long b){
   long factor= Math.min(a, b);
   for(long loop= factor;loop > 1;loop--){
      if(a % loop == 0 && b % loop == 0){
         return loop;
      }
   }
   return 1;
}

```

### java_code_3.txt
```java
public static int gcd(int a, int b) //valid for positive integers.
{
	while(b > 0)
	{
		int c = a % b;
		a = b;
		b = c;
	}
	return a;
}

```

### java_code_4.txt
```java
static int gcd(int a,int b)
	{
		int min=a>b?b:a,max=a+b-min, div=min;
		for(int i=1;i<min;div=min/++i)
			if(min%div==0&&max%div==0)
				return div;
		return 1;
	}

```

### java_code_5.txt
```java
public static long gcd(long u, long v){
  long t, k;
 
  if (v == 0) return u;
  
  u = Math.abs(u);
  v = Math.abs(v); 
  if (u < v){
    t = u;
    u = v;
    v = t;
  }
 
  for(k = 1; (u & 1) == 0 && (v & 1) == 0; k <<= 1){
    u >>= 1; v >>= 1;
  }
 
  t = (u & 1) != 0 ? -v : u;
  while (t != 0){
    while ((t & 1) == 0) t >>= 1;
 
    if (t > 0)
      u = t;
    else
      v = -t;
 
    t = u - v;
  }
  return u * k;
}

```

### java_code_6.txt
```java
public static long gcd(long a, long b){
   if(a == 0) return b;
   if(b == 0) return a;
   if(a > b) return gcd(b, a % b);
   return gcd(a, b % a);
}

```

### java_code_7.txt
```java
import java.math.BigInteger;

public static long gcd(long a, long b){
   return BigInteger.valueOf(a).gcd(BigInteger.valueOf(b)).longValue();
}

```

## Python Code
### python_code_1.txt
```python
from fractions import gcd

```

### python_code_2.txt
```python
from math import gcd

```

### python_code_3.txt
```python
def gcd_iter(u, v):
    while v:
        u, v = v, u % v
    return abs(u)

```

### python_code_4.txt
```python
def gcd(u, v):
    return gcd(v, u % v) if v else abs(u)

```

### python_code_5.txt
```python
def gcd_bin(u, v):
    u, v = abs(u), abs(v) # u >= 0, v >= 0
    if u < v:
        u, v = v, u # u >= v >= 0
    if v == 0:
        return u
   
    # u >= v > 0
    k = 1
    while u & 1 == 0 and v & 1 == 0: # u, v - even
        u >>= 1; v >>= 1
        k <<= 1
       
    t = -v if u & 1 else u
    while t:
        while t & 1 == 0:
            t >>= 1
        if t > 0:
            u = t
        else:
            v = -t
        t = u - v
    return u * k

```

