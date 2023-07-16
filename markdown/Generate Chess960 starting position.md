# Generate Chess960 starting position

## Task Link
[Rosetta Code - Generate Chess960 starting position](https://rosettacode.org/wiki/Generate_Chess960_starting_position)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Chess960{
	private static List<Character> pieces = Arrays.asList('R','B','N','Q','K','N','B','R');

	public static List<Character> generateFirstRank(){
		do{
			Collections.shuffle(pieces);
		}while(!check(pieces.toString().replaceAll("[^\\p{Upper}]", ""))); //List.toString adds some human stuff, remove that 
		
		return pieces;
	}

	private static boolean check(String rank){
		if(!rank.matches(".*R.*K.*R.*")) return false;			//king between rooks
		if(!rank.matches(".*B(..|....|......|)B.*")) return false;	//all possible ways bishops can be placed
		return true;
	}

	public static void main(String[] args){
		for(int i = 0; i < 10; i++){
			System.out.println(generateFirstRank());
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> from itertools import permutations
>>> pieces = 'KQRrBbNN'
>>> starts = {''.join(p).upper() for p in permutations(pieces)
                     if p.index('B') % 2 != p.index('b') % 2 		# Bishop constraint
                     and ( p.index('r') < p.index('K') < p.index('R')	# King constraint	
                           or p.index('R') < p.index('K') < p.index('r') ) }
>>> len(starts)
960
>>> starts.pop()
'QNBRNKRB'
>>>

```

### python_code_2.txt
```python
>>> import re
>>> pieces = 'KQRRBBNN'
>>> bish = re.compile(r'B(|..|....|......)B').search
>>> king = re.compile(r'R.*K.*R').search
>>> starts3 = {p for p in (''.join(q) for q in permutations(pieces))
            if bish(p) and king(p)}
>>> len(starts3)
960
>>> starts3.pop()
'QRNKBNRB'
>>>

```

### python_code_3.txt
```python
from random import choice

def random960():
    start = ['R', 'K', 'R']         # Subsequent order unchanged by insertions.
    #
    for piece in ['Q', 'N', 'N']:
        start.insert(choice(range(len(start)+1)), piece)
    #
    bishpos = choice(range(len(start)+1))
    start.insert(bishpos, 'B')
    start.insert(choice(range(bishpos + 1, len(start) + 1, 2)), 'B')
    return start
    return ''.join(start).upper()

print(random960())

```

### python_code_4.txt
```python
from random import choice

def generate960():
    start = ('R', 'K', 'R')         # Subsequent order unchanged by insertions.

    # Insert QNN in all combinations of places
    starts = {start}
    for piece in ['Q', 'N', 'N']:
        starts2 = set()
        for s in starts:
            for pos in range(len(s)+1):
                s2 = list(s)
                s2.insert(pos, piece)
                starts2.add(tuple(s2))
        starts = starts2
    
    # For each of the previous starting positions insert the bishops in their 16 positions
    starts2 = set()
    for s in starts:
        for bishpos in range(len(s)+1):
            s2 = list(s)
            s2.insert(bishpos, 'B')
            for bishpos2 in range(bishpos+1, len(s)+2, 2):
                s3 = s2[::]
                s3.insert(bishpos2, 'B')
                starts2.add(tuple(s3))
                
    return  list(starts2)

gen = generate960()
print(''.join(choice(gen)))

```

