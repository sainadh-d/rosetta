# Enumerations

## Task Link
[Rosetta Code - Enumerations](https://rosettacode.org/wiki/Enumerations)

## Java Code
### java_code_1.txt
```java
enum Fruits{
   APPLE, BANANA, CHERRY
}

```

### java_code_2.txt
```java
enum Fruits{
  APPLE(0), BANANA(1), CHERRY(2)
  private final int value;
  fruits(int value) { this.value = value; }
  public int value() { return value; }
}

```

## Python Code
### python_code_1.txt
```python
>>> from enum import Enum
>>> Contact = Enum('Contact', 'FIRST_NAME, LAST_NAME, PHONE')
>>> Contact.__members__
mappingproxy(OrderedDict([('FIRST_NAME', <Contact.FIRST_NAME: 1>), ('LAST_NAME', <Contact.LAST_NAME: 2>), ('PHONE', <Contact.PHONE: 3>)]))
>>> 
>>> # Explicit
>>> class Contact2(Enum):
	FIRST_NAME = 1
	LAST_NAME = 2
	PHONE = 3

	
>>> Contact2.__members__
mappingproxy(OrderedDict([('FIRST_NAME', <Contact2.FIRST_NAME: 1>), ('LAST_NAME', <Contact2.LAST_NAME: 2>), ('PHONE', <Contact2.PHONE: 3>)]))
>>>

```

### python_code_2.txt
```python
FIRST_NAME, LAST_NAME, PHONE = range(3)

```

### python_code_3.txt
```python
vars().update((key,val) for val,key in enumerate(("FIRST_NAME","LAST_NAME","PHONE")))

```

