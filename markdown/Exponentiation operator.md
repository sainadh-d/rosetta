# Exponentiation operator

## Task Link
[Rosetta Code - Exponentiation operator](https://rosettacode.org/wiki/Exponentiation_operator)

## Java Code
### java_code_1.txt
```java
public class Exp{
   public static void main(String[] args){
      System.out.println(pow(2,30));
      System.out.println(pow(2.0,30)); //tests
      System.out.println(pow(2.0,-2));
   }

   public static double pow(double base, int exp){
      if(exp < 0) return 1 / pow(base, -exp);
      double ans = 1.0;
      for(;exp > 0;--exp) ans *= base;
      return ans;
   }
}

```

## Python Code
### python_code_1.txt
```python
MULTIPLY = lambda x, y: x*y

class num(float):
    # the following method has complexity O(b)
    # rather than O(log b) via the rapid exponentiation
    def __pow__(self, b):
        return reduce(MULTIPLY, [self]*b, 1)

# works with ints as function or operator
print num(2).__pow__(3)
print num(2) ** 3

# works with floats as function or operator
print num(2.3).__pow__(8)
print num(2.3) ** 8

```

