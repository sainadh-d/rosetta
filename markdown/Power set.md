# Power set

## Task Link
[Rosetta Code - Power set](https://rosettacode.org/wiki/Power_set)

## Java Code
### java_code_1.txt
```java
public static ArrayList<String> getpowerset(int a[],int n,ArrayList<String> ps)
    {
        if(n<0)
        {
            return null;
        }
        if(n==0)
        {
            if(ps==null)
                ps=new ArrayList<String>();
            ps.add(" ");
            return ps;
        }
        ps=getpowerset(a, n-1, ps);
        ArrayList<String> tmp=new ArrayList<String>();
        for(String s:ps)
        {
            if(s.equals(" "))
                tmp.add(""+a[n-1]);
            else
                tmp.add(s+a[n-1]);
        }
        ps.addAll(tmp);
        return ps;
    }

```

### java_code_2.txt
```java
public static <T> List<List<T>> powerset(Collection<T> list) {
  List<List<T>> ps = new ArrayList<List<T>>();
  ps.add(new ArrayList<T>());   // add the empty set

  // for every item in the original list
  for (T item : list) {
    List<List<T>> newPs = new ArrayList<List<T>>();

    for (List<T> subset : ps) {
      // copy all of the current powerset's subsets
      newPs.add(subset);

      // plus the subsets appended with the current item
      List<T> newSubset = new ArrayList<T>(subset);
      newSubset.add(item);
      newPs.add(newSubset);
    }

    // powerset is now powerset of list.subList(0, list.indexOf(item)+1)
    ps = newPs;
  }
  return ps;
}

```

### java_code_3.txt
```java
public static <T extends Comparable<? super T>> LinkedList<LinkedList<T>> BinPowSet(
		LinkedList<T> A){
	LinkedList<LinkedList<T>> ans= new LinkedList<LinkedList<T>>();
	int ansSize = (int)Math.pow(2, A.size());
	for(int i= 0;i< ansSize;++i){
		String bin= Integer.toBinaryString(i); //convert to binary
		while(bin.length() < A.size()) bin = "0" + bin; //pad with 0's
		LinkedList<T> thisComb = new LinkedList<T>(); //place to put one combination
		for(int j= 0;j< A.size();++j){
			if(bin.charAt(j) == '1')thisComb.add(A.get(j));
		}
		Collections.sort(thisComb); //sort it for easy checking
		ans.add(thisComb); //put this set in the answer list
	}
	return ans;
}

```

## Python Code
### python_code_1.txt
```python
def list_powerset(lst):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in lst:
        # for every additional element in our set
        # the power set consists of the subsets that don't
        # contain this element (just take the previous power set)
        # plus the subsets that do contain the element (use list
        # comprehension to add [x] onto everything in the
        # previous power set)
        result.extend([subset + [x] for subset in result])
    return result

# the above function in one statement
def list_powerset2(lst):
    return reduce(lambda result, x: result + [subset + [x] for subset in result],
                  lst, [[]])

def powerset(s):
    return frozenset(map(frozenset, list_powerset(list(s))))

```

### python_code_2.txt
```python
def powersetlist(s):
    r = [[]]
    for e in s:
        print "r: %-55r e: %r" % (r,e)
        r += [x+[e] for x in r]
    return r

s= [0,1,2,3]    
print "\npowersetlist(%r) =\n  %r" % (s, powersetlist(s))

```

### python_code_3.txt
```python
def powersequence(val):
    ''' Generate a 'powerset' for sequence types that are indexable by integers.
        Uses a binary count to enumerate the members and returns a list

        Examples:
            >>> powersequence('STR')   # String
            ['', 'S', 'T', 'ST', 'R', 'SR', 'TR', 'STR']
            >>> powersequence([0,1,2]) # List
            [[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2]]
            >>> powersequence((3,4,5)) # Tuple
            [(), (3,), (4,), (3, 4), (5,), (3, 5), (4, 5), (3, 4, 5)]
            >>> 
    '''
    vtype = type(val); vlen = len(val); vrange = range(vlen)
    return [ reduce( lambda x,y: x+y, (val[i:i+1] for i in vrange if 2**i & n), vtype())
             for n in range(2**vlen) ]

def powerset(s):
    ''' Generate the powerset of s

        Example:
            >>> powerset(set([6,7,8]))
            set([frozenset([7]), frozenset([8, 6, 7]), frozenset([6]), frozenset([6, 7]), frozenset([]), frozenset([8]), frozenset([8, 7]), frozenset([8, 6])])
    '''
    return set( frozenset(x) for x in powersequence(list(s)) )

```

### python_code_4.txt
```python
def p(l):
    if not l: return [[]]
    return p(l[1:]) + [[l[0]] + x for x in p(l[1:])]

```

### python_code_5.txt
```python
>>> from pprint import pprint as pp
>>> from itertools import chain, combinations
>>> 
>>> def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

>>> pp(set(powerset({1,2,3,4})))
{(),
 (1,),
 (1, 2),
 (1, 2, 3),
 (1, 2, 3, 4),
 (1, 2, 4),
 (1, 3),
 (1, 3, 4),
 (1, 4),
 (2,),
 (2, 3),
 (2, 3, 4),
 (2, 4),
 (3,),
 (3, 4),
 (4,)}
>>>

```

