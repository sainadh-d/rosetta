# Probabilistic choice

## Task Link
[Rosetta Code - Probabilistic choice](https://rosettacode.org/wiki/Probabilistic_choice)

## Java Code
### java_code_1.txt
```java
public class Prob{
	static long TRIALS= 1000000;

	private static class Expv{
		public String name;
		public int probcount;
		public double expect;
		public double mapping;

		public Expv(String name, int probcount, double expect, double mapping){
			this.name= name;
			this.probcount= probcount;
			this.expect= expect;
			this.mapping= mapping;
		}
	}

	static Expv[] items=
			{new Expv("aleph", 0, 0.0, 0.0), new Expv("beth", 0, 0.0, 0.0),
					new Expv("gimel", 0, 0.0, 0.0),
					new Expv("daleth", 0, 0.0, 0.0),
					new Expv("he", 0, 0.0, 0.0), new Expv("waw", 0, 0.0, 0.0),
					new Expv("zayin", 0, 0.0, 0.0),
					new Expv("heth", 0, 0.0, 0.0)};

	public static void main(String[] args){
		int i, j;
		double rnum, tsum= 0.0;

		for(i= 0, rnum= 5.0;i < 7;i++, rnum+= 1.0){
			items[i].expect= 1.0 / rnum;
			tsum+= items[i].expect;
		}
		items[7].expect= 1.0 - tsum;

		items[0].mapping= 1.0 / 5.0;
		for(i= 1;i < 7;i++){
			items[i].mapping= items[i - 1].mapping + 1.0 / ((double)i + 5.0);
		}
		items[7].mapping= 1.0;


		for(i= 0;i < TRIALS;i++){
			rnum= Math.random();
			for(j= 0;j < 8;j++){
				if(rnum < items[j].mapping){
					items[j].probcount++;
					break;
				}
			}
		}

		System.out.printf("Trials: %d\n", TRIALS);
		System.out.printf("Items:          ");
		for(i= 0;i < 8;i++)
			System.out.printf("%-8s ", items[i].name);
		System.out.printf("\nTarget prob.:   ");
		for(i= 0;i < 8;i++)
			System.out.printf("%8.6f ", items[i].expect);
		System.out.printf("\nAttained prob.: ");
		for(i= 0;i < 8;i++)
			System.out.printf("%8.6f ", (double)(items[i].probcount)
					/ (double)TRIALS);
		System.out.printf("\n");

	}
}

```

### java_code_2.txt
```java
import java.util.EnumMap;

public class Prob {
	public static long TRIALS= 1000000;
	public enum Glyph{
		ALEPH, BETH, GIMEL, DALETH, HE, WAW, ZAYIN, HETH;
	}
	
	public static EnumMap<Glyph, Double> probs = new EnumMap<Glyph, Double>(Glyph.class){{
		put(Glyph.ALEPH,   1/5.0);
		put(Glyph.BETH,    1/6.0);
		put(Glyph.GIMEL,   1/7.0);
		put(Glyph.DALETH,  1/8.0);
		put(Glyph.HE,      1/9.0);
		put(Glyph.WAW,     1/10.0);
		put(Glyph.ZAYIN,   1/11.0);
		put(Glyph.HETH,    1759./27720);
	}};
	
	public static EnumMap<Glyph, Double> counts = new EnumMap<Glyph, Double>(Glyph.class){{
		put(Glyph.ALEPH, 0.);put(Glyph.BETH,   0.);
		put(Glyph.GIMEL, 0.);put(Glyph.DALETH, 0.);
		put(Glyph.HE,    0.);put(Glyph.WAW,    0.);
		put(Glyph.ZAYIN, 0.);put(Glyph.HETH,   0.);
	}};
	
	public static void main(String[] args){
		System.out.println("Target probabliities:\t" + probs);
		for(long i = 0; i < TRIALS; i++){
			Glyph choice = getChoice();
			counts.put(choice, counts.get(choice) + 1);
		}

		//correct the counts to probablities in (0..1]
		for(Glyph glyph:counts.keySet()){
			counts.put(glyph, counts.get(glyph) / TRIALS);
		}
		
		System.out.println("Actual probabliities:\t" + counts);
	}
	
	private static Glyph getChoice() {
		double rand = Math.random();
		for(Glyph item:Glyph.values()){
			if(rand < probs.get(item)){
				return item;
			}
			rand -= probs.get(item);
		}
		return null;
	}
}

```

## Python Code
### python_code_1.txt
```python
import random, bisect

def probchoice(items, probs):
  '''\
  Splits the interval 0.0-1.0 in proportion to probs
  then finds where each random.random() choice lies
  '''
  
  prob_accumulator = 0
  accumulator = []
  for p in probs:
    prob_accumulator += p
    accumulator.append(prob_accumulator)
    
  while True:
    r = random.random()
    yield items[bisect.bisect(accumulator, r)]

def probchoice2(items, probs, bincount=10000):
  '''\
  Puts items in bins in proportion to probs
  then uses random.choice() to select items.
  
  Larger bincount for more memory use but
  higher accuracy (on avarage).
  '''
  
  bins = []
  for item,prob in zip(items, probs):
    bins += [item]*int(bincount*prob)
  while True:
    yield random.choice(bins)
      
      
def tester(func=probchoice, items='good bad ugly'.split(),
                    probs=[0.5, 0.3, 0.2],
                    trials = 100000
                    ):
  def problist2string(probs):
    '''\
    Turns a list of probabilities into a string
    Also rounds FP values
    '''
    return ",".join('%8.6f' % (p,) for p in probs)
  
  from collections import defaultdict
   
  counter = defaultdict(int)
  it = func(items, probs)
  for dummy in xrange(trials):
    counter[it.next()] += 1
  print "\n##\n## %s\n##" % func.func_name.upper()  
  print "Trials:              ", trials
  print "Items:               ", ' '.join(items)
  print "Target probability:  ", problist2string(probs)
  print "Attained probability:", problist2string(
    counter[x]/float(trials) for x in items)

if __name__ == '__main__':
  items = 'aleph beth gimel daleth he waw zayin heth'.split()
  probs = [1/(float(n)+5) for n in range(len(items))]
  probs[-1] = 1-sum(probs[:-1])
  tester(probchoice, items, probs, 1000000)
  tester(probchoice2, items, probs, 1000000)

```

