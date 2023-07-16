# Bitwise operations

## Task Link
[Rosetta Code - Bitwise operations](https://rosettacode.org/wiki/Bitwise_operations)

## Java Code
### java_code_2.txt
```java
public static void bitwise(int a, int b){
  System.out.println("a AND b: " + (a & b));
  System.out.println("a OR b: "+ (a | b));
  System.out.println("a XOR b: "+ (a ^ b));
  System.out.println("NOT a: " + ~a);
  System.out.println("a << b: " + (a << b)); // left shift
  System.out.println("a >> b: " + (a >> b)); // arithmetic right shift
  System.out.println("a >>> b: " + (a >>> b)); // logical right shift
  System.out.println("a rol b: " + Integer.rotateLeft(a, b)); //rotate left, Java 1.5+
  System.out.println("a ror b: " + Integer.rotateRight(a, b)); //rotate right, Java 1.5+
}

```

### java_code_3.txt
```java
a <<= 3;
a = a << 3;
a *= 8; //2 * 2 * 2 = 8
a = a * 8;

```

## Python Code
### python_code_1.txt
```python
def bitwise_built_ins(width, a, b):
    mask = (1 << width) - 1
    print(f"""\
    AND:     0b{a :0{width}b} 
           & 0b{b :0{width}b} 
           = 0b{(a & b) & mask :0{width}b}
           
    OR:      0b{a :0{width}b} 
           | 0b{b :0{width}b} 
           = 0b{(a | b) & mask :0{width}b}
           
    XOR:     0b{a :0{width}b} 
           ^ 0b{b :0{width}b} 
           = 0b{(a ^ b) & mask :0{width}b}
           
    NOT:   ~ 0b{a :0{width}b} 
           = 0b{(~a) & mask :0{width}b}
           
    SHIFTS
    
      RIGHT:   0b{a :0{width}b} >> 1
             = 0b{(a >> 1) & mask :0{width}b}      
    
      LEFT:    0b{a :0{width}b} << 1
             = 0b{(a << 1) & mask :0{width}b}      
""")

def rotr(width, a, n):
    "Rotate a, n times to the right"
    if n < 0:
        return rotl(width, a, -n)
    elif n == 0:
        return a
    else:
        mask = (1 << width) - 1
        a, n = a & mask, n % width
        return ((a >> n)    # top moved down
                | ((a & ((1 << n) - 1))   # Bottom masked...
                   << (width - n)))  # ... then moved up    

def rotl(width, a, n):
    "Rotate a, n times to the left"
    if n < 0:
        return rotr(width, a, -n)
    elif n == 0:
        return a
    else:
        mask = (1 << width) - 1
        a, n = a & mask, n % width
        return (((a << n) & mask)      # bottom shifted up and masked
                | (a >> (width - n)))  # Top moved down  
    
def asr(width, a, n):
    "Arithmetic shift a, n times to the right. (sign preserving)."
    mask, top_bit_mask = ((1 << width) - 1), 1 << (width - 1)
    if n < 0:
        return  (a << -n) & mask
    elif n == 0:
        return a
    elif n >= width:
        return mask if a & top_bit_mask else 0
    else:
        a = a & mask
        if a & top_bit_mask:    # Sign bit set?
            signs = (1 << n) - 1
            return a >> n | (signs << width - n)
        else:
            return a >> n
    
      
def helper_funcs(width, a):
    mask, top_bit_mask = ((1 << width) - 1), 1 << (width - 1)
    aa = a | top_bit_mask  # a with top bit set
    print(f"""\
    ROTATIONS
    
      RIGHT:   rotr({width}, 0b{a :0{width}b}, 1)
               =       0b{rotr(width, a, 1) :0{width}b}      
               rotr({width}, 0b{a :0{width}b}, 2)
               =       0b{rotr(width, a, 2) :0{width}b}      
               rotr({width}, 0b{a :0{width}b}, 4)
               =       0b{rotr(width, a, 4) :0{width}b}      
    
      LEFT:    rotl({width}, 0b{a :0{width}b}, 1)
               =       0b{rotl(width, a, 1) :0{width}b}      
               rotl({width}, 0b{a :0{width}b}, 2)
               =       0b{rotl(width, a, 2) :0{width}b}      
               rotl({width}, 0b{a :0{width}b}, 4)
               =       0b{rotl(width, a, 4) :0{width}b}    
    
    SIGN-EXTENDING ARITHMETIC SHIFT RIGHT
    
               asr({width}, 0b{a :0{width}b}, 1)
               =      0b{asr(width, a, 1) :0{width}b}      
               asr({width}, 0b{aa :0{width}b}, 1)
               =      0b{asr(width, aa, 1) :0{width}b}      
               asr({width}, 0b{a :0{width}b}, 2)
               =      0b{asr(width, a, 2) :0{width}b}      
               asr({width}, 0b{aa :0{width}b}, 2)
               =      0b{asr(width, aa, 2) :0{width}b}      
               asr({width}, 0b{a :0{width}b}, 4)
               =      0b{asr(width, a, 4) :0{width}b} 
               asr({width}, 0b{aa :0{width}b}, 4)
               =      0b{asr(width, aa, 4) :0{width}b} 
""")

if __name__ == '__main__':
    bitwise_built_ins(8, 27, 125)
    helper_funcs(8, 27)

```

### python_code_2.txt
```python
def bitwise(a, b):
        print 'a and b:', a & b
        print 'a or b:', a | b
        print 'a xor b:', a ^ b
        print 'not a:', ~a
        print 'a << b:', a << b # left shift
        print 'a >> b:', a >> b # arithmetic right shift

```

### python_code_3.txt
```python
# 8-bit bounded shift:
x = x << n & 0xff
# ditto for 16 bit:
x = x << n & 0xffff
# ... and 32-bit:
x = x << n & 0xffffffff
# ... and 64-bit:
x = x << n & 0xffffffffffffffff

```

### python_code_4.txt
```python
def bitstr(n, width=None):
   """return the binary representation of n as a string and
      optionally zero-fill (pad) it to a given length
   """
   result = list()
   while n:
      result.append(str(n%2))
      n = int(n/2)
   if (width is not None) and len(result) < width:
      result.extend(['0'] * (width - len(result)))
   result.reverse()
   return ''.join(result)

def mask(n):
   """Return a bitmask of length n (suitable for masking against an
      int to coerce the size to a given length)
   """
   if n >= 0:
       return 2**n - 1
   else:
       return 0

def rol(n, rotations=1, width=8):
    """Return a given number of bitwise left rotations of an integer n,
       for a given bit field width.
    """
    rotations %= width
    if rotations < 1:
        return n
    n &= mask(width) ## Should it be an error to truncate here?
    return ((n << rotations) & mask(width)) | (n >> (width - rotations))

def ror(n, rotations=1, width=8):
    """Return a given number of bitwise right rotations of an integer n,
       for a given bit field width.
    """
    rotations %= width
    if rotations < 1:
        return n
    n &= mask(width)
    return (n >> rotations) | ((n << (width - rotations)) & mask(width))

```

