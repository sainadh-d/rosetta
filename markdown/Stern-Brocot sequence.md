# Stern-Brocot sequence

## Task Link
[Rosetta Code - Stern-Brocot sequence](https://rosettacode.org/wiki/Stern-Brocot_sequence)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.LinkedList;

public class SternBrocot {
	static LinkedList<Integer> sequence = new LinkedList<Integer>(){{
		add(1); add(1);
	}};
	
	private static void genSeq(int n){
		for(int conIdx = 1; sequence.size() < n; conIdx++){
			int consider = sequence.get(conIdx);
			int pre = sequence.get(conIdx - 1);
			sequence.add(consider + pre);
			sequence.add(consider);
		}
		
	}
	
	public static void main(String[] args){
		genSeq(1200);
		System.out.println("The first 15 elements are: " + sequence.subList(0, 15));
		for(int i = 1; i <= 10; i++){
			System.out.println("First occurrence of " + i + " is at " + (sequence.indexOf(i) + 1));
		}
		
		System.out.println("First occurrence of 100 is at " + (sequence.indexOf(100) + 1));
		
		boolean failure = false;
		for(int i = 0; i < 999; i++){
			failure |= !BigInteger.valueOf(sequence.get(i)).gcd(BigInteger.valueOf(sequence.get(i + 1))).equals(BigInteger.ONE);
		}
		System.out.println("All GCDs are" + (failure ? " not" : "") + " 1");
	}
}

```

### java_code_2.txt
```java
import java.awt.*;
import javax.swing.*;

public class SternBrocot extends JPanel {

    public SternBrocot() {
        setPreferredSize(new Dimension(800, 500));
        setFont(new Font("Arial", Font.PLAIN, 18));
        setBackground(Color.white);
    }

    private void drawTree(int n1, int d1, int n2, int d2,
            int x, int y, int gap, int lvl, Graphics2D g) {

        if (lvl == 0)
            return;

        // mediant
        int numer = n1 + n2;
        int denom = d1 + d2;

        if (lvl > 1) {
            g.drawLine(x + 5, y + 4, x - gap + 5, y + 124);
            g.drawLine(x + 5, y + 4, x + gap + 5, y + 124);
        }

        g.setColor(getBackground());
        g.fillRect(x - 10, y - 15, 35, 40);

        g.setColor(getForeground());
        g.drawString(String.valueOf(numer), x, y);
        g.drawString("_", x, y + 2);
        g.drawString(String.valueOf(denom), x, y + 22);

        drawTree(n1, d1, numer, denom, x - gap, y + 120, gap / 2, lvl - 1, g);
        drawTree(numer, denom, n2, d2, x + gap, y + 120, gap / 2, lvl - 1, g);
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        int w = getWidth();

        drawTree(0, 1, 1, 0, w / 2, 50, w / 4, 4, g);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Stern-Brocot Tree");
            f.setResizable(false);
            f.add(new SternBrocot(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
def stern_brocot(predicate=lambda series: len(series) < 20):
    """\
    Generates members of the stern-brocot series, in order, returning them when the predicate becomes false

    >>> print('The first 10 values:',
              stern_brocot(lambda series: len(series) < 10)[:10])
    The first 10 values: [1, 1, 2, 1, 3, 2, 3, 1, 4, 3]
    >>>
    """

    sb, i = [1, 1], 0
    while predicate(sb):
        sb += [sum(sb[i:i + 2]), sb[i + 1]]
        i += 1
    return sb


if __name__ == '__main__':
    from fractions import gcd

    n_first = 15
    print('The first %i values:\n  ' % n_first,
          stern_brocot(lambda series: len(series) < n_first)[:n_first])
    print()
    n_max = 10
    for n_occur in list(range(1, n_max + 1)) + [100]:
        print('1-based index of the first occurrence of %3i in the series:' % n_occur,
              stern_brocot(lambda series: n_occur not in series).index(n_occur) + 1)
              # The following would be much faster. Note that new values always occur at odd indices
              # len(stern_brocot(lambda series: n_occur != series[-2])) - 1)

    print()
    n_gcd = 1000
    s = stern_brocot(lambda series: len(series) < n_gcd)[:n_gcd]
    assert all(gcd(prev, this) == 1
               for prev, this in zip(s, s[1:])), 'A fraction from adjacent terms is reducible'

```

### python_code_2.txt
```python
>>> from itertools import takewhile, tee, islice
>>>  from collections import deque
>>> from fractions import gcd
>>> 
>>> def stern_brocot():
    sb = deque([1, 1])
    while True:
        sb += [sb[0] + sb[1], sb[1]]
        yield sb.popleft()

        
>>> [s for _, s in zip(range(15), stern_brocot())]
[1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4]
>>> [1 + sum(1 for i in takewhile(lambda x: x != occur, stern_brocot()))
     for occur in (list(range(1, 11)) + [100])]
[1, 3, 5, 9, 11, 33, 19, 21, 35, 39, 1179]
>>> prev, this = tee(stern_brocot(), 2)
>>> next(this)
1
>>> all(gcd(p, t) == 1 for p, t in islice(zip(prev, this), 1000))
True
>>>

```

### python_code_3.txt
```python
'''Stern-Brocot sequence'''

import math
import operator
from itertools import count, dropwhile, islice, takewhile


# sternBrocot :: Generator [Int]
def sternBrocot():
    '''Non-finite list of the Stern-Brocot
       sequence of integers.
    '''
    def go(xs):
        [a, b] = xs[:2]
        return (a, xs[1:] + [a + b, b])
    return unfoldr(go)([1, 1])


# ------------------------ TESTS -------------------------
# main :: IO ()
def main():
    '''Various tests'''

    [eq, ne, gcd] = map(
        curry,
        [operator.eq, operator.ne, math.gcd]
    )

    sbs = take(1200)(sternBrocot())
    ixSB = zip(sbs, enumFrom(1))

    print(unlines(map(str, [

        # First 15 members of the sequence.
        take(15)(sbs),

        # Indices of where the numbers [1..10] first appear.
        take(10)(
            nubBy(on(eq)(fst))(
                sorted(
                    takewhile(
                        compose(ne(12))(fst),
                        ixSB
                    ),
                    key=fst
                )
            )
        ),

        #  Index of where the number 100 first appears.
        take(1)(dropwhile(compose(ne(100))(fst), ixSB)),

        # Is the gcd of any two consecutive members,
        # up to the 1000th member, always one ?
        every(compose(eq(1)(gcd)))(
            take(1000)(zip(sbs, tail(sbs)))
        )
    ])))


# ----------------- GENERIC ABSTRACTIONS -----------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    '''A curried function derived
       from an uncurried function.'''
    return lambda a: lambda b: f(a, b)


# enumFrom :: Enum a => a -> [a]
def enumFrom(x):
    '''A non-finite stream of enumerable values,
       starting from the given value.'''
    return count(x) if isinstance(x, int) else (
        map(chr, count(ord(x)))
    )


# every :: (a -> Bool) -> [a] -> Bool
def every(p):
    '''True if p(x) holds for every x in xs'''
    return lambda xs: all(map(p, xs))


# fst :: (a, b) -> a
def fst(tpl):
    '''First member of a pair.'''
    return tpl[0]


# head :: [a] -> a
def head(xs):
    '''The first element of a non-empty list.'''
    return xs[0]


# nubBy :: (a -> a -> Bool) -> [a] -> [a]
def nubBy(p):
    '''A sublist of xs from which all duplicates,
       (as defined by the equality predicate p)
       are excluded.
    '''
    def go(xs):
        if not xs:
            return []
        x = xs[0]
        return [x] + go(
            list(filter(
                lambda y: not p(x)(y),
                xs[1:]
            ))
        )
    return go


# on :: (b -> b -> c) -> (a -> b) -> a -> a -> c
def on(f):
    '''A function returning the value of applying
      the binary f to g(a) g(b)'''
    return lambda g: lambda a: lambda b: f(g(a))(g(b))


# tail :: [a] -> [a]
# tail :: Gen [a] -> [a]
def tail(xs):
    '''The elements following the head of a
       (non-empty) list or generator stream.'''
    if isinstance(xs, list):
        return xs[1:]
    else:
        islice(xs, 1)  # First item dropped.
        return xs


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.'''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )


# unfoldr :: (b -> Maybe (a, b)) -> b -> Gen [a]
def unfoldr(f):
    '''A lazy (generator) list unfolded from a seed value
       by repeated application of f until no residue remains.
       Dual to fold/reduce.
       f returns either None or just (value, residue).
       For a strict output list, wrap the result with list()
    '''
    def go(x):
        valueResidue = f(x)
        while valueResidue:
            yield valueResidue[0]
            valueResidue = f(valueResidue[1])
    return go


# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.'''
    return '\n'.join(xs)


# MAIN ---
if __name__ == '__main__':
    main()

```

