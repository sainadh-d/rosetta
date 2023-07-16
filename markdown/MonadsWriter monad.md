# Monads/Writer monad

## Task Link
[Rosetta Code - Monads/Writer monad](https://rosettacode.org/wiki/Monads/Writer_monad)

## Java Code
### java_code_1.txt
```java
import java.util.function.Function;

public final class MonadWriter {

	public static void main(String[] aArgs) {
		Monad<Double> initial = Monad.unit(5.0, "Initial value");
	    Monad<Double> result = initial.bind(MonadWriter::root).bind(MonadWriter::addOne).bind(MonadWriter::half);
	    System.out.println("The Golden Ratio is " + result.getValue() + System.lineSeparator());
	    System.out.println("This was derived as follows:"  + System.lineSeparator() + result.getText());
	}
	
	private static Monad<Double> root(double aD) {
		return Monad.unit(Math.sqrt(aD), "Took square root");
	}

	private static Monad<Double> addOne(double aD) {
		return Monad.unit(aD + 1.0, "Added one");
	}

	private static Monad<Double> half(double aD) {
		return Monad.unit(aD / 2.0, "Divided by two");
	}
	
}
	
final class Monad<T> {		
	
	public static <T> Monad<T> unit(T aValue, String aText) {
		return new Monad<T>(aValue, aText);
	}
	
	public Monad<T> bind(Function<T, Monad<T>> aFunction) {
		Monad<T> monad = aFunction.apply(value);
		monad.text = text + monad.text;
		return monad;
	}
	
	public T getValue() {
		return value;
	}
	
	public String getText() {
		return text;
	}
	
	private Monad(T aValue, String aText) {
		value = aValue;
		text = String.format("%-21s%s%n", "    " + aText, ": " + aValue);
	}
	
	private T value;
	private String text;
	
}

```

## Python Code
### python_code_1.txt
```python
"""A Writer Monad. Requires Python >= 3.7 for type hints."""
from __future__ import annotations

import functools
import math
import os

from typing import Any
from typing import Callable
from typing import Generic
from typing import List
from typing import TypeVar
from typing import Union


T = TypeVar("T")


class Writer(Generic[T]):
    def __init__(self, value: Union[T, Writer[T]], *msgs: str):
        if isinstance(value, Writer):
            self.value: T = value.value
            self.msgs: List[str] = value.msgs + list(msgs)
        else:
            self.value = value
            self.msgs = list(f"{msg}: {self.value}" for msg in msgs)

    def bind(self, func: Callable[[T], Writer[Any]]) -> Writer[Any]:
        writer = func(self.value)
        return Writer(writer, *self.msgs)

    def __rshift__(self, func: Callable[[T], Writer[Any]]) -> Writer[Any]:
        return self.bind(func)

    def __str__(self):
        return f"{self.value}\n{os.linesep.join(reversed(self.msgs))}"

    def __repr__(self):
        return f"Writer({self.value}, \"{', '.join(reversed(self.msgs))}\")"


def lift(func: Callable, msg: str) -> Callable[[Any], Writer[Any]]:
    """Return a writer monad version of the simple function `func`."""

    @functools.wraps(func)
    def wrapped(value):
        return Writer(func(value), msg)

    return wrapped


if __name__ == "__main__":
    square_root = lift(math.sqrt, "square root")
    add_one = lift(lambda x: x + 1, "add one")
    half = lift(lambda x: x / 2, "div two")

    print(Writer(5, "initial") >> square_root >> add_one >> half)

```

