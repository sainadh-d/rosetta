# Odd word problem

## Task Link
[Rosetta Code - Odd word problem](https://rosettacode.org/wiki/Odd_word_problem)

## Java Code
### java_code_1.txt
```java
public class OddWord {
    interface CharHandler {
	CharHandler handle(char c) throws Exception;
    }
    final CharHandler fwd = new CharHandler() {
	public CharHandler handle(char c) {
	    System.out.print(c);
	    return (Character.isLetter(c) ? fwd : rev);
	}
    };
    class Reverser extends Thread implements CharHandler {
	Reverser() {
	    setDaemon(true);
	    start();
	}
	private Character ch; // For inter-thread comms
	private char recur() throws Exception {
	    notify();
	    while (ch == null) wait();
	    char c = ch, ret = c;
	    ch = null;
	    if (Character.isLetter(c)) {
		ret = recur();
		System.out.print(c);
	    }
	    return ret;
	}
	public synchronized void run() {
	    try {
		while (true) {
		    System.out.print(recur());
		    notify();
		}
	    } catch (Exception e) {}
	}
	public synchronized CharHandler handle(char c) throws Exception {
	    while (ch != null) wait();
	    ch = c;
	    notify();
	    while (ch != null) wait();
	    return (Character.isLetter(c) ? rev : fwd);
	}
    }
    final CharHandler rev = new Reverser();

    public void loop() throws Exception {
	CharHandler handler = fwd;
	int c;
	while ((c = System.in.read()) >= 0) {
	    handler = handler.handle((char) c);
	}
    }

    public static void main(String[] args) throws Exception {
	new OddWord().loop();
    }
}

```

## Python Code
### python_code_1.txt
```python
from sys import stdin, stdout

def char_in(): return stdin.read(1)
def char_out(c): stdout.write(c)

def odd(prev = lambda: None):
	a = char_in()
	if not a.isalpha():
		prev()
		char_out(a)
		return a != '.'

	# delay action until later, in the shape of a closure
	def clos():
		char_out(a)
		prev()

	return odd(clos)

def even():
	while True:
		c = char_in()
		char_out(c)
		if not c.isalpha(): return c != '.'

e = False
while odd() if e else even():
	e = not e

```

### python_code_2.txt
```python
from sys import stdin, stdout

def char_in(): return stdin.read(1)
def char_out(c): stdout.write(c)

def odd():
	a = char_in()
	if a.isalpha():
		r = odd()
		char_out(a)
		return r

	# delay printing terminator until later, in the shape of a closure
	def clos():
		char_out(a)
		return a != '.'

	return clos

def even():
	while True:
		c = char_in()
		char_out(c)
		if not c.isalpha(): return c != '.'

e = False
while odd()() if e else even():
	e = not e

```

### python_code_3.txt
```python
from sys import stdin, stdout

def fwd(c):
    if c.isalpha():
        return [stdout.write(c), (yield from fwd((yield f)))][1]
    else:
        return c

def rev(c):
    if c.isalpha():
        return [(yield from rev((yield r))), stdout.write(c)][0]
    else:
        return c

def fw():
    while True:
        stdout.write((yield from fwd((yield r))))

def re():
    while True:
        stdout.write((yield from rev((yield f))))

f = fw()
r = re()
next(f)
next(r)

coro = f
while True:
    c = stdin.read(1)
    if not c:
        break
    coro = coro.send(c)

```

