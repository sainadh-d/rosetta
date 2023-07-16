# Bioinformatics/base count

## Task Link
[Rosetta Code - Bioinformatics/base count](https://rosettacode.org/wiki/Bioinformatics/base_count)

## Java Code
### java_code_1.txt
```java
void printBaseCount(String string) throws IOException {
    BufferedReader reader = new BufferedReader(new StringReader(string));
    int index = 0;
    String sequence;
    int A = 0, C = 0, G = 0, T = 0;
    int a, c, g, t;
    while ((sequence = reader.readLine()) != null) {
        System.out.printf("%d %s ", index++, sequence);
        a = c = g = t = 0;
        for (char base : sequence.toCharArray()) {
            switch (base) {
                case 'A' -> {
                    A++;
                    a++;
                }
                case 'C' -> {
                    C++;
                    c++;
                }
                case 'G' -> {
                    G++;
                    g++;
                }
                case 'T' -> {
                    T++;
                    t++;
                }
            }
        }
        System.out.printf("[A %2d, C %2d, G %2d, T %2d]%n", a, c, g, t);
    }
    reader.close();
    int total = A + C + G + T;
    System.out.printf("%nTotal of %d bases%n", total);
    System.out.printf("A %3d (%.2f%%)%n", A, ((double) A / total) * 100);
    System.out.printf("C %3d (%.2f%%)%n", C, ((double) C / total) * 100);
    System.out.printf("G %3d (%.2f%%)%n", G, ((double) G / total) * 100);
    System.out.printf("T %3d (%.2f%%)%n", T, ((double) T / total) * 100);
}

```

### java_code_2.txt
```java
import java.util.HashMap;
import java.util.Map;

public class orderedSequence {
    public static void main(String[] args) {
        Sequence gene = new Sequence("CGTAAAAAATTACAACGTCCTTTGGCTATCTCTTAAACTCCTGCTAAATGCTCGTGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTGAGGACAAAGGTCAAGATGGAGCGCATCGAACGCAATAAGGATCATTTGATGGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTTCGATTCTGCTTATAACACTATGTTCTTATGAAATGGATGTTCTGAGTTGGTCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTATATTTAATTTTTCTATATAGCGATCTGTATTTAAGCAATTCATTTAGGTTATCGCCGCGATGCTCGGTTCGGACCGCCAAGCATCTGGCTCCACTGCTAGTGTCCTAAATTTGAATGGCAAACACAAATAAGATTTAGCAATTCGTGTAGACGACCGGGGACTTGCATGATGGGAGCAGCTTTGTTAAACTACGAACGTAAT");
        gene.runSequence();
    }
}

/** Separate class for defining behaviors */
public class Sequence {
    
    private final String seq;
    
    public Sequence(String sq) {
        this.seq = sq;
    }
    
    /** print the organized structure of the sequence */
    public void prettyPrint() {
        System.out.println("Sequence:");
        int i = 0;
        for ( ; i < seq.length() - 50 ; i += 50) {
            System.out.printf("%5s : %s\n", i + 50, seq.substring(i, i + 50));
        }
        System.out.printf("%5s : %s\n", seq.length(), seq.substring(i));
    }
    
    /** display a base vs. frequency chart */
    public void displayCount() {
        Map<Character, Integer> counter = new HashMap<>();
        for (int i = 0 ; i < seq.length() ; ++i) {
            counter.merge(seq.charAt(i), 1, Integer::sum);
        }

        System.out.println("Base vs. Count:");
        counter.forEach(
            key, value -> System.out.printf("%5s : %s\n", key, value));
        System.out.printf("%5s: %s\n", "SUM", seq.length());
    }
    
    public void runSequence() {
        this.prettyPrint();
        this.displayCount();
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import Counter

def basecount(dna):
    return sorted(Counter(dna).items())

def seq_split(dna, n=50):
    return [dna[i: i+n] for i in range(0, len(dna), n)]

def seq_pp(dna, n=50):
    for i, part in enumerate(seq_split(dna, n)):
        print(f"{i*n:>5}: {part}")
    print("\n  BASECOUNT:")
    tot = 0
    for base, count in basecount(dna):
        print(f"    {base:>3}: {count}")
        tot += count
    base, count = 'TOT', tot
    print(f"    {base:>3}= {count}")
    
if __name__ == '__main__':
    print("SEQUENCE:")
    sequence = '''\
CGTAAAAAATTACAACGTCCTTTGGCTATCTCTTAAACTCCTGCTAAATG\
CTCGTGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTG\
AGGACAAAGGTCAAGATGGAGCGCATCGAACGCAATAAGGATCATTTGAT\
GGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTT\
CGATTCTGCTTATAACACTATGTTCTTATGAAATGGATGTTCTGAGTTGG\
TCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTATA\
TTTAATTTTTCTATATAGCGATCTGTATTTAAGCAATTCATTTAGGTTAT\
CGCCGCGATGCTCGGTTCGGACCGCCAAGCATCTGGCTCCACTGCTAGTG\
TCCTAAATTTGAATGGCAAACACAAATAAGATTTAGCAATTCGTGTAGAC\
GACCGGGGACTTGCATGATGGGAGCAGCTTTGTTAAACTACGAACGTAAT'''
    seq_pp(sequence)

```

### python_code_2.txt
```python
"""
	Python 3.10.5 (main, Jun  6 2022, 18:49:26) [GCC 12.1.0] on linux

	Created on Wed 2022/08/17 11:19:31
	
"""


def main ():

	def DispCount () :

	    return f'\n\nBases :\n\n' + f''.join ( [ f'{i} =\t{D [ i ]:4d}\n' for i in  sorted ( BoI ) ] )


	S =	'CGTAAAAAATTACAACGTCCTTTGGCTATCTCTTAAACTCCTGCTAAATGCTCGTGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTG' \
		'AGGACAAAGGTCAAGATGGAGCGCATCGAACGCAATAAGGATCATTTGATGGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTT' \
		'CGATTCTGCTTATAACACTATGTTCTTATGAAATGGATGTTCTGAGTTGGTCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTATA' \
		'TTTAATTTTTCTATATAGCGATCTGTATTTAAGCAATTCATTTAGGTTATCGCCGCGATGCTCGGTTCGGACCGCCAAGCATCTGGCTCCACTGCTAGTG' \
		'TCCTAAATTTGAATGGCAAACACAAATAAGATTTAGCAATTCGTGTAGACGACCGGGGACTTGCATGATGGGAGCAGCTTTGTTAAACTACGAACGTAAT'

	All   = set( S ) 
	
	BoI   = set ( [ "A","C","G","T" ] )
	
	other = All - BoI
	
	D     = { k : S.count ( k ) for k in All }
	
	print ( 'Sequence:\n\n')

	print ( ''.join ( [ f'{k:4d} : {S [ k: k + 50 ]}\n' for k in range ( 0, len ( S ), 50 ) ] ) )

	print ( f'{DispCount ()} \n------------')

	print ( '' if ( other == set () ) else f'Other\t{sum ( [ D [ k ] for k in sorted ( other ) ] ):4d}\n\n' )

	print ( f'Σ = \t {sum ( [ D [ k ] for k in sorted ( All ) ] ) } \n============\n')
	
	pass


def test ():

	pass


## START

LIVE = True

if ( __name__ == '__main__' ) :

	main () if LIVE else test ()

```

### python_code_3.txt
```python
'''Bioinformatics – base count'''

from itertools import count
from functools import reduce


# genBankFormatWithBaseCounts :: String -> String
def genBankFormatWithBaseCounts(sequence):
    '''DNA Sequence displayed in a subset of the GenBank format.
       See example at foot of:
       https://www.genomatix.de/online_help/help/sequence_formats.html
    '''
    ks, totals = zip(*baseCounts(sequence))
    ns = list(map(str, totals))
    w = 2 + max(map(len, ns))

    return '\n'.join([
        'DEFINITION  len=' + str(sum(totals)),
        'BASE COUNT  ' + ''.join(
            n.rjust(w) + ' ' + k.lower() for (k, n)
            in zip(ks, ns)
        ),
        'ORIGIN'
    ] + [
        str(i).rjust(9) + ' ' + k for i, k
        in zip(
            count(1, 60),
            [
                ' '.join(row) for row in
                chunksOf(6)(chunksOf(10)(sequence))
            ]
        )
    ] + ['//'])


# baseCounts :: String -> Zip [(String, Int)]
def baseCounts(baseString):
    '''Sums for each base type in the given sequence string, with
       a fifth sum for any characters not drawn from {A, C, G, T}.'''
    bases = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }
    return zip(
        list(bases.keys()) + ['Other'],
        foldl(
            lambda a: compose(
                nthArrow(succ)(a),
                flip(curry(bases.get))(4)
            )
        )((0, 0, 0, 0, 0))(baseString)
    )


# -------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Base counts and sequence displayed in GenBank format
    '''
    print(
        genBankFormatWithBaseCounts('''\
CGTAAAAAATTACAACGTCCTTTGGCTATCTCTTAAACTCCTGCTAAATG\
CTCGTGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTG\
AGGACAAAGGTCAAGATGGAGCGCATCGAACGCAATAAGGATCATTTGAT\
GGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTT\
CGATTCTGCTTATAACACTATGTTCTTATGAAATGGATGTTCTGAGTTGG\
TCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTATA\
TTTAATTTTTCTATATAGCGATCTGTATTTAAGCAATTCATTTAGGTTAT\
CGCCGCGATGCTCGGTTCGGACCGCCAAGCATCTGGCTCCACTGCTAGTG\
TCCTAAATTTGAATGGCAAACACAAATAAGATTTAGCAATTCGTGTAGAC\
GACCGGGGACTTGCATGATGGGAGCAGCTTTGTTAAACTACGAACGTAAT''')
    )


# ------------------------ GENERIC -------------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n, subdividing the
       contents of xs. Where the length of xs is not evenly
       divible, the final list will be shorter than n.
    '''
    return lambda xs: reduce(
        lambda a, i: a + [xs[i:n + i]],
        range(0, len(xs), n), []
    ) if 0 < n else []


# compose :: ((a -> a), ...) -> (a -> a)
def compose(*fs):
    '''Composition, from right to left,
       of a series of functions.
    '''
    def go(f, g):
        def fg(x):
            return f(g(x))
        return fg
    return reduce(go, fs, lambda x: x)


# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    '''A curried function derived
       from an uncurried function.
    '''
    return lambda x: lambda y: f(x, y)


# flip :: (a -> b -> c) -> b -> a -> c
def flip(f):
    '''The (curried or uncurried) function f with its
       arguments reversed.
    '''
    return lambda a: lambda b: f(b)(a)


# foldl :: (a -> b -> a) -> a -> [b] -> a
def foldl(f):
    '''Left to right reduction of a list,
       using the binary operator f, and
       starting with an initial value a.
    '''
    def go(acc, xs):
        return reduce(lambda a, x: f(a)(x), xs, acc)
    return lambda acc: lambda xs: go(acc, xs)


# nthArrow :: (a -> b) -> Tuple -> Int -> Tuple
def nthArrow(f):
    '''A simple function lifted to one which applies
       to a tuple, transforming only its nth value.
    '''
    def go(v, n):
        return v if n > len(v) else [
            x if n != i else f(x)
            for i, x in enumerate(v)
        ]
    return lambda tpl: lambda n: tuple(go(tpl, n))


# succ :: Enum a => a -> a
def succ(x):
    '''The successor of a value.
       For numeric types, (1 +).
    '''
    return 1 + x


# MAIN ---
if __name__ == '__main__':
    main()

```

