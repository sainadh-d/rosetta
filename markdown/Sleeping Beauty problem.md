# Sleeping Beauty problem

## Task Link
[Rosetta Code - Sleeping Beauty problem](https://rosettacode.org/wiki/Sleeping_Beauty_problem)

## Java Code
### java_code_1.txt
```java
import java.util.concurrent.ThreadLocalRandom;

public final class SleepingBeauty {

	public static void main(String[] aArgs) {
		final int experiments = 1_000_000;
	    ThreadLocalRandom random = ThreadLocalRandom.current();
	    
	    enum Coin { HEADS, TAILS }
	    
	    int heads = 0;
	    int awakenings = 0;	    
	    
	    for ( int i = 0; i < experiments; i++ ) {
	        Coin coin = Coin.values()[random.nextInt(0, 2)];
	        switch ( coin ) {
	        	case HEADS -> { awakenings += 1; heads += 1; }
	        	case TAILS -> awakenings += 2;
	        }
	    }
	    
	    System.out.println("Awakenings over " + experiments + " experiments: " + awakenings);
	    String credence = String.format("%.3f", (double) heads / awakenings); 
	    System.out.println("Sleeping Beauty should estimate a credence of: " + credence);
	}
	
}

```

## Python Code
### python_code_1.txt
```python
from random import choice

def sleeping_beauty_experiment(repetitions):
    """
    Run the Sleeping Beauty Problem experiment `repetitions` times, checking to see
    how often we had heads on waking Sleeping Beauty.
    """
    gotheadsonwaking = 0
    wakenings = 0
    for _ in range(repetitions):
        coin_result = choice(["heads", "tails"])

        # On Monday, we check if we got heads.
        wakenings += 1
        if coin_result == "heads":
            gotheadsonwaking += 1

        # If tails, we do this again, but of course we will not add as if it was heads..
        if coin_result == "tails":
            wakenings += 1
            if coin_result == "heads":
                gotheadsonwaking += 1   # never done


    # Show the number of times she was wakened.
    print("Wakenings over", repetitions, "experiments:", wakenings)

    # Return the number of correct bets SB made out of the total number
    # of times she is awoken over all the experiments with that bet.
    return gotheadsonwaking / wakenings


CREDENCE = sleeping_beauty_experiment(1_000_000)
print("Results of experiment:  Sleeping Beauty should estimate a credence of:", CREDENCE)

```

### python_code_2.txt
```python
'''Sleeping Beauty Problem'''

from random import choice
from itertools import repeat
from functools import reduce


# experiment :: (Int, Int) -> IO (Int, Int)
def experiment(headsWakings):
    '''A pair of counts updated by a coin flip.
    '''
    heads, wakings = headsWakings

    return (
        1 + heads, 1 + wakings
    ) if "h" == choice(["h", "t"]) else (
        heads, 2 + wakings
    )


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Observed results from one million runs.'''

    n = 1_000_000
    heads, wakes = applyN(n)(
        experiment
    )(
        (0, 0)
    )

    print(
        f'{wakes} wakenings over {n} experiments.\n'
    )
    print('Sleeping Beauty should estimate credence')
    print(f'at around {round(heads/wakes, 3)}')


# ----------------------- GENERIC ------------------------

# applyN :: Int -> (a -> a) -> a -> a
def applyN(n):
    '''n applications of f.
       (Church numeral n).
    '''
    def go(f):
        def ga(a, g):
            return g(a)

        def fn(x):
            return reduce(ga, repeat(f, n), x)
        return fn
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

