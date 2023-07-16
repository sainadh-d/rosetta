# Tokenize a string

## Task Link
[Rosetta Code - Tokenize a string](https://rosettacode.org/wiki/Tokenize_a_string)

## Java Code
### java_code_1.txt
```java
String toTokenize = "Hello,How,Are,You,Today";
System.out.println(String.join(".", toTokenize.split(",")));

```

### java_code_2.txt
```java
String toTokenize = "Hello,How,Are,You,Today";

String words[] = toTokenize.split(",");//splits on one comma, multiple commas yield multiple splits
               //toTokenize.split(",+") if you want to ignore empty fields
for(int i=0; i<words.length; i++) {
    System.out.print(words[i] + ".");
}

```

### java_code_3.txt
```java
String toTokenize = "Hello,How,Are,You,Today";

StringTokenizer tokenizer = new StringTokenizer(toTokenize, ",");
while(tokenizer.hasMoreTokens()) {
    System.out.print(tokenizer.nextToken() + ".");
}

```

## Python Code
### python_code_1.txt
```python
let text = 'Hello,How,Are,You,Today'
let tokens = text.split(||,||)
print tokens.join(with: '.')

```

### python_code_2.txt
```python
text = "Hello,How,Are,You,Today"
tokens = text.split(',')
print ('.'.join(tokens))

```

### python_code_3.txt
```python
print ('.'.join('Hello,How,Are,You,Today'.split(',')))

```

