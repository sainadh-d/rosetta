# Nonogram solver

## Task Link
[Rosetta Code - Nonogram solver](https://rosettacode.org/wiki/Nonogram_solver)

## Java Code
### java_code_1.txt
```java
import java.util.*;
import static java.util.Arrays.*;
import static java.util.stream.Collectors.toList;

public class NonogramSolver {

    static String[] p1 = {"C BA CB BB F AE F A B", "AB CA AE GA E C D C"};

    static String[] p2 = {"F CAC ACAC CN AAA AABB EBB EAA ECCC HCCC", "D D AE "
        + "CD AE A DA BBB CC AAB BAA AAB DA AAB AAA BAB AAA CD BBA DA"};

    static String[] p3 = {"CA BDA ACC BD CCAC CBBAC BBBBB BAABAA ABAD AABB BBH "
        + "BBBD ABBAAA CCEA AACAAB BCACC ACBH DCH ADBE ADBB DBE ECE DAA DB CC",
        "BC CAC CBAB BDD CDBDE BEBDF ADCDFA DCCFB DBCFC ABDBA BBF AAF BADB DBF "
        + "AAAAD BDG CEF CBDB BBB FC"};

    static String[] p4 = {"E BCB BEA BH BEK AABAF ABAC BAA BFB OD JH BADCF Q Q "
        + "R AN AAN EI H G", "E CB BAB AAA AAA AC BB ACC ACCA AGB AIA AJ AJ "
        + "ACE AH BAF CAG DAG FAH FJ GJ ADK ABK BL CM"};

    public static void main(String[] args) {
        for (String[] puzzleData : new String[][]{p1, p2, p3, p4})
            newPuzzle(puzzleData);
    }

    static void newPuzzle(String[] data) {
        String[] rowData = data[0].split("\\s");
        String[] colData = data[1].split("\\s");

        List<List<BitSet>> cols, rows;
        rows = getCandidates(rowData, colData.length);
        cols = getCandidates(colData, rowData.length);

        int numChanged;
        do {
            numChanged = reduceMutual(cols, rows);
            if (numChanged == -1) {
                System.out.println("No solution");
                return;
            }
        } while (numChanged > 0);

        for (List<BitSet> row : rows) {
            for (int i = 0; i < cols.size(); i++)
                System.out.print(row.get(0).get(i) ? "# " : ". ");
            System.out.println();
        }
        System.out.println();
    }

    // collect all possible solutions for the given clues
    static List<List<BitSet>> getCandidates(String[] data, int len) {
        List<List<BitSet>> result = new ArrayList<>();

        for (String s : data) {
            List<BitSet> lst = new LinkedList<>();

            int sumChars = s.chars().map(c -> c - 'A' + 1).sum();
            List<String> prep = stream(s.split(""))
                    .map(x -> repeat(x.charAt(0) - 'A' + 1, "1")).collect(toList());

            for (String r : genSequence(prep, len - sumChars + 1)) {
                char[] bits = r.substring(1).toCharArray();
                BitSet bitset = new BitSet(bits.length);
                for (int i = 0; i < bits.length; i++)
                    bitset.set(i, bits[i] == '1');
                lst.add(bitset);
            }
            result.add(lst);
        }
        return result;
    }

    // permutation generator, translated from Python via D
    static List<String> genSequence(List<String> ones, int numZeros) {
        if (ones.isEmpty())
            return asList(repeat(numZeros, "0"));

        List<String> result = new ArrayList<>();
        for (int x = 1; x < numZeros - ones.size() + 2; x++) {
            List<String> skipOne = ones.stream().skip(1).collect(toList());
            for (String tail : genSequence(skipOne, numZeros - x))
                result.add(repeat(x, "0") + ones.get(0) + tail);
        }
        return result;
    }

    static String repeat(int n, String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++)
            sb.append(s);
        return sb.toString();
    }

    /* If all the candidates for a row have a value in common for a certain cell,
    then it's the only possible outcome, and all the candidates from the
    corresponding column need to have that value for that cell too. The ones
    that don't, are removed. The same for all columns. It goes back and forth,
    until no more candidates can be removed or a list is empty (failure). */

    static int reduceMutual(List<List<BitSet>> cols, List<List<BitSet>> rows) {
        int countRemoved1 = reduce(cols, rows);
        if (countRemoved1 == -1)
            return -1;

        int countRemoved2 = reduce(rows, cols);
        if (countRemoved2 == -1)
            return -1;

        return countRemoved1 + countRemoved2;
    }

    static int reduce(List<List<BitSet>> a, List<List<BitSet>> b) {
        int countRemoved = 0;

        for (int i = 0; i < a.size(); i++) {

            BitSet commonOn = new BitSet();
            commonOn.set(0, b.size());
            BitSet commonOff = new BitSet();

            // determine which values all candidates of ai have in common
            for (BitSet candidate : a.get(i)) {
                commonOn.and(candidate);
                commonOff.or(candidate);
            }

            // remove from bj all candidates that don't share the forced values
            for (int j = 0; j < b.size(); j++) {
                final int fi = i, fj = j;

                if (b.get(j).removeIf(cnd -> (commonOn.get(fj) && !cnd.get(fi))
                        || (!commonOff.get(fj) && cnd.get(fi))))
                    countRemoved++;

                if (b.get(j).isEmpty())
                    return -1;
            }
        }
        return countRemoved;
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import izip

def gen_row(w, s):
    """Create all patterns of a row or col that match given runs."""
    def gen_seg(o, sp):
        if not o:
            return [[2] * sp]
        return [[2] * x + o[0] + tail
                for x in xrange(1, sp - len(o) + 2)
                for tail in gen_seg(o[1:], sp - x)]

    return [x[1:] for x in gen_seg([[1] * i for i in s], w + 1 - sum(s))]


def deduce(hr, vr):
    """Fix inevitable value of cells, and propagate."""
    def allowable(row):
        return reduce(lambda a, b: [x | y for x, y in izip(a, b)], row)

    def fits(a, b):
        return all(x & y for x, y in izip(a, b))

    def fix_col(n):
        """See if any value in a given column is fixed;
        if so, mark its corresponding row for future fixup."""
        c = [x[n] for x in can_do]
        cols[n] = [x for x in cols[n] if fits(x, c)]
        for i, x in enumerate(allowable(cols[n])):
            if x != can_do[i][n]:
                mod_rows.add(i)
                can_do[i][n] &= x

    def fix_row(n):
        """Ditto, for rows."""
        c = can_do[n]
        rows[n] = [x for x in rows[n] if fits(x, c)]
        for i, x in enumerate(allowable(rows[n])):
            if x != can_do[n][i]:
                mod_cols.add(i)
                can_do[n][i] &= x

    def show_gram(m):
        # If there's 'x', something is wrong.
        # If there's '?', needs more work.
        for x in m:
            print " ".join("x#.?"[i] for i in x)
        print

    w, h = len(vr), len(hr)
    rows = [gen_row(w, x) for x in hr]
    cols = [gen_row(h, x) for x in vr]
    can_do = map(allowable, rows)

    # Initially mark all columns for update.
    mod_rows, mod_cols = set(), set(xrange(w))

    while mod_cols:
        for i in mod_cols:
            fix_col(i)
        mod_cols = set()
        for i in mod_rows:
            fix_row(i)
        mod_rows = set()

    if all(can_do[i][j] in (1, 2) for j in xrange(w) for i in xrange(h)):
        print "Solution would be unique" # but could be incorrect!
    else:
        print "Solution may not be unique, doing exhaustive search:"

    # We actually do exhaustive search anyway. Unique solution takes
    # no time in this phase anyway, but just in case there's no
    # solution (could happen?).
    out = [0] * h

    def try_all(n = 0):
        if n >= h:
            for j in xrange(w):
                if [x[j] for x in out] not in cols[j]:
                    return 0
            show_gram(out)
            return 1
        sol = 0
        for x in rows[n]:
            out[n] = x
            sol += try_all(n + 1)
        return sol

    n = try_all()
    if not n:
        print "No solution."
    elif n == 1:
        print "Unique solution."
    else:
        print n, "solutions."
    print


def solve(p, show_runs=True):
    s = [[[ord(c) - ord('A') + 1 for c in w] for w in l.split()]
         for l in p.splitlines()]
    if show_runs:
        print "Horizontal runs:", s[0]
        print "Vertical runs:", s[1]
    deduce(s[0], s[1])


def main():
    # Read problems from file.
    fn = "nonogram_problems.txt"
    for p in (x for x in open(fn).read().split("\n\n") if x):
        solve(p)

    print "Extra example not solvable by deduction alone:"
    solve("B B A A\nB B A A")

    print "Extra example where there is no solution:"
    solve("B A A\nA A A")

main()

```

### python_code_2.txt
```python
from functools import reduce

def gen_row(w, s):
    """Create all patterns of a row or col that match given runs."""
    def gen_seg(o, sp):
        if not o:
            return [[2] * sp]
        return [[2] * x + o[0] + tail
                for x in range(1, sp - len(o) + 2)
                for tail in gen_seg(o[1:], sp - x)]
 
    return [x[1:] for x in gen_seg([[1] * i for i in s], w + 1 - sum(s))]
 
 
def deduce(hr, vr):
    """Fix inevitable value of cells, and propagate."""
    def allowable(row):
        return reduce(lambda a, b: [x | y for x, y in zip(a, b)], row)
 
    def fits(a, b):
        return all(x & y for x, y in zip(a, b))
 
    def fix_col(n):
        """See if any value in a given column is fixed;
        if so, mark its corresponding row for future fixup."""
        c = [x[n] for x in can_do]
        cols[n] = [x for x in cols[n] if fits(x, c)]
        for i, x in enumerate(allowable(cols[n])):
            if x != can_do[i][n]:
                mod_rows.add(i)
                can_do[i][n] &= x
 
    def fix_row(n):
        """Ditto, for rows."""
        c = can_do[n]
        rows[n] = [x for x in rows[n] if fits(x, c)]
        for i, x in enumerate(allowable(rows[n])):
            if x != can_do[n][i]:
                mod_cols.add(i)
                can_do[n][i] &= x
 
    def show_gram(m):
        # If there's 'x', something is wrong.
        # If there's '?', needs more work.
        for x in m:
            print(" ".join("x#.?"[i] for i in x))
        print()
 
    w, h = len(vr), len(hr)
    rows = [gen_row(w, x) for x in hr]
    cols = [gen_row(h, x) for x in vr]
    can_do = list(map(allowable, rows))
 
    # Initially mark all columns for update.
    mod_rows, mod_cols = set(), set(range(w))
 
    while mod_cols:
        for i in mod_cols:
            fix_col(i)
        mod_cols = set()
        for i in mod_rows:
            fix_row(i)
        mod_rows = set()
 
    if all(can_do[i][j] in (1, 2) for j in range(w) for i in range(h)):
        print("Solution would be unique")  # but could be incorrect!
    else:
        print("Solution may not be unique, doing exhaustive search:")
 
    # We actually do exhaustive search anyway. Unique solution takes
    # no time in this phase anyway, but just in case there's no
    # solution (could happen?).
    out = [0] * h
 
    def try_all(n = 0):
        if n >= h:
            for j in range(w):
                if [x[j] for x in out] not in cols[j]:
                    return 0
            show_gram(out)
            return 1
        sol = 0
        for x in rows[n]:
            out[n] = x
            sol += try_all(n + 1)
        return sol
 
    n = try_all()
    if not n:
        print("No solution.")
    elif n == 1:
        print("Unique solution.")
    else:
        print(n, "solutions.")
    print()
 
 
def solve(s, show_runs=True):
    s = [[[ord(c) - ord('A') + 1 for c in w] for w in l.split()]
         for l in p.splitlines()]
    if show_runs:
        print("Horizontal runs:", s[0])
        print("Vertical runs:", s[1])
    deduce(s[0], s[1])

```

