# Ranking methods

## Task Link
[Rosetta Code - Ranking methods](https://rosettacode.org/wiki/Ranking_methods)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class RankingMethods {

    final static String[] input = {"44 Solomon", "42 Jason", "42 Errol",
        "41 Garry", "41 Bernard", "41 Barry", "39 Stephen"};

    public static void main(String[] args) {
        int len = input.length;

        Map<String, int[]> map = new TreeMap<>((a, b) -> b.compareTo(a));
        for (int i = 0; i < len; i++) {
            String key = input[i].split("\\s+")[0];
            int[] arr;
            if ((arr = map.get(key)) == null)
                arr = new int[]{i, 0};
            arr[1]++;
            map.put(key, arr);
        }
        int[][] groups = map.values().toArray(new int[map.size()][]);

        standardRanking(len, groups);
        modifiedRanking(len, groups);
        denseRanking(len, groups);
        ordinalRanking(len);
        fractionalRanking(len, groups);
    }

    private static void standardRanking(int len, int[][] groups) {
        System.out.println("\nStandard ranking");
        for (int i = 0, rank = 0, group = 0; i < len; i++) {
            if (group < groups.length && i == groups[group][0]) {
                rank = i + 1;
                group++;
            }
            System.out.printf("%d %s%n", rank, input[i]);
        }
    }

    private static void modifiedRanking(int len, int[][] groups) {
        System.out.println("\nModified ranking");
        for (int i = 0, rank = 0, group = 0; i < len; i++) {
            if (group < groups.length && i == groups[group][0])
                rank += groups[group++][1];
            System.out.printf("%d %s%n", rank, input[i]);
        }
    }

    private static void denseRanking(int len, int[][] groups) {
        System.out.println("\nDense ranking");
        for (int i = 0, rank = 0; i < len; i++) {
            if (rank < groups.length && i == groups[rank][0])
                rank++;
            System.out.printf("%d %s%n", rank, input[i]);
        }
    }

    private static void ordinalRanking(int len) {
        System.out.println("\nOrdinal ranking");
        for (int i = 0; i < len; i++)
            System.out.printf("%d %s%n", i + 1, input[i]);
    }

    private static void fractionalRanking(int len, int[][] groups) {
        System.out.println("\nFractional ranking");
        float rank = 0;
        for (int i = 0, tmp = 0, group = 0; i < len; i++) {
            if (group < groups.length && i == groups[group][0]) {
                tmp += groups[group++][1];
                rank = (i + 1 + tmp) / 2.0F;
            }
            System.out.printf("%2.1f %s%n", rank, input[i]);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def mc_rank(iterable, start=1):
    """Modified competition ranking"""
    lastresult, fifo = None, []
    for n, item in enumerate(iterable, start-1):
        if item[0] == lastresult:
            fifo += [item]
        else:
            while fifo:
                yield n, fifo.pop(0)
            lastresult, fifo = item[0], fifo + [item]
    while fifo:
        yield n+1, fifo.pop(0)


def sc_rank(iterable, start=1):
    """Standard competition ranking"""
    lastresult, lastrank = None, None
    for n, item in enumerate(iterable, start):
        if item[0] == lastresult:
            yield lastrank, item
        else:
            yield n, item
            lastresult, lastrank = item[0], n


def d_rank(iterable, start=1):
    """Dense ranking"""
    lastresult, lastrank = None, start - 1,
    for item in iterable:
        if item[0] == lastresult:
            yield lastrank, item
        else:
            lastresult, lastrank = item[0], lastrank + 1
            yield lastrank, item


def o_rank(iterable, start=1):
    """Ordinal  ranking"""
    yield from enumerate(iterable, start)


def f_rank(iterable, start=1):
    """Fractional ranking"""
    last, fifo = None, []
    for n, item in enumerate(iterable, start):
        if item[0] != last:
            if fifo:
                mean = sum(f[0] for f in fifo) / len(fifo)
                while fifo:
                    yield mean, fifo.pop(0)[1]
        last = item[0]
        fifo.append((n, item))
    if fifo:
        mean = sum(f[0] for f in fifo) / len(fifo)
        while fifo:
            yield mean, fifo.pop(0)[1]


if __name__ == '__main__':
    scores = [(44, 'Solomon'),
              (42, 'Jason'),
              (42, 'Errol'),
              (41, 'Garry'),
              (41, 'Bernard'),
              (41, 'Barry'),
              (39, 'Stephen')]

    print('\nScores to be ranked (best first):')
    for s in scores:
        print('        %2i %s' % (s ))
    for ranker in [sc_rank, mc_rank, d_rank, o_rank, f_rank]:
        print('\n%s:' % ranker.__doc__)
        for rank, score in ranker(scores):
            print('  %3g, %r' % (rank, score))

```

