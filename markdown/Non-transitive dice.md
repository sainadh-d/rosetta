# Non-transitive dice

## Task Link
[Rosetta Code - Non-transitive dice](https://rosettacode.org/wiki/Non-transitive_dice)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    private static List<List<Integer>> fourFaceCombos() {
        List<List<Integer>> res = new ArrayList<>();
        Set<Integer> found = new HashSet<>();

        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                for (int k = 1; k <= 4; k++) {
                    for (int l = 1; l <= 4; l++) {
                        List<Integer> c = IntStream.of(i, j, k, l).sorted().boxed().collect(Collectors.toList());

                        int key = 64 * (c.get(0) - 1) + 16 * (c.get(1) - 1) + 4 * (c.get(2) - 1) + (c.get(3) - 1);
                        if (found.add(key)) {
                            res.add(c);
                        }
                    }
                }
            }
        }

        return res;
    }

    private static int cmp(List<Integer> x, List<Integer> y) {
        int xw = 0;
        int yw = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (x.get(i) > y.get(j)) {
                    xw++;
                } else if (x.get(i) < y.get(j)) {
                    yw++;
                }
            }
        }
        return Integer.compare(xw, yw);
    }

    private static List<List<List<Integer>>> findIntransitive3(List<List<Integer>> cs) {
        int c = cs.size();
        List<List<List<Integer>>> res = new ArrayList<>();

        for (int i = 0; i < c; i++) {
            for (int j = 0; j < c; j++) {
                if (cmp(cs.get(i), cs.get(j)) == -1) {
                    for (List<Integer> kl : cs) {
                        if (cmp(cs.get(j), kl) == -1 && cmp(kl, cs.get(i)) == -1) {
                            res.add(List.of(cs.get(i), cs.get(j), kl));
                        }
                    }
                }
            }
        }

        return res;
    }

    private static List<List<List<Integer>>> findIntransitive4(List<List<Integer>> cs) {
        int c = cs.size();
        List<List<List<Integer>>> res = new ArrayList<>();

        for (int i = 0; i < c; i++) {
            for (int j = 0; j < c; j++) {
                if (cmp(cs.get(i), cs.get(j)) == -1) {
                    for (int k = 0; k < cs.size(); k++) {
                        if (cmp(cs.get(j), cs.get(k)) == -1) {
                            for (List<Integer> ll : cs) {
                                if (cmp(cs.get(k), ll) == -1 && cmp(ll, cs.get(i)) == -1) {
                                    res.add(List.of(cs.get(i), cs.get(j), cs.get(k), ll));
                                }
                            }
                        }
                    }
                }
            }
        }

        return res;
    }

    public static void main(String[] args) {
        List<List<Integer>> combos = fourFaceCombos();
        System.out.printf("Number of eligible 4-faced dice: %d%n", combos.size());
        System.out.println();

        List<List<List<Integer>>> it3 = findIntransitive3(combos);
        System.out.printf("%d ordered lists of 3 non-transitive dice found, namely:%n", it3.size());
        for (List<List<Integer>> a : it3) {
            System.out.println(a);
        }
        System.out.println();

        List<List<List<Integer>>> it4 = findIntransitive4(combos);
        System.out.printf("%d ordered lists of 4 non-transitive dice found, namely:%n", it4.size());
        for (List<List<Integer>> a : it4) {
            System.out.println(a);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import combinations_with_replacement as cmbr
from time import time
 
def dice_gen(n, faces, m):
    dice = list(cmbr(faces, n))
 
    succ = [set(j for j, b in enumerate(dice)
                    if sum((x>y) - (x<y) for x in a for y in b) > 0)
                for a in dice]
 
    def loops(seq):
        s = succ[seq[-1]]

        if len(seq) == m:
            if seq[0] in s: yield seq
            return

        for d in (x for x in s if x > seq[0] and not x in seq):
            yield from loops(seq + (d,))
 
    yield from (tuple(''.join(dice[s]) for s in x)
                    for i, v in enumerate(succ)
                    for x in loops((i,)))
 
t = time()
for n, faces, loop_len in [(4, '1234', 3), (4, '1234', 4), (6, '123456', 3), (6, '1234567', 3)]:
    for i, x in enumerate(dice_gen(n, faces, loop_len)): pass
 
    print(f'{n}-sided, markings {faces}, loop length {loop_len}:')
    print(f'\t{i + 1}*{loop_len} solutions, e.g. {" > ".join(x)} > [loop]')
    t, t0 = time(), t
    print(f'\ttime: {t - t0:.4f} seconds\n')

```

### python_code_2.txt
```python
from collections import namedtuple
from itertools import permutations, product
from functools import lru_cache


Die = namedtuple('Die', 'name, faces')

@lru_cache(maxsize=None)
def cmpd(die1, die2):
    'compares two die returning 1, -1 or 0 for >, < =='
    # Numbers of times one die wins against the other for all combinations
    # cmp(x, y) is `(x > y) - (y > x)` to return 1, 0, or -1 for numbers
    tot = [0, 0, 0]
    for d1, d2 in product(die1.faces, die2.faces):
        tot[1 + (d1 > d2) - (d2 > d1)] += 1
    win2, _, win1 = tot
    return (win1 > win2) - (win2 > win1)
    
def is_non_trans(dice):
    "Check if ordering of die in dice is non-transitive returning dice or None"
    check = (all(cmpd(c1, c2) == -1 
                 for c1, c2 in zip(dice, dice[1:]))  # Dn < Dn+1
             and cmpd(dice[0], dice[-1]) ==  1)      # But D[0] > D[-1]
    return dice if check else False

def find_non_trans(alldice, n=3):
    return [perm for perm in permutations(alldice, n) 
            if is_non_trans(perm)]

def possible_dice(sides, mx):
    print(f"\nAll possible 1..{mx} {sides}-sided dice")
    dice = [Die(f"D{n+1}", faces)
            for n, faces in enumerate(product(range(1, mx+1), repeat=sides))]
    print(f'  Created {len(dice)} dice')
    print('  Remove duplicate with same bag of numbers on different faces')
    found = set()
    filtered = []
    for d in dice:
        count = tuple(sorted(d.faces))
        if count not in found:
            found.add(count)
            filtered.append(d)      
    l = len(filtered)
    print(f'   Return {l} filtered dice')
    return filtered

#%% more verbose extra checks
def verbose_cmp(die1, die2):
    'compares two die returning their relationship of their names as a string'
    # Numbers of times one die wins against the other for all combinations
    win1 = sum(d1 > d2 for d1, d2 in product(die1.faces, die2.faces))
    win2 = sum(d2 > d1 for d1, d2 in product(die1.faces, die2.faces))
    n1, n2 = die1.name, die2.name
    return f'{n1} > {n2}' if win1 > win2 else (f'{n1} < {n2}' if win1 < win2 else f'{n1} = {n2}')

def verbose_dice_cmp(dice):
    c = [verbose_cmp(x, y) for x, y in zip(dice, dice[1:])]
    c += [verbose_cmp(dice[0], dice[-1])]
    return ', '.join(c)


#%% Use
if __name__ == '__main__':
    dice = possible_dice(sides=4, mx=4)
    for N in (3, 4):   # length of non-transitive group of dice searched for
        non_trans = find_non_trans(dice, N)
        print(f'\n  Non_transitive length-{N} combinations found: {len(non_trans)}')
        for lst in non_trans:
            print()
            for i, die in enumerate(lst):
                print(f"    {' ' if i else '['}{die}{',' if i < N-1 else ']'}")
        if non_trans:
            print('\n  More verbose comparison of last non_transitive result:')
            print(' ',   verbose_dice_cmp(non_trans[-1]))
        print('\n  ====')

```

