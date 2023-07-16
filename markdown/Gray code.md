# Gray code

## Task Link
[Rosetta Code - Gray code](https://rosettacode.org/wiki/Gray_code)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public class GrayCode {
	
	public static long grayEncode(long n){
		return n ^ ( n >>> 1 );
	}
	
	public static long grayDecode(long n) {
		long p = n;
		while ( ( n >>>= 1 ) != 0 ) {
			p ^= n;
		}
		return p;
	} 
	
	public static BigInteger grayEncode(BigInteger n) {
		return n.xor(n.shiftRight(1));
	}
	
	public static BigInteger grayDecode(BigInteger n) {
		BigInteger p = n;
		while ( ( n = n.shiftRight(1) ).signum() != 0 ) {
			p = p.xor(n);
		}
		return p;
	}
	
	/**
	 * An alternative version of grayDecode,
	 * less efficient, but demonstrates the principal of gray decoding.
	 */
	public static BigInteger grayDecode2(BigInteger n) {
		String nBits = n.toString(2);
		String result = nBits.substring(0, 1);
		for ( int i = 1; i < nBits.length(); i++ ) {
			// bin[i] = gray[i] ^ bin[i-1]
			// XOR using characters 
			result += nBits.charAt(i) != result.charAt(i - 1) ? "1" : "0";
		}
		return new BigInteger(result, 2);
	}
	
	/**
	 * An alternative version of grayEncode,
	 * less efficient, but demonstrates the principal of gray encoding.
	 */
	public static long grayEncode2(long n) {
		long result = 0;
		for ( int exp = 0; n > 0; n >>= 1, exp++ ) {
			long nextHighestBit = ( n >> 1 ) & 1;
			if ( nextHighestBit == 1 ) {
				result += ( ( n & 1 ) == 0 ) ? ( 1 << exp ) : 0; // flip this bit
			} else {
				result += ( n & 1 ) * ( 1 << exp ); // don't flip this bit
			}
		}
		return result;
	}
	
	public static void main(String[] args){
		System.out.println("i\tBinary\tGray\tGray2\tDecoded");
		System.out.println("=======================================");
		for ( int i = 0; i < 32; i++ ) {
			System.out.print(i + "\t");
			System.out.print(Integer.toBinaryString(i) + "\t");
			System.out.print(Long.toBinaryString(grayEncode(i)) + "\t");
			System.out.print(Long.toBinaryString(grayEncode2(i)) + "\t");
			System.out.println(grayDecode(grayEncode(i)));
		}
		System.out.println();
		
		final BigInteger base = BigInteger.TEN.pow(25).add( new BigInteger("12345678901234567890") );		
		for ( int i = 0; i < 5; i++ ) {
			BigInteger test = base.add(BigInteger.valueOf(i));
			System.out.println("test decimal      = " + test);
			System.out.println("gray code decimal = " + grayEncode(test));
			System.out.println("gray code binary  = " + grayEncode(test).toString(2));
			System.out.println("decoded decimal   = " + grayDecode(grayEncode(test)));
			System.out.println("decoded2 decimal  = " + grayDecode2(grayEncode(test)));
			System.out.println();
		}
	}
	
}

```

## Python Code
### python_code_1.txt
```python
>>> def int2bin(n):
	'From positive integer to list of binary bits, msb at index 0'
	if n:
		bits = []
		while n:
			n,remainder = divmod(n, 2)
			bits.insert(0, remainder)
		return bits
	else: return [0]

	
>>> def bin2int(bits):
	'From binary bits, msb at index 0 to integer'
	i = 0
	for bit in bits:
		i = i * 2 + bit
	return i

```

### python_code_2.txt
```python
>>> def bin2gray(bits):
	return bits[:1] + [i ^ ishift for i, ishift in zip(bits[:-1], bits[1:])]

>>> def gray2bin(bits):
	b = [bits[0]]
	for nextb in bits[1:]: b.append(b[-1] ^ nextb)
	return b

```

### python_code_3.txt
```python
>>> for i in range(16):
	print('int:%2i -> bin:%12r -> gray:%12r -> bin:%12r -> int:%2i' %
	      ( i,
	        int2bin(i),
	        bin2gray(int2bin(i)),
	        gray2bin(bin2gray(int2bin(i))),
	        bin2int(gray2bin(bin2gray(int2bin(i))))
	      ))

	
int: 0 -> bin:         [0] -> gray:         [0] -> bin:         [0] -> int: 0
int: 1 -> bin:         [1] -> gray:         [1] -> bin:         [1] -> int: 1
int: 2 -> bin:      [1, 0] -> gray:      [1, 1] -> bin:      [1, 0] -> int: 2
int: 3 -> bin:      [1, 1] -> gray:      [1, 0] -> bin:      [1, 1] -> int: 3
int: 4 -> bin:   [1, 0, 0] -> gray:   [1, 1, 0] -> bin:   [1, 0, 0] -> int: 4
int: 5 -> bin:   [1, 0, 1] -> gray:   [1, 1, 1] -> bin:   [1, 0, 1] -> int: 5
int: 6 -> bin:   [1, 1, 0] -> gray:   [1, 0, 1] -> bin:   [1, 1, 0] -> int: 6
int: 7 -> bin:   [1, 1, 1] -> gray:   [1, 0, 0] -> bin:   [1, 1, 1] -> int: 7
int: 8 -> bin:[1, 0, 0, 0] -> gray:[1, 1, 0, 0] -> bin:[1, 0, 0, 0] -> int: 8
int: 9 -> bin:[1, 0, 0, 1] -> gray:[1, 1, 0, 1] -> bin:[1, 0, 0, 1] -> int: 9
int:10 -> bin:[1, 0, 1, 0] -> gray:[1, 1, 1, 1] -> bin:[1, 0, 1, 0] -> int:10
int:11 -> bin:[1, 0, 1, 1] -> gray:[1, 1, 1, 0] -> bin:[1, 0, 1, 1] -> int:11
int:12 -> bin:[1, 1, 0, 0] -> gray:[1, 0, 1, 0] -> bin:[1, 1, 0, 0] -> int:12
int:13 -> bin:[1, 1, 0, 1] -> gray:[1, 0, 1, 1] -> bin:[1, 1, 0, 1] -> int:13
int:14 -> bin:[1, 1, 1, 0] -> gray:[1, 0, 0, 1] -> bin:[1, 1, 1, 0] -> int:14
int:15 -> bin:[1, 1, 1, 1] -> gray:[1, 0, 0, 0] -> bin:[1, 1, 1, 1] -> int:15
>>>

```

