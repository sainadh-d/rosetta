# Pseudo-random numbers/Splitmix64

## Task Link
[Rosetta Code - Pseudo-random numbers/Splitmix64](https://rosettacode.org/wiki/Pseudo-random_numbers/Splitmix64)

## Java Code
### java_code_1.txt
```java
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public final class PseudoRandomSplitmix64 {

	public static void main(String[] aArgs) {
		Splitmix64 random = new Splitmix64();
		random.seed(1234567);
		for ( int i = 0; i < 5; i++ ) {
			System.out.println(random.nextInt());
		}
		
		List<Integer> counts = new ArrayList<Integer>(Collections.nCopies(5, 0));
		
		Splitmix64 rand = new Splitmix64(987654321);
	    for ( int i = 0; i < 100_000; i++ ) {	    	
	        BigDecimal value = rand.nextFloat();
	        final int count = value.multiply(BigDecimal.valueOf(5.0)).toBigInteger().intValue();
	        counts.set(count, counts.get(count) + 1);
	    }
	    
	    System.out.println(System.lineSeparator() + "The counts for 100,000 repetitions are: ");
	    for ( int i = 0; i < 5; i++ ) {
	    	System.out.print(i + ": " + counts.get(i) + "   ");
	    }
	    System.out.println();
    }
	
}

final class Splitmix64 {
	
	public Splitmix64() {
		state = BigInteger.ZERO;
	}
	
	public Splitmix64(long aSeed) {
		state = BigInteger.valueOf(aSeed).and(mask64);
	}
	
	public void seed(long aNumber) {
		state = BigInteger.valueOf(aNumber);
	}
	    
	public BigInteger nextInt() {
		state = state.add(constant1).and(mask64);
        BigInteger z = state;
        z = z.xor(z.shiftRight(30)).multiply(constant2).and(mask64);
        z = z.xor(z.shiftRight(27)).multiply(constant3).and(mask64);
        BigInteger result = z.xor(z.shiftRight(31)).and(mask64);
    
        return result;
	}
	    
	public BigDecimal nextFloat() {
		return new BigDecimal(nextInt()).divide(twoPower64, MathContext.DECIMAL64);
	}
	    
	private BigInteger state;
	
	private final BigInteger constant1 = new BigInteger("9e3779b97f4a7c15", 16);
	private final BigInteger constant2 = new BigInteger("bf58476d1ce4e5b9", 16); 
	private final BigInteger constant3 = new BigInteger("94d049bb133111eb", 16);
	private final BigInteger mask64 = BigInteger.ONE.shiftLeft(64).subtract(BigInteger.ONE);
	private final BigDecimal twoPower64 = new BigDecimal(BigInteger.ONE.shiftLeft(64));

}

```

## Python Code
### python_code_1.txt
```python
MASK64 = (1 << 64) - 1
C1 = 0x9e3779b97f4a7c15
C2 = 0xbf58476d1ce4e5b9
C3 = 0x94d049bb133111eb



class Splitmix64():
    
    def __init__(self, seed=0):
        self.state = seed & MASK64

    def seed(self, num):
        self.state =  num & MASK64
    
    def next_int(self):
        "return random int between 0 and 2**64"
        z = self.state = (self.state + C1) & MASK64
        z = ((z ^ (z >> 30)) * C2) & MASK64
        z = ((z ^ (z >> 27)) * C3) & MASK64
        answer = (z ^ (z >> 31)) & MASK64

        return answer
    
    def  next_float(self):
        "return random float between 0 and 1"
        return self.next_int() / (1 << 64)
    

if __name__ == '__main__':
    random_gen = Splitmix64()
    random_gen.seed(1234567)
    for i in range(5):
        print(random_gen.next_int())
        
    random_gen.seed(987654321)
    hist = {i:0 for i in range(5)}
    for i in range(100_000):
        hist[int(random_gen.next_float() *5)] += 1
    print(hist)

```

