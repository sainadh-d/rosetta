# Convert seconds to compound duration

## Task Link
[Rosetta Code - Convert seconds to compound duration](https://rosettacode.org/wiki/Convert_seconds_to_compound_duration)

## Java Code
### java_code_1.txt
```java
String duration(int seconds) {
    StringBuilder string = new StringBuilder();
    if (seconds >= 604_800 /* 1 wk */) {
        string.append("%,d wk".formatted(seconds / 604_800));
        seconds %= 604_800;
    }
    if (seconds >= 86_400 /* 1 d */) {
        if (!string.isEmpty()) string.append(", ");
        string.append("%d d".formatted(seconds / 86_400));
        seconds %= 86_400;
    }
    if (seconds >= 3600 /* 1 hr */) {
        if (!string.isEmpty()) string.append(", ");
        string.append("%d hr".formatted(seconds / 3600));
        seconds %= 3600;
    }
    if (seconds >= 60 /* 1 min */) {
        if (!string.isEmpty()) string.append(", ");
        string.append("%d min".formatted(seconds / 60));
        seconds %= 60;
    }
    if (seconds > 0) {
        if (!string.isEmpty()) string.append(", ");
        string.append("%d sec".formatted(seconds));
    }
    return string.toString();
}

```

### java_code_2.txt
```java
public class CompoundDuration {

    public static void main(String[] args) {
        compound(7259);
        compound(86400);
        compound(6000_000);
    }

    private static void compound(long seconds) {
        StringBuilder sb = new StringBuilder();

        seconds = addUnit(sb, seconds, 604800, " wk, ");
        seconds = addUnit(sb, seconds, 86400, " d, ");
        seconds = addUnit(sb, seconds, 3600, " hr, ");
        seconds = addUnit(sb, seconds, 60, " min, ");
        addUnit(sb, seconds, 1, " sec, ");

        sb.setLength(sb.length() > 2 ? sb.length() - 2 : 0);

        System.out.println(sb);
    }

    private static long addUnit(StringBuilder sb, long sec, long unit, String s) {
        long n;
        if ((n = sec / unit) > 0) {
            sb.append(n).append(s);
            sec %= (n * unit);
        }
        return sec;
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def duration(seconds):
	t= []
	for dm in (60, 60, 24, 7):
		seconds, m = divmod(seconds, dm)
		t.append(m)
	t.append(seconds)
	return ', '.join('%d %s' % (num, unit)
			 for num, unit in zip(t[::-1], 'wk d hr min sec'.split())
			 if num)

>>> for seconds in [7259, 86400, 6000000]:
	print("%7d sec = %s" % (seconds, duration(seconds)))

	
   7259 sec = 2 hr, 59 sec
  86400 sec = 1 d
6000000 sec = 9 wk, 6 d, 10 hr, 40 min
>>>

```

### python_code_2.txt
```python
>>> def duration(seconds, _maxweeks=99999999999):
    return ', '.join('%d %s' % (num, unit)
		     for num, unit in zip([(seconds // d) % m
					   for d, m in ((604800, _maxweeks), 
                                                        (86400, 7), (3600, 24), 
                                                        (60, 60), (1, 60))],
					  ['wk', 'd', 'hr', 'min', 'sec'])
		     if num)

>>> for seconds in [7259, 86400, 6000000]:
	print("%7d sec = %s" % (seconds, duration(seconds)))

	
   7259 sec = 2 hr, 59 sec
  86400 sec = 1 d
6000000 sec = 9 wk, 6 d, 10 hr, 40 min
>>>

```

### python_code_3.txt
```python
'''Compound duration'''

from functools import reduce
from itertools import chain


# compoundDurationFromUnits :: [Num] -> [String] -> Num -> [(Num, String)]
def compoundDurationFromUnits(qs):
    '''A list of compound string representions of a number n of time units,
       in terms of the multiples given in qs, and the labels given in ks.
    '''
    return lambda ks: lambda n: list(
        chain.from_iterable(map(
            lambda v, k: [(v, k)] if 0 < v else [],
            mapAccumR(
                lambda a, x: divmod(a, x) if 0 < x else (1, a)
            )(n)(qs)[1],
            ks
        ))
    )


# --------------------------TEST---------------------------
# main :: IO ()
def main():
    '''Tests of various durations, with a
       particular set of units and labels.
    '''

    print(
        fTable('Compound durations from numbers of seconds:\n')(str)(
            quoted("'")
        )(
            lambda n: ', '.join([
                str(v) + ' ' + k for v, k in
                compoundDurationFromUnits([0, 7, 24, 60, 60])(
                    ['wk', 'd', 'hr', 'min', 'sec']
                )(n)
            ])
        )([7259, 86400, 6000000])
    )


# -------------------------GENERIC-------------------------

# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
       f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# mapAccumR :: (acc -> x -> (acc, y)) -> acc -> [x] -> (acc, [y])
def mapAccumR(f):
    '''A tuple of an accumulation and a list derived by a combined
       map and fold, with accumulation from right to left.
    '''
    def go(a, x):
        acc, y = f(a[0], x)
        return (acc, [y] + a[1])
    return lambda acc: lambda xs: (
        reduce(go, reversed(xs), (acc, []))
    )


# quoted :: Char -> String -> String
def quoted(c):
    '''A string flanked on both sides
       by a specified quote character.
    '''
    return lambda s: c + s + c


# MAIN ---
if __name__ == '__main__':
    main()

```

