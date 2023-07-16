# 99 bottles of beer

## Task Link
[Rosetta Code - 99 bottles of beer](https://rosettacode.org/wiki/99_bottles_of_beer)

## Java Code
### java_code_2.txt
```java
import java.text.MessageFormat;

public class Beer {
    static String bottles(int n) {
        return MessageFormat.format("{0,choice,0#No more bottles|1#One bottle|2#{0} bottles} of beer", n);
    }

    public static void main(String[] args) {
        String bottles = bottles(99);
        for (int n = 99; n > 0; ) {
            System.out.println(bottles + " on the wall");
            System.out.println(bottles);
            System.out.println("Take one down, pass it around");
            bottles = bottles(--n);
            System.out.println(bottles + " on the wall");
            System.out.println();
        }
    }
}

```

### java_code_3.txt
```java
public class Beer {
    public static void main(String[] args) {
        int bottles = 99;
        StringBuilder sb = new StringBuilder();
        String verse1 = " bottles of beer on the wall\n";
        String verse2 = " bottles of beer.\nTake one down, pass it around,\n";
        String verse3 = "Better go to the store and buy some more.";

        while (bottles > 0)
            sb.append(bottles).append(verse1).append(bottles).append(verse2).append(--bottles).append(verse1).append("\n");

        System.out.println(sb.append(verse3));
    }
}

```

### java_code_4.txt
```java
public class Beer {
    public static void main(String args[]) {
        song(99);
    }

    public static void song(int bottles) {
        if (bottles >= 0) {
            if (bottles > 1)
                System.out.println(bottles + " bottles of beer on the wall\n" + bottles + " bottles of beer\nTake one down, pass it around\n" + (bottles - 1) + " bottles of beer on the wall.\n");
            else if (bottles == 1)
                System.out.println(bottles + " bottle of beer on the wall\n" + bottles + " bottle of beer\nTake one down, pass it around\n" + (bottles - 1) + " bottles of beer on the wall.\n");
            else
                System.out.println(bottles + " bottles of beer on the wall\n" + bottles + " bottles of beer\nBetter go to the store and buy some more!");
            song(bottles - 1);
        }
    }
}

```

### java_code_5.txt
```java
import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;

public class Beer extends JFrame {
    private int x;
    private JTextArea text;

    public static void main(String[] args) {
        new Beer().setVisible(true);
    }

    public Beer() {
        x = 99;
        
        JButton take = new JButton("Take one down, pass it around");
        take.addActionListener(this::onTakeClick);
        
        text = new JTextArea(4, 30);
        text.setText(x + " bottles of beer on the wall\n" + x + " bottles of beer");
        text.setEditable(false);
        
        setLayout(new BorderLayout());
        add(text, BorderLayout.CENTER);
        add(take, BorderLayout.PAGE_END);
        pack();
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
    }

    private void onTakeClick(ActionEvent event) {
        JOptionPane.showMessageDialog(null, --x + " bottles of beer on the wall");
        text.setText(x + " bottles of beer on the wall\n" + x + " bottles of beer");
        if (x == 0) {
            dispose();
        }
    }
}

```

### java_code_6.txt
```java
int i = 99;
void setup() {
  size(200, 140);
}
void draw() {
  background(0);
  text(i + " bottles of beer on the wall\n"
     + i + " bottles of beer\nTake one down, pass it around\n"
 + (i-1) + " bottles of beer on the wall\n\n", 
    10, 20);
  if (frameCount%240==239) next();  // auto-advance every 4 secs
}
void mouseReleased() {
  next();  // manual advance
}
void next() {
  i = max(i-1, 1);  // stop decreasing at 1-0 bottles
}

```

## Python Code
### python_code_2.txt
```python
i = 99
def setup():
    size(200, 140)

def draw():
    background(0)
    text("{} bottles of beer on the wall\n".format(i) +
         "{} bottles of beer\n".format(i) + 
         "Take one down, pass it around\n" +
         "{} bottles of beer on the wall\n\n".format(i - 1),
         10, 20)
    if frameCount % 240 == 239:  # auto-advance every 4 secs
         next()
         
def mouseReleased():
    next()  # manual advance

def next():
    global i
    i = max(i - 1, 1)  # stop decreasing at 1-0 bottles

```

### python_code_3.txt
```python
for i in range(99, 0, -1):b='bottles of beer';w=f' {b} on the wall';print(f'{i}{w}, {i} {b}\nTake one down and pass it around, {i-1}{w}.\n')

```

### python_code_4.txt
```python
VERSE = '''\
{n} bottle{s} of beer on the wall
{n} bottle{s} of beer
Take one down, pass it around
{n_minus_1} bottle{s2} of beer on the wall

'''


for n in range(99, 0, -1):
    if n == 1:
        n_minus_1 = 'No more'
        s = ''
        s2 = 's'
    elif n == 2:
        n_minus_1 = n - 1;
        s = 's'
        s2 = ''
    else:
        n_minus_1 = n - 1;
        s = 's'
        s2 = 's'
    
    
    print(VERSE.format(n=n, s=s, s2=s2, n_minus_1=n_minus_1))

```

### python_code_5.txt
```python
'''99 Units of Disposable Asset'''


from itertools import chain


# main :: IO ()
def main():
    '''Modalised asset dispersal procedure.'''

    # localisation :: (String, String, String)
    localisation = (
        'on the wall',
        'Take one down, pass it around',
        'Better go to the store to buy some more'
    )

    print(unlines(map(
        incantation(localisation),
        enumFromThenTo(99)(98)(0)
    )))


# incantation :: (String, String, String) -> Int -> String
def incantation(localisation):
    '''Versification of asset disposal
       and inventory update.'''

    location, distribution, solution = localisation

    def inventory(n):
        return unwords([asset(n), location])
    return lambda n: solution if 0 == n else (
        unlines([
            inventory(n),
            asset(n),
            distribution,
            inventory(pred(n))
        ])
    )


# asset :: Int -> String
def asset(n):
    '''Quantified asset.'''
    def suffix(n):
        return [] if 1 == n else 's'
    return unwords([
        str(n),
        concat(reversed(concat(cons(suffix(n))(["elttob"]))))
    ])


# GENERIC -------------------------------------------------

# concat :: [[a]] -> [a]
# concat :: [String] -> String
def concat(xxs):
    '''The concatenation of all the elements in a list.'''
    xs = list(chain.from_iterable(xxs))
    unit = '' if isinstance(xs, str) else []
    return unit if not xs else (
        ''.join(xs) if isinstance(xs[0], str) else xs
    )


# cons :: a -> [a] -> [a]
def cons(x):
    '''Construction of a list from x as head,
       and xs as tail.'''
    return lambda xs: [x] + xs if (
        isinstance(xs, list)
    ) else chain([x], xs)


# enumFromThenTo :: Int -> Int -> Int -> [Int]
def enumFromThenTo(m):
    '''Integer values enumerated from m to n
       with a step defined by nxt-m.'''
    def go(nxt, n):
        d = nxt - m
        return list(range(m, d + n, d))
    return lambda nxt: lambda n: (
        go(nxt, n)
    )


# pred ::  Enum a => a -> a
def pred(x):
    '''The predecessor of a value. For numeric types, (- 1).'''
    return x - 1 if isinstance(x, int) else (
        chr(ord(x) - 1)
    )


# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.'''
    return '\n'.join(xs)


# unwords :: [String] -> String
def unwords(xs):
    '''A space-separated string derived from
       a list of words.'''
    return ' '.join(xs)


if __name__ == '__main__':
    main()

```

### python_code_6.txt
```python
"""
    99 Bottles of Beer on the Wall made functional
    
    Main function accepts a number of parameters, so you can specify a name of 
    the drink, its container and other things. English only.
"""

from functools import partial
from typing import Callable


def regular_plural(noun: str) -> str:
    """English rule to get the plural form of a word"""
    if noun[-1] == "s":
        return noun + "es"
    
    return noun + "s"


def beer_song(
    *,
    location: str = 'on the wall',
    distribution: str = 'Take one down, pass it around',
    solution: str = 'Better go to the store to buy some more!',
    container: str = 'bottle',
    plurifier: Callable[[str], str] = regular_plural,
    liquid: str = "beer",
    initial_count: int = 99,
) -> str:
    """
    Return the lyrics of the beer song
    :param location: initial location of the drink
    :param distribution: specifies the process of its distribution
    :param solution: what happens when we run out of drinks
    :param container: bottle/barrel/flask or other containers
    :param plurifier: function converting a word to its plural form
    :param liquid: the name of the drink in the given container
    :param initial_count: how many containers available initially
    """
    
    verse = partial(
        get_verse,
        initial_count = initial_count, 
        location = location,
        distribution = distribution,
        solution = solution,
        container = container,
        plurifier = plurifier,
        liquid = liquid,
    )
    
    verses = map(verse, range(initial_count, -1, -1))
    return '\n\n'.join(verses)


def get_verse(
    count: int,
    *,
    initial_count: str,
    location: str,
    distribution: str,
    solution: str,
    container: str,
    plurifier: Callable[[str], str],
    liquid: str,
) -> str:
    """Returns the verse for the given amount of drinks"""
    
    asset = partial(
        get_asset,
        container = container,
        plurifier = plurifier,
        liquid = liquid,
    )
    
    current_asset = asset(count)
    next_number = count - 1 if count else initial_count
    next_asset = asset(next_number)
    action = distribution if count else solution
    
    inventory = partial(
        get_inventory,
        location = location,
    )
    
    return '\n'.join((
        inventory(current_asset),
        current_asset,
        action,
        inventory(next_asset),
    ))


def get_inventory(
    asset: str,
    *,
    location: str,
) -> str:
    """
    Used to return the first or the fourth line of the verse

    >>> get_inventory("10 bottles of beer", location="on the wall")
    "10 bottles of beer on the wall"
    """
    return ' '.join((asset, location))


def get_asset(
    count: int,
    *,
    container: str,
    plurifier: Callable[[str], str],
    liquid: str,
) -> str:
    """
    Quantified asset
    
    >>> get_asset(0, container="jar", plurifier=regular_plural, liquid='milk')
    "No more jars of milk"
    """
    
    containers = plurifier(container) if count != 1 else container
    spelled_out_quantity = str(count) if count else "No more" 
    return ' '.join((spelled_out_quantity, containers, "of", liquid))


if __name__ == '__main__':
    print(beer_song())

```

### python_code_7.txt
```python
"""
Excercise of style. An overkill for the task :-D

1. OOP, with abstract class and implementation with much common magic methods
2. you can customize:
    a. the initial number
    b. the name of the item and its plural
    c. the string to display when there's no more items
    d. the normal action
    e. the final action
    f. the template used, for foreign languages
3. strofas of the song are created with multiprocessing
4. when you launch it as a script, you can specify an optional parameter for 
   the number of initial items
"""

from string import Template
from abc import ABC, abstractmethod
from multiprocessing.pool import Pool as ProcPool
from functools import partial
import sys

class Song(ABC):
    @abstractmethod
    def sing(self):
        """
        it must return the song as a text-like object
        """
        
        pass

class MuchItemsSomewhere(Song):
    eq_attrs = (
        "initial_number", 
        "zero_items", 
        "action1", 
        "action2", 
        "item", 
        "items", 
        "strofa_tpl"
    )
    
    hash_attrs = eq_attrs
    repr_attrs = eq_attrs
    
    __slots__ = eq_attrs + ("_repr", "_hash")
    
    def __init__(
        self, 
        items = "bottles of beer", 
        item = "bottle of beer",
        where = "on the wall",
        initial_number = None,
        zero_items = "No more",
        action1 = "Take one down, pass it around",
        action2 = "Go to the store, buy some more",
        template = None,
    ):
        initial_number_true = 99 if initial_number is None else initial_number
        
        try:
            is_initial_number_int = (initial_number_true % 1) == 0
        except Exception:
            is_initial_number_int = False
        
        if not is_initial_number_int:
            raise ValueError("`initial_number` parameter must be None or a int-like object")
        
        if initial_number_true < 0:
            raise ValueError("`initial_number` parameter must be >=0")
        
        
        true_tpl = template or """\
$i $items1 $where
$i $items1
$action
$j $items2 $where"""
        
        strofa_tpl_tmp = Template(true_tpl)
        strofa_tpl = Template(strofa_tpl_tmp.safe_substitute(where=where))
        
        self.zero_items = zero_items
        self.action1 = action1
        self.action2 = action2
        self.initial_number = initial_number_true
        self.item = item
        self.items = items
        self.strofa_tpl = strofa_tpl
        self._hash = None
        self._repr = None
    
    def strofa(self, number):
        zero_items = self.zero_items
        item = self.item
        items = self.items
        
        if number == 0:
            i = zero_items
            action = self.action2
            j = self.initial_number
        else:
            i = number
            action = self.action1
            j = i - 1
        
        if i == 1:
            items1 = item
            j = zero_items
        else:
            items1 = items
        
        if j == 1:
            items2 = item
        else:
            items2 = items
        
        return self.strofa_tpl.substitute(
            i = i, 
            j = j, 
            action = action, 
            items1 = items1, 
            items2 = items2
        )
    
    def sing(self):
        with ProcPool() as proc_pool:
            strofa = self.strofa
            initial_number = self.initial_number
            args = range(initial_number, -1, -1)
            return "\n\n".join(proc_pool.map(strofa, args))
    
    def __copy__(self, *args, **kwargs):
        return self
    
    def __deepcopy__(self, *args, **kwargs):
        return self
    
    def __eq__(self, other, *args, **kwargs):
        if self is other:
            return True
        
        getmyattr = partial(getattr, self)
        getotherattr = partial(getattr, other)
        eq_attrs = self.eq_attrs
        
        for attr in eq_attrs:
            val = getmyattr(attr)
            
            try:
                val2 = getotherattr(attr)
            except Exception:
                return False
            
            if attr == "strofa_tpl":
                val_true = val.safe_substitute()
                val2_true = val.safe_substitute()
            else:
                val_true = val
                val2_true = val
            
            if val_true != val2_true:
                return False
        
        return True
    
    def __hash__(self, *args, **kwargs):
        _hash = self._hash
        
        if _hash is None:
            getmyattr = partial(getattr, self)
            attrs = self.hash_attrs
            hash_true = self._hash = hash(tuple(map(getmyattr, attrs)))
        else:
            hash_true = _hash
        
        return hash_true
    
    def __repr__(self, *args, **kwargs):
        _repr = self._repr
        
        if _repr is None:
            repr_attrs = self.repr_attrs
            getmyattr = partial(getattr, self)
            
            attrs = []
            
            for attr in repr_attrs:
                val = getmyattr(attr)
                
                if attr == "strofa_tpl":
                    val_true = val.safe_substitute()
                else:
                    val_true = val
                
                attrs.append(f"{attr}={repr(val_true)}")
            
            repr_true = self._repr = f"{self.__class__.__name__}({', '.join(attrs)})"
        else:
            repr_true = _repr
        
        return repr_true

def muchBeersOnTheWall(num):
    song = MuchItemsSomewhere(initial_number=num)
    
    return song.sing()

def balladOfProgrammer(num):
    """
    Prints
    "99 Subtle Bugs in Production"
    or
    "The Ballad of Programmer"
    """
    
    song = MuchItemsSomewhere(
        initial_number = num,
        items = "subtle bugs",
        item = "subtle bug",
        where = "in Production",
        action1 = "Debug and catch, commit a patch",
        action2 = "Release the fixes, wait for some tickets",
        zero_items = "Zarro",
    )

    return song.sing()

def main(num):
    print(f"### {num} Bottles of Beers on the Wall ###")
    print()
    print(muchBeersOnTheWall(num))
    print()
    print()
    print('### "The Ballad of Programmer", by Marco Sulla')
    print()
    print(balladOfProgrammer(num))

if __name__ == "__main__":
    # Ok, argparse is **really** too much
    argv = sys.argv
    
    if len(argv) == 1:
        num = None
    elif len(argv) == 2:
        try:
            num = int(argv[1])
        except Exception:
            raise ValueError(
                f"{__file__} parameter must be an integer, or can be omitted"
            )
    else:
        raise RuntimeError(f"{__file__} takes one parameter at max")
    
    main(num)

__all__ = (Song.__name__, MuchItemsSomewhere.__name__, muchBeersOnTheWall.__name__, balladOfProgrammer.__name__)

```

