# EKG sequence convergence

## Task Link
[Rosetta Code - EKG sequence convergence](https://rosettacode.org/wiki/EKG_sequence_convergence)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class EKGSequenceConvergence {

    public static void main(String[] args) {
        System.out.println("Calculate and show here the first 10 members of EKG[2], EKG[5], EKG[7], EKG[9] and EKG[10].");
        for ( int i : new int[] {2, 5, 7, 9, 10} ) {
            System.out.printf("EKG[%d] = %s%n", i, ekg(i, 10));
        }
        System.out.println("Calculate and show here at which term EKG[5] and EKG[7] converge.");
        List<Integer> ekg5 = ekg(5, 100);
        List<Integer> ekg7 = ekg(7, 100);
        for ( int i = 1 ; i < ekg5.size() ; i++ ) {
            if ( ekg5.get(i) == ekg7.get(i) && sameSeq(ekg5, ekg7, i)) {
                System.out.printf("EKG[%d](%d) = EKG[%d](%d) = %d, and are identical from this term on%n", 5, i+1, 7, i+1, ekg5.get(i));
                break;
            }
        }
    }
    
    //  Same last element, and all elements in sequence are identical
    private static boolean sameSeq(List<Integer> seq1, List<Integer> seq2, int n) {
        List<Integer> list1 = new ArrayList<>(seq1.subList(0, n));
        Collections.sort(list1);
        List<Integer> list2 = new ArrayList<>(seq2.subList(0, n));
        Collections.sort(list2);
        for ( int i = 0 ; i < n ; i++ ) {
            if ( list1.get(i) != list2.get(i) ) {
                return false;
            }
        }
        return true;
    }
    
    //  Without HashMap to identify seen terms, need to examine list.
    //    Calculating 3000 terms in this manner takes 10 seconds
    //  With HashMap to identify the seen terms, calculating 3000 terms takes .1 sec.
    private static List<Integer> ekg(int two, int maxN) {
        List<Integer> result = new ArrayList<>();
        result.add(1);
        result.add(two);
        Map<Integer,Integer> seen = new HashMap<>();
        seen.put(1, 1);
        seen.put(two, 1);
        int minUnseen = two == 2 ? 3 : 2;
        int prev = two;
        for ( int n = 3 ; n <= maxN ; n++ ) {
            int test = minUnseen - 1;
            while ( true ) {
                test++;
                if ( ! seen.containsKey(test) && gcd(test, prev) > 1 ) {
                    
                    result.add(test);
                    seen.put(test, n);
                    prev = test;
                    if ( minUnseen == test ) {
                        do {
                            minUnseen++;
                        } while ( seen.containsKey(minUnseen) );
                    }
                    break;
                }
            }
        }
        return result;
    }

    private static final int gcd(int a, int b) {
        if ( b == 0 ) {
            return a;
        }
        return gcd(b, a%b);
    }
        
}

```

## Python Code
### python_code_1.txt
```python
from itertools import count, islice, takewhile
from math import gcd

def EKG_gen(start=2):
    """\
    Generate the next term of the EKG together with the minimum cache of 
    numbers left in its production; (the "state" of the generator).
    Using math.gcd
    """
    c = count(start + 1)
    last, so_far = start, list(range(2, start))
    yield 1, []
    yield last, []
    while True:
        for index, sf in enumerate(so_far):
            if gcd(last, sf) > 1:
                last = so_far.pop(index)
                yield last, so_far[::]
                break
        else:
            so_far.append(next(c))

def find_convergence(ekgs=(5,7)):
    "Returns the convergence point or zero if not found within the limit"
    ekg = [EKG_gen(n) for n in ekgs]
    for e in ekg:
        next(e)    # skip initial 1 in each sequence
    return 2 + len(list(takewhile(lambda state: not all(state[0] == s for  s in state[1:]),
                                  zip(*ekg))))

if __name__ == '__main__':
    for start in 2, 5, 7, 9, 10:
        print(f"EKG({start}):", str([n[0] for n in islice(EKG_gen(start), 10)])[1: -1])
    print(f"\nEKG(5) and EKG(7) converge at term {find_convergence(ekgs=(5,7))}!")

```

### python_code_2.txt
```python
# After running the above, in the terminal:
from pprint import pprint as pp

for start in 5, 7:
    print(f"EKG({start}):\n[(<next>, [<state>]), ...]")
    pp(([n for n in islice(EKG_gen(start), 21)]))

```

