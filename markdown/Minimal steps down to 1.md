# Minimal steps down to 1

## Task Link
[Rosetta Code - Minimal steps down to 1](https://rosettacode.org/wiki/Minimal_steps_down_to_1)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MinimalStepsDownToOne {

    public static void main(String[] args) {
        runTasks(getFunctions1());
        runTasks(getFunctions2());
        runTasks(getFunctions3());
    }
    
    private static void runTasks(List<Function> functions) {
        Map<Integer,List<String>> minPath = getInitialMap(functions, 5);

        //  Task 1
        int max = 10;
        populateMap(minPath, functions, max);
        System.out.printf("%nWith functions:  %s%n", functions);
        System.out.printf("  Minimum steps to 1:%n");
        for ( int n = 2 ; n <= max ; n++ ) {
            int steps = minPath.get(n).size();
            System.out.printf("    %2d: %d step%1s: %s%n", n, steps, steps == 1 ? "" : "s", minPath.get(n));
        }
        
        //  Task 2
        displayMaxMin(minPath, functions, 2000);

        //  Task 2a
        displayMaxMin(minPath, functions, 20000);

        //  Task 2a +
        displayMaxMin(minPath, functions, 100000);
    }
    
    private static void displayMaxMin(Map<Integer,List<String>> minPath, List<Function> functions, int max) {
        populateMap(minPath, functions, max);
        List<Integer> maxIntegers = getMaxMin(minPath, max);
        int maxSteps = maxIntegers.remove(0);
        int numCount = maxIntegers.size();
        System.out.printf("  There %s %d number%s in the range 1-%d that have maximum 'minimal steps' of %d:%n    %s%n", numCount == 1 ? "is" : "are", numCount, numCount == 1 ? "" : "s", max, maxSteps, maxIntegers);
        
    }
    
    private static List<Integer> getMaxMin(Map<Integer,List<String>> minPath, int max) {
        int maxSteps = Integer.MIN_VALUE;
        List<Integer> maxIntegers = new ArrayList<Integer>();
        for ( int n = 2 ; n <= max ; n++ ) {
            int len = minPath.get(n).size();
            if ( len > maxSteps ) {
                maxSteps = len;
                maxIntegers.clear();
                maxIntegers.add(n);
            }
            else if ( len == maxSteps ) {
                maxIntegers.add(n);
            }
        }
        maxIntegers.add(0, maxSteps);
        return maxIntegers;
    }

    private static void populateMap(Map<Integer,List<String>> minPath, List<Function> functions, int max) {
        for ( int n = 2 ; n <= max ; n++ ) {
            if ( minPath.containsKey(n) ) {
                continue;
            }
            Function minFunction = null;
            int minSteps = Integer.MAX_VALUE;
            for ( Function f : functions ) {
                if ( f.actionOk(n) ) {
                    int result = f.action(n);
                    int steps = 1 + minPath.get(result).size();
                    if ( steps < minSteps ) {
                        minFunction = f;
                        minSteps = steps;
                    }
                }
            }
            int result = minFunction.action(n);
            List<String> path = new ArrayList<String>();
            path.add(minFunction.toString(n));
            path.addAll(minPath.get(result));
            minPath.put(n, path);
        }
        
    }

    private static Map<Integer,List<String>> getInitialMap(List<Function> functions, int max) {
        Map<Integer,List<String>> minPath = new HashMap<>();
        for ( int i = 2 ; i <= max ; i++ ) {
            for ( Function f : functions ) {
                if ( f.actionOk(i) ) {
                    int result = f.action(i);
                    if ( result == 1 ) {
                        List<String> path = new ArrayList<String>();
                        path.add(f.toString(i));
                        minPath.put(i, path);
                    }
                }
            }
        }
        return minPath;
    }

    private static List<Function> getFunctions3() {
        List<Function> functions = new ArrayList<>();
        functions.add(new Divide2Function());
        functions.add(new Divide3Function());
        functions.add(new Subtract2Function());
        functions.add(new Subtract1Function());
        return functions;
    }

    private static List<Function> getFunctions2() {
        List<Function> functions = new ArrayList<>();
        functions.add(new Divide3Function());
        functions.add(new Divide2Function());
        functions.add(new Subtract2Function());
        return functions;
    }

    private static List<Function> getFunctions1() {
        List<Function> functions = new ArrayList<>();
        functions.add(new Divide3Function());
        functions.add(new Divide2Function());
        functions.add(new Subtract1Function());
        return functions;
    }
    
    public abstract static class Function {
        abstract public int action(int n);
        abstract public boolean actionOk(int n);
        abstract public String toString(int n);
    }
    
    public static class Divide2Function extends Function {
        @Override public int action(int n) {
            return n/2;
        }

        @Override public boolean actionOk(int n) {
            return n % 2 == 0;
        }

        @Override public String toString(int n) {
            return "/2 -> " + n/2;
        }
        
        @Override public String toString() {
            return "Divisor 2";
        }
        
    }

    public static class Divide3Function extends Function {
        @Override public int action(int n) {
            return n/3;
        }

        @Override public boolean actionOk(int n) {
            return n % 3 == 0;
        }

        @Override public String toString(int n) {
            return "/3 -> " + n/3;
        }

        @Override public String toString() {
            return "Divisor 3";
        }

    }

    public static class Subtract1Function extends Function {
        @Override public int action(int n) {
            return n-1;
        }

        @Override public boolean actionOk(int n) {
            return true;
        }
    
        @Override public String toString(int n) {
            return "-1 -> " + (n-1);
        }

        @Override public String toString() {
            return "Subtractor 1";
        }

    }

    public static class Subtract2Function extends Function {
        @Override public int action(int n) {
            return n-2;
        }

        @Override public boolean actionOk(int n) {
            return n > 2;
        }
    
        @Override public String toString(int n) {
            return "-2 -> " + (n-2);
        }

        @Override public String toString() {
            return "Subtractor 2";
        }

    }

}

```

## Python Code
### python_code_1.txt
```python
from functools import lru_cache


#%%

DIVS = {2, 3}
SUBS = {1}

class Minrec():
    "Recursive, memoised minimised steps to 1"

    def __init__(self, divs=DIVS, subs=SUBS):
        self.divs, self.subs = divs, subs

    @lru_cache(maxsize=None)
    def _minrec(self, n):
        "Recursive, memoised"
        if n == 1:
            return 0, ['=1']
        possibles = {}
        for d in self.divs:
            if n % d == 0:
                possibles[f'/{d}=>{n // d:2}'] = self._minrec(n // d)
        for s in self.subs:
            if n > s:
                possibles[f'-{s}=>{n - s:2}'] = self._minrec(n - s)
        thiskind, (count, otherkinds) = min(possibles.items(), key=lambda x: x[1])
        ret = 1 + count, [thiskind] + otherkinds
        return ret

    def __call__(self, n):
        "Recursive, memoised"
        ans = self._minrec(n)[1][:-1]
        return len(ans), ans


if __name__ == '__main__':
    for DIVS, SUBS in [({2, 3}, {1}), ({2, 3}, {2})]:
        minrec = Minrec(DIVS, SUBS)
        print('\nMINIMUM STEPS TO 1: Recursive algorithm')
        print('  Possible divisors:  ', DIVS)
        print('  Possible decrements:', SUBS)
        for n in range(1, 11):
            steps, how = minrec(n)
            print(f'    minrec({n:2}) in {steps:2} by: ', ', '.join(how))

        upto = 2000
        print(f'\n    Those numbers up to {upto} that take the maximum, "minimal steps down to 1":')
        stepn = sorted((minrec(n)[0], n) for n in range(upto, 0, -1))
        mx = stepn[-1][0]
        ans = [x[1] for x in stepn if x[0] == mx]
        print('      Taking', mx, f'steps is/are the {len(ans)} numbers:',
              ', '.join(str(n) for n in sorted(ans)))
        #print(minrec._minrec.cache_info())
        print()

```

### python_code_2.txt
```python
class Mintab():
    "Tabulation, memoised minimised steps to 1"

    def __init__(self, divs=DIVS, subs=SUBS):
        self.divs, self.subs = divs, subs
        self.table = None   # Last tabulated table
        self.hows = None    # Last tabulated sample steps

    def _mintab(self, n):
        "Tabulation, memoised minimised steps to 1"
        divs, subs = self.divs, self.subs

        table = [n + 2] * (n + 1)   # sentinels
        table[1] = 0                # zero steps to 1 from 1
        how = [[''] for _ in range(n + 2)]  # What steps are taken
        how[1] = ['=']
        for t in range(1, n):
            thisplus1 = table[t] + 1
            for d in divs:
                dt = d * t
                if dt <= n and thisplus1 < table[dt]:
                    table[dt] = thisplus1
                    how[dt] = how[t] + [f'/{d}=>{t:2}']
            for s in subs:
                st = s + t
                if st <= n and thisplus1 < table[st]:
                    table[st] = thisplus1
                    how[st] = how[t] + [f'-{s}=>{t:2}']
        self.table = table
        self.hows = [h[::-1][:-1] for h in how]   # Order and trim
        return self.table, self.hows

    def __call__(self, n):
        "Tabulation"
        table, hows = self._mintab(n)
        return table[n], hows[n]


if __name__ == '__main__':
    for DIVS, SUBS in [({2, 3}, {1}), ({2, 3}, {2})]:
        print('\nMINIMUM STEPS TO 1: Tabulation algorithm')
        print('  Possible divisors:  ', DIVS)
        print('  Possible decrements:', SUBS)
        mintab = Mintab(DIVS, SUBS)
        mintab(10)
        table, hows = mintab.table, mintab.hows
        for n in range(1, 11):
            steps, how = table[n], hows[n]
            print(f'    mintab({n:2}) in {steps:2} by: ', ', '.join(how))

        for upto in [2000, 50_000]:
            mintab(upto)
            table = mintab.table
            print(f'\n    Those numbers up to {upto} that take the maximum, "minimal steps down to 1":')
            mx = max(table[1:])
            ans = [n for n, steps in enumerate(table) if steps == mx]
            print('      Taking', mx, f'steps is/are the {len(ans)} numbers:',
                  ', '.join(str(n) for n in ans))

```

