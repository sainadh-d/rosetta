# Arithmetic/Integer

## Task Link
[Rosetta Code - Arithmetic/Integer](https://rosettacode.org/wiki/Arithmetic/Integer)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;

public class IntegerArithmetic {
    public static void main(String[] args) {
        // Get the 2 numbers from command line arguments
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int sum = a + b;        // The result of adding 'a' and 'b' (Note: integer addition is discouraged in print statements due to confusion with string concatenation)
        int difference = a - b; // The result of subtracting 'b' from 'a'
        int product = a * b;    // The result of multiplying 'a' and 'b'
        int division = a / b;   // The result of dividing 'a' by 'b' (Note: 'division' does not contain the fractional result)
        int remainder = a % b;  // The remainder of dividing 'a' by 'b'

        System.out.println("a + b = " + sum);
        System.out.println("a - b = " + difference);
        System.out.println("a * b = " + product);
        System.out.println("quotient of a / b = " + division);   // truncates towards 0
        System.out.println("remainder of a / b = " + remainder);   // same sign as first operand
    }
}

```

## Python Code
### python_code_1.txt
```python
x = int(raw_input("Number 1: "))
y = int(raw_input("Number 2: "))

print "Sum: %d" % (x + y)
print "Difference: %d" % (x - y)
print "Product: %d" % (x * y)
print "Quotient: %d" % (x / y)     #  or x // y  for newer python versions.
                                   # truncates towards negative infinity
print "Remainder: %d" % (x % y)    # same sign as second operand
print "Quotient: %d with Remainder: %d" % divmod(x, y)
print "Power: %d" % x**y

## Only used to keep the display up when the program ends
raw_input( )

```

### python_code_2.txt
```python
def getnum(prompt):
    while True: # retrying ...
        try:
            n = int(raw_input(prompt))
        except ValueError:
            print "Input could not be parsed as an integer. Please try again."\
            continue
        break
    return n

x = getnum("Number1: ")
y = getnum("Number2: ")
...

```

### python_code_3.txt
```python
def arithmetic(x, y):
    for op in "+ - * // % **".split():
        expr = "%(x)s %(op)s %(y)s" % vars()
        print("%s\t=> %s" % (expr, eval(expr)))


arithmetic(12, 8)
arithmetic(input("Number 1: "), input("Number 2: "))

```

### python_code_4.txt
```python
input1 = 18
# input1 = input()
input2 = 7
# input2 = input()

qq = input1 + input2
print("Sum: 		  " + str(qq))
ww = input1 - input2
print("Difference: 	  " + str(ww))
ee = input1 * input2
print("Product: 	  " + str(ee))
rr = input1 / input2
print("Integer quotient: " + str(int(rr)))
print("Float quotient:   " + str(float(rr)))
tt = float(input1 / input2)
uu = (int(tt) - float(tt))*-10
#print(tt)
print("Whole Remainder:  " + str(int(uu)))
print("Actual Remainder: " + str(uu))
yy = input1 ** input2
print("Exponentiation:   " + str(yy))

```

### python_code_5.txt
```python
a <- (read)
b <- (read)
prn "sum: " a+b
prn "difference: " a-b
prn "product: " a*b
prn "quotient: " a/b
prn "integer quotient: " (int a/b)
prn "remainder: " a%b
prn "exponent: " a^b

```

