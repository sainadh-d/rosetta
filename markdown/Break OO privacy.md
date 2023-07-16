# Break OO privacy

## Task Link
[Rosetta Code - Break OO privacy](https://rosettacode.org/wiki/Break_OO_privacy)

## Java Code
### java_code_2.txt
```java
class Example {
    String stringA = "rosetta";
    private String stringB = "code";
}

```

### java_code_3.txt
```java
Example example = new Example();
Field field = example.getClass().getDeclaredField("stringB");

```

### java_code_4.txt
```java
field.setAccessible(true);

```

### java_code_5.txt
```java
String stringB = (String) field.get(example);

```

### java_code_6.txt
```java
Example example = new Example();
Field field = example.getClass().getDeclaredField("stringB");
field.setAccessible(true);
String stringA = example.stringA;
String stringB = (String) field.get(example);
System.out.println(stringA + " " + stringB);

```

### java_code_7.txt
```java
class Example {
    String stringA = "rosetta";

    private String stringB() {
        return "code";
    }
}

```

### java_code_8.txt
```java
Example example = new Example();
Method method = example.getClass().getDeclaredMethod("stringB");
method.setAccessible(true);
String stringA = example.stringA;
String stringB = (String) method.invoke(example);
System.out.println(stringA + " " + stringB);

```

## Python Code
### python_code_1.txt
```python
>>> class MyClassName:
	__private = 123
	non_private = __private * 2

	
>>> mine = MyClassName()
>>> mine.non_private
246
>>> mine.__private
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    mine.__private
AttributeError: 'MyClassName' object has no attribute '__private'
>>> mine._MyClassName__private
123
>>>

```

