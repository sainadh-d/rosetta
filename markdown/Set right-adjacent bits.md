# Set right-adjacent bits

## Task Link
[Rosetta Code - Set right-adjacent bits](https://rosettacode.org/wiki/Set_right-adjacent_bits)

## Java Code
### java_code_1.txt
```java
public final class SetRightAdjacentBits {

	public static void main(String[] aArgs) {
		setRightAdjacent("1000", 2);
		setRightAdjacent("0100", 2);
		setRightAdjacent("0010", 2);
		setRightAdjacent("0000", 2);
		
		String test = "010000000000100000000010000000010000000100000010000010000100010010";
		setRightAdjacent(test, 0);
		setRightAdjacent(test, 1);
		setRightAdjacent(test, 2);
		setRightAdjacent(test, 3);
	}	
	
	private static void setRightAdjacent(String aText, int aNumber) {
		System.out.println("n = " + aNumber + ", Width = " + aText.length() + ", Input: " + aText);	
		
		char[] text = aText.toCharArray();
		char[] result = aText.toCharArray();
	    for ( int i = 0; i < result.length; i++ ) {
	    	if ( text[i] == '1' ) {	    		
	    		for ( int j = i + 1; j <= i + aNumber && j < result.length; j++ ) {
	    			result[j] = '1';
	    		}
	    	}
	    }
	    
	    String spaces = " ".repeat(16 + String.valueOf(aText.length()).length());
		System.out.println(spaces + "Result: " + new String(result) + System.lineSeparator());
	}

}

```

## Python Code
### python_code_1.txt
```python
from operator import or_
from functools import reduce

def set_right_adjacent_bits(n: int, b: int) -> int:
    return reduce(or_, (b >> x for x in range(n+1)), 0)


if __name__ == "__main__":
    print("SAME n & Width.\n")
    n = 2  # bits to the right of set bits, to also set
    bits = "1000 0100 0010 0000"
    first = True
    for b_str in bits.split():
        b = int(b_str, 2)
        e = len(b_str)
        if first:
            first = False
            print(f"n = {n}; Width e = {e}:\n")
        result = set_right_adjacent_bits(n, b)
        print(f"     Input b: {b:0{e}b}")
        print(f"      Result: {result:0{e}b}\n")
        
    print("SAME Input & Width.\n")
    #bits = "01000010001001010110"
    bits = '01' + '1'.join('0'*x for x in range(10, 0, -1))
    for n in range(4):
        first = True
        for b_str in bits.split():
            b = int(b_str, 2)
            e = len(b_str)
            if first:
                first = False
                print(f"n = {n}; Width e = {e}:\n")
            result = set_right_adjacent_bits(n, b)
            print(f"     Input b: {b:0{e}b}")
            print(f"      Result: {result:0{e}b}\n")

```

### python_code_2.txt
```python
from typing import List


def set_right_adjacent_bits_list(n: int, b: List[int]) -> List[int]:
    #   [0]*x is padding b on the left.
    #   zip(*(list1, list2,..)) returns the n'th elements on list1, list2,...
    #   int(any(...)) or's them.
    return [int(any(shifts))
            for shifts in zip(*([0]*x + b for x in range(n+1)))]

def _list2bin(b: List[int]) -> str:
    "List of 0/1 ints to bool string."
    return ''.join(str(x) for x in b)

def _to_list(bits: str) -> List[int]:
    return [int(char) for char in bits]

if __name__ == "__main__":
    print("SAME n & Width.\n")
    n = 2  # bits to the right of set bits, to also set
    bits = "1000 0100 0010 0000"
    first = True
    for b_str in bits.split():
        b = _to_list(b_str)
        e = len(b_str)
        if first:
            first = False
            print(f"n = {n}; Width e = {e}:\n")
        result = set_right_adjacent_bits_list(n, b)
        print(f"     Input b: {_list2bin(b)}")
        print(f"      Result: {_list2bin(result)}\n")
        
    print("SAME Input & Width.\n")
    #bits = "01000010001001010110"
    bits = '01' + '1'.join('0'*x for x in range(10, 0, -1))
    for n in range(4):
        first = True
        for b_str in bits.split():
            b = _to_list(b_str)
            e = len(b_str)
            if first:
                first = False
                print(f"n = {n}; Width e = {e}:\n")
                result = set_right_adjacent_bits_list(n, b)
            print(f"     Input b: {_list2bin(b)}")
            print(f"      Result: {_list2bin(result)}\n")

```

