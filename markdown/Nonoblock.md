# Nonoblock

## Task Link
[Rosetta Code - Nonoblock](https://rosettacode.org/wiki/Nonoblock)

## Java Code
### java_code_1.txt
```java
import java.util.*;
import static java.util.Arrays.stream;
import static java.util.stream.Collectors.toList;

public class Nonoblock {

    public static void main(String[] args) {
        printBlock("21", 5);
        printBlock("", 5);
        printBlock("8", 10);
        printBlock("2323", 15);
        printBlock("23", 5);
    }

    static void printBlock(String data, int len) {
        int sumChars = data.chars().map(c -> Character.digit(c, 10)).sum();
        String[] a = data.split("");

        System.out.printf("%nblocks %s, cells %s%n", Arrays.toString(a), len);
        if (len - sumChars <= 0) {
            System.out.println("No solution");
            return;
        }

        List<String> prep = stream(a).filter(x -> !"".equals(x))
                .map(x -> repeat(Character.digit(x.charAt(0), 10), "1"))
                .collect(toList());

        for (String r : genSequence(prep, len - sumChars + 1))
            System.out.println(r.substring(1));
    }

    // permutation generator, translated from Python via D
    static List<String> genSequence(List<String> ones, int numZeros) {
        if (ones.isEmpty())
            return Arrays.asList(repeat(numZeros, "0"));

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
}

```

## Python Code
### python_code_1.txt
```python
def nonoblocks(blocks, cells):
    if not blocks or blocks[0] == 0:
        yield [(0, 0)]
    else:
        assert sum(blocks) + len(blocks)-1 <= cells, \
            'Those blocks will not fit in those cells'
        blength, brest = blocks[0], blocks[1:]      # Deal with the first block of length
        minspace4rest = sum(1+b for b in brest)     # The other blocks need space
        # Slide the start position from left to max RH index allowing for other blocks.
        for bpos in range(0, cells - minspace4rest - blength + 1):
            if not brest:
                # No other blocks to the right so just yield this one.
                yield [(bpos, blength)]
            else:
                # More blocks to the right so create a *sub-problem* of placing
                # the brest blocks in the cells one space to the right of the RHS of 
                # this block.
                offset = bpos + blength +1
                nonoargs = (brest, cells - offset)  # Pre-compute arguments to nonoargs
                # recursive call to nonoblocks yields multiple sub-positions
                for subpos in nonoblocks(*nonoargs):
                    # Remove the offset from sub block positions
                    rest = [(offset + bp, bl) for bp, bl in subpos]
                    # Yield this block plus sub blocks positions
                    vec = [(bpos, blength)] + rest
                    yield vec

def pblock(vec, cells):
    'Prettyprints each run of blocks with a different letter A.. for each block of filled cells'
    vector = ['_'] * cells
    for ch, (bp, bl) in enumerate(vec, ord('A')):
        for i in range(bp, bp + bl):
            vector[i] = chr(ch) if vector[i] == '_' else'?'
    return '|' + '|'.join(vector) + '|'


if __name__ == '__main__':
    for blocks, cells in (
            ([2, 1], 5),
            ([], 5),
            ([8], 10),
            ([2, 3, 2, 3], 15),
           # ([4, 3], 10),
           # ([2, 1], 5),
           # ([3, 1], 10),
            ([2, 3], 5),
            ):
        print('\nConfiguration:\n    %s # %i cells and %r blocks' % (pblock([], cells), cells, blocks))        
        print('  Possibilities:')
        for i, vector in enumerate(nonoblocks(blocks, cells)):
            print('   ', pblock(vector, cells))
        print('  A total of %i Possible configurations.' % (i+1))

```

