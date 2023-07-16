# Evolutionary algorithm

## Task Link
[Rosetta Code - Evolutionary algorithm](https://rosettacode.org/wiki/Evolutionary_algorithm)

## Java Code
### java_code_1.txt
```java
import java.util.Random;

public class EvoAlgo {
  static final String target = "METHINKS IT IS LIKE A WEASEL";
  static final char[] possibilities = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ".toCharArray();
  static int C = 100; //number of spawn per generation
  static double minMutateRate = 0.09;
  static int perfectFitness = target.length();
  private static String parent;
  static Random rand = new Random();

  private static int fitness(String trial){
    int retVal = 0;
    for(int i = 0;i < trial.length(); i++){
      if (trial.charAt(i) == target.charAt(i)) retVal++;
    }
    return retVal;
  }

  private static double newMutateRate(){
    return (((double)perfectFitness - fitness(parent)) / perfectFitness * (1 - minMutateRate));
  }

  private static String mutate(String parent, double rate){
    String retVal = "";
    for(int i = 0;i < parent.length(); i++){
      retVal += (rand.nextDouble() <= rate) ?
        possibilities[rand.nextInt(possibilities.length)]:
        parent.charAt(i);
    }
    return retVal;
  }
  
  public static void main(String[] args){
    parent = mutate(target, 1);
    int iter = 0;
    while(!target.equals(parent)){
      double rate = newMutateRate();
      iter++;
      if(iter % 100 == 0){
        System.out.println(iter +": "+parent+ ", fitness: "+fitness(parent)+", rate: "+rate);
      }
      String bestSpawn = null;
      int bestFit = 0;
      for(int i = 0; i < C; i++){
        String spawn = mutate(parent, rate);
        int fitness = fitness(spawn);
        if(fitness > bestFit){
          bestSpawn = spawn;
          bestFit = fitness;
        }
      }
      parent = bestFit > fitness(parent) ? bestSpawn : parent;
    }
    System.out.println(parent+", "+iter);
  }

}

```

## Python Code
### python_code_1.txt
```python
from string import letters
from random import choice, random
 
target  = list("METHINKS IT IS LIKE A WEASEL")
charset = letters + ' '
parent  = [choice(charset) for _ in range(len(target))]
minmutaterate  = .09
C = range(100)
 
perfectfitness = float(len(target))
    
def fitness(trial):
    'Sum of matching chars by position'
    return sum(t==h for t,h in zip(trial, target))
 
def mutaterate():
    'Less mutation the closer the fit of the parent'
    return 1-((perfectfitness - fitness(parent)) / perfectfitness * (1 - minmutaterate))
 
def mutate(parent, rate):
    return [(ch if random() <= rate else choice(charset)) for ch in parent]
 
def que():
    '(from the favourite saying of Manuel in Fawlty Towers)'
    print ("#%-4i, fitness: %4.1f%%, '%s'" %
           (iterations, fitness(parent)*100./perfectfitness, ''.join(parent)))

def mate(a, b):
    place = 0
    if choice(xrange(10)) < 7:
        place = choice(xrange(len(target)))
    else:
        return a, b
    
    return a, b, a[:place] + b[place:], b[:place] + a[place:]

iterations = 0
center = len(C)/2
while parent != target:
    rate = mutaterate()
    iterations += 1
    if iterations % 100 == 0: que()
    copies = [ mutate(parent, rate) for _ in C ]  + [parent]
    parent1 = max(copies[:center], key=fitness)
    parent2 = max(copies[center:], key=fitness)
    parent = max(mate(parent1, parent2), key=fitness)
que()

```

### python_code_2.txt
```python
from random import choice, random

target  = list("METHINKS IT IS LIKE A WEASEL")
alphabet = " ABCDEFGHIJLKLMNOPQRSTUVWXYZ"
p = 0.05 # mutation probability
c = 100  # number of children in each generation

def neg_fitness(trial):
    return sum(t != h for t,h in zip(trial, target))

def mutate(parent):
    return [(choice(alphabet) if random() < p else ch) for ch in parent]

parent = [choice(alphabet) for _ in xrange(len(target))]
i = 0
print "%3d" % i, "".join(parent)
while parent != target:
    copies = (mutate(parent) for _ in xrange(c))
    parent = min(copies, key=neg_fitness)
    print "%3d" % i, "".join(parent)
    i += 1

```

