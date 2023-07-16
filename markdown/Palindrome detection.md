# Palindrome detection

## Task Link
[Rosetta Code - Palindrome detection](https://rosettacode.org/wiki/Palindrome_detection)

## Java Code
### java_code_1.txt
```java
public static boolean pali(String testMe){
	StringBuilder sb = new StringBuilder(testMe);
	return testMe.equals(sb.reverse().toString());
}

```

### java_code_2.txt
```java
public static boolean isPalindrome(String input) {
	for (int i = 0, j = input.length() - 1; i < j; i++, j--) {
		char startChar = input.charAt(i);
		char endChar = input.charAt(j);

		// Handle surrogate pairs in UTF-16
		if (Character.isLowSurrogate(endChar)) {
			if (startChar != input.charAt(--j)) {
				return false;
			}
			if (input.charAt(++i) != endChar) {
				return false;
			}
		} else if (startChar != endChar) {
			return false;
		}
	}
	return true;
}

```

### java_code_3.txt
```java
public static boolean rPali(String testMe){
	if(testMe.length()<=1){
		return true;
	}
	if(!(testMe.charAt(0)+"").equals(testMe.charAt(testMe.length()-1)+"")){
		return false;
	}
	return rPali(testMe.substring(1, testMe.length()-1));
}

```

### java_code_4.txt
```java
public static boolean rPali(String testMe){
	int strLen = testMe.length();
	return rPaliHelp(testMe, strLen-1, strLen/2, 0);
}

public static boolean rPaliHelp(String testMe, int strLen, int testLen, int index){
	if(index > testLen){
		return true;
	}
	if(testMe.charAt(index) != testMe.charAt(strLen-index)){
		return false;
	}
	return rPaliHelp(testMe, strLen, testLen, index + 1);
}

```

### java_code_5.txt
```java
public static boolean pali(String testMe){
	return testMe.matches("|(?:(.)(?<=(?=^.*?(\\1\\2?)$).*))+(?<=(?=^\\2$).*)");
}

```

## Python Code
### python_code_1.txt
```python
def is_palindrome(s):
  return s == s[::-1]

```

### python_code_2.txt
```python
def is_palindrome(s):
  low = 0
  high = len(s) - 1
  while low < high:
    if not s[low].isalpha():
      low += 1
    elif not s[high].isalpha():
      high -= 1
    else:
      if s[low].lower() != s[high].lower():
        return False
      else:
        low += 1
        high -= 1
        return True

```

### python_code_3.txt
```python
def is_palindrome_r(s):
  if len(s) <= 1:
    return True
  elif s[0] != s[-1]:
    return False
  else:
    return is_palindrome_r(s[1:-1])

```

### python_code_4.txt
```python
def is_palindrome_r2(s):
  return not s or s[0] == s[-1] and is_palindrome_r2(s[1:-1])

```

### python_code_5.txt
```python
def test(f, good, bad):
  assert all(f(x) for x in good)
  assert not any(f(x) for x in bad)
  print '%s passed all %d tests' % (f.__name__, len(good)+len(bad))

pals = ('', 'a', 'aa', 'aba', 'abba')
notpals = ('aA', 'abA', 'abxBa', 'abxxBa')
for ispal in is_palindrome, is_palindrome_r, is_palindrome_r2:
  test(ispal, pals, notpals)

```

### python_code_6.txt
```python
def p_loop():
  import re, string
  re1=""       # Beginning of Regex
  re2=""       # End of Regex
  pal=raw_input("Please Enter a word or phrase: ")
  pd = pal.replace(' ','')
  for c in string.punctuation:
     pd = pd.replace(c,"")
  if pal == "" :
    return -1
  c=len(pd)   # Count of chars.
  loops = (c+1)/2 
  for x in range(loops):
    re1 = re1 + "(\w)"
    if (c%2 == 1 and x == 0):
       continue 
    p = loops - x
    re2 = re2 + "\\" + str(p)
  regex= re1+re2+"$"   # regex is like "(\w)(\w)(\w)\2\1$"
  #print(regex)  # To test regex before re.search
  m = re.search(r'^'+regex,pd,re.IGNORECASE)
  if (m):
     print("\n   "+'"'+pal+'"')
     print("   is a Palindrome\n")
     return 1
  else:
     print("Nope!")
     return 0

```

### python_code_7.txt
```python
'''Palindrome detection'''


# isPalindrome :: String -> Bool
def isPalindrome(s):
    '''True if the string is unchanged under reversal.
       (The left half is a reflection of the right half)
    '''
    d, m = divmod(len(s), 2)
    return s[0:d] == s[d + m:][::-1]


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Test'''

    print('\n'.join(
        f'{repr(s)} -> {isPalindrome(cleaned(s))}' for s in [
            "",
            "a",
            "ab",
            "aba",
            "abba",
            "In girum imus nocte et consumimur igni"
        ]
    ))


# cleaned :: String -> String
def cleaned(s):
    '''A lower-case copy of s, with spaces pruned.'''
    return [c.lower() for c in s if ' ' != c]


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_8.txt
```python
def palindromic(str):
    for i in range(len(str)//2):
        if str[i] != str[~i]:
            return(False)
    return(True)

```

