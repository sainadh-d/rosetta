# Chaocipher

## Task Link
[Rosetta Code - Chaocipher](https://rosettacode.org/wiki/Chaocipher)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class Chaocipher {
    private enum Mode {
        ENCRYPT,
        DECRYPT
    }

    private static final String L_ALPHABET = "HXUCZVAMDSLKPEFJRIGTWOBNYQ";
    private static final String R_ALPHABET = "PTLNBQDEOYSFAVZKGJRIHWXUMC";

    private static int indexOf(char[] a, char c) {
        for (int i = 0; i < a.length; ++i) {
            if (a[i] == c) {
                return i;
            }
        }
        return -1;
    }

    private static String exec(String text, Mode mode) {
        return exec(text, mode, false);
    }

    private static String exec(String text, Mode mode, Boolean showSteps) {
        char[] left = L_ALPHABET.toCharArray();
        char[] right = R_ALPHABET.toCharArray();
        char[] eText = new char[text.length()];
        char[] temp = new char[26];

        for (int i = 0; i < text.length(); ++i) {
            if (showSteps) {
                System.out.printf("%s  %s\n", new String(left), new String(right));
            }
            int index;
            if (mode == Mode.ENCRYPT) {
                index = indexOf(right, text.charAt(i));
                eText[i] = left[index];
            } else {
                index = indexOf(left, text.charAt(i));
                eText[i] = right[index];
            }
            if (i == text.length() - 1) {
                break;
            }

            // permute left

            if (26 - index >= 0) System.arraycopy(left, index, temp, 0, 26 - index);
            System.arraycopy(left, 0, temp, 26 - index, index);
            char store = temp[1];
            System.arraycopy(temp, 2, temp, 1, 12);
            temp[13] = store;
            left = Arrays.copyOf(temp, temp.length);

            // permute right

            if (26 - index >= 0) System.arraycopy(right, index, temp, 0, 26 - index);
            System.arraycopy(right, 0, temp, 26 - index, index);
            store = temp[0];
            System.arraycopy(temp, 1, temp, 0, 25);
            temp[25] = store;
            store = temp[2];
            System.arraycopy(temp, 3, temp, 2, 11);
            temp[13] = store;
            right = Arrays.copyOf(temp, temp.length);
        }

        return new String(eText);
    }

    public static void main(String[] args) {
        String plainText = "WELLDONEISBETTERTHANWELLSAID";
        System.out.printf("The original plaintext is : %s\n", plainText);
        System.out.println("\nThe left and right alphabets after each permutation during encryption are:");
        String cipherText = exec(plainText, Mode.ENCRYPT, true);
        System.out.printf("\nThe cipher text is : %s\n", cipherText);
        String plainText2 = exec(cipherText, Mode.DECRYPT);
        System.out.printf("\nThe recovered plaintext is : %s\n", plainText2);
    }
}

```

## Python Code
### python_code_1.txt
```python
# Python3 implementation of Chaocipher 
# left wheel = ciphertext wheel
# right wheel = plaintext wheel

def main():
    # letters only! makealpha(key) helps generate lalpha/ralpha. 
    lalpha = "HXUCZVAMDSLKPEFJRIGTWOBNYQ"
    ralpha = "PTLNBQDEOYSFAVZKGJRIHWXUMC"
    msg = "WELLDONEISBETTERTHANWELLSAID"

    print("L:", lalpha)
    print("R:", ralpha)
    print("I:", msg)
    print("O:", do_chao(msg, lalpha, ralpha, 1, 0), "\n")
    
    do_chao(msg, lalpha, ralpha, 1, 1)

def do_chao(msg, lalpha, ralpha, en=1, show=0):
    msg = correct_case(msg)
    out = ""    
    if show:
        print("="*54)        
        print(10*" " + "left:" + 21*" " + "right: ")
        print("="*54)        
        print(lalpha, ralpha, "\n")
    for L in msg:
        if en:
            lalpha, ralpha = rotate_wheels(lalpha, ralpha, L)
            out += lalpha[0]
        else:
            ralpha, lalpha = rotate_wheels(ralpha, lalpha, L)
            out += ralpha[0]
        lalpha, ralpha = scramble_wheels(lalpha, ralpha)
        if show:
            print(lalpha, ralpha)            
    return out
    
def makealpha(key=""):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    z = set()
    key = [x.upper() for x in (key + alpha[::-1])
           if not (x.upper() in z or z.add(x.upper()))]
    return "".join(key)

def correct_case(string):
    return "".join([s.upper() for s in string if s.isalpha()])

def permu(alp, num):
    alp = alp[:num], alp[num:]
    return "".join(alp[::-1])

def rotate_wheels(lalph, ralph, key):
    newin = ralph.index(key)
    return permu(lalph, newin), permu(ralph, newin)    

def scramble_wheels(lalph, ralph):
    # LEFT = cipher wheel 
    # Cycle second[1] through nadir[14] forward
    lalph = list(lalph)
    lalph = "".join([*lalph[0],
                    *lalph[2:14],
                    lalph[1],
                    *lalph[14:]])
    
    # RIGHT = plain wheel                    
    # Send the zenith[0] character to the end[25],
    # cycle third[2] through nadir[14] characters forward
    ralph = list(ralph)
    ralph = "".join([*ralph[1:3],
                     *ralph[4:15],
                     ralph[3],
                     *ralph[15:],
                     ralph[0]])
    return lalph, ralph

main()

```

### python_code_2.txt
```python
'''Chaocipher'''

from itertools import chain, cycle, islice


# chao :: String -> String -> Bool -> String -> String
def chao(l):
    '''Chaocipher encoding or decoding for the given
       left and right 'wheels'.
       A ciphertext is returned if the boolean flag
       is True, and a plaintext if the flag is False.
    '''
    def go(l, r, plain, xxs):
        if xxs:
            (src, dst) = (l, r) if plain else (r, l)
            (x, xs) = (xxs[0], xxs[1:])

            def chaoProcess(n):
                return [dst[n]] + go(
                    shifted(1)(14)(rotated(n, l)),
                    compose(shifted(2)(14))(shifted(0)(26))(
                        rotated(n, r)
                    ),
                    plain,
                    xs
                )

            return maybe('')(chaoProcess)(
                elemIndex(x)(src)
            )
        else:
            return []
    return lambda r: lambda plain: lambda xxs: concat(go(
        l, r, plain, xxs
    ))


# rotated :: Int -> [a] -> [a]
def rotated(z, s):
    '''Rotation of string s by z characters.'''
    return take(len(s))(
        drop(z)(
            cycle(s)
        )
    )


# shifted :: Int -> Int -> [a] -> [a]
def shifted(src):
    '''The string s with a set of its characters cyclically
       shifted from a source index to a destination index.
    '''
    def go(dst, s):
        (a, b) = splitAt(dst)(s)
        (x, y) = splitAt(src)(a)
        return concat([x, rotated(1, y), b])
    return lambda dst: lambda s: go(dst, s)


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Print the plain text, followed by
       a corresponding cipher text,
       and a decode of that cipher text.
    '''
    chaoWheels = chao(
        "HXUCZVAMDSLKPEFJRIGTWOBNYQ"
    )(
        "PTLNBQDEOYSFAVZKGJRIHWXUMC"
    )
    plainText = "WELLDONEISBETTERTHANWELLSAID"
    cipherText = chaoWheels(False)(plainText)

    print(plainText)
    print(cipherText)
    print(
        chaoWheels(True)(cipherText)
    )


# GENERIC -------------------------------------------------

# Just :: a -> Maybe a
def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.
       Wrapper containing the result of a computation.
    '''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


# Nothing :: Maybe a
def Nothing():
    '''Constructor for an empty Maybe (option type) value.
       Empty wrapper returned where a computation is not possible.
    '''
    return {'type': 'Maybe', 'Nothing': True}


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# concat :: [[a]] -> [a]
# concat :: [String] -> String
def concat(xs):
    '''The concatenation of all the elements
       in a list or iterable.
    '''
    def f(ys):
        zs = list(chain(*ys))
        return ''.join(zs) if isinstance(ys[0], str) else zs

    return (
        f(xs) if isinstance(xs, list) else (
            chain.from_iterable(xs)
        )
    ) if xs else []


# drop :: Int -> [a] -> [a]
# drop :: Int -> String -> String
def drop(n):
    '''The sublist of xs beginning at
       (zero-based) index n.
    '''
    def go(xs):
        if isinstance(xs, (list, tuple, str)):
            return xs[n:]
        else:
            take(n)(xs)
            return xs
    return lambda xs: go(xs)


# elemIndex :: Eq a => a -> [a] -> Maybe Int
def elemIndex(x):
    '''Just the index of the first element in xs
       which is equal to x,
       or Nothing if there is no such element.
    '''
    def go(xs):
        try:
            return Just(xs.index(x))
        except ValueError:
            return Nothing()
    return lambda xs: go(xs)


# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(v):
    '''Either the default value v, if m is Nothing,
       or the application of f to x,
       where m is Just(x).
    '''
    return lambda f: lambda m: v if None is m or m.get('Nothing') else (
        f(m.get('Just'))
    )


# splitAt :: Int -> [a] -> ([a], [a])
def splitAt(n):
    '''A tuple pairing the prefix of length n
       with the rest of xs.
    '''
    return lambda xs: (xs[0:n], xs[n:])


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, (list, tuple))
        else list(islice(xs, n))
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

