# Hash from two arrays

## Task Link
[Rosetta Code - Hash from two arrays](https://rosettacode.org/wiki/Hash_from_two_arrays)

## Java Code
### java_code_1.txt
```java
import java.util.HashMap;
public static void main(String[] args){
	String[] keys= {"a", "b", "c"};
	int[] vals= {1, 2, 3};
	HashMap<String, Integer> hash= new HashMap<String, Integer>();

	for(int i= 0; i < keys.length; i++){
	   hash.put(keys[i], vals[i]);
	}
}

```

## Python Code
### python_code_1.txt
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
hash = {key: value for key, value in zip(keys, values)}

```

### python_code_2.txt
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
hash = dict(zip(keys, values))

# Lazily, Python 2.3+, not 3.x:
from itertools import izip
hash = dict(izip(keys, values))

```

### python_code_3.txt
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
hash = {}
for k,v in zip(keys, values):
    hash[k] = v

```

### python_code_4.txt
```python
>>> class Hashable(object):
	def __hash__(self):
		return id(self) ^ 0xBEEF

	
>>> my_inst = Hashable()
>>> my_int = 1
>>> my_complex = 0 + 1j
>>> my_float = 1.2
>>> my_string = "Spam"
>>> my_bool = True
>>> my_unicode = u'Ham'
>>> my_list = ['a', 7]
>>> my_tuple = ( 0.0, 1.4 )
>>> my_set = set(my_list)
>>> def my_func():
	pass

>>> class my_class(object):
	pass

>>> keys = [my_inst, my_tuple, my_int, my_complex, my_float, my_string,
	my_bool, my_unicode, frozenset(my_set), tuple(my_list),
	my_func, my_class]
>>> values = range(12)
>>> d = dict(zip(keys, values))
>>> for key, value in d.items(): print key, ":", value

1 : 6
1j : 3
Ham : 7
Spam : 5
(0.0, 1.3999999999999999) : 1
frozenset(['a', 7]) : 8
1.2 : 4
('a', 7) : 9
<function my_func at 0x0128E7B0> : 10
<class '__main__.my_class'> : 11
<__main__.Hashable object at 0x012AFC50> : 0
>>> # Notice that the key "True" disappeared, and its value got associated with the key "1"
>>> # This is because 1 == True in Python, and dictionaries cannot have two equal keys

```

