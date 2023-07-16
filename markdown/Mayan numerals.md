# Mayan numerals

## Task Link
[Rosetta Code - Mayan numerals](https://rosettacode.org/wiki/Mayan_numerals)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public class MayanNumerals {

    public static void main(String[] args) {
        for ( long base10 : new long[] {4005, 8017, 326205, 886205, 1000000000, 1081439556L, 26960840421L, 503491211079L }) {
            displayMyan(BigInteger.valueOf(base10));
            System.out.printf("%n");
        }
    }
    
    private static char[] digits = "0123456789ABCDEFGHJK".toCharArray();
    private static BigInteger TWENTY = BigInteger.valueOf(20);
    
    private static void displayMyan(BigInteger numBase10) {
        System.out.printf("As base 10:  %s%n", numBase10);
        String numBase20 = "";
        while ( numBase10.compareTo(BigInteger.ZERO) > 0 ) {
            numBase20 = digits[numBase10.mod(TWENTY).intValue()] + numBase20;
            numBase10 = numBase10.divide(TWENTY);
        }
        System.out.printf("As base 20:  %s%nAs Mayan:%n", numBase20);
        displayMyanLine1(numBase20);
        displayMyanLine2(numBase20);
        displayMyanLine3(numBase20);
        displayMyanLine4(numBase20);
        displayMyanLine5(numBase20);
        displayMyanLine6(numBase20);
    }
 
    private static char boxUL = Character.toChars(9556)[0];
    private static char boxTeeUp = Character.toChars(9574)[0];
    private static char boxUR = Character.toChars(9559)[0];
    private static char boxHorz = Character.toChars(9552)[0];
    private static char boxVert = Character.toChars(9553)[0];
    private static char theta = Character.toChars(952)[0];
    private static char boxLL = Character.toChars(9562)[0];
    private static char boxLR = Character.toChars(9565)[0];
    private static char boxTeeLow = Character.toChars(9577)[0];
    private static char bullet = Character.toChars(8729)[0];
    private static char dash = Character.toChars(9472)[0];
    
    private static void displayMyanLine1(String base20) {
        char[] chars = base20.toCharArray();
        StringBuilder sb = new StringBuilder();
        for ( int i = 0 ; i < chars.length ; i++ ) {
            if ( i == 0 ) {
                sb.append(boxUL);
            }
            for ( int j = 0 ; j < 4 ; j++ ) {
                sb.append(boxHorz);
            }
            sb.append(i < chars.length-1 ? boxTeeUp : boxUR);
        }
        System.out.println(sb.toString());
    }
    
    private static String getBullet(int count) {
        StringBuilder sb = new StringBuilder();
        switch ( count ) {
        case 1:  sb.append(" " + bullet + "  "); break;
        case 2:  sb.append(" " + bullet + bullet + " "); break;
        case 3:  sb.append("" + bullet + bullet + bullet + " "); break;
        case 4:  sb.append("" + bullet + bullet + bullet + bullet); break;
        default:  throw new IllegalArgumentException("Must be 1-4:  " + count);
        }
        return sb.toString();
    }

    private static void displayMyanLine2(String base20) {
        char[] chars = base20.toCharArray();
        StringBuilder sb = new StringBuilder();
        for ( int i = 0 ; i < chars.length ; i++ ) {
            if ( i == 0 ) {
                sb.append(boxVert);
            }
            switch ( chars[i] ) {
            case 'G':  sb.append(getBullet(1)); break;
            case 'H':  sb.append(getBullet(2)); break;
            case 'J':  sb.append(getBullet(3)); break;
            case 'K':  sb.append(getBullet(4)); break;
            default :  sb.append("    ");
            }
            sb.append(boxVert);
        }
        System.out.println(sb.toString());
    }
    
    private static String DASH = getDash();
    
    private static String getDash() {
        StringBuilder sb = new StringBuilder();
        for ( int i = 0 ; i < 4 ; i++ ) {
            sb.append(dash);
        }
        return sb.toString();
    }

    private static void displayMyanLine3(String base20) {
        char[] chars = base20.toCharArray();
        StringBuilder sb = new StringBuilder();
        for ( int i = 0 ; i < chars.length ; i++ ) {
            if ( i == 0 ) {
                sb.append(boxVert);
            }
            switch ( chars[i] ) {
            case 'B':  sb.append(getBullet(1)); break;
            case 'C':  sb.append(getBullet(2)); break;
            case 'D':  sb.append(getBullet(3)); break;
            case 'E':  sb.append(getBullet(4)); break;
            case 'F': case 'G': case 'H': case 'J': case 'K':
                sb.append(DASH); break;
            default :  sb.append("    ");
            }
            sb.append(boxVert);
        }
        System.out.println(sb.toString());
    }

    private static void displayMyanLine4(String base20) {
        char[] chars = base20.toCharArray();
        StringBuilder sb = new StringBuilder();
        for ( int i = 0 ; i < chars.length ; i++ ) {
            if ( i == 0 ) {
                sb.append(boxVert);
            }
            switch ( chars[i] ) {
            case '6':  sb.append(getBullet(1)); break;
            case '7':  sb.append(getBullet(2)); break;
            case '8':  sb.append(getBullet(3)); break;
            case '9':  sb.append(getBullet(4)); break;
            case 'A': case 'B': case 'C': case 'D': case 'E':
            case 'F': case 'G': case 'H': case 'J': case 'K':
                sb.append(DASH); break;
            default :  sb.append("    ");
            }
            sb.append(boxVert);
        }
        System.out.println(sb.toString());
    }

    private static void displayMyanLine5(String base20) {
        char[] chars = base20.toCharArray();
        StringBuilder sb = new StringBuilder();
        for ( int i = 0 ; i < chars.length ; i++ ) {
            if ( i == 0 ) {
                sb.append(boxVert);
            }
            switch ( chars[i] ) {
            case '0':  sb.append(" " + theta + "  "); break;
            case '1':  sb.append(getBullet(1)); break;
            case '2':  sb.append(getBullet(2)); break;
            case '3':  sb.append(getBullet(3)); break;
            case '4':  sb.append(getBullet(4)); break;
            case '5': case '6': case '7': case '8': case '9': 
            case 'A': case 'B': case 'C': case 'D': case 'E':
            case 'F': case 'G': case 'H': case 'J': case 'K':
                sb.append(DASH); break;
            default :  sb.append("    ");
            }
            sb.append(boxVert);
        }
        System.out.println(sb.toString());
    }

    private static void displayMyanLine6(String base20) {
        char[] chars = base20.toCharArray();
        StringBuilder sb = new StringBuilder();
        for ( int i = 0 ; i < chars.length ; i++ ) {
            if ( i == 0 ) {
                sb.append(boxLL);
            }
            for ( int j = 0 ; j < 4 ; j++ ) {
                sb.append(boxHorz);
            }
            sb.append(i < chars.length-1 ? boxTeeLow : boxLR);
        }
        System.out.println(sb.toString());
    }

}

```

## Python Code
### python_code_1.txt
```python
'''Mayan numerals'''

from functools import (reduce)


# -------------------- MAYAN NUMERALS --------------------

# mayanNumerals :: Int -> [[String]]
def mayanNumerals(n):
    '''Rows of Mayan digit cells,
       representing the integer n.
    '''
    return showIntAtBase(20)(
        mayanDigit
    )(n)([])


# mayanDigit :: Int -> [String]
def mayanDigit(n):
    '''List of strings representing a Mayan digit.'''
    if 0 < n:
        r = n % 5
        return [
            (['●' * r] if 0 < r else []) +
            (['━━'] * (n // 5))
        ]
    else:
        return ['Θ']


# mayanFramed :: Int -> String
def mayanFramed(n):
    '''Mayan integer in the form of a
       Wiki table source string.
    '''
    return 'Mayan ' + str(n) + ':\n\n' + (
        wikiTable({
            'class': 'wikitable',
            'style': cssFromDict({
                'text-align': 'center',
                'background-color': '#F0EDDE',
                'color': '#605B4B',
                'border': '2px solid silver'
            }),
            'colwidth': '3em',
            'cell': 'vertical-align: bottom;'
        })([[
            '<br>'.join(col) for col in mayanNumerals(n)
        ]])
    )


# ------------------------- TEST -------------------------

# main :: IO ()
def main():
    '''Mayan numeral representations of various integers'''
    print(
        main.__doc__ + ':\n\n' +
        '\n'.join(mayanFramed(n) for n in [
            4005, 8017, 326205, 886205, 1081439556,
            1000000, 1000000000
        ])
    )


# ------------------------ BOXES -------------------------

# wikiTable :: Dict -> [[a]] -> String
def wikiTable(opts):
    '''Source text for wiki-table display of rows of cells,
       using CSS key-value pairs in the opts dictionary.
    '''
    def colWidth():
        return 'width:' + opts['colwidth'] + '; ' if (
            'colwidth' in opts
        ) else ''

    def cellStyle():
        return opts['cell'] if 'cell' in opts else ''

    return lambda rows: '{| ' + reduce(
        lambda a, k: (
            a + k + '="' + opts[k] + '" ' if (
                k in opts
            ) else a
        ),
        ['class', 'style'],
        ''
    ) + '\n' + '\n|-\n'.join(
        '\n'.join(
            ('|' if (
                0 != i and ('cell' not in opts)
            ) else (
                '|style="' + colWidth() + cellStyle() + '"|'
            )) + (
                str(x) or ' '
            ) for x in row
        ) for i, row in enumerate(rows)
    ) + '\n|}\n\n'


# ----------------------- GENERIC ------------------------

# cssFromDict :: Dict -> String
def cssFromDict(dct):
    '''CSS string from a dictinary of key-value pairs'''
    return reduce(
        lambda a, k: a + k + ':' + dct[k] + '; ',
        dct.keys(),
        ''
    )


# showIntAtBase :: Int -> (Int -> String)
# -> Int -> String -> String
def showIntAtBase(base):
    '''String representation of an integer in a given base,
       using a supplied function for the string
       representation of digits.
    '''
    def wrap(toChr, n, rs):
        def go(nd, r):
            n, d = nd
            r_ = toChr(d) + r
            return go(divmod(n, base), r_) if 0 != n else r_
        return 'unsupported base' if 1 >= base else (
            'negative number' if 0 > n else (
                go(divmod(n, base), rs))
        )
    return lambda toChr: lambda n: lambda rs: (
        wrap(toChr, n, rs)
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

