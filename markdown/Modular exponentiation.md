# Modular exponentiation

## Task Link
[Rosetta Code - Modular exponentiation](https://rosettacode.org/wiki/Modular_exponentiation)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public class PowMod {
    public static void main(String[] args){
        BigInteger a = new BigInteger(
      "2988348162058574136915891421498819466320163312926952423791023078876139");
        BigInteger b = new BigInteger(
      "2351399303373464486466122544523690094744975233415544072992656881240319");
        BigInteger m = new BigInteger("10000000000000000000000000000000000000000");
        
        System.out.println(a.modPow(b, m));
    }
}

```

## Python Code
### python_code_1.txt
```python
a = 2988348162058574136915891421498819466320163312926952423791023078876139
b = 2351399303373464486466122544523690094744975233415544072992656881240319
m = 10 ** 40
print(pow(a, b, m))

```

### python_code_2.txt
```python
def power_mod(b, e, m):
    " Without using builtin function "
    x = 1
    while e > 0:
        b, e, x = (
            b * b % m,
            e // 2,
            b * x % m if e % 2 else x
        )

    return x


a = 2988348162058574136915891421498819466320163312926952423791023078876139
b = 2351399303373464486466122544523690094744975233415544072992656881240319
m = 10 ** 40
print(power_mod(a, b, m))

```

