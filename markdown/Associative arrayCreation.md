# Associative array/Creation

## Task Link
[Rosetta Code - Associative array/Creation](https://rosettacode.org/wiki/Associative_array/Creation)

## Java Code
### java_code_1.txt
```java
Map<String, Int> map = new HashMap();
map["foo"] = 5;      // or: map.put("foo", 5)
map["bar"] = 10;
map["baz"] = 15;
map["foo"] = 6;      // replaces previous value of 5

```

### java_code_10.txt
```java
map.replace("rosetta", 300);

```

### java_code_11.txt
```java
boolean replaced = map.replace("rosetta", 100, 300);

```

### java_code_12.txt
```java
boolean contains = map.containsKey("rosetta");

```

### java_code_13.txt
```java
boolean contains = map.containsValue(100);

```

### java_code_14.txt
```java
Map<String, Integer> map = new LinkedHashMap<>();
map.put("rosetta", 100);
map.put("code", 200);

```

### java_code_15.txt
```java
Map<String, Integer> map = new TreeMap<>();
map.put("rosetta", 100);
map.put("code", 200);

```

### java_code_16.txt
```java
Comparator<String> comparator = new Comparator<String>() {
    public int compare(String stringA, String stringB) {
        if (stringA.compareTo(stringB) > 0) {
            return -1;
        } else if (stringA.compareTo(stringB) < 0) {
            return 1;
        }
        return 0;
    }
};

```

### java_code_17.txt
```java
Map<String, Integer> map = new TreeMap<>(comparator);

```

### java_code_18.txt
```java
Comparator<String> comparator = (stringA, stringB) -> {
    if (stringA.compareTo(stringB) > 0) {
        return -1;
    } else if (stringA.compareTo(stringB) < 0) {
        return 1;
    }
    return 0;
};

```

### java_code_2.txt
```java
Map<String, Int> map = ["foo"=6, "bar"=10, "baz"=15];

```

### java_code_3.txt
```java
Int? mightBeNull = map["foo"];
Int neverNull = map.getOrDefault("foo", 0);
if (Int n := map.get("foo")) {
    // if "foo" is in the map, then the variable "n" is set to its value
} else {
    // if "foo" is not in the map, then the variable "n" is not defined
}

```

### java_code_4.txt
```java
for (String key : map) {
    // the variable "key" is defined here
}

```

### java_code_5.txt
```java
for (Int value : map.values) {
    // the variable "value" is defined here
}

```

### java_code_6.txt
```java
for ((String key, Int value) : map) {
    // the variables "key" and "value" are defined here
}

```

### java_code_7.txt
```java
Map<String, Integer> map = new HashMap<>();

```

### java_code_8.txt
```java
map.put("rosetta", 100);
map.put("code", 200);

```

### java_code_9.txt
```java
int valueA = map.get("rosetta");
int valueB = map.get("code");

```

## Python Code
### python_code_1.txt
```python
hash = dict()  # 'dict' is the dictionary type.
hash = dict(red="FF0000", green="00FF00", blue="0000FF")
hash = { 'key1':1, 'key2':2, }
value = hash[key]

```

### python_code_2.txt
```python
# empty dictionary
d = {}
d['spam'] = 1
d['eggs'] = 2  

# dictionaries with two keys
d1 = {'spam': 1, 'eggs': 2}
d2 = dict(spam=1, eggs=2)

# dictionaries from tuple list
d1 = dict([('spam', 1), ('eggs', 2)])
d2 = dict(zip(['spam', 'eggs'], [1, 2]))

# iterating over keys
for key in d:
  print key, d[key]

# iterating over (key, value) pairs
for key, value in d.iteritems():
  print key, value

```

### python_code_3.txt
```python
myDict = { '1': 'a string', 1: 'an integer', 1.0: 'a floating point number', (1,): 'a tuple' }

```

