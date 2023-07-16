# One-dimensional cellular automata

## Task Link
[Rosetta Code - One-dimensional cellular automata](https://rosettacode.org/wiki/One-dimensional_cellular_automata)

## Java Code
### java_code_1.txt
```java
public class Life{
	public static void main(String[] args) throws Exception{
		String start= "_###_##_#_#_#_#__#__";
		int numGens = 10;
		for(int i= 0; i < numGens; i++){
			System.out.println("Generation " + i + ": " + start);
			start= life(start);
		}
	}

	public static String life(String lastGen){
		String newGen= "";
		for(int i= 0; i < lastGen.length(); i++){
			int neighbors= 0;
			if (i == 0){//left edge
				neighbors= lastGen.charAt(1) == '#' ? 1 : 0;
			} else if (i == lastGen.length() - 1){//right edge
				neighbors= lastGen.charAt(i - 1) == '#' ? 1 : 0;
			} else{//middle
				neighbors= getNeighbors(lastGen.substring(i - 1, i + 2));
			}

			if (neighbors == 0){//dies or stays dead with no neighbors
				newGen+= "_";
			}
			if (neighbors == 1){//stays with one neighbor
				newGen+= lastGen.charAt(i);
			}
			if (neighbors == 2){//flips with two neighbors
				newGen+= lastGen.charAt(i) == '#' ? "_" : "#";
			}
		}
		return newGen;
	}

	public static int getNeighbors(String group){
		int ans= 0;
		if (group.charAt(0) == '#') ans++;
		if (group.charAt(2) == '#') ans++;
		return ans;
	}
}

```

### java_code_2.txt
```java
public class Life{
	private static char[] trans = "___#_##_".toCharArray();

	private static int v(StringBuilder cell, int i){
		return (cell.charAt(i) != '_') ? 1 : 0;
	}

	public static boolean evolve(StringBuilder cell){
		boolean diff = false;
		StringBuilder backup = new StringBuilder(cell.toString());

		for(int i = 1; i < cell.length() - 3; i++){
			/* use left, self, right as binary number bits for table index */
			backup.setCharAt(i, trans[v(cell, i - 1) * 4 + v(cell, i) * 2
			      					+ v(cell, i + 1)]);
			diff = diff || (backup.charAt(i) != cell.charAt(i));
		}

		cell.delete(0, cell.length());//clear the buffer
		cell.append(backup);//replace it with the new generation
		return diff;
	}

	public static void main(String[] args){
		StringBuilder  c = new StringBuilder("_###_##_#_#_#_#__#__\n");

		do{
			System.out.printf(c.substring(1));
		}while(evolve(c));
	}
}

```

## Python Code
### python_code_1.txt
```python
import random

printdead, printlive = '_#'
maxgenerations = 10
cellcount = 20
offendvalue = '0'

universe = ''.join(random.choice('01') for i in range(cellcount))

neighbours2newstate = {
 '000': '0',
 '001': '0',
 '010': '0',
 '011': '1',
 '100': '0',
 '101': '1',
 '110': '1',
 '111': '0',
 }

for i in range(maxgenerations):
    print "Generation %3i:  %s" % ( i,
          universe.replace('0', printdead).replace('1', printlive) )
    universe = offendvalue + universe + offendvalue
    universe = ''.join(neighbours2newstate[universe[i:i+3]] for i in range(cellcount))

```

### python_code_2.txt
```python
import random

nquads = 5
maxgenerations = 10
fmt = '%%0%ix'%nquads
nbits = 4*nquads
a = random.getrandbits(nbits)  << 1
#a = int('01110110101010100100', 2) << 1
endmask = (2<<nbits)-2;
endvals = 0<<(nbits+1) | 0
tr = ('____', '___#', '__#_', '__##', '_#__', '_#_#', '_##_', '_###',
      '#___', '#__#', '#_#_', '#_##', '##__', '##_#', '###_', '####' )
for i in range(maxgenerations):
   print "Generation %3i:  %s" % (i,(''.join(tr[int(t,16)] for t in (fmt%(a>>1)))))
   a |= endvals
   a = ((a&((a<<1) | (a>>1))) ^ ((a<<1)&(a>>1))) & endmask

```

### python_code_3.txt
```python
>>> gen = [ch == '#' for ch in '_###_##_#_#_#_#__#__']
>>> for n in range(10):
	print(''.join('#' if cell else '_' for cell in gen))
	gen = [0] + gen + [0]
	gen = [sum(gen[m:m+3]) == 2 for m in range(len(gen)-2)]

	
_###_##_#_#_#_#__#__
_#_#####_#_#_#______
__##___##_#_#_______
__##___###_#________
__##___#_##_________
__##____###_________
__##____#_#_________
__##_____#__________
__##________________
__##________________
>>>

```

### python_code_4.txt
```python
'''Cellular Automata'''

from itertools import islice, repeat
from functools import reduce
from random import randint


# nextRowByRule :: Int -> [Bool] -> [Bool]
def nextRowByRule(intRule):
    '''A row of booleans derived by Wolfram rule n
       from another boolean row of the same length.
    '''
    # step :: (Bool, Bool, Bool) -> Bool
    def step(l, x, r):
        return bool(intRule & 2**intFromBools([l, x, r]))

    # go :: [Bool] -> [Bool]
    def go(xs):
        return [False] + list(map(
            step,
            xs, xs[1:], xs[2:]
        )) + [False]
    return go


# intFromBools :: [Bool] -> Int
def intFromBools(xs):
    '''Integer derived by binary interpretation
       of a list of booleans.
    '''
    def go(b, pn):
        power, n = pn
        return (2 * power, n + power if b else n)
    return foldr(go)([1, 0])(xs)[1]


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Samples of Wolfram rule evolutions.
    '''
    print(
        unlines(map(showRuleSample, [104, 30, 110]))
    )


# ----------------------- DISPLAY ------------------------

# showRuleSample :: Int -> String
def showRuleSample(intRule):
    '''16 steps in the evolution
       of a given Wolfram rule.
    '''
    return 'Rule ' + str(intRule) + ':\n' + (
        unlines(map(
            showCells,
            take(16)(
                iterate(nextRowByRule(intRule))(
                    onePixelInLineOf(64) if (
                        bool(randint(0, 1))
                    ) else randomPixelsInLineOf(64)
                )
            )
        ))
    )


# boolsFromInt :: Int -> [Bool]
def boolsFromInt(n):
    '''List of booleans derived by binary
       decomposition of an integer.
    '''
    def go(x):
        return Just((x // 2, bool(x % 2))) if x else Nothing()
    return unfoldl(go)(n)


# nBoolsFromInt :: Int -> Int -> [Bool]
def nBoolsFromInt(n):
    '''List of bools, left-padded to given length n,
       derived by binary decomposition of an integer x.
    '''
    def go(n, x):
        bs = boolsFromInt(x)
        return list(repeat(False, n - len(bs))) + bs
    return lambda x: go(n, x)


# onePixelInLineOf :: Int -> [Bool]
def onePixelInLineOf(n):
    '''A row of n (mainly False) booleans,
       with a single True value in the middle.
    '''
    return nBoolsFromInt(n)(
        2**(n // 2)
    )


# randomPixelsInLineOf :: Int -> [Bool]
def randomPixelsInLineOf(n):
    '''A row of n booleans with pseudorandom values.
    '''
    return [bool(randint(0, 1)) for _ in range(1, 1 + n)]


# showCells :: [Bool] -> String
def showCells(xs):
    '''A block string representation of a list of booleans.
    '''
    return ''.join([chr(9608) if x else ' ' for x in xs])


# ----------------------- GENERIC ------------------------

# Just :: a -> Maybe a
def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.
       Wrapper containing the result of a computation.
    '''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


# Nothing :: () -> Maybe a
def Nothing():
    '''Constructor for an empty Maybe (option type) value.
       Empty wrapper returned where a computation is not possible.
    '''
    return {'type': 'Maybe', 'Nothing': True}


# foldr :: (a -> b -> b) -> b -> [a] -> b
def foldr(f):
    '''Right to left reduction of a list,
       using the binary operator f, and
       starting with an initial accumulator value.
    '''
    def g(a, x):
        return f(x, a)
    return lambda acc: lambda xs: reduce(
        g, xs[::-1], acc
    )


# iterate :: (a -> a) -> a -> Gen [a]
def iterate(f):
    '''An infinite list of repeated
       applications of f to x.
    '''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return go


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


# unfoldl :: (b -> Maybe (b, a)) -> b -> [a]
def unfoldl(f):
    '''Dual to reduce or foldl.
       Where these reduce a list to a summary value, unfoldl
       builds a list from a seed value.
       Where f returns Just(a, b), a is appended to the list,
       and the residual b is used as the argument for the next
       application of f.
       When f returns Nothing, the completed list is returned.
    '''
    def go(v):
        x, r = v, v
        xs = []
        while True:
            mb = f(x)
            if mb.get('Nothing'):
                return xs
            else:
                x, r = mb.get('Just')
                xs.insert(0, r)
        return xs
    return go


# unlines :: [String] -> String
def unlines(xs):
    '''A single string formed by the intercalation
       of a list of strings with the newline character.
    '''
    return '\n'.join(xs)


# MAIN -------------------------------------------------
if __name__ == '__main__':
    main()

```

### python_code_5.txt
```python
def (gens n l)
  prn l
  repeat n
    zap! gen l
    prn l

def (gen l)
  with (a nil  b nil  c l.0)
    collect nil  # won't insert paren without second token
      each x cdr.l
        shift! a b c x
        yield (next a b c)
      yield (next b c nil)

def (next a b c)  # next state of b given neighbors a and c
  if (and a c)  not.b
     (or a c)  b

```

### python_code_6.txt
```python
def (uca l)  # new datatype: Uni-dimensional Cellular Automaton
  (tag uca (list l len.l))

def (len l) :case (isa uca l)  # how to compute its length
  rep.l.1

defcoerce uca list  # how to convert it to a list
  (fn(_) rep._.0)

def (pr l) :case (isa uca l)  # how to print it
  each x l  # transparently coerces to a list for iterating over
    pr (if x "#" "_")

# (l i) returns ith cell when l is a uca, and nil when i is out-of-bounds
defcall uca (l i)
  if (0 <= i < len.l)
    rep.l.0.i

def (gens n l)
  prn l
  repeat n
    zap! gen l
    prn l

def (gen l)
  uca+collect+for i 0 (i < len.l) ++i
    yield (next  (l i-1)  l.i  (l i+1))

# next state of b, given neighbors a and c
def (next a b c)
  if (and a c) not.b
     (or a c)  b

```

