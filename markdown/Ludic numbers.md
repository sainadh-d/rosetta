# Ludic numbers

## Task Link
[Rosetta Code - Ludic numbers](https://rosettacode.org/wiki/Ludic_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class Ludic{
	public static List<Integer> ludicUpTo(int n){
		List<Integer> ludics = new ArrayList<Integer>(n);
		for(int i = 1; i <= n; i++){   //fill the initial list
			ludics.add(i);
		}
		
		//start at index 1 because the first ludic number is 1 and we don't remove anything for it
		for(int cursor = 1; cursor < ludics.size(); cursor++){
			int thisLudic = ludics.get(cursor); //the first item in the list is a ludic number
			int removeCursor = cursor + thisLudic; //start removing that many items later
			while(removeCursor < ludics.size()){
				ludics.remove(removeCursor);		     //remove the next item
				removeCursor = removeCursor + thisLudic - 1; //move the removal cursor up as many spaces as we need to
									     //then back one to make up for the item we just removed
			}
		}
		return ludics;
	}
	
	public static List<List<Integer>> getTriplets(List<Integer> ludics){
		List<List<Integer>> triplets = new ArrayList<List<Integer>>();
		for(int i = 0; i < ludics.size() - 2; i++){ //only need to check up to the third to last item
			int thisLudic = ludics.get(i);
			if(ludics.contains(thisLudic + 2) && ludics.contains(thisLudic + 6)){
				List<Integer> triplet = new ArrayList<Integer>(3);
				triplet.add(thisLudic);
				triplet.add(thisLudic + 2);
				triplet.add(thisLudic + 6);
				triplets.add(triplet);
			}
		}
		return triplets;
	}
	
	public static void main(String[] srgs){
		System.out.println("First 25 Ludics: " + ludicUpTo(110));				//110 will get us 25 numbers
		System.out.println("Ludics up to 1000: " + ludicUpTo(1000).size());
		System.out.println("2000th - 2005th Ludics: " + ludicUpTo(22000).subList(1999, 2005));  //22000 will get us 2005 numbers
		System.out.println("Triplets up to 250: " + getTriplets(ludicUpTo(250)));
	}
}

```

## Python Code
### python_code_1.txt
```python
def ludic(nmax=100000):
    yield 1
    lst = list(range(2, nmax + 1))
    while lst:
        yield lst[0]
        del lst[::lst[0]]

ludics = [l for l in ludic()]

print('First 25 ludic primes:')
print(ludics[:25])
print("\nThere are %i ludic numbers <= 1000"
      % sum(1 for l in ludics if l <= 1000)) 
print("\n2000'th..2005'th ludic primes:")
print(ludics[2000-1: 2005])

n = 250
triplets = [(x, x+2, x+6)
            for x in ludics
            if x+6 < n and x+2 in ludics and x+6 in ludics]
print('\nThere are %i triplets less than %i:\n  %r'
      % (len(triplets), n, triplets))

```

### python_code_2.txt
```python
def ludic(nmax=64):
    yield 1
    taken = []
    while True:
        lst, nmax = list(range(2, nmax + 1)), nmax * 2
        for t in taken:
            del lst[::t]
        while lst:
            t = lst[0]
            taken.append(t)
            yield t
            del lst[::t]

```

### python_code_3.txt
```python
def ludic():
    yield 1
    ludics = []
    while True:
        k = 0 
        for j in reversed(ludics):
            k = (k*j)//(j-1) + 1
        ludics.append(k+2) 
        yield k+2
def triplets():
    a, b, c, d = 0, 0, 0, 0
    for k in ludic():
        if k-4 in (b, c, d) and k-6 in (a, b, c):
            yield k-6, k-4, k
        a, b, c, d = b, c, d, k

first_25 = [k for i, k in zip(range(25), gen_ludic())]
print(f'First 25 ludic numbers: {first_25}')
count = 0
for k in gen_ludic():
    if k > 1000:
        break
    count += 1
print(f'Number of ludic numbers <= 1000: {count}')
it = iter(gen_ludic())
for i in range(1999):
    next(it)
ludic2000 = [next(it) for i in range(6)]
print(f'Ludic numbers 2000..2005: {ludic2000}')    
   
print('Ludic triplets < 250:')
for a, b, c in triplets():
    if c >= 250:
        break
    print(f'[{a}, {b}, {c}]')

```

