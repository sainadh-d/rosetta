# Balanced brackets

## Task Link
[Rosetta Code - Balanced brackets](https://rosettacode.org/wiki/Balanced_brackets)

## Java Code
### java_code_2.txt
```java
public class BalancedBrackets {

    public static boolean hasBalancedBrackets(String str) {
        int brackets = 0;
        for (char ch : str.toCharArray()) {
            if (ch == '[') {
                brackets++;
            } else if (ch == ']') {
                brackets--;
            } else {
                return false;   // non-bracket chars
            }
            if (brackets < 0) {   // closing bracket before opening bracket
                return false;
            }
        }
        return brackets == 0;
    }

    public static String generateBalancedBrackets(int n) {
        assert n % 2 == 0;   // if n is odd we can't match brackets
        char[] ans = new char[n];
        int openBracketsLeft = n / 2;
        int unclosed = 0;
        for (int i = 0; i < n; i++) {
            if (Math.random() >= 0.5 && openBracketsLeft > 0 || unclosed == 0) {
                ans[i] = '[';
                openBracketsLeft--;
                unclosed++;
            } else {
                ans[i] = ']';
                unclosed--;
            }
        }
        return String.valueOf(ans);
    }

    public static void main(String[] args) {
        for (int i = 0; i <= 16; i += 2) {
            String brackets = generateBalancedBrackets(i);
            System.out.println(brackets + ": " + hasBalancedBrackets(brackets));
        }

        String[] tests = {"", "[]", "][", "[][]", "][][", "[[][]]", "[]][[]"};
        for (String test : tests) {
            System.out.println(test + ": " + hasBalancedBrackets(test));
        }
    }
}

```

### java_code_3.txt
```java
import java.util.ArrayDeque;
import java.util.Deque;

public class BalancedBrackets {
	
	public static boolean areSquareBracketsBalanced(String expr) {
		return isBalanced(expr, "", "", "[", "]", false);  
	}
	public static boolean areBracketsBalanced(String expr) {
		return isBalanced(expr, "", "", "{([", "})]", false);  
	}
	public static boolean areStringAndBracketsBalanced(String expr) {
		return isBalanced(expr, "'\"", "\\\\", "{([", "})]", true);  
	}
	public static boolean isBalanced(String expr, String lit, String esc, String obr, String cbr, boolean other) {
		boolean[] inLit = new boolean[lit.length()];
		Deque<Character> stack = new ArrayDeque<Character>();
		for (int i=0; i<expr.length(); i+=1) {
			char c = get(expr, i);
			int x;
			if ((x = indexOf(inLit, true)) != -1) {
				if (c == get(lit, x) && get(expr, i-1) != get(esc, x)) inLit[x] = false;
			}
			else if ((x = indexOf(lit, c)) != -1)
				inLit[x] = true;
			else if ((x = indexOf(obr, c)) != -1)
				stack.push(get(cbr, x));
			else if (indexOf(cbr, c) != -1) {
				if (stack.isEmpty() || stack.pop() != c) return false;
			}
			else if (!other)
				return false;
		}
		return stack.isEmpty();
	}
	
	static int indexOf(boolean[] a, boolean b) {
		for (int i=0; i<a.length; i+=1) if (a[i] == b) return i;
		return -1;
	}
	static int indexOf(String s, char c) {
		return s.indexOf(c);
	}
	static char get(String s, int i) {
		return s.charAt(i);
	}

	public static void main(String[] args) {
		System.out.println("With areSquareBracketsBalanced:");
		for (String s: new String[] {
				"", "[]", "[][]", "[[][]]", "][", "][][", "[]][[]", "[", "]"
			}
		) {
			System.out.printf("%s: %s\n", s, areSquareBracketsBalanced(s));
		}
		System.out.println("\nBut also with areStringAndBracketsBalanced:");
		for (String s: new String[] {
				"x[]", "[x]", "[]x", "([{}])", "([{}]()", "([{ '([{\\'([{' \"([{\\\"([{\" }])",
			}
		) {
			System.out.printf("%s: %s\n", s, areStringAndBracketsBalanced(s));
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> def gen(N):
...     txt = ['[', ']'] * N
...     random.shuffle( txt )
...     return ''.join(txt)
... 
>>> def balanced(txt):
...     braced = 0
...     for ch in txt:
...         if ch == '[': braced += 1
...         if ch == ']':
...             braced -= 1
...             if braced < 0: return False
...     return braced == 0
... 
>>> for txt in (gen(N) for N in range(10)):
...     print ("%-22r is%s balanced" % (txt, '' if balanced(txt) else ' not'))
... 
''                     is balanced
'[]'                   is balanced
'[][]'                 is balanced
'][[[]]'               is not balanced
'[]][[][]'             is not balanced
'[][[][]]]['           is not balanced
'][]][][[]][['         is not balanced
'[[]]]]][]][[[['       is not balanced
'[[[[]][]]][[][]]'     is balanced
'][[][[]]][]]][[[[]'   is not balanced

```

### python_code_2.txt
```python
>>> from itertools import accumulate
>>> from random import shuffle
>>> def gen(n):
...     txt = list('[]' * n)
...     shuffle(txt)
...     return ''.join(txt)
...
>>> def balanced(txt):
...     brackets = ({'[': 1, ']': -1}.get(ch, 0) for ch in txt)
...     return all(x>=0 for x in accumulate(brackets))
...
>>> for txt in (gen(N) for N in range(10)):
...     print ("%-22r is%s balanced" % (txt, '' if balanced(txt) else ' not'))
...
''                     is balanced
']['                   is not balanced
'[]]['                 is not balanced
']][[[]'               is not balanced
'][[][][]'             is not balanced
'[[[][][]]]'           is balanced
'][[[][][]][]'         is not balanced
'][]][][[]][[]['       is not balanced
'][[]]][][[]][[[]'     is not balanced
'][[][[]]]][[[]][]['   is not balanced

```

### python_code_3.txt
```python
>>> import numpy as np
>>> from random import shuffle
>>> def gen(n):
...     txt = list('[]' * n)
...     shuffle(txt)
...     return ''.join(txt)
...
>>> m = np.array([{'[': 1, ']': -1}.get(chr(c), 0) for c in range(128)])
>>> def balanced(txt):
...     a = np.array(txt, 'c').view(np.uint8)
...     return np.all(m[a].cumsum() >= 0)
...
>>> for txt in (gen(N) for N in range(10)):
...     print ("%-22r is%s balanced" % (txt, '' if balanced(txt) else ' not'))
...
''                     is balanced
']['                   is not balanced
'[[]]'                 is balanced
'[]][]['               is not balanced
']][]][[['             is not balanced
'[[]][[][]]'           is balanced
'[][[]][[]]]['         is not balanced
'[][[[]][[]]][]'       is balanced
'[[][][[]]][[[]]]'     is balanced
'][]][][[]][]][][[['   is not balanced

```

