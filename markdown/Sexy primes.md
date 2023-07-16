# Sexy primes

## Task Link
[Rosetta Code - Sexy primes](https://rosettacode.org/wiki/Sexy_primes)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class SexyPrimes {

    public static void main(String[] args) {
        sieve();
        int pairs = 0;
        List<String> pairList = new ArrayList<>();
        int triples = 0;
        List<String> tripleList = new ArrayList<>();
        int quadruplets = 0;
        List<String> quadrupletList = new ArrayList<>();
        int unsexyCount = 1;  //  2 (the even prime) not found in tests below.
        List<String> unsexyList = new ArrayList<>();
        for ( int i = 3 ; i < MAX ; i++ ) {
            if ( i-6 >= 3 && primes[i-6] && primes[i] ) {
                pairs++;
                pairList.add((i-6) + " " + i);
                if ( pairList.size() > 5 ) {
                    pairList.remove(0);
                }
            }
            else if ( i < MAX-2 && primes[i] && ! (i+6<MAX && primes[i] && primes[i+6])) {
                unsexyCount++;
                unsexyList.add("" + i);
                if ( unsexyList.size() > 10 ) {
                    unsexyList.remove(0);
                }
            }
            if ( i-12 >= 3 && primes[i-12] && primes[i-6] && primes[i] ) {
                triples++;
                tripleList.add((i-12) + " " + (i-6) + " " + i);
                if ( tripleList.size() > 5 ) {
                    tripleList.remove(0);
                }
            }
            if ( i-16 >= 3 && primes[i-18] && primes[i-12] && primes[i-6] && primes[i] ) {
                quadruplets++;
                quadrupletList.add((i-18) + " " + (i-12) + " " + (i-6) + " " + i);
                if ( quadrupletList.size() > 5 ) {
                    quadrupletList.remove(0);
                }
            }
        }
        System.out.printf("Count of sexy triples less than %,d = %,d%n", MAX, pairs);
        System.out.printf("The last 5 sexy pairs:%n  %s%n%n", pairList.toString().replaceAll(", ", "], ["));
        System.out.printf("Count of sexy triples less than %,d = %,d%n", MAX, triples);
        System.out.printf("The last 5 sexy triples:%n  %s%n%n", tripleList.toString().replaceAll(", ", "], ["));
        System.out.printf("Count of sexy quadruplets less than %,d = %,d%n", MAX, quadruplets);
        System.out.printf("The last 5 sexy quadruplets:%n  %s%n%n", quadrupletList.toString().replaceAll(", ", "], ["));
        System.out.printf("Count of unsexy primes less than %,d = %,d%n", MAX, unsexyCount);
        System.out.printf("The last 10 unsexy primes:%n  %s%n%n", unsexyList.toString().replaceAll(", ", "], ["));
    }

    private static int MAX = 1_000_035;
    private static boolean[] primes = new boolean[MAX];

    private static final void sieve() {
        //  primes
        for ( int i = 2 ; i < MAX ; i++ ) {
            primes[i] = true;            
        }
        for ( int i = 2 ; i < MAX ; i++ ) {
            if ( primes[i] ) {
                for ( int j = 2*i ; j < MAX ; j += i ) {
                    primes[j] = false;
                }
            }
        }
    }

}

```

## Python Code
### python_code_1.txt
```python
LIMIT = 1_000_035
def primes2(limit=LIMIT):
    if limit < 2: return []
    if limit < 3: return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]

primes = primes2(LIMIT +6)
primeset = set(primes)
primearray = [n in primeset for n in range(LIMIT)]

#%%
s = [[] for x in range(4)]
unsexy = []

for p in primes:
    if p > LIMIT:
        break
    if p + 6 in primeset and p + 6 < LIMIT:
        s[0].append((p, p+6))
    elif p + 6 in primeset:
        break
    else:
        if p - 6 not in primeset:
            unsexy.append(p)
        continue
    if p + 12 in primeset and p + 12 < LIMIT:
        s[1].append((p, p+6, p+12))
    else:
        continue
    if p + 18 in primeset and p + 18 < LIMIT:
        s[2].append((p, p+6, p+12, p+18))
    else:
        continue
    if p + 24 in primeset and p + 24 < LIMIT:
        s[3].append((p, p+6, p+12, p+18, p+24))

#%%
print('"SEXY" PRIME GROUPINGS:')
for sexy, name in zip(s, 'pairs triplets quadruplets quintuplets'.split()):
    print(f'  {len(sexy)} {na (not isPrime(n-6))))) |> Array.ofSeq
printfn "There are %d unsexy primes less than 1,000,035. The last 10 are:" n.Length
Array.skip (n.Length-10) n |> Array.iter(fun n->printf "%d " n); printfn ""
let ni=pCache |> Seq.takeWhile(fun n->nme} ending with ...')
    for sx in sexy[-5:]:
        print('   ',sx)

print(f'\nThere are {len(unsexy)} unsexy primes ending with ...')
for usx in unsexy[-10:]:
    print(' ',usx)

```

### python_code_2.txt
```python
#Functional Sexy Primes. Nigel Galloway: October 5th., 2018
from itertools import *
z=primes()
n=frozenset(takewhile(lambda x: x<1000035,z))
ni=sorted(list(filter(lambda g: n.__contains__(g+6) ,n)))
print ("There are",len(ni),"sexy prime pairs all components of which are less than 1,000,035. The last 5 are:")
for g in islice(ni,max(len(ni)-5,0),len(ni)): print(format("(%d,%d) " % (g,g+6)))
nig=list(filter(lambda g: n.__contains__(g+12) ,ni))
print ("There are",len(nig),"sexy prime triplets all components of which are less than 1,000,035. The last 5 are:")
for g in islice(nig,max(len(nig)-5,0),len(nig)): print(format("(%d,%d,%d) " % (g,g+6,g+12)))
nige=list(filter(lambda g: n.__contains__(g+18) ,nig))
print ("There are",len(nige),"sexy prime quadruplets all components of which are less than 1,000,035. The last 5 are:")
for g in islice(nige,max(len(nige)-5,0),len(nige)): print(format("(%d,%d,%d,%d) " % (g,g+6,g+12,g+18)))
nigel=list(filter(lambda g: n.__contains__(g+24) ,nige))
print ("There are",len(nigel),"sexy prime quintuplets all components of which are less than 1,000,035. The last 5 are:")
for g in islice(nigel,max(len(nigel)-5,0),len(nigel)): print(format("(%d,%d,%d,%d,%d) " % (g,g+6,g+12,g+18,g+24)))
un=frozenset(takewhile(lambda x: x<1000050,z)).union(n)
unsexy=sorted(list(filter(lambda g: not un.__contains__(g+6) and not un.__contains__(g-6),n)))
print ("There are",len(unsexy),"unsexy primes less than 1,000,035. The last 10 are:")
for g in islice(unsexy,max(len(unsexy)-10,0),len(unsexy)): print(g)

```

