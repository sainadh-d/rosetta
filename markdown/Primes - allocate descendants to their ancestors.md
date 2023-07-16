# Primes - allocate descendants to their ancestors

## Task Link
[Rosetta Code - Primes - allocate descendants to their ancestors](https://rosettacode.org/wiki/Primes_-_allocate_descendants_to_their_ancestors)

## Java Code
### java_code_1.txt
```java
import java.io.*;
import java.util.*;

public class PrimeDescendants {
    public static void main(String[] args) {
        try (Writer writer = new BufferedWriter(new OutputStreamWriter(System.out))) {
            printPrimeDesc(writer, 100);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    private static void printPrimeDesc(Writer writer, int limit) throws IOException {
        List<Long> primes = findPrimes(limit);

        List<Long> ancestor = new ArrayList<>(limit);
        List<List<Long>> descendants = new ArrayList<>(limit);
        for (int i = 0; i < limit; ++i) {
            ancestor.add(Long.valueOf(0));
            descendants.add(new ArrayList<Long>());
        }

        for (Long prime : primes) {
            int p = prime.intValue();
            descendants.get(p).add(prime);
            for (int i = 0; i + p < limit; ++i) {
                int s = i + p;
                for (Long n : descendants.get(i)) {
                    Long prod = n * p;
                    descendants.get(s).add(prod);
                    if (prod < limit)
                        ancestor.set(prod.intValue(), Long.valueOf(s));
                }
            }
        }

        // print the results
        int totalDescendants = 0;
        for (int i = 1; i < limit; ++i) {
            List<Long> ancestors = getAncestors(ancestor, i);
            writer.write("[" + i + "] Level: " + ancestors.size() + "\n");
            writer.write("Ancestors: ");
            Collections.sort(ancestors);
            print(writer, ancestors);

            writer.write("Descendants: ");
            List<Long> desc = descendants.get(i);
            if (!desc.isEmpty()) {
                Collections.sort(desc);
                if (desc.get(0) == i)
                    desc.remove(0);
            }
            writer.write(desc.size() + "\n");
            totalDescendants += desc.size();
            if (!desc.isEmpty())
                print(writer, desc);
            writer.write("\n");
        }
        writer.write("Total descendants: " + totalDescendants + "\n");
    }

    // find the prime numbers up to limit
    private static List<Long> findPrimes(int limit) {
        boolean[] isprime = new boolean[limit];
        Arrays.fill(isprime, true);
        isprime[0] = isprime[1] = false;
        for (int p = 2; p * p < limit; ++p) {
            if (isprime[p]) {
                for (int i = p * p; i < limit; i += p)
                    isprime[i] = false;
            }
        }
        List<Long> primes = new ArrayList<>();
        for (int p = 2; p < limit; ++p) {
            if (isprime[p])
                primes.add(Long.valueOf(p));
        }
        return primes;
    }

    // returns all ancestors of n. n is not its own ancestor.
    private static List<Long> getAncestors(List<Long> ancestor, int n) {
        List<Long> result = new ArrayList<>();
        for (Long a = ancestor.get(n); a != 0 && a != n; ) {
            n = a.intValue();
            a = ancestor.get(n);
            result.add(Long.valueOf(n));
        }
        return result;
    }

    private static void print(Writer writer, List<Long> list) throws IOException {
        if (list.isEmpty()) {
            writer.write("none\n");
            return;
        }
        int i = 0;
        writer.write(String.valueOf(list.get(i++)));
        for (; i != list.size(); ++i)
            writer.write(", " + list.get(i));
        writer.write("\n");
    }
}

```

### java_code_2.txt
```java
import static java.lang.Math.sqrt;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PrimeAncestorsDescendants {

	public static void main(String[] args) {
		print(100);
	}

	public static void print(int limit) {
		print(get(limit));
	}

	record PAD (int limit, List<List<Integer>> ancestors, List<List<Long>> descendants, int totalDescendants) {}

	public static PAD get(int limit) {
		List<List<Integer>> ancestors = new ArrayList<>(limit);
		List<List<Long>> descendants = new ArrayList<>(limit);
		for (int i=0; i<limit; i+=1) {
			ancestors.add(new ArrayList<>());
			descendants.add(new ArrayList<>());
		}
		
		List<Integer> primes = primesBelow(limit);
		for (int p: primes) {
			descendants.get(p).add((long) p);
			for (int i=0, s=p; s<limit; s+=1, i+=1) {
				for (long d: descendants.get(i)) {
					descendants.get(s).add(p*d);
				}
			}
		}
		
		descendants.get(4).remove(0);
		for (int p: primes) removeLast(descendants.get(p));
		
		int totalDescendants = 0;
		for (int i=1; i<limit; i+=1) {
			List<Long> desc = sort(descendants.get(i));
			totalDescendants += desc.size();
			for (long d: desc) {
				if (d >= limit) break;
				ancestors.set((int) d, add(ancestors.get(i), i));
			}
		}
		
		return new PAD(limit, ancestors, descendants, totalDescendants);
	}

	private static List<Integer> primesBelow(int limit) {
		List<Integer> primes = new ArrayList<>();
		boolean[] isComposite = new boolean[limit];
		//int p=2; for (; p*p<limit; p+=1) {
		int p=2; for (int sr=(int) sqrt(limit); p<sr; p+=1) {
			if (isComposite[p]) continue;
			primes.add(p);
			for (int i=p*p; i<limit; i+=p) isComposite[i] = true;
		}
		for (; p<limit; p+=1) {
			if (isComposite[p]) continue;
			primes.add(p);
		}
		return primes;
	}

	private static List<Long> removeLast(List<Long> list) {
		int size = list.size();
		if (size > 0) list.remove(size-1);
		return list;
	}
	
	private static <T extends Comparable<? super T>> List<T> sort(List<T> list) {
		Collections.sort(list);
		return list;
	}

	private static List<Integer> add(List<Integer> list, int n) {
		list = new ArrayList<>(list);
		list.add(n);
		return list;
	}
	
	public static void print(PAD pad) {
		for (int i=1; i<pad.limit; i+=1) {
			if (i > 20 && i != 46 && i != 74 && i != 94 && i != 99)	continue;
			System.out.printf("%2d:", i);
			printf(" %,d ancestors %-17s", pad.ancestors.get(i));
			printf(" %,6d descendants %s\n", pad.descendants.get(i));
		}
		System.out.printf("\nTotal descendants: %,d\n",  pad.totalDescendants);
	}
	
	private static <T extends Number> void printf(String fmt, List<T> list) {
		System.out.printf(fmt, list.size(), format(list));
	}
	
	private static <T extends Number> String format(List<T> list) {
		if (list.isEmpty()) return "";
		StringBuilder sb = new StringBuilder("[");
		if (list.size() <= 10) {
			for (int i=0; i<list.size(); i+=1) sb.append(format(list, i));
		}
		else {
			for (int i=0; i<5; i+=1) sb.append(format(list, i));
			sb.append(", ...");
			for (int i=list.size()-3; i<list.size(); i+=1) sb.append(format(list, i));
		}
		return sb.append("]").toString();
	}

	private static <T extends Number> String format(List<T> list, int i) {
		return (i==0 ? "" : ", ") + String.format("%,d", list.get(i).longValue());
	}
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function
from itertools import takewhile

maxsum = 99

def get_primes(max):
    if max < 2:
        return []
    lprimes = [2]
    for x in range(3, max + 1, 2):
        for p in lprimes:
            if x % p == 0:
                break
        else:
            lprimes.append(x)
    return lprimes

descendants = [[] for _ in range(maxsum + 1)]
ancestors = [[] for _ in range(maxsum + 1)]

primes = get_primes(maxsum)

for p in primes:
    descendants[p].append(p)
    for s in range(1, len(descendants) - p):
        descendants[s + p] += [p * pr for pr in descendants[s]]

for p in primes + [4]:
    descendants[p].pop()

total = 0
for s in range(1, maxsum + 1):
    descendants[s].sort()
    for d in takewhile(lambda x: x <= maxsum, descendants[s]):
        ancestors[d] = ancestors[s] + [s]
    print([s], "Level:", len(ancestors[s]))
    print("Ancestors:", ancestors[s] if len(ancestors[s]) else "None")
    print("Descendants:", len(descendants[s]) if len(descendants[s]) else "None")
    if len(descendants[s]):
        print(descendants[s])
    print()
    total += len(descendants[s])

print("Total descendants", total)

```

