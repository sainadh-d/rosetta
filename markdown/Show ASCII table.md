# Show ASCII table

## Task Link
[Rosetta Code - Show ASCII table](https://rosettacode.org/wiki/Show_ASCII_table)

## Java Code
### java_code_2.txt
```java
public class ShowAsciiTable {

    public static void main(String[] args) {
        for ( int i = 32 ; i <= 127 ; i++ ) {
            if ( i == 32 || i == 127 ) {
                String s = i == 32 ? "Spc" : "Del";
                System.out.printf("%3d: %s ", i, s);
            }
            else {
                System.out.printf("%3d: %c   ", i, i);
            }
            if ( (i-1) % 6 == 0 ) {
                System.out.println();
            }
        }
    }

}

```

### java_code_3.txt
```java
String printASCIITable() {
    StringBuilder string = new StringBuilder();
    String newline = System.lineSeparator();
    string.append("dec hex binary oct char").append(newline);
    for (int decimal = 32; decimal <= 127; decimal++) {
        string.append(format(decimal));
        switch (decimal) {
            case 32 -> string.append("[SPACE]");
            case 127 -> string.append("[DELETE]");
            default -> string.append((char) decimal);
        }
        string.append(newline);
    }
    return string.toString();
}

String format(int value) {
    return "%-3d %01$-2x %7s %01$-3o ".formatted(value, Integer.toBinaryString(value));
}

```

## Python Code
### python_code_1.txt
```python
for i in range(16):
    for j in range(32+i, 127+1, 16):
        if j == 32:
            k = 'Spc'
        elif j == 127:
            k = 'Del'
        else:
            k = chr(j)
        print("%3d : %-3s" % (j,k), end="")
    print()

```

### python_code_2.txt
```python
from unicodedata import name
from html import escape

def pp(n):
    if n <= 32:
        return chr(0x2400 + n)
    if n == 127:
        return '␡'
    return chr(n)

print('<table border="3px" style="background-color:LightCyan;text-align:center">\n <tr>')
for n in range(128):
    if n %16 == 0 and 1 < n: 
        print(" </tr><tr>")
    print(f'  <td style="center">{n}<br>0x{n:02x}<br><big><b title="{escape(name(pp(n)))}">{escape(pp(n))}</b></big></td>')
print(""" </tr>\n</table>""")

```

### python_code_3.txt
```python
'''Plain text ASCII code table'''

from functools import reduce
from itertools import chain


# asciiTable :: String
def asciiTable():
    '''Table of ASCII codes arranged in 16 rows * 6 columns.'''
    return unlines(
        concat(c.ljust(12, ' ') for c in xs) for xs in (
            transpose(chunksOf(16)(
                [asciiEntry(n) for n in enumFromTo(32)(127)]
            ))
        )
    )


# asciiEntry :: Int -> String
def asciiEntry(n):
    '''Number, and name or character, for given point in ASCII code.'''
    k = asciiName(n)
    return k if '' == k else (
        concat([str(n).rjust(3, ' '), ' : ', k])
    )


# asciiName :: Int -> String
def asciiName(n):
    '''Name or character for given ASCII code.'''
    return '' if 32 > n or 127 < n else (
        'Spc' if 32 == n else (
            'Del' if 127 == n else chr(n)
        )
    )


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Test'''
    print(
        asciiTable()
    )


# GENERIC ABSTRACTIONS ------------------------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n,
       subdividing the contents of xs.
       Where the length of xs is not evenly divible
       the final list will be shorter than n.'''
    return lambda xs: reduce(
        lambda a, i: a + [xs[i:n + i]],
        range(0, len(xs), n), []
    ) if 0 < n else []


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


# splitAt :: Int -> [a] -> ([a], [a])
def splitAt(n):
    '''A tuple pairing the prefix of length n
       with the rest of xs.'''
    return lambda xs: (xs[0:n], xs[n:])


# transpose :: Matrix a -> Matrix a
def transpose(m):
    '''The rows and columns of the argument transposed.
       (The matrix containers and rows can be lists or tuples).'''
    if m:
        inner = type(m[0])
        z = zip(*m)
        return (type(m))(
            map(inner, z) if tuple != inner else z
        )
    else:
        return m


# unlines :: [String] -> String
def unlines(xs):
    '''A single newline-delimited string derived
       from a list of strings.'''
    return '\n'.join(xs)


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
# One-liner 
# print('\n'.join([''.join(["%3d : %-3s" % (a, 'Spc' if a == 32 else 'Del' if a == 127 else chr(a)) for a in lst]) for lst in [[i+c*16 for c in range(6)] for i in range(32, 47+1)]])

## Detailed version

# List of 16 lists of integers corresponding to
# each row of the table
rows_as_ints = [[i+c*16 for c in range(6)] for i in range(32, 47+1)]

# Function for converting numeric value to string
codepoint2str = lambda codepoint: 'Spc' if codepoint == 32 else 'Del' if codepoint == 127 else chr(codepoint)

rows_as_strings = [["%3d : %-3s" % (a, codepoint2str(a)) for a in row] for row in rows_as_ints]

# Joining columns into rows and printing rows one in a separate line
print('\n'.join([''.join(row) for row in rows_as_strings]))

```

