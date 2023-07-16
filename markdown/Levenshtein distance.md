# Levenshtein distance

## Task Link
[Rosetta Code - Levenshtein distance](https://rosettacode.org/wiki/Levenshtein_distance)

## Java Code
### java_code_1.txt
```java
public class Levenshtein {

    public static int distance(String a, String b) {
        a = a.toLowerCase();
        b = b.toLowerCase();
        // i == 0
        int [] costs = new int [b.length() + 1];
        for (int j = 0; j < costs.length; j++)
            costs[j] = j;
        for (int i = 1; i <= a.length(); i++) {
            // j == 0; nw = lev(i - 1, j)
            costs[0] = i;
            int nw = i - 1;
            for (int j = 1; j <= b.length(); j++) {
                int cj = Math.min(1 + Math.min(costs[j], costs[j - 1]), a.charAt(i - 1) == b.charAt(j - 1) ? nw : nw + 1);
                nw = costs[j];
                costs[j] = cj;
            }
        }
        return costs[b.length()];
    }

    public static void main(String [] args) {
        String [] data = { "kitten", "sitting", "saturday", "sunday", "rosettacode", "raisethysword" };
        for (int i = 0; i < data.length; i += 2)
            System.out.println("distance(" + data[i] + ", " + data[i+1] + ") = " + distance(data[i], data[i+1]));
    }
}

```

### java_code_2.txt
```java
public class Levenshtein{
    public static int levenshtein(String s, String t){
        /* if either string is empty, difference is inserting all chars 
         * from the other
         */
        if(s.length() == 0) return t.length();
        if(t.length() == 0) return s.length();

        /* if first letters are the same, the difference is whatever is
         * required to edit the rest of the strings
         */
        if(s.charAt(0) == t.charAt(0))
            return levenshtein(s.substring(1), t.substring(1));

        /* else try:
         *      changing first letter of s to that of t,
         *      remove first letter of s, or
         *      remove first letter of t
         */
        int a = levenshtein(s.substring(1), t.substring(1));
        int b = levenshtein(s, t.substring(1));
        int c = levenshtein(s.substring(1), t);

        if(a > b) a = b;
        if(a > c) a = c;

        //any of which is 1 edit plus editing the rest of the strings
        return a + 1;
    }

    public static void main(String[] args) {
        String s1 = "kitten";
        String s2 = "sitting";
        System.out.println("distance between '" + s1 + "' and '"
                + s2 + "': " + levenshtein(s1, s2));
        s1 = "rosettacode";
        s2 = "raisethysword";
        System.out.println("distance between '" + s1 + "' and '"
                + s2 + "': " + levenshtein(s1, s2));
        StringBuilder sb1 = new StringBuilder(s1);
        StringBuilder sb2 = new StringBuilder(s2);
        System.out.println("distance between '" + sb1.reverse() + "' and '"
                + sb2.reverse() + "': "
                + levenshtein(sb1.reverse().toString(), sb2.reverse().toString()));
    }
}

```

### java_code_3.txt
```java
import static java.lang.Math.abs;
import static java.lang.Math.max;

public class Levenshtein {

	public static int ld(String a, String b) { 
		return distance(a, b, -1);
	}
	public static boolean ld(String a, String b, int max) {
		return distance(a, b, max) <= max;
	}
	
	private static int distance(String a, String b, int max) {
		if (a == b) return 0;
		int la = a.length();
		int lb = b.length();
		if (max >= 0 && abs(la - lb) > max) return max+1;
		if (la == 0) return lb;
		if (lb == 0) return la;
		if (la < lb) {
			int tl = la; la = lb; lb = tl;
			String ts = a;  a = b; b = ts;
		}
		
		int[] cost = new int[lb+1];
		for (int i=0; i<=lb; i+=1) {
			cost[i] = i;
		}

		for (int i=1; i<=la; i+=1) {
			cost[0] = i;
			int prv = i-1;
			int min = prv;
			for (int j=1; j<=lb; j+=1) {
				int act = prv + (a.charAt(i-1) == b.charAt(j-1) ? 0 : 1);
				cost[j] = min(1+(prv=cost[j]), 1+cost[j-1], act);
				if (prv < min) min = prv;
			}
			if (max >= 0 && min > max) return max+1;
		}
		if (max >= 0 && cost[lb] > max) return max+1;
		return cost[lb];	
	}
	
	private static int min(int ... a) {
		int min = Integer.MAX_VALUE;
		for (int i: a) if (i<min) min = i;
		return min;
	}
	
	public static void main(String[] args) {
		System.out.println(
			ld("kitten","kitten") + " " + // 0
			ld("kitten","sitten") + " " + // 1
			ld("kitten","sittes") + " " + // 2
			ld("kitten","sityteng") + " " + // 3
			ld("kitten","sittYing") + " " + // 4
			ld("rosettacode","raisethysword") + " " + // 8 
			ld("kitten","kittenaaaaaaaaaaaaaaaaa") + " " + // 17
			ld("kittenaaaaaaaaaaaaaaaaa","kitten") // 17
		);
		System.out.println(
			ld("kitten","kitten", 3) + " " + // true
			ld("kitten","sitten", 3) + " " + // true
			ld("kitten","sittes", 3) + " " + // true
			ld("kitten","sityteng", 3) + " " + // true
			ld("kitten","sittYing", 3) + " " + // false
			ld("rosettacode","raisethysword", 3) + " " + // false 
			ld("kitten","kittenaaaaaaaaaaaaaaaaa", 3) + " " + // false
			ld("kittenaaaaaaaaaaaaaaaaa","kitten", 3) // false
		);
	}
}

```

## Python Code
### python_code_1.txt
```python
def setup():
    println(distance("kitten", "sitting"))

def distance(a, b):
    costs = []
    for j in range(len(b) + 1):
        costs.append(j)
    for i in range(1, len(a) + 1):
        costs[0] = i
        nw = i - 1
        for j in range(1, len(b) + 1):
            cj = min(1 + min(costs[j], costs[j - 1]),
                     nw if a[i - 1] == b[j - 1] else nw + 1)
            nw = costs[j]
            costs[j] = cj

    return costs[len(b)]

```

### python_code_2.txt
```python
def levenshteinDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    d = [[i] for i in range(1, m + 1)]   # d matrix rows
    d.insert(0, list(range(0, n + 1)))   # d matrix columns
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:   # Python (string) is 0-based
                substitutionCost = 0
            else:
                substitutionCost = 1
            d[i].insert(j, min(d[i - 1][j] + 1,
                               d[i][j - 1] + 1,
                               d[i - 1][j - 1] + substitutionCost))
    return d[-1][-1]

print(levenshteinDistance("kitten","sitting"))
print(levenshteinDistance("rosettacode","raisethysword"))

```

### python_code_3.txt
```python
def minimumEditDistance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]
 
print(minimumEditDistance("kitten","sitting"))
print(minimumEditDistance("rosettacode","raisethysword"))

```

### python_code_4.txt
```python
def ld(a, b, mx=-1):	
    def result(d): return d if mx < 0 else False if d > mx else True
    
    if a == b: return result(0)
    la, lb = len(a), len(b)
    if mx >= 0 and abs(la - lb) > mx: return result(mx+1)
    if la == 0: return result(lb)
    if lb == 0: return result(la)
    if lb > la: a, b, la, lb = b, a, lb, la
    
    cost = array('i', range(lb + 1))
    for i in range(1, la + 1):
        cost[0] = i; ls = i-1; mn = ls
        for j in range(1, lb + 1):
            ls, act = cost[j], ls + int(a[i-1] != b[j-1])
            cost[j] = min(ls+1, cost[j-1]+1, act)
            if (ls < mn): mn = ls
        if mx >= 0 and mn > mx: return result(mx+1)
    if mx >= 0 and cost[lb] > mx: return result(mx+1)
    return result(cost[lb])

print(
    ld('kitten','kitten'), # 0
    ld('kitten','sitten'), # 1
    ld('kitten','sittes'), # 2
    ld('kitten','sityteng'), # 3
    ld('kitten','sittYing'), # 4
    ld('rosettacode','raisethysword'), # 8 
    ld('kitten','kittenaaaaaaaaaaaaaaaaa'), # 17
    ld('kittenaaaaaaaaaaaaaaaaa','kitten') # 17
)

print(
    ld('kitten','kitten',3), # True
    ld('kitten','sitten',3), # True
    ld('kitten','sittes',3), # True
    ld('kitten','sityteng',3), # True
    ld('kitten','sittYing',3), # False
    ld('rosettacode','raisethysword',3), # False
    ld('kitten','kittenaaaaaaaaaaaaaaaaa',3), # False
    ld('kittenaaaaaaaaaaaaaaaaa','kitten',3) # False
)

```

### python_code_5.txt
```python
>>> from functools import lru_cache
>>> @lru_cache(maxsize=4095)
def ld(s, t):
	if not s: return len(t)
	if not t: return len(s)
	if s[0] == t[0]: return ld(s[1:], t[1:])
	l1 = ld(s, t[1:])
	l2 = ld(s[1:], t)
	l3 = ld(s[1:], t[1:])
	return 1 + min(l1, l2, l3)

>>> print( ld("kitten","sitting"),ld("rosettacode","raisethysword") )
3 8

```

### python_code_6.txt
```python
'''Levenshtein distance'''

from itertools import (accumulate, chain, islice)
from functools import reduce


# levenshtein :: String -> String -> Int
def levenshtein(sa):
    '''Levenshtein distance between
       two strings.'''
    s1 = list(sa)

    # go :: [Int] -> Char -> [Int]
    def go(ns, c):
        n, ns1 = ns[0], ns[1:]

        # gap :: Int -> (Char, Int, Int) -> Int
        def gap(z, c1xy):
            c1, x, y = c1xy
            return min(
                succ(y),
                succ(z),
                succ(x) if c != c1 else x
            )
        return scanl(gap)(succ(n))(
            zip(s1, ns, ns1)
        )
    return lambda sb: reduce(
        go, list(sb), enumFromTo(0)(len(s1))
    )[-1]


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Tests'''

    pairs = [
        ('rosettacode', 'raisethysword'),
        ('kitten', 'sitting'),
        ('saturday', 'sunday')
    ]

    print(
        tabulated(
            'Levenshtein minimum edit distances:\n'
        )(str)(str)(
            uncurry(levenshtein)
        )(concat(map(
            list,
            zip(pairs, map(swap, pairs))
        )))
    )


# GENERIC -------------------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# concat :: [[a]] -> [a]
# concat :: [String] -> String
def concat(xxs):
    '''The concatenation of all the elements in a list.'''
    xs = list(chain.from_iterable(xxs))
    unit = '' if isinstance(xs, str) else []
    return unit if not xs else (
        ''.join(xs) if isinstance(xs[0], str) else xs
    )


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# scanl :: (b -> a -> b) -> b -> [a] -> [b]
def scanl(f):
    '''scanl is like reduce, but returns a succession of
       intermediate values, building from the left.'''
    return lambda a: lambda xs: (
        list(accumulate(chain([a], xs), f))
    )


# swap :: (a, b) -> (b, a)
def swap(tpl):
    '''The swapped components of a pair.'''
    return (tpl[1], tpl[0])


# succ :: Int => Int -> Int
def succ(x):
    '''The successor of a value.
       For numeric types, (1 +).'''
    return 1 + x


# tabulated :: String -> (a -> String) ->
#                        (b -> String) ->
#                        (a -> b) -> [a] -> String
def tabulated(s):
    '''Heading -> x display function ->
                 fx display function ->
                 f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join([
            xShow(x).rjust(w, ' ') + ' -> ' + fxShow(f(x))
            for x in xs

        ])
    return lambda xShow: lambda fxShow: (
        lambda f: lambda xs: go(
            xShow, fxShow, f, xs
        )
    )


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.'''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )


# uncurry :: (a -> b -> c) -> ((a, b) -> c)
def uncurry(f):
    '''A function over a tuple
       derived from a curried function.'''
    return lambda xy: f(xy[0])(
        xy[1]
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

