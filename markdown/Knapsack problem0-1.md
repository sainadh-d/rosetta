# Knapsack problem/0-1

## Task Link
[Rosetta Code - Knapsack problem/0-1](https://rosettacode.org/wiki/Knapsack_problem/0-1)

## Java Code
### java_code_1.txt
```java
package hu.pj.alg.test;

import hu.pj.alg.ZeroOneKnapsack;
import hu.pj.obj.Item;
import java.util.*;
import java.text.*;

public class ZeroOneKnapsackForTourists {

    public ZeroOneKnapsackForTourists() {
        ZeroOneKnapsack zok = new ZeroOneKnapsack(400); // 400 dkg = 400 dag = 4 kg

        // making the list of items that you want to bring
        zok.add("map", 9, 150);
        zok.add("compass", 13, 35);
        zok.add("water", 153, 200);
        zok.add("sandwich", 50, 160);
        zok.add("glucose", 15, 60);
        zok.add("tin", 68, 45);
        zok.add("banana", 27, 60);
        zok.add("apple", 39, 40);
        zok.add("cheese", 23, 30);
        zok.add("beer", 52, 10);
        zok.add("suntan cream", 11, 70);
        zok.add("camera", 32, 30);
        zok.add("t-shirt", 24, 15);
        zok.add("trousers", 48, 10);
        zok.add("umbrella", 73, 40);
        zok.add("waterproof trousers", 42, 70);
        zok.add("waterproof overclothes", 43, 75);
        zok.add("note-case", 22, 80);
        zok.add("sunglasses", 7, 20);
        zok.add("towel", 18, 12);
        zok.add("socks", 4, 50);
        zok.add("book", 30, 10);

        // calculate the solution:
        List<Item> itemList = zok.calcSolution();

        // write out the solution in the standard output
        if (zok.isCalculated()) {
            NumberFormat nf  = NumberFormat.getInstance();

            System.out.println(
                "Maximal weight           = " +
                nf.format(zok.getMaxWeight() / 100.0) + " kg"
            );
            System.out.println(
                "Total weight of solution = " +
                nf.format(zok.getSolutionWeight() / 100.0) + " kg"
            );
            System.out.println(
                "Total value              = " +
                zok.getProfit()
            );
            System.out.println();
            System.out.println(
                "You can carry the following materials " +
                "in the knapsack:"
            );
            for (Item item : itemList) {
                if (item.getInKnapsack() == 1) {
                    System.out.format(
                        "%1$-23s %2$-3s %3$-5s %4$-15s \n",
                        item.getName(),
                        item.getWeight(), "dag  ",
                        "(value = " + item.getValue() + ")"
                    );
                }
            }
        } else {
            System.out.println(
                "The problem is not solved. " +
                "Maybe you gave wrong data."
            );
        }

    }

    public static void main(String[] args) {
        new ZeroOneKnapsackForTourists();
    }

} // class

```

### java_code_2.txt
```java
package hu.pj.alg;

import hu.pj.obj.Item;
import java.util.*;

public class ZeroOneKnapsack {

    protected List<Item> itemList  = new ArrayList<Item>();
    protected int maxWeight        = 0;
    protected int solutionWeight   = 0;
    protected int profit           = 0;
    protected boolean calculated   = false;

    public ZeroOneKnapsack() {}

    public ZeroOneKnapsack(int _maxWeight) {
        setMaxWeight(_maxWeight);
    }

    public ZeroOneKnapsack(List<Item> _itemList) {
        setItemList(_itemList);
    }

    public ZeroOneKnapsack(List<Item> _itemList, int _maxWeight) {
        setItemList(_itemList);
        setMaxWeight(_maxWeight);
    }

    // calculte the solution of 0-1 knapsack problem with dynamic method:
    public List<Item> calcSolution() {
        int n = itemList.size();

        setInitialStateForCalculation();
        if (n > 0  &&  maxWeight > 0) {
            List< List<Integer> > c = new ArrayList< List<Integer> >();
            List<Integer> curr = new ArrayList<Integer>();

            c.add(curr);
            for (int j = 0; j <= maxWeight; j++)
                curr.add(0);
            for (int i = 1; i <= n; i++) {
                List<Integer> prev = curr;
                c.add(curr = new ArrayList<Integer>());
                for (int j = 0; j <= maxWeight; j++) {
                    if (j > 0) {
                        int wH = itemList.get(i-1).getWeight();
                        curr.add(
                            (wH > j)
                            ?
                            prev.get(j)
                            :
                            Math.max(
                                prev.get(j),
                                itemList.get(i-1).getValue() + prev.get(j-wH)
                            )
                        );
                    } else {
                        curr.add(0);
                    }
                } // for (j...)
            } // for (i...)
            profit = curr.get(maxWeight);

            for (int i = n, j = maxWeight; i > 0  &&  j >= 0; i--) {
                int tempI   = c.get(i).get(j);
                int tempI_1 = c.get(i-1).get(j);
                if (
                    (i == 0  &&  tempI > 0)
                    ||
                    (i > 0  &&  tempI != tempI_1)
                )
                {
                    Item iH = itemList.get(i-1);
                    int  wH = iH.getWeight();
                    iH.setInKnapsack(1);
                    j -= wH;
                    solutionWeight += wH;
                }
            } // for()
            calculated = true;
        } // if()
        return itemList;
    }

    // add an item to the item list
    public void add(String name, int weight, int value) {
        if (name.equals(""))
            name = "" + (itemList.size() + 1);
        itemList.add(new Item(name, weight, value));
        setInitialStateForCalculation();
    }

    // add an item to the item list
    public void add(int weight, int value) {
        add("", weight, value); // the name will be "itemList.size() + 1"!
    }

    // remove an item from the item list
    public void remove(String name) {
        for (Iterator<Item> it = itemList.iterator(); it.hasNext(); ) {
            if (name.equals(it.next().getName())) {
                it.remove();
            }
        }
        setInitialStateForCalculation();
    }

    // remove all items from the item list
    public void removeAllItems() {
        itemList.clear();
        setInitialStateForCalculation();
    }

    public int getProfit() {
        if (!calculated)
            calcSolution();
        return profit;
    }

    public int getSolutionWeight() {return solutionWeight;}
    public boolean isCalculated() {return calculated;}
    public int getMaxWeight() {return maxWeight;}

    public void setMaxWeight(int _maxWeight) {
        maxWeight = Math.max(_maxWeight, 0);
    }

    public void setItemList(List<Item> _itemList) {
        if (_itemList != null) {
            itemList = _itemList;
            for (Item item : _itemList) {
                item.checkMembers();
            }
        }
    }

    // set the member with name "inKnapsack" by all items:
    private void setInKnapsackByAll(int inKnapsack) {
        for (Item item : itemList)
            if (inKnapsack > 0)
                item.setInKnapsack(1);
            else
                item.setInKnapsack(0);
    }

    // set the data members of class in the state of starting the calculation:
    protected void setInitialStateForCalculation() {
        setInKnapsackByAll(0);
        calculated     = false;
        profit         = 0;
        solutionWeight = 0;
    }

} // class

```

### java_code_3.txt
```java
package hu.pj.obj;

public class Item {

    protected String name    = "";
    protected int weight     = 0;
    protected int value      = 0;
    protected int bounding   = 1; // the maximal limit of item's pieces
    protected int inKnapsack = 0; // the pieces of item in solution

    public Item() {}

    public Item(Item item) {
        setName(item.name);
        setWeight(item.weight);
        setValue(item.value);
        setBounding(item.bounding);
    }

    public Item(int _weight, int _value) {
        setWeight(_weight);
        setValue(_value);
    }

    public Item(int _weight, int _value, int _bounding) {
        setWeight(_weight);
        setValue(_value);
        setBounding(_bounding);
    }

    public Item(String _name, int _weight, int _value) {
        setName(_name);
        setWeight(_weight);
        setValue(_value);
    }

    public Item(String _name, int _weight, int _value, int _bounding) {
        setName(_name);
        setWeight(_weight);
        setValue(_value);
        setBounding(_bounding);
    }

    public void setName(String _name) {name = _name;}
    public void setWeight(int _weight) {weight = Math.max(_weight, 0);}
    public void setValue(int _value) {value = Math.max(_value, 0);}

    public void setInKnapsack(int _inKnapsack) {
        inKnapsack = Math.min(getBounding(), Math.max(_inKnapsack, 0));
    }

    public void setBounding(int _bounding) {
        bounding = Math.max(_bounding, 0);
        if (bounding == 0)
            inKnapsack = 0;
    }

    public void checkMembers() {
        setWeight(weight);
        setValue(value);
        setBounding(bounding);
        setInKnapsack(inKnapsack);
    }

    public String getName() {return name;}
    public int getWeight() {return weight;}
    public int getValue() {return value;}
    public int getInKnapsack() {return inKnapsack;}
    public int getBounding() {return bounding;}

} // class

```

## Python Code
### python_code_1.txt
```python
from itertools import combinations

def anycomb(items):
    ' return combinations of any length from the items '
    return ( comb
             for r in range(1, len(items)+1)
             for comb in combinations(items, r)
             )

def totalvalue(comb):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt  += wt
        totval += val
    return (totval, -totwt) if totwt <= 400 else (0, 0)

items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )
bagged = max( anycomb(items), key=totalvalue) # max val or min wt if values equal
print("Bagged the following items\n  " +
      '\n  '.join(sorted(item for item,_,_ in bagged)))
val, wt = totalvalue(bagged)
print("for a total value of %i and a total weight of %i" % (val, -wt))

```

### python_code_2.txt
```python
try:
    xrange
except:
    xrange = range

def totalvalue(comb):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt  += wt
        totval += val
    return (totval, -totwt) if totwt <= 400 else (0, 0)

items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )

def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]
 
    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)
 
    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]

        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt
 
    return result


bagged = knapsack01_dp(items, 400)
print("Bagged the following items\n  " +
      '\n  '.join(sorted(item for item,_,_ in bagged)))
val, wt = totalvalue(bagged)
print("for a total value of %i and a total weight of %i" % (val, -wt))

```

### python_code_3.txt
```python
def total_value(items, max_weight):
    return  sum([x[2] for x in items]) if sum([x[1] for x in items]) <= max_weight else 0
 
cache = {}
def solve(items, max_weight):
    if not items:
        return ()
    if (items,max_weight) not in cache:
        head = items[0]
        tail = items[1:]
        include = (head,) + solve(tail, max_weight - head[1])
        dont_include = solve(tail, max_weight)
        if total_value(include, max_weight) > total_value(dont_include, max_weight):
            answer = include
        else:
            answer = dont_include
        cache[(items,max_weight)] = answer
    return cache[(items,max_weight)]
 
items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )
max_weight = 400

solution = solve(items, max_weight)
print "items:"
for x in solution:
    print x[0]
print "value:", total_value(solution, max_weight)
print "weight:", sum([x[1] for x in solution])

```

### python_code_4.txt
```python
n=5; N=n+1; G=5; a=2**N	# KNAPSACK 0-1 DANILIN 	
L=[];C=[];e=[];j=[];q=[];s=[] # rextester.com/BCKP19591
d=[];L=[1]*n;C=[1]*n;e=[1]*a	
j=[1]*n;q=[0]*a;s=[0]*a;d=[0]*a

from random import randint
for i in range(0,n):
    L[i]=randint(1,3)
    C[i]=10+randint(1,9)
    print(i+1,L[i],C[i])
print()

for h in range(a-1,(a-1)//2,-1):
    b=str(bin(h))
    e[h]=b[3:len(b)]
        
    for k in range (n):
        j[k]=int(e[h][k])
        q[h]=q[h]+L[k]*j[k]*C[k]
        d[h]=d[h]+L[k]*j[k]
        
    if d[h]<= G:
        print(e[h], G, d[h], q[h])
print()   

max=0; m=1 
for i in range(a):
    if d[i]<=G and q[i]>max:
        max=q[i]; m=i	
print (d[m], q[m], e[m])

```

