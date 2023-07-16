# Associative array/Merging

## Task Link
[Rosetta Code - Associative array/Merging](https://rosettacode.org/wiki/Associative_array/Merging)

## Java Code
### java_code_1.txt
```java
import java.util.LinkedHashMap;
import java.util.Map;

```

### java_code_2.txt
```java
Map<String, String> mapA = new LinkedHashMap<>();
mapA.put("name", "Rocket Skates");
mapA.put("price", "12.75");
mapA.put("color", "yellow");

Map<String, String> mapB = new LinkedHashMap<>();
mapB.put("price", "15.25");
mapB.put("color", "red");
mapB.put("year", "1974");

Map<String, String> mapC = new LinkedHashMap<>();
mapC.putAll(mapA);
mapC.putAll(mapB);

```

### java_code_3.txt
```java
for(Map.Entry<String, String> entry : mapA.entrySet())
    System.out.printf("%-20s%s%n", entry.getKey(), entry.getValue());

for(Map.Entry<String, String> entry : mapB.entrySet())
    System.out.printf("%-20s%s%n", entry.getKey(), entry.getValue());

for(Map.Entry<String, String> entry : mapC.entrySet())
    System.out.printf("%-20s%s%n", entry.getKey(), entry.getValue());

```

### java_code_4.txt
```java
Map<String, Object> mapA = new LinkedHashMap<>();
mapA.put("name", "Rocket Skates");
mapA.put("price", 12.75);
mapA.put("color", "yellow");

Map<String, Object> mapB = new LinkedHashMap<>();
mapB.put("price", 15.25);
mapB.put("color", "red");
mapB.put("year", 1974);

Map<String, Object> mapC = new LinkedHashMap<>();
mapC.putAll(mapA);
mapC.putAll(mapB);

```

## Python Code
### python_code_1.txt
```python
base = {"name":"Rocket Skates", "price":12.75, "color":"yellow"}
update = {"price":15.25, "color":"red", "year":1974}

result = {**base, **update}

print(result)

```

### python_code_2.txt
```python
base = {"name":"Rocket Skates", "price":12.75, "color":"yellow"}
update = {"price":15.25, "color":"red", "year":1974}

result = base.copy()
result.update(update)

print(result)

```

### python_code_3.txt
```python
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> base = {"name":"Rocket Skates", "price":12.75, "color":"yellow"}
>>> update = {"price":15.25, "color":"red", "year":1974}
>>> result = base | update
>>> result
{'name': 'Rocket Skates', 'price': 15.25, 'color': 'red', 'year': 1974}
>>>

```

