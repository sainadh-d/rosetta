# Intersecting number wheels

## Task Link
[Rosetta Code - Intersecting number wheels](https://rosettacode.org/wiki/Intersecting_number_wheels)

## Java Code
### java_code_1.txt
```java
package intersectingNumberWheels;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.IntStream;

public class WheelController {
	private static final String IS_NUMBER = "[0-9]";
	private static final int TWENTY = 20;
	private static Map<String, WheelModel> wheelMap;

	public static void advance(String wheel) {
		WheelModel w = wheelMap.get(wheel);
		if (w.list.get(w.position).matches(IS_NUMBER)) {
			w.printThePosition();
			w.advanceThePosition();
		} else {
			String wheelName = w.list.get(w.position);
			advance(wheelName);
			w.advanceThePosition();
		}
	}

	public static void run() {
		System.out.println(wheelMap);
		IntStream.rangeClosed(1, TWENTY).forEach(i -> advance("A"));
		System.out.println();
		wheelMap.clear();
	}

	public static void main(String[] args) {
		wheelMap = new HashMap<>();
		wheelMap.put("A", new WheelModel("A", "1", "2", "3"));
		run();
		wheelMap.put("A", new WheelModel("A", "1", "B", "2"));
		wheelMap.put("B", new WheelModel("B", "3", "4"));
		run();
		wheelMap.put("A", new WheelModel("A", "1", "D", "D"));
		wheelMap.put("D", new WheelModel("D", "6", "7", "8"));
		run();
		wheelMap.put("A", new WheelModel("A", "1", "B", "C"));
		wheelMap.put("B", new WheelModel("B", "3", "4"));
		wheelMap.put("C", new WheelModel("C", "5", "B"));
		run();
	}

}

class WheelModel {
	String name;
	List<String> list;
	int position;
	int endPosition;
	private static final int INITIAL = 0;

	public WheelModel(String name, String... values) {
		super();

		this.name = name.toUpperCase();
		this.list = new ArrayList<>();
		for (String value : values) {
			list.add(value);
		}
		this.position = INITIAL;
		this.endPosition = this.list.size() - 1;
	}

	@Override
	public String toString() {
		return list.toString();
	}

	public void advanceThePosition() {
		if (this.position == this.endPosition) {
			this.position = INITIAL;// new beginning
		} else {
			this.position++;// advance position
		}
	}

	public void printThePosition() {
		System.out.print(" " + this.list.get(position));
	}
}

```

## Python Code
### python_code_1.txt
```python
from itertools import islice

class INW():
    """
    Intersecting Number Wheels
    represented as a dict mapping
    name to tuple of values.
    """

    def __init__(self, **wheels):
        self._wheels = wheels
        self.isect = {name: self._wstate(name, wheel) 
                      for name, wheel in wheels.items()}
    
    def _wstate(self, name, wheel):
        "Wheel state holder"
        assert all(val in self._wheels for val in wheel if type(val) == str), \
               f"ERROR: Interconnected wheel not found in {name}: {wheel}"
        pos = 0
        ln = len(wheel)
        while True:
            nxt, pos = wheel[pos % ln], pos + 1
            yield next(self.isect[nxt]) if type(nxt) == str else nxt
                
    def __iter__(self):
        base_wheel_name = next(self.isect.__iter__())
        yield from self.isect[base_wheel_name]
        
    def __repr__(self):
        return f"{self.__class__.__name__}({self._wheels})"
    
    def __str__(self):
        txt = "Intersecting Number Wheel group:"
        for name, wheel in self._wheels.items():
            txt += f"\n  {name+':':4}" + ' '.join(str(v) for v in wheel)
        return txt

def first(iter, n):
    "Pretty print first few terms"
    return ' '.join(f"{nxt}" for nxt in islice(iter, n))

if __name__ == '__main__':
    for group in[
      {'A': (1, 2, 3)},
      {'A': (1, 'B', 2),
       'B': (3, 4)},
      {'A': (1, 'D', 'D'),
       'D': (6, 7, 8)},
      {'A': (1, 'B', 'C'),
       'B': (3, 4),
       'C': (5, 'B')}, # 135143145...
     ]:
        w = INW(**group)
        print(f"{w}\n  Generates:\n    {first(w, 20)} ...\n")

```

### python_code_2.txt
```python
def nextfrom(w, name):
    while True:
        nxt, w[name] = w[name][0], w[name][1:] + w[name][:1]
        if '0' <= nxt[0] <= '9':
            return nxt
        name = nxt
            
if __name__ == '__main__':
    for group in '''
A: 1 2 3
A: 1 B 2; B: 3 4
A: 1 D D; D: 6 7 8
A: 1 B C; B: 3 4; C: 5 B'''.strip().split('\n'):
        print(f"Intersecting Number Wheel group:\n  {group}")
        wheel, first = {}, None
        for w in group.strip().split(';'):
            name, *values = w.strip().split()
            wheel[name[:-1]] = values
            first = name[:-1] if first is None else first
        gen = ' '.join(nextfrom(wheel, first) for i in range(20))
        print(f"  Generates:\n    {gen} ...\n")

```

### python_code_3.txt
```python
def nextfromr(w, name):
    nxt, w[name] = w[name][0], w[name][1:] + w[name][:1]
    return nxt if '0' <= nxt[0] <= '9' else nextfromr(w, nxt)
            
if __name__ == '__main__':
    for group in [{'A': '123'},
                  {'A': '1B2', 'B': '34'},
                  {'A': '1DD', 'D': '678'},
                  {'A': '1BC', 'B': '34', 'C': '5B'},]:
        print(f"Intersecting Number Wheel group:\n  {group}")
        first = next(group.__iter__())
        gen = ' '.join(nextfromr(group, first) for i in range(20))
        print(f"  Generates:\n   {gen} ...\n")

```

### python_code_4.txt
```python
'''Intersecting number wheels'''

from itertools import cycle, islice
from functools import reduce


# clockWorkTick :: Dict -> (Dict, Char)
def clockWorkTick(wheelMap):
    '''The new state of the wheels, tupled with a
       digit found by recursive descent from a single
       click of the first wheel.'''
    def click(wheels):
        def go(wheelName):
            wheel = wheels.get(wheelName, ['?'])
            v = wheel[0]
            return (Tuple if v.isdigit() or '?' == v else click)(
                insertDict(wheelName)(leftRotate(wheel))(wheels)
            )(v)
        return go
    return click(wheelMap)('A')


# leftRotate :: [a] -> String
def leftRotate(xs):
    ''' A string shifted cyclically towards
        the left by one position.
    '''
    return ''.join(islice(cycle(xs), 1, 1 + len(xs)))


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''First twenty values from each set of test wheels.'''

    wheelMaps = [dict(kvs) for kvs in [
        [('A', "123")],
        [('A', "1B2"), ('B', "34")],
        [('A', "1DD"), ('D', "678")],
        [('A', "1BC"), ('B', "34"), ('C', "5B")]
    ]]
    print('New state of wheel sets, after 20 clicks of each:\n')
    for wheels, series in [
            mapAccumL(compose(const)(clockWorkTick))(
                dct
            )(' ' * 20) for dct in wheelMaps
    ]:
        print((wheels, ''.join(series)))

    print('\nInital states:')
    for x in wheelMaps:
        print(x)


# ----------------------- GENERIC ------------------------

# Tuple (,) :: a -> b -> (a, b)
def Tuple(x):
    '''Constructor for a pair of values,
       possibly of two different types.
    '''
    return lambda y: (
        x + (y,)
    ) if isinstance(x, tuple) else (x, y)


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# const :: a -> b -> a
def const(k):
    '''The latter of two arguments,
       with the first discarded.
    '''
    return lambda _: k


# insertDict :: String -> a -> Dict -> Dict
def insertDict(k):
    '''A new dictionary updated with a (k, v) pair.'''
    def go(v, dct):
        return dict(dct, **{k: v})
    return lambda v: lambda dct: go(v, dct)


# mapAccumL :: (acc -> x -> (acc, y)) -> acc -> [x] -> (acc, [y])
def mapAccumL(f):
    '''A tuple of an accumulation and a map
       with accumulation from left to right.
    '''
    def nxt(a, x):
        tpl = f(a[0])(x)
        return tpl[0], a[1] + [tpl[1]]

    def go(acc):
        def g(xs):
            return reduce(nxt, xs, (acc, []))
        return g
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

