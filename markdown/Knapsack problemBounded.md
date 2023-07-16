# Knapsack problem/Bounded

## Task Link
[Rosetta Code - Knapsack problem/Bounded](https://rosettacode.org/wiki/Knapsack_problem/Bounded)

## Java Code
### java_code_1.txt
```java
package hu.pj.alg.test;

import hu.pj.alg.BoundedKnapsack;
import hu.pj.obj.Item;
import java.util.*;
import java.text.*;

public class BoundedKnapsackForTourists {
    public BoundedKnapsackForTourists() {
        BoundedKnapsack bok = new BoundedKnapsack(400); // 400 dkg = 400 dag = 4 kg

        // making the list of items that you want to bring
        bok.add("map", 9, 150, 1);
        bok.add("compass", 13, 35, 1);
        bok.add("water", 153, 200, 3);
        bok.add("sandwich", 50, 60, 2);
        bok.add("glucose", 15, 60, 2);
        bok.add("tin", 68, 45, 3);
        bok.add("banana", 27, 60, 3);
        bok.add("apple", 39, 40, 3);
        bok.add("cheese", 23, 30, 1);
        bok.add("beer", 52, 10, 3);
        bok.add("suntan cream", 11, 70, 1);
        bok.add("camera", 32, 30, 1);
        bok.add("t-shirt", 24, 15, 2);
        bok.add("trousers", 48, 10, 2);
        bok.add("umbrella", 73, 40, 1);
        bok.add("waterproof trousers", 42, 70, 1);
        bok.add("waterproof overclothes", 43, 75, 1);
        bok.add("note-case", 22, 80, 1);
        bok.add("sunglasses", 7, 20, 1);
        bok.add("towel", 18, 12, 2);
        bok.add("socks", 4, 50, 1);
        bok.add("book", 30, 10, 2);

        // calculate the solution:
        List<Item> itemList = bok.calcSolution();

        // write out the solution in the standard output
        if (bok.isCalculated()) {
            NumberFormat nf  = NumberFormat.getInstance();

            System.out.println(
                "Maximal weight           = " +
                nf.format(bok.getMaxWeight() / 100.0) + " kg"
            );
            System.out.println(
                "Total weight of solution = " +
                nf.format(bok.getSolutionWeight() / 100.0) + " kg"
            );
            System.out.println(
                "Total value              = " +
                bok.getProfit()
            );
            System.out.println();
            System.out.println(
                "You can carry te following materials " +
                "in the knapsack:"
            );
            for (Item item : itemList) {
                if (item.getInKnapsack() > 0) {
                    System.out.format(
                        "%1$-10s %2$-23s %3$-3s %4$-5s %5$-15s \n",
                        item.getInKnapsack() + " unit(s) ",
                        item.getName(),
                        item.getInKnapsack() * item.getWeight(), "dag  ",
                        "(value = " + item.getInKnapsack() * item.getValue() + ")"
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
        new BoundedKnapsackForTourists();
    }
} // class

```

### java_code_2.txt
```java
package hu.pj.alg;

import hu.pj.obj.Item;
import java.util.*;

public class BoundedKnapsack extends ZeroOneKnapsack {
    public BoundedKnapsack() {}

    public BoundedKnapsack(int _maxWeight) {
        setMaxWeight(_maxWeight);
    }

    public BoundedKnapsack(List<Item> _itemList) {
        setItemList(_itemList);
    }

    public BoundedKnapsack(List<Item> _itemList, int _maxWeight) {
        setItemList(_itemList);
        setMaxWeight(_maxWeight);
    }

    @Override
    public List<Item> calcSolution() {
        int n = itemList.size();

        // add items to the list, if bounding > 1
        for (int i = 0; i < n; i++) {
            Item item = itemList.get(i);
            if (item.getBounding() > 1) {
                for (int j = 1; j < item.getBounding(); j++) {
                    add(item.getName(), item.getWeight(), item.getValue());
                }
            }
        }
        
        super.calcSolution();

        // delete the added items, and increase the original items
        while (itemList.size() > n) {
            Item lastItem = itemList.get(itemList.size() - 1);
            if (lastItem.getInKnapsack() == 1) {
                for (int i = 0; i < n; i++) {
                    Item iH = itemList.get(i);
                    if (lastItem.getName().equals(iH.getName())) {
                        iH.setInKnapsack(1 + iH.getInKnapsack());
                        break;
                    }
                }
            }
            itemList.remove(itemList.size() - 1);
        }

        return itemList;
    }

    // add an item to the item list
    public void add(String name, int weight, int value, int bounding) {
        if (name.equals(""))
            name = "" + (itemList.size() + 1);
        itemList.add(new Item(name, weight, value, bounding));
        setInitialStateForCalculation();
    }
} // class

```

### java_code_3.txt
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

### java_code_4.txt
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
### python_code_2.txt
```python
from itertools import groupby
from collections import namedtuple

def anyvalidcomb(items, maxwt, val=0, wt=0):
    ' All combinations below the maxwt '
    if not items:
        yield [], val, wt
    else:
        this, *items = items            # car, cdr
        for n in range(this.number + 1):
            w = wt  + n * this.weight
            if w > maxwt:
                break
            v = val + n * this.value
            this_comb = [this] * n
            for comb, value, weight in anyvalidcomb(items, maxwt, v, w):
                yield this_comb + comb, value, weight

maxwt = 400
COMB, VAL, WT = range(3)
Item  = namedtuple('Items', 'name weight value number')
items = [ Item(*x) for x in
          (
            ("map", 9, 150, 1),
            ("compass", 13, 35, 1),
            ("water", 153, 200, 3),
            ("sandwich", 50, 60, 2),
            ("glucose", 15, 60, 2),
            ("tin", 68, 45, 3),
            ("banana", 27, 60, 3),
            ("apple", 39, 40, 3),
            ("cheese", 23, 30, 1),
            ("beer", 52, 10, 3),
            ("suntan cream", 11, 70, 1),
            ("camera", 32, 30, 1),
            ("t-shirt", 24, 15, 2),
            ("trousers", 48, 10, 2),
            ("umbrella", 73, 40, 1),
            ("waterproof trousers", 42, 70, 1),
            ("waterproof overclothes", 43, 75, 1),
            ("note-case", 22, 80, 1),
            ("sunglasses", 7, 20, 1),
            ("towel", 18, 12, 2),
            ("socks", 4, 50, 1),
            ("book", 30, 10, 2),
           ) ]  

bagged = max( anyvalidcomb(items, maxwt), key=lambda c: (c[VAL], -c[WT])) # max val or min wt if values equal
print("Bagged the following %i items" % len(bagged[COMB]))
print('\n\t'.join('%i off: %s' % (len(list(grp)), item.name) for item, grp in groupby(sorted(bagged[COMB]))))
print("for a total value of %i and a total weight of %i" % bagged[1:])

```

### python_code_3.txt
```python
from itertools import groupby

try:
    xrange
except:
    xrange = range

maxwt = 400

groupeditems = (
            ("map", 9, 150, 1),
            ("compass", 13, 35, 1),
            ("water", 153, 200, 3),
            ("sandwich", 50, 60, 2),
            ("glucose", 15, 60, 2),
            ("tin", 68, 45, 3),
            ("banana", 27, 60, 3),
            ("apple", 39, 40, 3),
            ("cheese", 23, 30, 1),
            ("beer", 52, 10, 3),
            ("suntan cream", 11, 70, 1),
            ("camera", 32, 30, 1),
            ("t-shirt", 24, 15, 2),
            ("trousers", 48, 10, 2),
            ("umbrella", 73, 40, 1),
            ("waterproof trousers", 42, 70, 1),
            ("waterproof overclothes", 43, 75, 1),
            ("note-case", 22, 80, 1),
            ("sunglasses", 7, 20, 1),
            ("towel", 18, 12, 2),
            ("socks", 4, 50, 1),
            ("book", 30, 10, 2),
           )
items = sum( ([(item, wt, val)]*n for item, wt, val,n in groupeditems), [])

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
 
 
bagged = knapsack01_dp(items, maxwt)
print("Bagged the following %i items\n  " % len(bagged) +
      '\n  '.join('%i off: %s' % (len(list(grp)), item[0])
                  for item,grp in groupby(sorted(bagged))))
print("for a total value of %i and a total weight of %i" % (
    sum(item[2] for item in bagged), sum(item[1] for item in bagged)))

```

### python_code_4.txt
```python
items = {
	"sandwich":	(50,	60,	2),
	"map": 		(9,	150,	1),
	"compass": 	(13,	35,	1),
	"water": 	(153,	200,	3),
	"glucose": 	(15,	60,	2),
	"tin": 		(68,	45,	3),
	"banana": 	(27,	60,	3),
	"apple": 	(39,	40,	3),
	"cheese": 	(23,	30,	1),
	"beer": 	(52,	10,	3),
	"suntan cream": (11,	70,	1),
	"camera": 	(32,	30,	1),
	"t-shirt": 	(24,	15,	2),
	"trousers": 	(48,	10,	2),
	"umbrella": 	(73,	40,	1),
	"w-trousers": 	(42,	70,	1),
	"w-overcoat": 	(43,	75,	1),
	"note-case": 	(22,	80,	1),
	"sunglasses": 	(7,	20,	1),
	"towel": 	(18,	12,	2),
	"socks": 	(4,	50,	1),
	"book": 	(30,	10,	2),
}

item_keys = list(items.keys())

#cache: could just use memoize module, but explicit caching is clearer
def choose_item(weight, idx, cache):
    if idx < 0: return 0, []
 
    k = (weight, idx)
    if k in cache: return cache[k]
 
    name, w, v, qty = item_keys[idx], *items[item_keys[idx]]
    best_v, best_list = 0, []
 
    for i in range(0, qty + 1):
        wlim = weight - i * w
        if wlim < 0: break
 
        val, taken = choose_item(wlim, idx - 1, cache)
        if val + i * v > best_v:
            best_v = val + i * v
            best_list = taken[:]
            best_list.append((i, name))
 
    cache[k] = [best_v, best_list]
    return best_v, best_list
 
 
v, lst = choose_item(400, len(items) - 1, {})
w = 0
for cnt, name in lst:
    if cnt > 0:
        print(cnt, name)        
        w = w + items[name][0] * cnt
 
print("Total weight:", w, "Value:", v)

```

