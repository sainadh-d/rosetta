# Sailors, coconuts and a monkey problem

## Task Link
[Rosetta Code - Sailors, coconuts and a monkey problem](https://rosettacode.org/wiki/Sailors,_coconuts_and_a_monkey_problem)

## Java Code
### java_code_1.txt
```java
public class Test {

    static boolean valid(int n, int nuts) {
        for (int k = n; k != 0; k--, nuts -= 1 + nuts / n)
            if (nuts % n != 1)
                return false;
        return nuts != 0 && (nuts % n == 0);
    }

    public static void main(String[] args) {
        int x = 0;
        for (int n = 2; n < 10; n++) {
            while (!valid(n, x))
                x++;
            System.out.printf("%d: %d%n", n, x);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def monkey_coconuts(sailors=5):
    "Parameterised the number of sailors using an inner loop including the last mornings case"    
    nuts = sailors
    while True:
        n0, wakes = nuts, []
        for sailor in range(sailors + 1):
            portion, remainder = divmod(n0, sailors)
            wakes.append((n0, portion, remainder))
            if portion <= 0 or remainder != (1 if sailor != sailors else 0):
                nuts += 1
                break
            n0 = n0 - portion - remainder
        else:
            break
    return nuts, wakes

if __name__ == "__main__":
    for sailors in [5, 6]:
        nuts, wake_stats = monkey_coconuts(sailors)
        print("\nFor %i sailors the initial nut count is %i" % (sailors, nuts))
        print("On each waking, the nut count, portion taken, and monkeys share are:\n ", 
              ',\n  '.join(repr(ws) for ws in wake_stats))

```

### python_code_2.txt
```python
def wake_and_split(n0, sailors, depth=None):
    if depth is None:
        depth = sailors
    portion, remainder = divmod(n0, sailors)
    if portion <= 0 or remainder != (1 if depth else 0):
        return None
    else:
        return n0 if not depth else wake_and_split(n0 - portion - remainder, sailors, depth - 1)
        
    
def monkey_coconuts(sailors=5):
    "Parameterised the number of sailors using recursion including the last mornings case"    
    nuts = sailors
    while True:
        if wake_and_split(n0=nuts, sailors=sailors) is None:
            nuts += 1
        else:
            break
    return nuts

if __name__ == "__main__":
    for sailors in [5, 6]:
        nuts = monkey_coconuts(sailors)
        print("For %i sailors the initial nut count is %i" % (sailors, nuts))

```

### python_code_3.txt
```python
# gives one solution of (x,y) for a x + by = c
def dioph(a, b, c):
	aa,bb,x,y = a, b, 0, 1

	while True:
		q,a,b = a//b, b, a%b
		x,y = y - q*x, x
		if abs(a) == 1: break

	if y*aa % bb != 1: y = -y
	x,y = y*c, (c - aa*y*c)//bb
	#assert(x*aa + y*bb == c)
	return x,y

# rems: what monkey got each turn
# min_share: each sailor needs to get at least this many in the final round
def calcnuts(rems, min_share = 0):
	n, r = len(rems) - 1, 0
	c = (n - 1)**n
	for x in rems: r,c = r + x*c, c//(n-1)*n

	a, b = (n-1)**n, n**(n+1)
	x, y = dioph(a, -b, r)
	k = (min_share - y + a - 1)//a
	return x + k*b, y + k*a

def distribute(nuts, monkey_nuts):
	n = len(monkey_nuts) - 1
	print("\n%d sailors, %d nuts:"%(n, nuts))
	for r in monkey_nuts[:-1]:
		p = (nuts - r)//n
		print("\tNuts %d, hide %d, monkey gets %d" % (nuts, p, r))
		nuts = p*(n - 1)

	r = monkey_nuts[-1]
	p = (nuts - r)//n
	print("Finally:\n\tNuts %d, each share %d, monkey gets %d" % (nuts, p, r))

for sailors in range(2, 10):
	monkey_loot = [1]*sailors + [0]
	distribute(calcnuts(monkey_loot, 1)[0], monkey_loot)

# many sailors, many nuts
#for i in range(1, 5): print(10**i, calcnuts([1]*10**i + [0])[0])

```

