# Modified random distribution

## Task Link
[Rosetta Code - Modified random distribution](https://rosettacode.org/wiki/Modified_random_distribution)

## Java Code
### java_code_1.txt
```java
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.Stream;

interface ModifierInterface {	
	double modifier(double aDouble);	
}

public final class ModifiedRandomDistribution222 {

	public static void main(String[] aArgs) {
		final int sampleSize = 100_000;
		final int binCount = 20;
		final double binSize = 1.0 / binCount;
		
		List<Integer> bins = Stream.generate( () -> 0 ).limit(binCount).toList();
		
	    for ( int i = 0; i < sampleSize; i++ ) {
	    	double random = modifiedRandom(modifier);
	        int binNumber = (int) Math.floor(random / binSize);
	        bins.set(binNumber, bins.get(binNumber) + 1);
	    }
		
		System.out.println("Modified random distribution with " + sampleSize + " samples in range [0, 1):");
		System.out.println();
		System.out.println("    Range           		  Number of samples within range");
		
		final int scaleFactor = 125;
		for ( int i = 0; i < binCount; i++ ) {
			String histogram = String.valueOf("#").repeat(bins.get(i) / scaleFactor);
			System.out.println(String.format("%4.2f ..< %4.2f %s %s",
				(float) i / binCount, (float) ( i + 1.0 ) / binCount, histogram, bins.get(i)));			
		}		
	}
	
	private static double modifiedRandom(ModifierInterface aModifier) {
		double result = -1.0;
		
		while ( result < 0.0 ) {
			double randomOne = RANDOM.nextDouble();
			double randomTwo = RANDOM.nextDouble();
			if ( randomTwo < aModifier.modifier(randomOne) ) {
				result = randomOne;
			}
		}
		
		return result;		
	}		
	
	private static ModifierInterface modifier = aX -> ( aX < 0.5 ) ? 2 * ( 0.5 - aX ) : 2 * ( aX - 0.5 );	
	
	private static final ThreadLocalRandom RANDOM = ThreadLocalRandom.current();

}

```

## Python Code
### python_code_1.txt
```python
import random
from typing import List, Callable, Optional


def modifier(x: float) -> float:
    """
    V-shaped, modifier(x) goes from 1 at 0 to 0 at 0.5 then back to 1 at 1.0 .

    Parameters
    ----------
    x : float
        Number, 0.0 .. 1.0 .

    Returns
    -------
    float
        Target probability for generating x; between 0 and 1.

    """
    return 2*(.5 - x) if x < 0.5 else 2*(x - .5)


def modified_random_distribution(modifier: Callable[[float], float],
                                 n: int) -> List[float]:
    """
    Generate n random numbers between 0 and 1 subject to modifier.

    Parameters
    ----------
    modifier : Callable[[float], float]
        Target random number gen. 0 <= modifier(x) < 1.0 for 0 <= x < 1.0 .
    n : int
        number of random numbers generated.

    Returns
    -------
    List[float]
        n random numbers generated with given probability.

    """
    d: List[float] = []
    while len(d) < n:
        r1 = prob = random.random()
        if random.random() < modifier(prob):
            d.append(r1)
    return d


if __name__ == '__main__':
    from collections import Counter

    data = modified_random_distribution(modifier, 50_000)
    bins = 15
    counts = Counter(d // (1 / bins) for d in data)
    #
    mx = max(counts.values())
    print("   BIN, COUNTS, DELTA: HISTOGRAM\n")
    last: Optional[float] = None
    for b, count in sorted(counts.items()):
        delta = 'N/A' if last is None else str(count - last)
        print(f"  {b / bins:5.2f},  {count:4},  {delta:>4}: "
              f"{'#' * int(40 * count / mx)}")
        last = count

```

