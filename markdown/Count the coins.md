# Count the coins

## Task Link
[Rosetta Code - Count the coins](https://rosettacode.org/wiki/Count_the_coins)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.math.BigInteger;

class CountTheCoins {
    private static BigInteger countChanges(int amount, int[] coins){
        final int n = coins.length;
        int cycle = 0;
        for (int c : coins)
            if (c <= amount && c >= cycle)
                cycle = c + 1;
        cycle *= n;
        BigInteger[] table = new BigInteger[cycle];
        Arrays.fill(table, 0, n, BigInteger.ONE);
        Arrays.fill(table, n, cycle, BigInteger.ZERO);

        int pos = n;
        for (int s = 1; s <= amount; s++) {
            for (int i = 0; i < n; i++) {
                if (i == 0 && pos >= cycle)
                    pos = 0;
                if (coins[i] <= s) {
                    final int q = pos - (coins[i] * n);
                    table[pos] = (q >= 0) ? table[q] : table[q + cycle];
                }
                if (i != 0)
                    table[pos] = table[pos].add(table[pos - 1]);
                pos++;
            }
        }

        return table[pos - 1];
    }

    public static void main(String[] args) {
        final int[][] coinsUsEu = {{100, 50, 25, 10, 5, 1},
                                   {200, 100, 50, 20, 10, 5, 2, 1}};

        for (int[] coins : coinsUsEu) {
            System.out.println(countChanges(     100,
                Arrays.copyOfRange(coins, 2, coins.length)));
            System.out.println(countChanges(  100000, coins));
            System.out.println(countChanges( 1000000, coins));
            System.out.println(countChanges(10000000, coins) + "\n");
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in xrange(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]

print changes(100, [1, 5, 10, 25])
print changes(100000, [1, 5, 10, 25, 50, 100])

```

### python_code_2.txt
```python
try:
    import psyco
    psyco.full()
except ImportError:
    pass

def count_changes(amount_cents, coins):
    n = len(coins)
    # max([]) instead of max() for Psyco
    cycle = max([c+1 for c in coins if c <= amount_cents]) * n
    table = [0] * cycle
    for i in xrange(n):
        table[i] = 1

    pos = n
    for s in xrange(1, amount_cents + 1):
        for i in xrange(n):
            if i == 0 and pos >= cycle:
                pos = 0
            if coins[i] <= s:
                q = pos - coins[i] * n
                table[pos]= table[q] if (q >= 0) else table[q + cycle]
            if i:
                table[pos] += table[pos - 1]
            pos += 1
    return table[pos - 1]

def main():
    us_coins = [100, 50, 25, 10, 5, 1]
    eu_coins = [200, 100, 50, 20, 10, 5, 2, 1]

    for coins in (us_coins, eu_coins):
        print count_changes(     100, coins[2:])
        print count_changes(  100000, coins)
        print count_changes( 1000000, coins)
        print count_changes(10000000, coins), "\n"

main()

```

