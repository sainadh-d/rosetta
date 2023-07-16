# Look-and-say sequence

## Task Link
[Rosetta Code - Look-and-say sequence](https://rosettacode.org/wiki/Look-and-say_sequence)

## Java Code
### java_code_1.txt
```java
public static String lookandsay(String number){
	StringBuilder result= new StringBuilder();

	char repeat= number.charAt(0);
	number= number.substring(1) + " ";
	int times= 1;

	for(char actual: number.toCharArray()){
		if(actual != repeat){
			result.append(times + "" + repeat);
			times= 1;
			repeat= actual;
		}else{
			times+= 1;
		}
	}
	return result.toString();
}

```

### java_code_2.txt
```java
public static void main(String[] args){
	String num = "1"; 
	 
	for (int i=1;i<=10;i++) {
		System.out.println(num);
		num = lookandsay(num);             
	}
}

```

## Python Code
### python_code_1.txt
```python
def lookandsay(number):
    result = ""

    repeat = number[0]
    number = number[1:]+" "
    times = 1

    for actual in number:
        if actual != repeat:
            result += str(times)+repeat
            times = 1
            repeat = actual
        else:
            times += 1

    return result

num = "1"

for i in range(10):
    print num
    num = lookandsay(num)

```

### python_code_2.txt
```python
>>> from itertools import groupby
>>> def lookandsay(number):
	return ''.join( str(len(list(g))) + k
		        for k,g in groupby(number) )

>>> numberstring='1'
>>> for i in range(10):
	print numberstring
	numberstring = lookandsay(numberstring)

```

### python_code_3.txt
```python
>>> from itertools import groupby, islice
>>> 
>>> def lookandsay(number='1'):
	while True:
		yield number
		number = ''.join( str(len(list(g))) + k
		                  for k,g in groupby(number) )

		
>>> print('\n'.join(islice(lookandsay(), 10)))
1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211

```

### python_code_4.txt
```python
import re

def lookandsay(str):
    return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), str)

num = "1"
for i in range(10):
    print num
    num = lookandsay(num)

```

