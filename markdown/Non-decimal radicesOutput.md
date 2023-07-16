# Non-decimal radices/Output

## Task Link
[Rosetta Code - Non-decimal radices/Output](https://rosettacode.org/wiki/Non-decimal_radices/Output)

## Java Code
### java_code_1.txt
```java
public static void main(String args[]){
   for(int a= 0;a < 33;a++){
      System.out.println(Integer.toBinaryString(a));
      System.out.println(Integer.toOctalString(a));
      System.out.println(Integer.toHexString(a));
      //the above methods treat the integer as unsigned
      //there are also corresponding Long.to***String() methods for long's.

      System.out.printf("%3o %2d %2x\n",a ,a ,a); //printf like the other languages; binary not supported
   }
}

```

## Python Code
### python_code_1.txt
```python
>>> for n in range(34):
  print " {0:6b} {1:3o} {2:2d} {3:2X}".format(n, n, n, n)
  #The following would give the same output, and, 
  #due to the outer brackets, works with Python 3.0 too
  #print ( " {n:6b} {n:3o} {n:2d} {n:2X}".format(n=n) )

  
      0   0  0  0
      1   1  1  1
     10   2  2  2
     11   3  3  3
    100   4  4  4
    101   5  5  5
    110   6  6  6
    111   7  7  7
   1000  10  8  8
   1001  11  9  9
   1010  12 10  A
   1011  13 11  B
   1100  14 12  C
   1101  15 13  D
   1110  16 14  E
   1111  17 15  F
  10000  20 16 10
  10001  21 17 11
  10010  22 18 12
  10011  23 19 13
  10100  24 20 14
  10101  25 21 15
  10110  26 22 16
  10111  27 23 17
  11000  30 24 18
  11001  31 25 19
  11010  32 26 1A
  11011  33 27 1B
  11100  34 28 1C
  11101  35 29 1D
  11110  36 30 1E
  11111  37 31 1F
 100000  40 32 20
 100001  41 33 21
>>>

```

### python_code_2.txt
```python
for n in range(34):
  print " %3o %2d %2X" % (n, n, n)

```

### python_code_3.txt
```python
n = 33
#Python 3.x:
print(bin(n), oct(n), n, hex(n)) # bin() only available in Python 3.x and 2.6
# output: 0b100001 0o41 33 0x21

#Python 2.x:
#print oct(n), n, hex(n)
# output: 041 33 0x21

```

