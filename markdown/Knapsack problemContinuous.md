# Knapsack problem/Continuous

## Task Link
[Rosetta Code - Knapsack problem/Continuous](https://rosettacode.org/wiki/Knapsack_problem/Continuous)

## Java Code
### java_code_1.txt
```java
package hu.pj.alg.test;

import hu.pj.alg.ContinuousKnapsack;
import hu.pj.obj.Item;
import java.util.*;
import java.text.*;

public class ContinousKnapsackForRobber {
    final private double tolerance = 0.0005;

    public ContinousKnapsackForRobber() {
        ContinuousKnapsack cok = new ContinuousKnapsack(15); // 15 kg

        // making the list of items that you want to bring
        cok.add("beef",     3.8, 36); // marhahús
        cok.add("pork",     5.4, 43); // disznóhús
        cok.add("ham",      3.6, 90); // sonka
        cok.add("greaves",  2.4, 45); // tepertő
        cok.add("flitch",   4.0, 30); // oldalas
        cok.add("brawn",    2.5, 56); // disznósajt
        cok.add("welt",     3.7, 67); // hurka
        cok.add("salami",   3.0, 95); // szalámi
        cok.add("sausage",  5.9, 98); // kolbász

        // calculate the solution:
        List<Item> itemList = cok.calcSolution();

        // write out the solution in the standard output
        if (cok.isCalculated()) {
            NumberFormat nf  = NumberFormat.getInstance();

            System.out.println(
                "Maximal weight           = " +
                nf.format(cok.getMaxWeight()) + " kg"
            );
            System.out.println(
                "Total weight of solution = " +
                nf.format(cok.getSolutionWeight()) + " kg"
            );
            System.out.println(
                "Total value (profit)     = " +
                nf.format(cok.getProfit())
            );
            System.out.println();
            System.out.println(
                "You can carry the following materials " +
                "in the knapsack:"
            );
            for (Item item : itemList) {
                if (item.getInKnapsack() > tolerance) {
                    System.out.format(
                        "%1$-10s %2$-15s %3$-15s \n",
                        nf.format(item.getInKnapsack()) + " kg ",
                        item.getName(),
                        "(value = " + nf.format(item.getInKnapsack() *
                                                (item.getValue() / item.getWeight())) + ")"
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
        new ContinousKnapsackForRobber();
    }

} // class

```

### java_code_2.txt
```java
package hu.pj.alg;

import hu.pj.obj.Item;
import java.util.*;

public class ContinuousKnapsack {

    protected List<Item> itemList   = new ArrayList<Item>();
    protected double maxWeight      = 0;
    protected double solutionWeight = 0;
    protected double profit         = 0;
    protected boolean calculated    = false;

    public ContinuousKnapsack() {}

    public ContinuousKnapsack(double _maxWeight) {
        setMaxWeight(_maxWeight);
    }

    public List<Item> calcSolution() {
        int n = itemList.size();

        setInitialStateForCalculation();
        if (n > 0  &&  maxWeight > 0) {
            Collections.sort(itemList);
            for (int i = 0; (maxWeight - solutionWeight) > 0.0  &&  i < n; i++) {
                Item item = itemList.get(i);
                if (item.getWeight() >= (maxWeight - solutionWeight)) {
                    item.setInKnapsack(maxWeight - solutionWeight);
                    solutionWeight = maxWeight;
                    profit += item.getInKnapsack() / item.getWeight() * item.getValue();
                    break;
                } else {
                    item.setInKnapsack(item.getWeight());
                    solutionWeight += item.getInKnapsack();
                    profit += item.getValue();
                }
            }
            calculated = true;
        }
        
        return itemList;
    }

    // add an item to the item list
    public void add(String name, double weight, double value) {
        if (name.equals(""))
            name = "" + (itemList.size() + 1);
        itemList.add(new Item(name, weight, value));
        setInitialStateForCalculation();
    }

    public double getMaxWeight() {return maxWeight;}
    public double getProfit() {return profit;}
    public double getSolutionWeight() {return solutionWeight;}
    public boolean isCalculated() {return calculated;}

    public void setMaxWeight(double _maxWeight) {
        maxWeight = Math.max(_maxWeight, 0);
    }

    // set the member with name "inKnapsack" by all items:
    private void setInKnapsackByAll(double inKnapsack) {
        for (Item item : itemList)
            item.setInKnapsack(inKnapsack);
    }

    // set the data members of class in the state of starting the calculation:
    protected void setInitialStateForCalculation() {
        setInKnapsackByAll(-0.0001);
        calculated     = false;
        profit         = 0.0;
        solutionWeight = 0.0;
    }

} // class

```

### java_code_3.txt
```java
package hu.pj.obj;

public class Item implements Comparable {

    protected String name       = "";
    protected double weight     = 0;
    protected double value      = 0;
    protected double inKnapsack = 0; // the weight of item in solution

    public Item() {}

    public Item(Item item) {
        setName(item.name);
        setWeight(item.weight);
        setValue(item.value);
    }

    public Item(double _weight, double _value) {
        setWeight(_weight);
        setValue(_value);
    }

    public Item(String _name, double _weight, double _value) {
        setName(_name);
        setWeight(_weight);
        setValue(_value);
    }

    public void setName(String _name) {name = _name;}
    public void setWeight(double _weight) {weight = Math.max(_weight, 0);}
    public void setValue(double _value) {value = Math.max(_value, 0);}

    public void setInKnapsack(double _inKnapsack) {
        inKnapsack = Math.max(_inKnapsack, 0);
    }

    public void checkMembers() {
        setWeight(weight);
        setValue(value);
        setInKnapsack(inKnapsack);
    }

    public String getName() {return name;}
    public double getWeight() {return weight;}
    public double getValue() {return value;}
    public double getInKnapsack() {return inKnapsack;}

    // implementing of Comparable interface:
    public int compareTo(Object item) {
        int result = 0;
        Item i2 = (Item)item;
        double rate1 = value / weight;
        double rate2 = i2.value / i2.weight;
        if (rate1 > rate2) result = -1;  // if greater, put it previously
        else if (rate1 < rate2) result = 1;
        return result;
    }

} // class

```

## Python Code
### python_code_1.txt
```python
#        NAME, WEIGHT, VALUE (for this weight)
items = [("beef",    3.8, 36.0),
         ("pork",    5.4, 43.0),
         ("ham",     3.6, 90.0),
         ("greaves", 2.4, 45.0),
         ("flitch",  4.0, 30.0),
         ("brawn",   2.5, 56.0),
         ("welt",    3.7, 67.0),
         ("salami",  3.0, 95.0),
         ("sausage", 5.9, 98.0)]

MAXWT = 15.0

sorted_items = sorted(((value/amount, amount, name)
                       for name, amount, value in items),
                      reverse = True)
wt = val = 0
bagged = []
for unit_value, amount, name in sorted_items:
    portion = min(MAXWT - wt, amount)
    wt     += portion
    addval  = portion * unit_value
    val    += addval
    bagged += [(name, portion, addval)]
    if wt >= MAXWT:
        break

print("    ITEM   PORTION VALUE")
print("\n".join("%10s %6.2f %6.2f" % item for item in bagged))
print("\nTOTAL WEIGHT: %5.2f\nTOTAL VALUE: %5.2f" % (wt, val))

```

