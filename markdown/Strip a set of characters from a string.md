# Strip a set of characters from a string

## Task Link
[Rosetta Code - Strip a set of characters from a string](https://rosettacode.org/wiki/Strip_a_set_of_characters_from_a_string)

## Java Code
### java_code_1.txt
```java
String stripCharacters(String string, String characters) {
    for (char character : characters.toCharArray())
        string = string.replace(String.valueOf(character), "");
    return string;
}

```

### java_code_2.txt
```java
String stripCharacters(String string, String characters) {
    StringBuilder stripped = new StringBuilder(string);
    /* traversing the string backwards is necessary to avoid collision */
    for (int index = string.length() - 1; index >= 0; index--) {
        if (characters.contains(String.valueOf(string.charAt(index))))
            stripped.deleteCharAt(index);
    }
    return stripped.toString();
}

```

### java_code_3.txt
```java
static String stripCharacters(String string, String characters) {
    /* be sure to 'quote' the 'characters' to avoid pattern collision */
    characters = Pattern.quote(characters);
    string = string.replaceAll("[%s]".formatted(characters), "");
    return string;
}

```

## Python Code
### python_code_1.txt
```python
>>> def stripchars(s, chars):
...     return s.translate(None, chars)
... 
>>> stripchars("She was a soul stripper. She took my heart!", "aei")
'Sh ws  soul strppr. Sh took my hrt!'

```

### python_code_2.txt
```python
>>> import string
>>> def stripchars(s, chars):
...     return s.translate(string.maketrans("", ""), chars)
... 
>>> stripchars("She was a soul stripper. She took my heart!", "aei")
'Sh ws  soul strppr. Sh took my hrt!'

```

### python_code_3.txt
```python
>>> def stripchars(s, chars):
...     return "".join(c for c in s if c not in chars)
... 
>>> stripchars("She was a soul stripper. She took my heart!", "aei")
'Sh ws  soul strppr. Sh took my hrt!'

```

### python_code_4.txt
```python
>>> import re
>>> def stripchars(s, chars):
	return re.sub('[%s]+' % re.escape(chars), '', s)

>>> stripchars("She was a soul stripper. She took my heart!", "aei")
'Sh ws  soul strppr. Sh took my hrt!'
>>>

```

