# Hofstadter Q sequence

## Task Link
[Rosetta Code - Hofstadter Q sequence](https://rosettacode.org/wiki/Hofstadter_Q_sequence)

## Java Code
### java_code_1.txt
```java
import java.util.HashMap;
import java.util.Map;

public class HofQ {
	private static Map<Integer, Integer> q = new HashMap<Integer, Integer>(){{
		put(1, 1);
		put(2, 1);
	}};
	
	private static int[] nUses = new int[100001];//not part of the task
	
	public static int Q(int n){
		nUses[n]++;//not part of the task
		if(q.containsKey(n)){
			return q.get(n);
		}
		int ans = Q(n - Q(n - 1)) + Q(n - Q(n - 2));
		q.put(n, ans);
		return ans;
	}
	
	public static void main(String[] args){
		for(int i = 1; i <= 10; i++){
			System.out.println("Q(" + i + ") = " + Q(i));
		}
		int last = 6;//value for Q(10)
		int count = 0;
		for(int i = 11; i <= 100000; i++){
			int curr = Q(i);
			if(curr < last) count++;
			last = curr;
			if(i == 1000) System.out.println("Q(1000) = " + curr);
		}
		System.out.println("Q(i) is less than Q(i-1) for i <= 100000 " + count + " times");
		
		//Optional stuff below here
		int maxUses = 0, maxN = 0;
		for(int i = 1; i<nUses.length;i++){
			if(nUses[i] > maxUses){
				maxUses = nUses[i];
				maxN = i;
			}
		}
		System.out.println("Q(" + maxN + ") was called the most with " + maxUses + " calls");
	}
}

```

## Python Code
### python_code_1.txt
```python
def q(n):
    if n < 1 or type(n) != int: raise ValueError("n must be an int >= 1")
    try:
        return q.seq[n]
    except IndexError:
        ans = q(n - q(n - 1)) + q(n - q(n - 2))
        q.seq.append(ans)
        return ans
q.seq = [None, 1, 1]

if __name__ == '__main__':
    first10 = [q(i) for i in range(1,11)]
    assert first10 == [1, 1, 2, 3, 3, 4, 5, 5, 6, 6], "Q() value error(s)"
    print("Q(n) for n = [1..10] is:", ', '.join(str(i) for i in first10))
    assert q(1000) == 502, "Q(1000) value error"
    print("Q(1000) =", q(1000))

```

### python_code_2.txt
```python
from sys import getrecursionlimit

def q1(n):
    if n < 1 or type(n) != int: raise ValueError("n must be an int >= 1")
    try:
        return q.seq[n]
    except IndexError:
        len_q, rlimit = len(q.seq), getrecursionlimit()
        if (n - len_q) > (rlimit // 5):
            for i in range(len_q, n, rlimit // 5):
                q(i)
        ans = q(n - q(n - 1)) + q(n - q(n - 2))
        q.seq.append(ans)
        return ans

if __name__ == '__main__':
    tmp = q1(100000)
    print("Q(i+1) < Q(i) for i [1..100000] is true %i times." %
          sum(k1 < k0 for k0, k1 in zip(q.seq[1:], q.seq[2:])))

```

### python_code_3.txt
```python
def q(n):
    l = len(q.seq)
    while l <= n:
        q.seq.append(q.seq[l - q.seq[l - 1]] + q.seq[l - q.seq[l - 2]])
	l += 1
    return q.seq[n]
q.seq = [None, 1, 1]

print("Q(n) for n = [1..10] is:", [q(i) for i in range(1, 11)])
print("Q(1000) =", q(1000))
q(100000)
print("Q(i+1) < Q(i) for i [1..100000] is true %i times." %
      sum([q.seq[i] > q.seq[i + 1] for i in range(1, 100000)]))

```

