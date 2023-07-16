# Arrays

## Task Link
[Rosetta Code - Arrays](https://rosettacode.org/wiki/Arrays)

## Java Code
### java_code_10.txt
```java
Arrays.toString(values);

```

### java_code_11.txt
```java
[100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

```

### java_code_12.txt
```java
List<String> strings;
List<Integer> values;

```

### java_code_13.txt
```java
List<String> strings = new ArrayList<>();
List<Integer> values = new ArrayList<>();

```

### java_code_14.txt
```java
strings.add("rosetta");
strings.add("code");
values.add(1);
values.add(2);
values.add(3);

```

### java_code_15.txt
```java
strings.add("code");
strings.add(0, "rosetta");

```

### java_code_16.txt
```java
strings.set(0, "ROSETTA");
strings.set(1, "CODE");

```

### java_code_17.txt
```java
Deque<String> strings = new ArrayDeque<>();

```

### java_code_18.txt
```java
strings.push("code");
strings.push("rosetta");

```

### java_code_19.txt
```java
strings.pop();

```

### java_code_2.txt
```java
String[] strings;
int[] values;

```

### java_code_3.txt
```java
String strings[];
int values[];

```

### java_code_4.txt
```java
String[] strings = new String[] { "rosetta", "code" };
int[] values = new int[] { 1, 2, 3 };

```

### java_code_5.txt
```java
String[] strings;
strings = new String[] { "rosetta", "code" };
int[] values;
values = new int[] { 1, 2, 3 };

```

### java_code_6.txt
```java
String[] strings = new String[2];
int[] values = new int[3];

```

### java_code_7.txt
```java
String string = strings[0];
int value = values[2];

```

### java_code_8.txt
```java
String[] strings = new String[2];
strings[0] = "rosetta";
strings[1] = "code";
String string = strings[0] + " " + strings[1];

```

### java_code_9.txt
```java
int[] values = new int[10];
Arrays.fill(values, 100);

```

## Python Code
### python_code_1.txt
```python
array = []

array.append(1)
array.append(3)

array[0] = 2

print(array[0])

```

### python_code_2.txt
```python
my_array = [0] * size

```

### python_code_3.txt
```python
my_array = [[0] * width] * height  # DOES NOT WORK AS INTENDED!!!

```

### python_code_4.txt
```python
my_array = [[0 for x in range(width)] for y in range(height)]

```

### python_code_5.txt
```python
my_array = list()
for x in range(height):
   my_array.append([0] * width)

```

### python_code_6.txt
```python
# Retrieve an element directly from the array.
item = array[index]

# Use the array like a stack.  Note that using the pop() method removes the element.
array.pop()  # Pop last item in a list
array.pop(0)  # Pop first item in a list

# Using a negative element counts from the end of the list.
item = array[-1]  # Retrieve last element in a list.

```

### python_code_7.txt
```python
try:
    # This will cause an exception, which will then be caught.
    print(array[len(array)])
except IndexError as e:
    # Print the exception. 
    print(e)

```

### python_code_8.txt
```python
another_array = my_array[1:3]

```

