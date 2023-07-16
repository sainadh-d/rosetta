# Zebra puzzle

## Task Link
[Rosetta Code - Zebra puzzle](https://rosettacode.org/wiki/Zebra_puzzle)

## Java Code
### java_code_1.txt
```java
package org.rosettacode.zebra;

import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.Objects;
import java.util.Set;

public class Zebra {

    private static final int[] orders = {1, 2, 3, 4, 5};
    private static final String[] nations = {"English", "Danish", "German", "Swedish", "Norwegian"};
    private static final String[] animals = {"Zebra", "Horse", "Birds", "Dog", "Cats"};
    private static final String[] drinks = {"Coffee", "Tea", "Beer", "Water", "Milk"};
    private static final String[] cigarettes = {"Pall Mall", "Blend", "Blue Master", "Prince", "Dunhill"};
    private static final String[] colors = {"Red", "Green", "White", "Blue", "Yellow"};

    static class Solver {
        private final PossibleLines puzzleTable = new PossibleLines();

        void solve() {
            PossibleLines constraints = new PossibleLines();
            constraints.add(new PossibleLine(null, "English", "Red", null, null, null));
            constraints.add(new PossibleLine(null, "Swedish", null, "Dog", null, null));
            constraints.add(new PossibleLine(null, "Danish", null, null, "Tea", null));
            constraints.add(new PossibleLine(null, null, "Green", null, "Coffee", null));
            constraints.add(new PossibleLine(null, null, null, "Birds", null, "Pall Mall"));
            constraints.add(new PossibleLine(null, null, "Yellow", null, null, "Dunhill"));
            constraints.add(new PossibleLine(3, null, null, null, "Milk", null));
            constraints.add(new PossibleLine(1, "Norwegian", null, null, null, null));
            constraints.add(new PossibleLine(null, null, null, null, "Beer", "Blue Master"));
            constraints.add(new PossibleLine(null, "German", null, null, null, "Prince"));
            constraints.add(new PossibleLine(2, null, "Blue", null, null, null));

            //Creating all possible combination of a puzzle line.
            //The maximum number of lines is 5^^6 (15625).
            //Each combination line is checked against a set of knowing facts, thus
            //only a small number of line result at the end.
            for (Integer orderId : Zebra.orders) {
                for (String nation : Zebra.nations) {
                    for (String color : Zebra.colors) {
                        for (String animal : Zebra.animals) {
                            for (String drink : Zebra.drinks) {
                                for (String cigarette : Zebra.cigarettes) {
                                    addPossibleNeighbors(constraints, orderId, nation, color, animal, drink, cigarette);
                                }
                            }
                        }
                    }
                }
            }

            System.out.println("After general rule set validation, remains " +
                    puzzleTable.size() + " lines.");

            for (Iterator<PossibleLine> it = puzzleTable.iterator(); it.hasNext(); ) {
                boolean validLine = true;

                PossibleLine possibleLine = it.next();

                if (possibleLine.leftNeighbor != null) {
                    PossibleLine neighbor = possibleLine.leftNeighbor;
                    if (neighbor.order < 1 || neighbor.order > 5) {
                        validLine = false;
                        it.remove();
                    }
                }
                if (validLine && possibleLine.rightNeighbor != null) {
                    PossibleLine neighbor = possibleLine.rightNeighbor;
                    if (neighbor.order < 1 || neighbor.order > 5) {
                        it.remove();
                    }
                }
            }

            System.out.println("After removing out of bound neighbors, remains " +
                    puzzleTable.size() + " lines.");

            //Setting left and right neighbors
            for (PossibleLine puzzleLine : puzzleTable) {
                for (PossibleLine leftNeighbor : puzzleLine.neighbors) {
                    PossibleLine rightNeighbor = leftNeighbor.copy();

                    //make it left neighbor
                    leftNeighbor.order = puzzleLine.order - 1;
                    if (puzzleTable.contains(leftNeighbor)) {
                        if (puzzleLine.leftNeighbor != null)
                            puzzleLine.leftNeighbor.merge(leftNeighbor);
                        else
                            puzzleLine.setLeftNeighbor(leftNeighbor);
                    }
                    rightNeighbor.order = puzzleLine.order + 1;
                    if (puzzleTable.contains(rightNeighbor)) {
                        if (puzzleLine.rightNeighbor != null)
                            puzzleLine.rightNeighbor.merge(rightNeighbor);
                        else
                            puzzleLine.setRightNeighbor(rightNeighbor);
                    }
                }
            }

            int iteration = 1;
            int lastSize = 0;

            //Recursively validate against neighbor rules
            while (puzzleTable.size() > 5 && lastSize != puzzleTable.size()) {
                lastSize = puzzleTable.size();
                puzzleTable.clearLineCountFlags();

                recursiveSearch(null, puzzleTable, -1);

                constraints.clear();
                // Assuming we'll get at leas one valid line each iteration, we create
                // a set of new rules with lines which have no more then one instance of same OrderId.
                for (int i = 1; i < 6; i++) {
                    if (puzzleTable.getLineCountByOrderId(i) == 1)
                        constraints.addAll(puzzleTable.getSimilarLines(new PossibleLine(i, null, null, null, null,
                                null)));
                }

                puzzleTable.removeIf(puzzleLine -> !constraints.accepts(puzzleLine));

                System.out.println("After " + iteration + " recursive iteration, remains "
                        + puzzleTable.size() + " lines");
                iteration++;
            }

            // Print the results
            System.out.println("-------------------------------------------");
            if (puzzleTable.size() == 5) {
                for (PossibleLine puzzleLine : puzzleTable) {
                    System.out.println(puzzleLine.getWholeLine());
                }
            } else
                System.out.println("Sorry, solution not found!");
        }

        private void addPossibleNeighbors(
                PossibleLines constraints, Integer orderId, String nation,
                String color, String animal, String drink, String cigarette) {
            boolean validLine = true;
            PossibleLine pzlLine = new PossibleLine(orderId,
                    nation,
                    color,
                    animal,
                    drink,
                    cigarette);
            // Checking against a set of knowing facts
            if (constraints.accepts(pzlLine)) {
                // Adding rules of neighbors
                if (cigarette.equals("Blend")
                        && (animal.equals("Cats") || drink.equals("Water")))
                    validLine = false;

                if (cigarette.equals("Dunhill")
                        && animal.equals("Horse"))
                    validLine = false;

                if (validLine) {
                    puzzleTable.add(pzlLine);

                    //set neighbors constraints
                    if (color.equals("Green")) {
                        pzlLine.setRightNeighbor(
                                new PossibleLine(null, null, "White", null, null, null));
                    }
                    if (color.equals("White")) {
                        pzlLine.setLeftNeighbor(
                                new PossibleLine(null, null, "Green", null, null, null));
                    }
                    //
                    if (animal.equals("Cats") && !cigarette.equals("Blend")) {
                        pzlLine.neighbors.add(new PossibleLine(null, null, null, null, null,
                                "Blend"));
                    }
                    if (cigarette.equals("Blend") && !animal.equals("Cats")) {
                        pzlLine.neighbors.add(new PossibleLine(null, null, null, "Cats", null
                                , null));
                    }
                    //
                    if (drink.equals("Water")
                            && !animal.equals("Cats")
                            && !cigarette.equals("Blend")) {
                        pzlLine.neighbors.add(new PossibleLine(null, null, null, null, null,
                                "Blend"));
                    }

                    if (cigarette.equals("Blend") && !drink.equals("Water")) {
                        pzlLine.neighbors.add(new PossibleLine(null, null, null, null, "Water"
                                , null));
                    }
                    //
                    if (animal.equals("Horse") && !cigarette.equals("Dunhill")) {
                        pzlLine.neighbors.add(new PossibleLine(null, null, null, null, null,
                                "Dunhill"));
                    }
                    if (cigarette.equals("Dunhill") && !animal.equals("Horse")) {
                        pzlLine.neighbors.add(new PossibleLine(null, null, null, "Horse",
                                null, null));
                    }
                }
            }
        }

        // Recursively checks the input set to ensure each line has right neighbor.
        // Neighbors can be of three type, left, right or undefined.
        // Direction: -1 left, 0 undefined, 1 right
        private boolean recursiveSearch(PossibleLine pzzlNodeLine,
                                        PossibleLines possibleLines, int direction) {
            boolean validLeaf = false;
            boolean hasNeighbor;
            PossibleLines puzzleSubSet;

            for (Iterator<PossibleLine> it = possibleLines.iterator(); it.hasNext(); ) {
                PossibleLine pzzlLeafLine = it.next();
                validLeaf = false;

                hasNeighbor = pzzlLeafLine.hasNeighbor(direction);

                if (hasNeighbor) {
                    puzzleSubSet = puzzleTable.getSimilarLines(pzzlLeafLine.getNeighbor(direction));
                    if (puzzleSubSet != null) {
                        if (pzzlNodeLine != null)
                            validLeaf = puzzleSubSet.contains(pzzlNodeLine);
                        else
                            validLeaf = recursiveSearch(pzzlLeafLine, puzzleSubSet, -1 * direction);
                    }
                }

                if (!validLeaf && pzzlLeafLine.hasNeighbor(-1 * direction)) {
                    hasNeighbor = true;
                    puzzleSubSet = puzzleTable.getSimilarLines(pzzlLeafLine.getNeighbor(-1 * direction));
                    if (puzzleSubSet != null) {
                        if (pzzlNodeLine != null)
                            validLeaf = puzzleSubSet.contains(pzzlNodeLine);
                        else
                            validLeaf = recursiveSearch(pzzlLeafLine, puzzleSubSet, direction);
                    }
                }

                if (pzzlNodeLine != null && validLeaf)
                    return true;

                if (pzzlNodeLine == null && hasNeighbor && !validLeaf) {
                    it.remove();
                }

                if (pzzlNodeLine == null) {
                    if (hasNeighbor && validLeaf) {
                        possibleLines.riseLineCountFlags(pzzlLeafLine.order);
                    }
                    if (!hasNeighbor) {
                        possibleLines.riseLineCountFlags(pzzlLeafLine.order);
                    }
                }
            }
            return validLeaf;
        }
    }

    public static void main(String[] args) {

        Solver solver = new Solver();
        solver.solve();
    }

    static class PossibleLines extends LinkedHashSet<PossibleLine> {

        private final int[] count = new int[5];

        public PossibleLine get(int index) {
            return ((PossibleLine) toArray()[index]);
        }

        public PossibleLines getSimilarLines(PossibleLine searchLine) {
            PossibleLines puzzleSubSet = new PossibleLines();
            for (PossibleLine possibleLine : this) {
                if (possibleLine.getCommonFactsCount(searchLine) == searchLine.getFactsCount())
                    puzzleSubSet.add(possibleLine);
            }
            if (puzzleSubSet.isEmpty())
                return null;

            return puzzleSubSet;
        }

        public boolean contains(PossibleLine searchLine) {
            for (PossibleLine puzzleLine : this) {
                if (puzzleLine.getCommonFactsCount(searchLine) == searchLine.getFactsCount())
                    return true;
            }
            return false;
        }

        public boolean accepts(PossibleLine searchLine) {
            int passed = 0;
            int notpassed = 0;

            for (PossibleLine puzzleSetLine : this) {
                int lineFactsCnt = puzzleSetLine.getFactsCount();
                int comnFactsCnt = puzzleSetLine.getCommonFactsCount(searchLine);

                if (lineFactsCnt != comnFactsCnt && lineFactsCnt != 0 && comnFactsCnt != 0) {
                    notpassed++;
                }

                if (lineFactsCnt == comnFactsCnt)
                    passed++;
            }
            return passed >= 0 && notpassed == 0;
        }

        public void riseLineCountFlags(int lineOrderId) {
            count[lineOrderId - 1]++;
        }

        public void clearLineCountFlags() {
            Arrays.fill(count, 0);
        }

        public int getLineCountByOrderId(int lineOrderId) {
            return count[lineOrderId - 1];
        }
    }

    static class PossibleLine {

        Integer order;
        String nation;
        String color;
        String animal;
        String drink;
        String cigarette;

        PossibleLine rightNeighbor;
        PossibleLine leftNeighbor;
        Set<PossibleLine> neighbors = new LinkedHashSet<>();

        public PossibleLine(Integer order, String nation, String color,
                            String animal, String drink, String cigarette) {
            this.animal = animal;
            this.cigarette = cigarette;
            this.color = color;
            this.drink = drink;
            this.nation = nation;
            this.order = order;
        }

        @Override
        public boolean equals(Object obj) {
            return obj instanceof PossibleLine
                    && getWholeLine().equals(((PossibleLine) obj).getWholeLine());
        }

        public int getFactsCount() {
            int facts = 0;
            facts += order != null ? 1 : 0;
            facts += nation != null ? 1 : 0;
            facts += color != null ? 1 : 0;
            facts += animal != null ? 1 : 0;
            facts += cigarette != null ? 1 : 0;
            facts += drink != null ? 1 : 0;
            return facts;
        }

        private static int common(Object a, Object b) {
            return a != null && Objects.equals(a, b) ? 1 : 0;
        }

        public int getCommonFactsCount(PossibleLine facts) {
            return common(order, facts.order)
                    + common(nation, facts.nation)
                    + common(color, facts.color)
                    + common(animal, facts.animal)
                    + common(cigarette, facts.cigarette)
                    + common(drink, facts.drink);
        }

        public void setLeftNeighbor(PossibleLine leftNeighbor) {
            this.leftNeighbor = leftNeighbor;
            this.leftNeighbor.order = order - 1;
        }

        public void setRightNeighbor(PossibleLine rightNeighbor) {
            this.rightNeighbor = rightNeighbor;
            this.rightNeighbor.order = order + 1;
        }

        public boolean hasNeighbor(int direction) {
            return getNeighbor(direction) != null;
        }

        public PossibleLine getNeighbor(int direction) {
            if (direction < 0)
                return leftNeighbor;
            else
                return rightNeighbor;
        }

        public String getWholeLine() {
            return order + " - " +
                    nation + " - " +
                    color + " - " +
                    animal + " - " +
                    drink + " - " +
                    cigarette;
        }

        @Override
        public int hashCode() {
            return Objects.hash(order, nation, color, animal, drink, cigarette);
        }

        public void merge(PossibleLine mergedLine) {
            if (order == null) order = mergedLine.order;
            if (nation == null) nation = mergedLine.nation;
            if (color == null) color = mergedLine.color;
            if (animal == null) animal = mergedLine.animal;
            if (drink == null) drink = mergedLine.drink;
            if (cigarette == null) cigarette = mergedLine.cigarette;
        }

        public PossibleLine copy() {
            PossibleLine clone = new PossibleLine(order, nation, color, animal, drink, cigarette);
            clone.leftNeighbor = leftNeighbor;
            clone.rightNeighbor = rightNeighbor;
            clone.neighbors = neighbors; // shallow copy
            return clone;
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from logpy import *
from logpy.core import lall
import time

def lefto(q, p, list):
	# give me q such that q is left of p in list
	# zip(list, list[1:]) gives a list of 2-tuples of neighboring combinations
	# which can then be pattern-matched against the query
	return membero((q,p), zip(list, list[1:]))

def nexto(q, p, list):
	# give me q such that q is next to p in list
	# match lefto(q, p) OR lefto(p, q)
	# requirement of vector args instead of tuples doesn't seem to be documented
	return conde([lefto(q, p, list)], [lefto(p, q, list)])

houses = var()

zebraRules = lall(
	# there are 5 houses
	(eq, 		(var(), var(), var(), var(), var()), houses),
	# the Englishman's house is red
	(membero,	('Englishman', var(), var(), var(), 'red'), houses),
	# the Swede has a dog
	(membero,	('Swede', var(), var(), 'dog', var()), houses),
	# the Dane drinks tea
	(membero,	('Dane', var(), 'tea', var(), var()), houses),
	# the Green house is left of the White house
	(lefto,		(var(), var(), var(), var(), 'green'),
				(var(), var(), var(), var(), 'white'), houses),
	# coffee is the drink of the green house
	(membero,	(var(), var(), 'coffee', var(), 'green'), houses),
	# the Pall Mall smoker has birds
	(membero,	(var(), 'Pall Mall', var(), 'birds', var()), houses),
	# the yellow house smokes Dunhills
	(membero,	(var(), 'Dunhill', var(), var(), 'yellow'), houses),
	# the middle house drinks milk
	(eq,		(var(), var(), (var(), var(), 'milk', var(), var()), var(), var()), houses),
	# the Norwegian is the first house
	(eq,		(('Norwegian', var(), var(), var(), var()), var(), var(), var(), var()), houses),
	# the Blend smoker is in the house next to the house with cats
	(nexto,		(var(), 'Blend', var(), var(), var()),
				(var(), var(), var(), 'cats', var()), houses),
	# the Dunhill smoker is next to the house where they have a horse
	(nexto,		(var(), 'Dunhill', var(), var(), var()),
				(var(), var(), var(), 'horse', var()), houses),
	# the Blue Master smoker drinks beer
	(membero,	(var(), 'Blue Master', 'beer', var(), var()), houses),
	# the German smokes Prince
	(membero,	('German', 'Prince', var(), var(), var()), houses),
	# the Norwegian is next to the blue house
	(nexto,		('Norwegian', var(), var(), var(), var()),
				(var(), var(), var(), var(), 'blue'), houses),
	# the house next to the Blend smoker drinks water
	(nexto,		(var(), 'Blend', var(), var(), var()),
				(var(), var(), 'water', var(), var()), houses),
	# one of the houses has a zebra--but whose?
	(membero,	(var(), var(), var(), 'zebra', var()), houses)
)

t0 = time.time()
solutions = run(0, houses, zebraRules)
t1 = time.time()
dur = t1-t0

count = len(solutions)
zebraOwner = [house for house in solutions[0] if 'zebra' in house][0][0]

print "%i solutions in %.2f seconds" % (count, dur)
print "The %s is the owner of the zebra" % zebraOwner
print "Here are all the houses:"
for line in solutions[0]:
	print str(line)

```

### python_code_2.txt
```python
import psyco; psyco.full()

class Content: elems= """Beer Coffee Milk Tea Water
                         Danish English German Norwegian Swedish
                         Blue Green Red White Yellow
                         Blend BlueMaster Dunhill PallMall Prince
                         Bird Cat Dog Horse Zebra""".split()
class Test: elems= "Drink Person Color Smoke Pet".split()
class House: elems= "One Two Three Four Five".split()

for c in (Content, Test, House):
  c.values = range(len(c.elems))
  for i, e in enumerate(c.elems):
    exec "%s.%s = %d" % (c.__name__, e, i)

def finalChecks(M):
  def diff(a, b, ca, cb):
    for h1 in House.values:
      for h2 in House.values:
        if M[ca][h1] == a and M[cb][h2] == b:
          return h1 - h2
    assert False

  return abs(diff(Content.Norwegian, Content.Blue,
                 Test.Person, Test.Color)) == 1 and \
         diff(Content.Green, Content.White,
              Test.Color, Test.Color) == -1 and \
         abs(diff(Content.Horse, Content.Dunhill,
                  Test.Pet, Test.Smoke)) == 1 and \
         abs(diff(Content.Water, Content.Blend,
                  Test.Drink, Test.Smoke)) == 1 and \
         abs(diff(Content.Blend, Content.Cat,
                  Test.Smoke, Test.Pet)) == 1

def constrained(M, atest):
      if atest == Test.Drink:
        return M[Test.Drink][House.Three] == Content.Milk
      elif atest == Test.Person:
        for h in House.values:
          if ((M[Test.Person][h] == Content.Norwegian and
               h != House.One) or
              (M[Test.Person][h] == Content.Danish and
               M[Test.Drink][h] != Content.Tea)):
            return False
        return True
      elif atest == Test.Color:
        for h in House.values:
          if ((M[Test.Person][h] == Content.English and
               M[Test.Color][h] != Content.Red) or
              (M[Test.Drink][h] == Content.Coffee and
               M[Test.Color][h] != Content.Green)):
            return False
        return True
      elif atest == Test.Smoke:
        for h in House.values:
          if ((M[Test.Color][h] == Content.Yellow and
               M[Test.Smoke][h] != Content.Dunhill) or
              (M[Test.Smoke][h] == Content.BlueMaster and
               M[Test.Drink][h] != Content.Beer) or
              (M[Test.Person][h] == Content.German and
               M[Test.Smoke][h] != Content.Prince)):
            return False
        return True
      elif atest == Test.Pet:
        for h in House.values:
          if ((M[Test.Person][h] == Content.Swedish and
               M[Test.Pet][h] != Content.Dog) or
              (M[Test.Smoke][h] == Content.PallMall and
               M[Test.Pet][h] != Content.Bird)):
            return False
        return finalChecks(M)

def show(M):
  for h in House.values:
    print "%5s:" % House.elems[h],
    for t in Test.values:
      print "%10s" % Content.elems[M[t][h]],
    print

def solve(M, t, n):
  if n == 1 and constrained(M, t):
    if t < 4:
      solve(M, Test.values[t + 1], 5)
    else:
      show(M)
      return

  for i in xrange(n):
    solve(M, t, n - 1)
    M[t][0 if n % 2 else i], M[t][n - 1] = \
      M[t][n - 1], M[t][0 if n % 2 else i]

def main():
  M = [[None] * len(Test.elems) for _ in xrange(len(House.elems))]
  for t in Test.values:
    for h in House.values:
      M[t][h] = Content.values[t * 5 + h]

  solve(M, Test.Drink, 5)

main()

```

### python_code_3.txt
```python
from itertools import permutations

class Number:elems= "One Two Three Four Five".split()
class Color: elems= "Red Green Blue White Yellow".split()
class Drink: elems= "Milk Coffee Water Beer Tea".split()
class Smoke: elems= "PallMall Dunhill Blend BlueMaster Prince".split()
class Pet:   elems= "Dog Cat Zebra Horse Bird".split()
class Nation:elems= "British Swedish Danish Norvegian German".split()

for c in (Number, Color, Drink, Smoke, Pet, Nation):
  for i, e in enumerate(c.elems):
    exec "%s.%s = %d" % (c.__name__, e, i)

def show_row(t, data):
  print "%6s: %12s%12s%12s%12s%12s" % (
    t.__name__, t.elems[data[0]],
    t.elems[data[1]], t.elems[data[2]],
    t.elems[data[3]], t.elems[data[4]])

def main():
  perms = list(permutations(range(5)))
  for number in perms:
    if number[Nation.Norvegian] == Number.One: # Constraint 10
      for color in perms:
        if color[Nation.British] == Color.Red: # Constraint 2
          if number[color.index(Color.Blue)] == Number.Two: # Constraint 15+10
            if number[color.index(Color.White)] - number[color.index(Color.Green)] == 1: # Constraint 5
              for drink in perms:
                if drink[Nation.Danish] == Drink.Tea: # Constraint 4
                  if drink[color.index(Color.Green)] == Drink.Coffee:  # Constraint 6
                    if drink[number.index(Number.Three)] == Drink.Milk: # Constraint 9
                      for smoke in perms:
                        if smoke[Nation.German] == Smoke.Prince: # Constraint 14
                          if drink[smoke.index(Smoke.BlueMaster)] == Drink.Beer: # Constraint 13
                            if smoke[color.index(Color.Yellow)] == Smoke.Dunhill: # Constraint 8
                              if number[smoke.index(Smoke.Blend)] - number[drink.index(Drink.Water)] in (1, -1): # Constraint 16
                                for pet in perms:
                                  if pet[Nation.Swedish] == Pet.Dog: # Constraint 3
                                    if pet[smoke.index(Smoke.PallMall)] == Pet.Bird: # Constraint 7
                                      if number[pet.index(Pet.Horse)] - number[smoke.index(Smoke.Dunhill)] in (1, -1): # Constraint 12
                                        if number[smoke.index(Smoke.Blend)] - number[pet.index(Pet.Cat)] in (1, -1): # Constraint 11
                                          print "Found a solution:"
                                          show_row(Nation, range(5))
                                          show_row(Number, number)
                                          show_row(Color, color)
                                          show_row(Drink, drink)
                                          show_row(Smoke, smoke)
                                          show_row(Pet, pet)
                                          print

main()

```

### python_code_4.txt
```python
from constraint import *

problem = Problem()

Nation = ["Englishman", "Spaniard", "Japanese",     "Ukrainian",   "Norwegian" ]
Color  = ["Red",        "Green",    "White",        "Yellow",      "Blue"      ]
Smoke  = ["Oldgold",    "Kools",    "Chesterfield", "Luckystrike", "Parliament"]
Pet    = ["Dog",        "Snails",   "Fox",          "Horse",       "Zebra"     ]
Drink  = ["Tea",        "Coffee",   "Milk",         "Orangejuice", "Water"     ]

# add variables: house numbers 1 to 5
problem.addVariables(Nation, range(1,5+1))
problem.addVariables(Color,  range(1,5+1))
problem.addVariables(Smoke,  range(1,5+1))
problem.addVariables(Pet,    range(1,5+1))
problem.addVariables(Drink,  range(1,5+1))

# add constraint: the values in each list are exclusive
problem.addConstraint(AllDifferentConstraint(), Nation)
problem.addConstraint(AllDifferentConstraint(), Color)
problem.addConstraint(AllDifferentConstraint(), Smoke)
problem.addConstraint(AllDifferentConstraint(), Pet)
problem.addConstraint(AllDifferentConstraint(), Drink)

# add constraint: actual constraints
problem.addConstraint(lambda a, b: a == b,                   ["Englishman",   "Red"        ])
problem.addConstraint(lambda a, b: a == b,                   ["Spaniard",     "Dog"        ])
problem.addConstraint(lambda a, b: a == b,                   ["Green",        "Coffee"     ])
problem.addConstraint(lambda a, b: a == b,                   ["Ukrainian",    "Tea"        ])
problem.addConstraint(lambda a, b: a == b + 1,               ["Green",        "White"      ])
problem.addConstraint(lambda a, b: a == b,                   ["Oldgold",      "Snails"     ])
problem.addConstraint(lambda a, b: a == b,                   ["Yellow",       "Kools"      ])
problem.addConstraint(lambda a: a == 3,                      ["Milk"                       ])
problem.addConstraint(lambda a: a == 1,                      ["Norwegian"                  ])
problem.addConstraint(lambda a, b: a == b - 1 or a == b + 1, ["Chesterfield", "Fox"        ])
problem.addConstraint(lambda a, b: a == b - 1 or a == b + 1, ["Kools",        "Horse"      ])
problem.addConstraint(lambda a, b: a == b,                   ["Luckystrike",  "Orangejuice"])
problem.addConstraint(lambda a, b: a == b,                   ["Japanese",     "Parliament" ])
problem.addConstraint(lambda a, b: a == b - 1 or a == b + 1, ["Norwegian",    "Blue"       ])

# get solution
sol = problem.getSolution()

# print the answers
nation = ["Nation" if i == 0 else ""  for i in range(6)]
color  = ["Color"  if i == 0 else ""  for i in range(6)]
smoke  = ["Smoke"  if i == 0 else ""  for i in range(6)]
pet    = ["Pet"    if i == 0 else ""  for i in range(6)]
drink  = ["Drink"  if i == 0 else ""  for i in range(6)]
for n in Nation:
    nation[sol[n]] = n
for n in Color:
    color[sol[n]] = n
for n in Smoke:
    smoke[sol[n]] = n
for n in Pet:
    pet[sol[n]] = n
for n in Drink:
    drink[sol[n]] = n
for d in [nation, color, smoke, pet, drink]:
    print("%6s: %14s%14s%14s%14s%14s" % (d[0], d[1], d[2], d[3], d[4], d[5]))

```

