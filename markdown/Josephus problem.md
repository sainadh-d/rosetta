# Josephus problem

## Task Link
[Rosetta Code - Josephus problem](https://rosettacode.org/wiki/Josephus_problem)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;

public class Josephus {
    public static int execute(int n, int k){
        int killIdx = 0;
        ArrayList<Integer> prisoners = new ArrayList<Integer>(n);
        for(int i = 0;i < n;i++){
            prisoners.add(i);
        }
        System.out.println("Prisoners executed in order:");
        while(prisoners.size() > 1){
            killIdx = (killIdx + k - 1) % prisoners.size();
            System.out.print(prisoners.get(killIdx) + " ");
            prisoners.remove(killIdx);
        }
        System.out.println();
        return prisoners.get(0);
    }
    
    public static ArrayList<Integer> executeAllButM(int n, int k, int m){
        int killIdx = 0;
        ArrayList<Integer> prisoners = new ArrayList<Integer>(n);
        for(int i = 0;i < n;i++){
            prisoners.add(i);
        }
        System.out.println("Prisoners executed in order:");
        while(prisoners.size() > m){
            killIdx = (killIdx + k - 1) % prisoners.size();
            System.out.print(prisoners.get(killIdx) + " ");
            prisoners.remove(killIdx);
        }
        System.out.println();
        return prisoners;
    }
    
    public static void main(String[] args){
        System.out.println("Survivor: " + execute(41, 3));
        System.out.println("Survivors: " + executeAllButM(41, 3, 3));
    }
}

```

### java_code_2.txt
```java
import java.util.ArrayList;
import java.util.List;

public class Josephus {

	public static void main(String[] args) {
		execute(5, 1);
		execute(41, 2);
		execute(23482, 3342, 3);
	}

	public static int[][] execute(int n, int k) {
		return execute(n, k, 1);
	}

	public static int[][] execute(int n, int k, int s) {
		List<Integer> ps = new ArrayList<Integer>(n);
		for (int i=0; i<n; i+=1) ps.add(i);
		List<Integer> ks = new ArrayList<Integer>(n-s);
		for (int i=k; ps.size()>s; i=(i+k)%ps.size()) ks.add(ps.remove(i));
		System.out.printf("Josephus(%d,%d,%d) -> %s / %s\n", n, k, s, toString(ps), toString(ks));
		return new int[][] {
			ps.stream().mapToInt(Integer::intValue).toArray(),
			ks.stream().mapToInt(Integer::intValue).toArray()
		};
	}
	
	private static String toString(List <Integer> ls) {
		String dot = "";
		if (ls.size() >= 45) {
			dot = ", ...";
			ls = ls.subList(0, 45);
		}
		String s = ls.toString();
		return s.substring(1, s.length()-1) + dot;
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> def j(n, k):
	p, i, seq = list(range(n)), 0, []
	while p:
		i = (i+k-1) % len(p)
		seq.append(p.pop(i))
	return 'Prisoner killing order: %s.\nSurvivor: %i' % (', '.join(str(i) for i in seq[:-1]), seq[-1])

>>> print(j(5, 2))
Prisoner killing order: 1, 3, 0, 4.
Survivor: 2
>>> print(j(41, 3))
Prisoner killing order: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 0, 4, 9, 13, 18, 22, 27, 31, 36, 40, 6, 12, 19, 25, 33, 39, 7, 16, 28, 37, 10, 24, 1, 21, 3, 34, 15.
Survivor: 30
>>>

```

### python_code_2.txt
```python
>>>def josephus(n, k):
        r = 0
        for i in xrange(1, n+1):
            r = (r+k)%i
        return 'Survivor: %d' %r

>>> print(josephus(5, 2))
Survivor: 2
>>> print(josephus(41, 3))
Survivor: 30
>>>

```

### python_code_3.txt
```python
def josephus(n, k):
    a = list(range(1, n + 1))
    a[n - 1] = 0
    p = 0
    v = []
    while a[p] != p:
        for i in range(k - 2):
            p = a[p]
        v.append(a[p])
        a[p] = a[a[p]]
        p = a[p]
    v.append(p)
    return v

josephus(10, 2)
[1, 3, 5, 7, 9, 2, 6, 0, 8, 4]

josephus(41, 3)[-1]
30

```

### python_code_4.txt
```python
from itertools import compress, cycle
def josephus(prisoner, kill, surviver):
    p = range(prisoner)
    k = [0] * kill
    k[kill-1] = 1
    s = [1] * kill
    s[kill -1] = 0
    queue = p
    
    queue = compress(queue, cycle(s))
    try:
        while True:
            p.append(queue.next())        
    except StopIteration:
        pass 

    kil=[]
    killed = compress(p, cycle(k))
    try:
        while True:
            kil.append(killed.next())
    except StopIteration:
        pass 
        
    print 'The surviver is: ', kil[-surviver:]
    print 'The kill sequence is ', kil[:prisoner-surviver]

josephus(41,3,2)
The surviver is:  [15, 30]
The kill sequence is  [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 0, 4, 9, 13, 18, 22, 27, 31, 36, 40, 6, 12, 19, 25, 33, 39, 7, 16, 28, 37, 10, 24, 1, 21, 3, 34]
josephus(5,2,1)
The surviver is:  [2]
The kill sequence is  [1, 3, 0, 4]

```

