# Latin Squares in reduced form

## Task Link
[Rosetta Code - Latin Squares in reduced form](https://rosettacode.org/wiki/Latin_Squares_in_reduced_form)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LatinSquaresInReducedForm {

    public static void main(String[] args) {
        System.out.printf("Reduced latin squares of order 4:%n");
        for ( LatinSquare square : getReducedLatinSquares(4) ) {
            System.out.printf("%s%n", square);
        }
        
        System.out.printf("Compute the number of latin squares from count of reduced latin squares:%n(Reduced Latin Square Count) * n! * (n-1)! = Latin Square Count%n");
        for ( int n = 1 ; n <= 6 ; n++ ) {
            List<LatinSquare> list = getReducedLatinSquares(n);
            System.out.printf("Size = %d, %d * %d * %d = %,d%n", n, list.size(), fact(n), fact(n-1), list.size()*fact(n)*fact(n-1));
        }
    }
    
    private static long fact(int n) {
        if ( n == 0 ) {
            return 1;
        }
        int prod = 1;
        for ( int i = 1 ; i <= n ; i++ ) {
            prod *= i;
        }
        return prod;
    }
    
    private static List<LatinSquare> getReducedLatinSquares(int n) {
        List<LatinSquare> squares = new ArrayList<>();
        
        squares.add(new LatinSquare(n));
        PermutationGenerator permGen = new PermutationGenerator(n);
        for ( int fillRow = 1 ; fillRow < n ; fillRow++ ) {
            List<LatinSquare> squaresNext = new ArrayList<>();
            for ( LatinSquare square : squares ) {
                while ( permGen.hasMore() ) {
                    int[] perm = permGen.getNext();
                    
                    //  If not the correct row - next permutation.
                    if ( (perm[0]+1) != (fillRow+1) ) {
                        continue;
                    }
                    
                    //  Check permutation against current square.
                    boolean permOk = true;
                    done:
                    for ( int row = 0 ; row < fillRow ; row++ ) {
                        for ( int col = 0 ; col < n ; col++ ) {
                            if ( square.get(row, col) == (perm[col]+1) ) {
                                permOk = false;
                                break done;
                            }
                        }
                    }
                    if ( permOk ) {
                        LatinSquare newSquare = new LatinSquare(square);
                        for ( int col = 0 ; col < n ; col++ ) {
                            newSquare.set(fillRow, col, perm[col]+1);
                        }
                        squaresNext.add(newSquare);
                    }
                }
                permGen.reset();
            }
            squares = squaresNext;
        }
        
        return squares;
    }
    
    @SuppressWarnings("unused")
    private static int[] display(int[] in) {
        int [] out = new int[in.length];
        for ( int i = 0 ; i < in.length ; i++ ) {
            out[i] = in[i] + 1;
        }
        return out;
    }
    
    private static class LatinSquare {
        
        int[][] square;
        int size;
        
        public LatinSquare(int n) {
            square = new int[n][n];
            size = n;
            for ( int col = 0 ; col < n ; col++ ) {
                set(0, col, col + 1);
            }
        }
        
        public LatinSquare(LatinSquare ls) {
            int n = ls.size;
            square = new int[n][n];
            size = n;
            for ( int row = 0 ; row < n ; row++ ) {
                for ( int col = 0 ; col < n ; col++ ) {
                    set(row, col, ls.get(row, col));
                }
            }
        }
        
        public void set(int row, int col, int value) {
            square[row][col] = value;
        }

        public int get(int row, int col) {
            return square[row][col];
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            for ( int row = 0 ; row < size ; row++ ) {
                sb.append(Arrays.toString(square[row]));
                sb.append("\n");
            }
            return sb.toString();
        }
        
        
    }

    private static class PermutationGenerator {

        private int[] a;
        private BigInteger numLeft;
        private BigInteger total;

        public PermutationGenerator (int n) {
            if (n < 1) {
                throw new IllegalArgumentException ("Min 1");
            }
            a = new int[n];
            total = getFactorial(n);
            reset();
        }

        private void reset () {
            for ( int i = 0 ; i < a.length ; i++ ) {
                a[i] = i;
            }
            numLeft = new BigInteger(total.toString());
        }

        public boolean hasMore() {
            return numLeft.compareTo(BigInteger.ZERO) == 1;
        }

        private static BigInteger getFactorial (int n) {
            BigInteger fact = BigInteger.ONE;
            for ( int i = n ; i > 1 ; i-- ) {
                fact = fact.multiply(new BigInteger(Integer.toString(i)));
            }
            return fact;
        }

        /*--------------------------------------------------------
         * Generate next permutation (algorithm from Rosen p. 284)
         *--------------------------------------------------------
         */
        public int[] getNext() {
            if ( numLeft.equals(total) ) {
                numLeft = numLeft.subtract (BigInteger.ONE);
                return a;
            }

            // Find largest index j with a[j] < a[j+1]
            int j = a.length - 2;
            while ( a[j] > a[j+1] ) {
                j--;
            }

            // Find index k such that a[k] is smallest integer greater than a[j] to the right of a[j]
            int k = a.length - 1;
            while ( a[j] > a[k] ) {
                k--;
            }

            // Interchange a[j] and a[k]
            int temp = a[k];
            a[k] = a[j];
            a[j] = temp;

            // Put tail end of permutation after jth position in increasing order
            int r = a.length - 1;
            int s = j + 1;
            while (r > s) {
                int temp2 = a[s];
                a[s] = a[r];
                a[r] = temp2;
                r--;
                s++;
            }

            numLeft = numLeft.subtract(BigInteger.ONE);
            return a;
        }
    }

}

```

## Python Code
### python_code_1.txt
```python
def dList(n, start):
    start -= 1 # use 0 basing
    a = range(n)
    a[start] = a[0]
    a[0] = start
    a[1:] = sorted(a[1:])
    first = a[1]
    # rescursive closure permutes a[1:]
    r = []
    def recurse(last):
        if (last == first):
            # bottom of recursion. you get here once for each permutation.
            # test if permutation is deranged.
            # yes, save a copy with 1 based indexing
            for j,v in enumerate(a[1:]):
                if j + 1 == v:
                    return # no, ignore it
            b = [x + 1 for x in a]
            r.append(b)
            return
        for i in xrange(last, 0, -1):
            a[i], a[last] = a[last], a[i]
            recurse(last - 1)
            a[i], a[last] = a[last], a[i]
    recurse(n - 1)
    return r

def printSquare(latin,n):
    for row in latin:
        print row
    print

def reducedLatinSquares(n,echo):
    if n <= 0:
        if echo:
            print []
        return 0
    elif n == 1:
        if echo:
            print [1]
        return 1

    rlatin = [None] * n
    for i in xrange(n):
        rlatin[i] = [None] * n
    # first row
    for j in xrange(0, n):
        rlatin[0][j] = j + 1

    class OuterScope:
        count = 0
    def recurse(i):
        rows = dList(n, i)

        for r in xrange(len(rows)):
            rlatin[i - 1] = rows[r]
            justContinue = False
            k = 0
            while not justContinue and k < i - 1:
                for j in xrange(1, n):
                    if rlatin[k][j] == rlatin[i - 1][j]:
                        if r < len(rows) - 1:
                            justContinue = True
                            break
                        if i > 2:
                            return
                k += 1
            if not justContinue:
                if i < n:
                    recurse(i + 1)
                else:
                    OuterScope.count += 1
                    if echo:
                        printSquare(rlatin, n)

    # remaining rows
    recurse(2)
    return OuterScope.count

def factorial(n):
    if n == 0:
        return 1
    prod = 1
    for i in xrange(2, n + 1):
        prod *= i
    return prod

print "The four reduced latin squares of order 4 are:\n"
reducedLatinSquares(4,True)

print "The size of the set of reduced latin squares for the following orders"
print "and hence the total number of latin squares of these orders are:\n"
for n in xrange(1, 7):
    size = reducedLatinSquares(n, False)
    f = factorial(n - 1)
    f *= f * n * size
    print "Order %d: Size %-4d x %d! x %d! => Total %d" % (n, size, n, n - 1, f)

```

