# Padovan n-step number sequences

## Task Link
[Rosetta Code - Padovan n-step number sequences](https://rosettacode.org/wiki/Padovan_n-step_number_sequences)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public final class PadovanNStep {

	public static void main(String[] aArgs) {
		final int limit = 8;
	    final int termCount = 15;
	    
	    System.out.println("First " + termCount + " terms of the Padovan n-step number sequences:");	    
	    padovan(limit, termCount);	    
	}
	
	private static void padovan(int aLimit, int aTermCount) {
		List<Integer> previous = List.of( 1, 1, 1 );
		
		for ( int N = 2; N <= aLimit; N++ ) {
			List<Integer> next = new ArrayList<Integer>(previous.subList(0, N + 1));
			
			while ( next.size() < aTermCount ) {
				int sum = 0;
				for ( int stepBack = 2; stepBack <= N + 1; stepBack++ ) {
					sum += next.get(next.size() - stepBack);
				}
				next.add(sum);
			}
			
			System.out.print(N + ": ");
			next.forEach( term -> System.out.print(String.format("%4d", term)));
			System.out.println();
			
			previous = next;
		}	
	}

}

```

## Python Code
### python_code_1.txt
```python
def pad_like(max_n=8, t=15):
    """
    First t terms of the first 2..max_n-step Padovan sequences.
    """
    start = [[], [1, 1, 1]]     # for n=0 and n=1 (hidden).
    for n in range(2, max_n+1):
        this = start[n-1][:n+1]     # Initialise from last
        while len(this) < t:
            this.append(sum(this[i] for i in range(-2, -n - 2, -1)))
        start.append(this)
    return start[2:]

def pr(p):
    print('''
:::: {| style="text-align: left;" border="4" cellpadding="2" cellspacing="2"
|+ Padovan <math>n</math>-step sequences
|- style="background-color: rgb(255, 204, 255);"
! <math>n</math> !! Values
|-
          '''.strip())
    for n, seq in enumerate(p, 2):
        print(f"| {n:2} || {str(seq)[1:-1].replace(' ', '')+', ...'}\n|-")
    print('|}')

if __name__ == '__main__':
    p = pad_like()
    pr(p)

```

### python_code_2.txt
```python
'''Padovan n-step number sequences'''

from itertools import chain, islice, repeat


# nStepPadovan :: Int -> [Int]
def nStepPadovan(n):
    '''Non-finite series of N-step Padovan numbers,
       defined by a recurrence relation.
    '''
    return unfoldr(recurrence(n))(
        take(1 + n)(
            repeat(1) if 3 > n else (
                nStepPadovan(n - 1)
            )
        )
    )


# recurrence :: Int -> [Int] -> Int
def recurrence(n):
    '''Recurrence relation in Fibonacci,
       Padovan and Perrin sequences.
    '''
    def go(xs):
        h, *t = xs
        return h, t + [sum(take(n)(xs))]
    return go


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''First 15 terms each nStepPadovan(n) series
       where n is drawn from [2..8]
    '''
    xs = range(2, 1 + 8)
    print('Padovan n-step series:\n')
    print(
        spacedTable(list(map(
            lambda k, n: list(chain(
                [k + ' -> '],
                (
                    str(x) for x
                    in take(15)(nStepPadovan(n))
                )
            )),
            (str(x) for x in xs),
            xs
        )))
    )


# ----------------------- GENERIC ------------------------

# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    def go(xs):
        return (
            xs[0:n]
            if isinstance(xs, (list, tuple))
            else list(islice(xs, n))
        )
    return go


# unfoldr :: (b -> Maybe (a, b)) -> b -> [a]
def unfoldr(f):
    '''Generic anamorphism.
       A lazy (generator) list unfolded from a seed value by
       repeated application of f until no residue remains.
       Dual to fold/reduce.
       f returns either None, or just (value, residue).
       For a strict output value, wrap in list().
    '''
    def go(x):
        valueResidue = f(x)
        while None is not valueResidue:
            yield valueResidue[0]
            valueResidue = f(valueResidue[1])
    return go


# ---------------------- FORMATTING ----------------------

# spacedTable :: [[String]] -> String
def spacedTable(rows):
    '''A table with right-aligned columns.
    '''
    columnWidths = [
        max([len(x) for x in col])
        for col in zip(*rows)
    ]
    return '\n'.join(
        ' '.join(map(
            lambda x, w: x.rjust(w, ' '),
            row, columnWidths
        ))
        for row in rows
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

