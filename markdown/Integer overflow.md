# Integer overflow

## Task Link
[Rosetta Code - Integer overflow](https://rosettacode.org/wiki/Integer_overflow)

## Java Code
### java_code_1.txt
```java
public class IntegerOverflow {
    public static void main(String[] args) {
        System.out.println("Signed 32-bit:");
        System.out.println(-(-2147483647 - 1));
        System.out.println(2000000000 + 2000000000);
        System.out.println(-2147483647 - 2147483647);
        System.out.println(46341 * 46341);
        System.out.println((-2147483647 - 1) / -1);
        System.out.println("Signed 64-bit:");
        System.out.println(-(-9223372036854775807L - 1));
        System.out.println(5000000000000000000L + 5000000000000000000L);
        System.out.println(-9223372036854775807L - 9223372036854775807L);
        System.out.println(3037000500L * 3037000500L);
        System.out.println((-9223372036854775807L - 1) / -1);
    }
}

```

## Python Code
### python_code_1.txt
```python
Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for calc in '''   -(-2147483647-1)
   2000000000 + 2000000000
   -2147483647 - 2147483647
   46341 * 46341
   (-2147483647-1) / -1'''.split('\n'):
	ans = eval(calc)
	print('Expression: %r evaluates to %s of type %s'
	      % (calc.strip(), ans, type(ans)))

	
Expression: '-(-2147483647-1)' evaluates to 2147483648 of type <type 'long'>
Expression: '2000000000 + 2000000000' evaluates to 4000000000 of type <type 'long'>
Expression: '-2147483647 - 2147483647' evaluates to -4294967294 of type <type 'long'>
Expression: '46341 * 46341' evaluates to 2147488281 of type <type 'long'>
Expression: '(-2147483647-1) / -1' evaluates to 2147483648 of type <type 'long'>
>>>

```

### python_code_2.txt
```python
Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for calc in '''   -(-2147483647-1)
   2000000000 + 2000000000
   -2147483647 - 2147483647
   46341 * 46341
   (-2147483647-1) / -1'''.split('\n'):
	ans = eval(calc)
	print('Expression: %r evaluates to %s of type %s'
	      % (calc.strip(), ans, type(ans)))

	
Expression: '-(-2147483647-1)' evaluates to 2147483648 of type <class 'int'>
Expression: '2000000000 + 2000000000' evaluates to 4000000000 of type <class 'int'>
Expression: '-2147483647 - 2147483647' evaluates to -4294967294 of type <class 'int'>
Expression: '46341 * 46341' evaluates to 2147488281 of type <class 'int'>
Expression: '(-2147483647-1) / -1' evaluates to 2147483648.0 of type <class 'float'>
>>>

```

