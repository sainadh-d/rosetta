# Dinesman's multiple-dwelling problem

## Task Link
[Rosetta Code - Dinesman's multiple-dwelling problem](https://rosettacode.org/wiki/Dinesman%27s_multiple-dwelling_problem)

## Java Code
### java_code_1.txt
```java
import java.util.*;

class DinesmanMultipleDwelling {

    private static void generatePermutations(String[] apartmentDwellers, Set<String> set, String curPermutation) {
        for (String s : apartmentDwellers) {
            if (!curPermutation.contains(s)) {
                String nextPermutation = curPermutation + s;
                if (nextPermutation.length() == apartmentDwellers.length) {
                    set.add(nextPermutation);
                } else {
                    generatePermutations(apartmentDwellers, set, nextPermutation);
                }
            }
        }
    }

    private static boolean topFloor(String permutation, String person) { //Checks to see if the person is on the top floor
        return permutation.endsWith(person);
    }

    private static boolean bottomFloor(String permutation, String person) {//Checks to see if the person is on the bottom floor
        return permutation.startsWith(person);
    }

    public static boolean livesAbove(String permutation, String upperPerson, String lowerPerson) {//Checks to see if the person lives above the other person
        return permutation.indexOf(upperPerson) > permutation.indexOf(lowerPerson);
    }

    public static boolean adjacent(String permutation, String person1, String person2) { //checks to see if person1 is adjacent to person2
        return (Math.abs(permutation.indexOf(person1) - permutation.indexOf(person2)) == 1);
    }

    private static boolean isPossible(String s) {
        /*
         What this does should be obvious...proper explaination can be given if needed
         Conditions here Switching any of these to ! or reverse will change what is given as a result
        
         example 
         if(topFloor(s, "B"){
         }
         to
         if(!topFloor(s, "B"){
         }
         or the opposite
         if(!topFloor(s, "B"){
         }
         to
         if(topFloor(s, "B"){
         }
         */
        if (topFloor(s, "B")) {//B is on Top Floor
            return false;
        }
        if (bottomFloor(s, "C")) {//C is on Bottom Floor
            return false;
        }
        if (topFloor(s, "F") || bottomFloor(s, "F")) {// F is on top or bottom floor
            return false;
        }
        if (!livesAbove(s, "M", "C")) {// M does not live above C
            return false;
        }
        if (adjacent(s, "S", "F")) { //S lives adjacent to F
            return false;
        }
        return !adjacent(s, "F", "C"); //F does not live adjacent to C 
    }

    public static void main(String[] args) {
        Set<String> set = new HashSet<String>();
        generatePermutations(new String[]{"B", "C", "F", "M", "S"}, set, ""); //Generates Permutations
        for (Iterator<String> iterator = set.iterator(); iterator.hasNext();) {//Loops through iterator
            String permutation = iterator.next();
            if (!isPossible(permutation)) {//checks to see if permutation is false if so it removes it
                iterator.remove();
            }
        }
        for (String s : set) {
            System.out.println("Possible arrangement: " + s);
            /*
            Prints out possible arranagement...changes depending on what you change in the "isPossible method"
             */
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import re
from itertools import product

problem_re = re.compile(r"""(?msx)(?:

# Multiple names of form n1, n2, n3, ... , and nK
(?P<namelist> [a-zA-Z]+ (?: , \s+ [a-zA-Z]+)* (?: ,? \s+ and) \s+ [a-zA-Z]+ )

# Flexible floor count (2 to 10 floors)
| (?:  .* house \s+ that \s+ contains \s+ only \s+
  (?P<floorcount> two|three|four|five|six|seven|eight|nine|ten ) \s+ floors \s* \.)

# Constraint: "does not live on the n'th floor" 
|(?: (?P<not_live>  \b [a-zA-Z]+ \s+ does \s+ not \s+ live \s+ on \s+ the \s+
  (?: top|bottom|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth) \s+ floor \s* \. ))

# Constraint: "does not live on either the I'th or the J'th [ or the K'th ...] floor
|(?P<not_either> \b [a-zA-Z]+ \s+ does \s+ not \s+ live \s+ on \s+ either
  (?: \s+ (?: or \s+)? the \s+       
    (?: top|bottom|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth))+ \s+ floor \s* \. )

# Constraint: "P1 lives on a higher/lower floor than P2 does"
|(?P<hi_lower> \b  [a-zA-Z]+ \s+ lives \s+ on \s+ a \s (?: higher|lower)
   \s+ floor \s+ than (?: \s+ does)  \s+  [a-zA-Z]+ \s* \. )

# Constraint: "P1 does/does not live on a floor adjacent to P2's"
|(?P<adjacency>  \b [a-zA-Z]+ \s+ does (?:\s+ not)? \s+ live \s+ on \s+ a \s+
   floor \s+ adjacent \s+ to \s+  [a-zA-Z]+ (?: 's )? \s* \. )

# Ask for the solution
|(?P<question> Where \s+ does \s+ everyone \s+ live \s* \?)

)
""")

names, lennames = None, None
floors = None
constraint_expr = 'len(set(alloc)) == lennames' # Start with all people on different floors

def do_namelist(txt):
    " E.g. 'Baker, Cooper, Fletcher, Miller, and Smith'"
    global names, lennames
    names = txt.replace(' and ', ' ').split(', ')
    lennames = len(names)

def do_floorcount(txt):
    " E.g. 'five'"
    global floors
    floors = '||two|three|four|five|six|seven|eight|nine|ten'.split('|').index(txt)

def do_not_live(txt):
    " E.g. 'Baker does not live on the top floor.'"
    global constraint_expr
    t = txt.strip().split()
    who, floor = t[0], t[-2]
    w, f = (names.index(who),
            ('|first|second|third|fourth|fifth|sixth|' +
             'seventh|eighth|ninth|tenth|top|bottom|').split('|').index(floor)
            )
    if f == 11: f = floors
    if f == 12: f = 1
    constraint_expr += ' and alloc[%i] != %i' % (w, f)
    
def do_not_either(txt):
    " E.g. 'Fletcher does not live on either the top or the bottom floor.'"
    global constraint_expr
    t = txt.replace(' or ', ' ').replace(' the ', ' ').strip().split()
    who, floor = t[0], t[6:-1]
    w, fl = (names.index(who),
             [('|first|second|third|fourth|fifth|sixth|' +
               'seventh|eighth|ninth|tenth|top|bottom|').split('|').index(f)
              for f in floor]
             )
    for f in fl:
        if f == 11: f = floors
        if f == 12: f = 1
        constraint_expr += ' and alloc[%i] != %i' % (w, f)
    

def do_hi_lower(txt):
    " E.g. 'Miller lives on a higher floor than does Cooper.'"
    global constraint_expr
    t = txt.replace('.', '').strip().split()
    name_indices = [names.index(who) for who in (t[0], t[-1])]
    if 'lower' in t:
        name_indices = name_indices[::-1]
    constraint_expr += ' and alloc[%i] > alloc[%i]' % tuple(name_indices)
    
def do_adjacency(txt):
    ''' E.g. "Smith does not live on a floor adjacent to Fletcher's."'''
    global constraint_expr
    t = txt.replace('.', '').replace("'s", '').strip().split()
    name_indices = [names.index(who) for who in (t[0], t[-1])]
    constraint_expr += ' and abs(alloc[%i] - alloc[%i]) > 1' % tuple(name_indices)
    
def do_question(txt):
    global constraint_expr, names, lennames

    exec_txt = '''
for alloc in product(range(1,floors+1), repeat=len(names)):
    if %s:
        break
else:
    alloc = None
''' % constraint_expr
    exec(exec_txt, globals(), locals())
    a = locals()['alloc']
    if a:
        output= ['Floors are numbered from 1 to %i inclusive.' % floors]
        for a2n in zip(a, names):
            output += ['  Floor %i is occupied by %s' % a2n]
        output.sort(reverse=True)
        print('\n'.join(output))
    else:
        print('No solution found.')
    print()

handler = {
    'namelist': do_namelist,
    'floorcount': do_floorcount,
    'not_live': do_not_live,
    'not_either': do_not_either,
    'hi_lower': do_hi_lower,
    'adjacency': do_adjacency,
    'question': do_question,
    }
def parse_and_solve(problem):
    p = re.sub(r'\s+', ' ', problem).strip()
    for x in problem_re.finditer(p):
        groupname, txt = [(k,v) for k,v in x.groupdict().items() if v][0]
        #print ("%r, %r" % (groupname, txt))
        handler[groupname](txt)

```

### python_code_2.txt
```python
if __name__ == '__main__':  
    parse_and_solve("""
        Baker, Cooper, Fletcher, Miller, and Smith
        live on different floors of an apartment house that contains
        only five floors. Baker does not live on the top floor. Cooper
        does not live on the bottom floor. Fletcher does not live on
        either the top or the bottom floor. Miller lives on a higher
        floor than does Cooper. Smith does not live on a floor
        adjacent to Fletcher's. Fletcher does not live on a floor
        adjacent to Cooper's. Where does everyone live?""")

    print('# Add another person with more constraints and more floors:')
    parse_and_solve("""
        Baker, Cooper, Fletcher, Miller, Guinan, and Smith
        live on different floors of an apartment house that contains
        only seven floors. Guinan does not live on either the top or the third or the fourth floor.
        Baker does not live on the top floor. Cooper
        does not live on the bottom floor. Fletcher does not live on
        either the top or the bottom floor. Miller lives on a higher
        floor than does Cooper. Smith does not live on a floor
        adjacent to Fletcher's. Fletcher does not live on a floor
        adjacent to Cooper's. Where does everyone live?""")

```

### python_code_3.txt
```python
from amb import Amb
 
if __name__ == '__main__':
    amb = Amb()

    maxfloors = 5
    floors = range(1, maxfloors+1)
    # Possible floors for each person
    Baker, Cooper, Fletcher, Miller, Smith = (amb(floors) for i in range(5))
    for _dummy in amb( lambda Baker, Cooper, Fletcher, Miller, Smith: (
                         len(set([Baker, Cooper, Fletcher, Miller, Smith])) == 5  # each to a separate floor
                         and Baker != maxfloors
                         and Cooper != 1
                         and Fletcher not in (maxfloors, 1)
                         and Miller > Cooper
                         and (Smith - Fletcher) not in (1, -1)  # Not adjacent
                         and (Fletcher - Cooper) not in (1, -1) # Not adjacent
                         ) ):

        print 'Floors are numbered from 1 to %i inclusive.' % maxfloors
        print '\n'.join(sorted('  Floor %i is occupied by %s'
                                   % (globals()[name], name)
                               for name in 'Baker, Cooper, Fletcher, Miller, Smith'.split(', ')))
        break
    else:
        print 'No solution found.'
    print

                       
    print '# Add another person with more constraints and more floors:'
    # The order that Guinan is added to any list of people must stay consistant
    
    amb = Amb()

    maxfloors = 7
    floors = range(1, maxfloors+1)
    # Possible floors for each person
    Baker, Cooper, Fletcher, Miller, Guinan, Smith = (amb(floors) for i in range(6))
    for _dummy in amb( lambda Baker, Cooper, Fletcher, Miller, Guinan, Smith: (
                         len(set([Baker, Cooper, Fletcher, Miller, Guinan, Smith])) == 6  # each to a separate floor
                         and Guinan not in (maxfloors, 3, 4)
                         and Baker != maxfloors
                         and Cooper != 1
                         and Fletcher not in (maxfloors, 1)
                         and Miller > Cooper
                         and (Smith - Fletcher) not in (1, -1)  # Not adjacent
                         and (Fletcher - Cooper) not in (1, -1) # Not adjacent
                         ) ):

        print 'Floors are numbered from 1 to %i inclusive.' % maxfloors
        print '\n'.join(sorted('  Floor %i is occupied by %s'
                                   % (globals()[name], name)
                               for name in 'Baker, Cooper, Fletcher, Miller, Guinan, Smith'.split(', ')))
        break
    else:
        print 'No solution found.'
    print

```

### python_code_4.txt
```python
from itertools import permutations

class Names:
    Baker, Cooper, Fletcher, Miller, Smith = range(5)
    seq = [Baker, Cooper, Fletcher, Miller, Smith]
    strings = "Baker Cooper Fletcher Miller Smith".split()

predicates = [
    lambda s: s[Names.Baker] != len(s)-1,
    lambda s: s[Names.Cooper] != 0,
    lambda s: s[Names.Fletcher] != 0 and s[Names.Fletcher] != len(s)-1,
    lambda s: s[Names.Miller] > s[Names.Cooper],
    lambda s: abs(s[Names.Smith] - s[Names.Fletcher]) != 1,
    lambda s: abs(s[Names.Cooper] - s[Names.Fletcher]) != 1];

for sol in permutations(Names.seq):
    if all(p(sol) for p in predicates):
        print(" ".join(x for x, y in sorted(zip(Names.strings, sol), key=lambda x: x[1])))

```

### python_code_5.txt
```python
'''Dinesman's multiple-dwelling problem'''

from itertools import permutations

print([
    (
        'Baker on ' + str(b),
        'Cooper on ' + str(c),
        'Fletcher on ' + str(f),
        'Miller on ' + str(m),
        'Smith on ' + str(s)
    ) for [b, c, f, m, s] in permutations(range(1, 6))
    if all([
        5 != b,
        1 != c,
        1 != f,
        5 != f,
        c < m,
        1 < abs(s - f),
        1 < abs(c - f)
    ])
])

```

### python_code_6.txt
```python
'''Dinesman's multiple-dwelling problem'''

from itertools import chain, permutations


# main :: IO ()
def main():
    '''Solution or null result.'''
    print(report(
        concatMap(dinesman)(
            permutations(range(1, 6))
        )
    ))


# dinesman :: (Int, Int, Int, Int, Int) -> [(Int, Int, Int, Int, Int)]
def dinesman(bcfms):
    '''A list containing the given permutation of five
       integers if it matches all the dinesman conditions,
       or an empty list if it does not.
    '''
    [b, c, f, m, s] = bcfms
    return [bcfms] if all([
        5 != b,
        1 != c,
        1 != f,
        5 != f,
        c < m,
        1 < abs(s - f),
        1 < abs(c - f)
    ]) else []


# report :: [(Int, Int, Int, Int, Int)] ->  String
def report(xs):
    '''A message summarizing the first (if any) solution found.
    '''
    return ', '.join(list(map(
        lambda k, n: k + ' in ' + str(n),
        ['Baker', 'Cooper', 'Fletcher', 'Miller', 'Smith'],
        xs[0]
    ))) + '.' if xs else 'No solution found.'


# GENERAL -------------------------------------------------

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been mapped.
       The list monad can be derived by using a function f which
       wraps its output in a list,
       (using an empty list to represent computational failure).
    '''
    return lambda xs: list(
        chain.from_iterable(map(f, xs))
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

