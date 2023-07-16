# Range consolidation

## Task Link
[Rosetta Code - Range consolidation](https://rosettacode.org/wiki/Range_consolidation)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class RangeConsolidation {

    public static void main(String[] args) {
        displayRanges( Arrays.asList(new Range(1.1, 2.2)));
        displayRanges( Arrays.asList(new Range(6.1, 7.2), new Range(7.2, 8.3)));
        displayRanges( Arrays.asList(new Range(4, 3), new Range(2, 1)));
        displayRanges( Arrays.asList(new Range(4, 3), new Range(2, 1), new Range(-1, -2), new Range(3.9, 10)));
        displayRanges( Arrays.asList(new Range(1, 3), new Range(-6, -1), new Range(-4, -5), new Range(8, 2), new Range(-6, -6)));
        displayRanges( Arrays.asList(new Range(1, 1), new Range(1, 1)));
        displayRanges( Arrays.asList(new Range(1, 1), new Range(1, 2)));
        displayRanges( Arrays.asList(new Range(1, 2), new Range(3, 4), new Range(1.5, 3.5), new Range(1.2, 2.5)));
    }
    
    private static final void displayRanges(List<Range> ranges) {
        System.out.printf("ranges = %-70s, colsolidated = %s%n", ranges, Range.consolidate(ranges));
    }
    
    private static final class RangeSorter implements Comparator<Range> {
        @Override
        public int compare(Range o1, Range o2) {
            return (int) (o1.left - o2.left);
        }        
    }

    private static class Range {
        double left;
        double right;
        
        public Range(double left, double right) {
            if ( left <= right ) {
                this.left = left;
                this.right = right;
            }
            else {
                this.left = right;
                this.right = left;
            }
        }
        
        public Range consolidate(Range range) {
            //  no overlap
            if ( this.right < range.left ) {
                return null;
            }
            //  no overlap
            if ( range.right < this.left ) {
                return null;
            }
            //  contained
            if ( this.left <= range.left && this.right >= range.right ) {
                return this;
            }
            //  contained
            if ( range.left <= this.left && range.right >= this.right ) {
                return range;
            }
            //  overlap
            if ( this.left <= range.left && this.right <= range.right ) {
                return new Range(this.left, range.right);
            }
            //  overlap
            if ( this.left >= range.left && this.right >= range.right ) {
                return new Range(range.left, this.right);
            }
            throw new RuntimeException("ERROR:  Logic invalid.");
        }
        
        @Override
        public String toString() {
            return "[" + left + ", " + right + "]";
        }
        
        private static List<Range> consolidate(List<Range> ranges) {
            List<Range> consolidated = new ArrayList<>();
            
            Collections.sort(ranges, new RangeSorter());
            
            for ( Range inRange : ranges ) {
                Range r = null;
                Range conRange = null;
                for ( Range conRangeLoop : consolidated ) {
                    r = inRange.consolidate(conRangeLoop);
                    if (r != null ) {
                        conRange = conRangeLoop;
                        break;
                    }
                }
                if ( r == null ) {
                    consolidated.add(inRange);
                }
                else {
                    consolidated.remove(conRange);
                    consolidated.add(r);                    
                }
            }
            
            Collections.sort(consolidated, new RangeSorter());
            
            return consolidated;
        }
    }

}

```

## Python Code
### python_code_1.txt
```python
def normalize(s):
    return sorted(sorted(bounds) for bounds in s if bounds)

def consolidate(ranges):
    norm = normalize(ranges)
    for i, r1 in enumerate(norm):
        if r1:
            for r2 in norm[i+1:]:
                if r2 and r1[-1] >= r2[0]:     # intersect?
                    r1[:] = [r1[0], max(r1[-1], r2[-1])]
                    r2.clear()
    return [rnge for rnge in norm if rnge]

if __name__ == '__main__':
    for s in [
            [[1.1, 2.2]],
            [[6.1, 7.2], [7.2, 8.3]],
            [[4, 3], [2, 1]],
            [[4, 3], [2, 1], [-1, -2], [3.9, 10]],
            [[1, 3], [-6, -1], [-4, -5], [8, 2], [-6, -6]],
            ]:
        print(f"{str(s)[1:-1]} => {str(consolidate(s))[1:-1]}")

```

### python_code_2.txt
```python
'''Range consolidation'''

from functools import reduce


# consolidated :: [(Float, Float)] -> [(Float, Float)]
def consolidated(xs):
    '''A consolidated list of
       [(Float, Float)] ranges.'''

    def go(abetc, xy):
        '''A copy of the accumulator abetc,
           with its head range ab either:
           1. replaced by or
           2. merged with
           the next range xy, or
           with xy simply prepended.'''
        if abetc:
            a, b = abetc[0]
            etc = abetc[1:]
            x, y = xy
            return [xy] + etc if y >= b else (   # ab replaced.
                [(x, b)] + etc if y >= a else (  # xy + ab merged.
                    [xy] + abetc                 # xy simply prepended.
                )
            )
        else:
            return [xy]

    def tupleSort(ab):
        a, b = ab
        return ab if a <= b else (b, a)

    return reduce(
        go,
        sorted(map(tupleSort, xs), reverse=True),
        []
    )


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Tests'''

    print(
        tabulated('Consolidation of numeric ranges:')(str)(str)(
            consolidated
        )([
            [(1.1, 2.2)],
            [(6.1, 7.2), (7.2, 8.3)],
            [(4, 3), (2, 1)],
            [(4, 3), (2, 1), (-1, -2), (3.9, 10)],
            [(1, 3), (-6, -1), (-4, -5), (8, 2), (-6, -6)]
        ])
    )


# GENERIC FUNCTIONS FOR DISPLAY ---------------------------


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# tabulated :: String -> (a -> String) ->
#                        (b -> String) ->
#                        (a -> b) -> [a] -> String
def tabulated(s):
    '''Heading -> x display function -> fx display function ->
          f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join([
            xShow(x).rjust(w, ' ') + ' -> ' + fxShow(f(x)) for x in xs
        ])
    return lambda xShow: lambda fxShow: (
        lambda f: lambda xs: go(
            xShow, fxShow, f, xs
        )
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

