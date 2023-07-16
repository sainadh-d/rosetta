# Pseudo-random numbers/Middle-square method

## Task Link
[Rosetta Code - Pseudo-random numbers/Middle-square method](https://rosettacode.org/wiki/Pseudo-random_numbers/Middle-square_method)

## Java Code
### java_code_1.txt
```java
public final class MiddleSquareTask {

	public static void main(String[] aArgs) {
		MiddleSquare random = new MiddleSquare(675248);
		
		for ( int i = 0; i < 5; i++ ) {
	        System.out.println(random.nextInt());
		}
	}	

}

final class MiddleSquare {
	
	public MiddleSquare(int aSeed) {
		final int length = String.valueOf(aSeed).length();
		if ( length % 2 == 1 ) {
			throw new IllegalArgumentException("Seed must have an even number of digits");
		}
		
		state = aSeed;
		divisor = (int) Math.pow(10, length / 2);
		modulus = (int) Math.pow(10, length);
	}
	
	public int nextInt() {
		state = ( ( state * state ) / divisor ) % modulus;		
		return (int) state;
	}
	
	private long state;
	
	private final int divisor, modulus;
	
}

```

## Python Code
### python_code_1.txt
```python
seed = 675248
def random():
    global seed
    seed = int(str(seed ** 2).zfill(12)[3:9])
    return seed
for _ in range(5):
    print(random())

```

