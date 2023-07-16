# Cullen and Woodall numbers

## Task Link
[Rosetta Code - Cullen and Woodall numbers](https://rosettacode.org/wiki/Cullen_and_Woodall_numbers)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public final  class CullenAndWoodhall {

	public static void main(String[] aArgs) {
		numberSequence(20, NumberType.Cullen);
		
		numberSequence(20, NumberType.Woodhall);
		
		primeSequence(5, NumberType.Cullen);
		
		primeSequence(12, NumberType.Woodhall);
	}

	private enum NumberType { Cullen, Woodhall }
	
	private static void numberSequence(int aCount, NumberType aNumberType) {
		System.out.println();
		System.out.println("The first " + aCount + " " + aNumberType + " numbers are:");
		numberInitialise();
		for ( int index = 1; index <= aCount; index++ ) {
			System.out.print(nextNumber(aNumberType) + " ");
		}	
		System.out.println();	
	}
	
	private static void primeSequence(int aCount, NumberType aNumberType) {
		System.out.println();
		System.out.println("The indexes of the first " + aCount + " " + aNumberType + " primes are:");
		primeInitialise();
		
		while ( count < aCount ) {			
			if ( nextNumber(aNumberType).isProbablePrime(CERTAINTY) ) {
				System.out.print(primeIndex + " ");
				count += 1;
			}
			
			primeIndex += 1; 
		}
		System.out.println();
	}
	
	private static BigInteger nextNumber(NumberType aNumberType) {
		number = number.add(BigInteger.ONE);
		power = power.shiftLeft(1);
		return switch ( aNumberType ) {
			case Cullen -> number.multiply(power).add(BigInteger.ONE);
			case Woodhall -> number.multiply(power).subtract(BigInteger.ONE);
		};
	}
	
	private static void numberInitialise() {
		number = BigInteger.ZERO;
		power = BigInteger.ONE;		
	}
	
	private static void primeInitialise() {	
		count = 0;
		primeIndex = 1;
		numberInitialise();
	}
	
	private static BigInteger number;
	private static BigInteger power;
	private static int count;
	private static int primeIndex;
	
	private static final int CERTAINTY = 20;
	
}

```

## Python Code
### python_code_1.txt
```python
print("working...")
print("First 20 Cullen numbers:")

for n in range(1,21):
    num = n*pow(2,n)+1
    print(str(num),end= " ")

print()
print("First 20 Woodall numbers:")

for n in range(1,21):
    num = n*pow(2,n)-1
    print(str(num),end=" ")

print()
print("done...")

```

### python_code_2.txt
```python
def cullen(n): return((n<<n)+1)
	
def woodall(n): return((n<<n)-1)

print("First 20 Cullen numbers:")
for i in range(1,21):
	print(cullen(i),end=" ")
print()
print()
print("First 20 Woodall numbers:")
for i in range(1,21): 
	print(woodall(i),end=" ")
print()

```

