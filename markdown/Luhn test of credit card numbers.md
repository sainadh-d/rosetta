# Luhn test of credit card numbers

## Task Link
[Rosetta Code - Luhn test of credit card numbers](https://rosettacode.org/wiki/Luhn_test_of_credit_card_numbers)

## Java Code
### java_code_1.txt
```java
public class Luhn {
    public static void main(String[] args) {
        System.out.println(luhnTest("49927398716"));
        System.out.println(luhnTest("49927398717"));
        System.out.println(luhnTest("1234567812345678"));
        System.out.println(luhnTest("1234567812345670"));
    }
    
    public static boolean luhnTest(String number){
        int s1 = 0, s2 = 0;
        String reverse = new StringBuffer(number).reverse().toString();
        for(int i = 0 ;i < reverse.length();i++){
            int digit = Character.digit(reverse.charAt(i), 10);
            if(i % 2 == 0){//this is for odd digits, they are 1-indexed in the algorithm
                s1 += digit;
            }else{//add 2 * digit for 0-4, add 2 * digit - 9 for 5-9
                s2 += 2 * digit;
                if(digit >= 5){
                    s2 -= 9;
                }
            }
        }
        return (s1 + s2) % 10 == 0;
    }
}

```

### java_code_2.txt
```java
public class Luhn {
  public static void main(String[] args) {
    System.out.println(luhnTest(49927398716L));
    System.out.println(luhnTest(499273987163L));
    System.out.println(luhnTest(1234567L));
    System.out.println(luhnTest(0L));
  }

  public static boolean luhnTest(Long digits) {
    int s1 = 0, s2 = 0;
    //Use an alternator for separate odd/even processing
    boolean alternator = true;

    //Confine digit numbers to 8 - 19 per ISO
    if (digits < 1e7 || digits >= 1e19) return false;

    for ( int i = 0; digits > 0; ++i) {
      Long oneDigit = digits % 10;

      if (alternator) {
        s1 += oneDigit.intValue();
      } else {
        oneDigit *= 2;
        s2 += oneDigit > 9 ? oneDigit.intValue() - 9: oneDigit.intValue();
      }
      digits /= 10;
      alternator = !alternator;
    }
    return (s1 + s2) % 10 == 0 ? true : false;
  }
}

```

## Python Code
### python_code_1.txt
```python
>>> def luhn(n):
	r = [int(ch) for ch in str(n)][::-1]
	return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0

>>> for n in (49927398716, 49927398717, 1234567812345678, 1234567812345670):
	print(n, luhn(n))

```

### python_code_2.txt
```python
'''Luhn test of credit card numbers'''

from operator import add, mul
from functools import reduce
from itertools import cycle


# luhn :: Integer -> Bool
def luhn(n):
    '''True if n is a valid Luhn credit card number.'''
    def divMod10Sum(a, x):
        return a + add(*divmod(x, 10))
    return 0 == reduce(
        divMod10Sum,
        map(
            mul,
            cycle([1, 2]),
            map(int, reversed(str(n)))
        ),
        0
    ) % 10


# ---------------------------TEST---------------------------
# main :: IO ()
def main():
    '''Tests'''
    print(list(
        map(luhn, [
            49927398716, 49927398717,
            1234567812345678, 1234567812345670
        ])
    ))


if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
'''Luhn test of credit card numbers'''

from itertools import cycle


# luhn :: String -> Bool
def luhn(k):
    '''True if k is a valid Luhn credit card number string
    '''
    def asDigits(s):
        return (int(c) for c in s)

    return 0 == sum(map(
        lambda f, x: f(x),
        cycle([
            lambda n: n,
            lambda n: sum(asDigits(str(2 * n)))
        ]),
        asDigits(reversed(k))
    )) % 10


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Tests'''
    print('\n'.join([
        repr((x, luhn(x))) for x in [
            "49927398716",
            "49927398717",
            "1234567812345678",
            "1234567812345670"
        ]
    ]))


if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
>>> def vérifLuhn(ch):
  sum = 0
  chParity = len(ch) % 2
  for i in range (len(ch)-1, -1, -1):
    j = int(ch[i])
    if ((i + 1) % 2 != chParity):
      j = j * 2 
    if (j > 9):
      j = j - 9 
    sum = sum + j
  print("value calculated = ", str(sum))
  return sum % 10 == 0         
   
for n in (49927398716, 49927398717, 1234567812345678, 1234567812345670):
        print (str(n)+" =>", vérifLuhn(str(n)))

```

