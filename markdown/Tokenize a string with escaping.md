# Tokenize a string with escaping

## Task Link
[Rosetta Code - Tokenize a string with escaping](https://rosettacode.org/wiki/Tokenize_a_string_with_escaping)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class TokenizeStringWithEscaping {

    public static void main(String[] args) {
        String sample = "one^|uno||three^^^^|four^^^|^cuatro|";
        char separator = '|';
        char escape = '^';

        System.out.println(sample);
        try {
            System.out.println(tokenizeString(sample, separator, escape));
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public static List<String> tokenizeString(String s, char sep, char escape)
            throws Exception {
        List<String> tokens = new ArrayList<>();
        StringBuilder sb = new StringBuilder();

        boolean inEscape = false;
        for (char c : s.toCharArray()) {
            if (inEscape) {
                inEscape = false;
            } else if (c == escape) {
                inEscape = true;
                continue;
            } else if (c == sep) {
                tokens.add(sb.toString());
                sb.setLength(0);
                continue;
            }
            sb.append(c);
        }
        if (inEscape)
            throw new Exception("Invalid terminal escape");

        tokens.add(sb.toString());

        return tokens;
    }
}

```

## Python Code
### python_code_1.txt
```python
def token_with_escape(a, escape = '^', separator = '|'):
    '''
        Issue  python -m doctest thisfile.py  to run the doctests.

        >>> print(token_with_escape('one^|uno||three^^^^|four^^^|^cuatro|'))
        ['one|uno', '', 'three^^', 'four^|cuatro', '']
    '''
    result = []
    token = ''
    state = 0
    for c in a:
        if state == 0:
            if c == escape:
                state = 1
            elif c == separator:
                result.append(token)
                token = ''
            else:
                token += c
        elif state == 1:
            token += c
            state = 0
    result.append(token)
    return result

```

### python_code_2.txt
```python
'''Tokenize a string with escaping'''

from functools import reduce


# tokenize :: Char -> Char -> String -> [String]
def tokenize(delim):
    '''A list of the tokens in a string, given
       a delimiting char and an escape char.
    '''
    def go(esc, s):
        def chop(a, x):
            tkn, xs, escaped = a
            literal = not escaped
            isEsc = literal and (esc == x)
            return ([], [tkn] + xs, isEsc) if (
                literal and (delim == x)
            ) else (tkn if isEsc else [x] + tkn, xs, isEsc)

        tkn, xs, _ = reduce(chop, list(s), ([], [], False))

        return list(reversed(
            [''.join(reversed(x)) for x in [tkn] + xs]
        ))
    return lambda esc: lambda s: go(esc, s)


# --------------------------TEST---------------------------
# main :: IO ()
def main():
    '''Test'''
    
    print(
        tokenize('|')('^')(
            "one^|uno||three^^^^|four^^^|^cuatro|"
        )
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
import re

STRING = 'one^|uno||three^^^^|four^^^|^cuatro|'

def tokenize(string=STRING, escape='^', separator='|'):

    escape, separator = map(re.escape, (escape, separator))

    tokens = ['']

    def start_new_token(scanner, substring):
        tokens.append('')

    def add_escaped_char(scanner, substring):
        char = substring[1]
        tokens[-1] += char

    def add_substring(scanner, substring):
        tokens[-1] += substring

    re.Scanner([
        # an escape followed by a character produces that character
        (fr'{escape}.', add_escaped_char),

        # when encountering a separator not preceded by an escape,
        # start a new token
        (fr'{separator}', start_new_token),

        # a sequence of regular characters (i.e. not escape or separator)
        # is just appended to the token
        (fr'[^{escape}{separator}]+', add_substring),
    ]).scan(string)

    return tokens


if __name__ == '__main__':
    print(list(tokenize()))

```

### python_code_4.txt
```python
import re

STRING = 'one^|uno||three^^^^|four^^^|^cuatro|'

def tokenize(string=STRING, escape='^', separator='|'):

    re_escape, re_separator = map(re.escape, (escape, separator))

    # token regex
    regex = re.compile(fr'''
        # lookbehind: a token must be preceded by a separator
        # (note that `(?<=^|{re_separator})` doesn't work in Python)
        (?<={re_separator})

        # a token consists either of an escape sequence,
        # or a regular (non-escape, non-separator) character,
        # repeated arbitrarily many times (even zero)
        (?:{re_escape}.|[^{re_escape}{re_separator}])*
      ''',
      flags=re.VERBOSE
    )

    # since each token must start with a separator,
    # we must add an extra separator at the beginning of input
    preprocessed_string = separator + string

    for almost_token in regex.findall(preprocessed_string):
      # now get rid of escape characters: '^^' -> '^' etc.
      token = re.sub(fr'{re_escape}(.)', r'\1', almost_token)
      yield token

if __name__ == '__main__':
    print(list(tokenize()))

```

