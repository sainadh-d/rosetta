# Associative array/Iteration

## Task Link
[Rosetta Code - Associative array/Iteration](https://rosettacode.org/wiki/Associative_array/Iteration)

## Java Code
### java_code_1.txt
```java
for (Map.Entry<String, Integer> entry : map.entrySet())
    System.out.println(entry);

```

### java_code_2.txt
```java
for (String key : map.keySet())
    System.out.println(key);

```

### java_code_3.txt
```java
for (int value : map.values())
    System.out.println(value);

```

### java_code_4.txt
```java
Map<String, Integer> map = new HashMap<>();
map.put("hello", 1);
map.put("world", 2);
map.put("!", 3);

// iterating over key-value pairs:
map.forEach((k, v) -> {
    System.out.printf("key = %s, value = %s%n", k, v);
});

// iterating over keys:
map.keySet().forEach(k -> System.out.printf("key = %s%n", k));

// iterating over values:
map.values().forEach(v -> System.out.printf("value = %s%n", v));

```

## Python Code
### python_code_1.txt
```python
myDict = { "hello": 13,
	   "world": 31,
	   "!"    : 71 }

# iterating over key-value pairs:
for key, value in myDict.items():
    print ("key = %s, value = %s" % (key, value))

# iterating over keys:
for key in myDict:
    print ("key = %s" % key)
# (is a shortcut for:)
for key in myDict.keys():
    print ("key = %s" % key)

# iterating over values:
for value in myDict.values():
    print ("value = %s" % value)

```

