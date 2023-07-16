# History variables

## Task Link
[Rosetta Code - History variables](https://rosettacode.org/wiki/History_variables)

## Java Code
### java_code_1.txt
```java
public class HistoryVariable
{
    private Object value;

    public HistoryVariable(Object v)
    {
        value = v;
    }

    public void update(Object v)
    {
        value = v;
    }

    public Object undo()
    {
        return value;
    }

    @Override
    public String toString()
    {
        return value.toString();
    }

    public void dispose()
    {
    }
}

```

### java_code_2.txt
```java
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public privileged aspect HistoryHandling
{
    before() : execution(HistoryVariable.new(..))
    {
        history.put((HistoryVariable) thisJoinPoint.getTarget(), new LinkedList<>());
    }

    after() : execution(void HistoryVariable.dispose())
    {
        history.remove(thisJoinPoint.getTarget());
    }

    before(Object v) : execution(void HistoryVariable.update(Object)) && args(v)
    {
        final HistoryVariable hv = (HistoryVariable) thisJoinPoint.getThis();
        history.get(hv).add(hv.value);
    }

    after() : execution(Object HistoryVariable.undo())
    {
        final HistoryVariable hv = (HistoryVariable) thisJoinPoint.getThis();
        final Deque<Object> q = history.get(hv);
        if (!q.isEmpty())
            hv.value = q.pollLast();
    }

    String around() : this(HistoryVariable) && execution(String toString())
    {
        final HistoryVariable hv = (HistoryVariable) thisJoinPoint.getThis();
        final Deque<Object> q = history.get(hv);
        if (q == null)
            return "<disposed>";
        else
            return "current: "+ hv.value + ", previous: " + q.toString();
    }

    private Map<HistoryVariable, Deque<Object>> history = new HashMap<>();
}

```

### java_code_3.txt
```java
public final class Main
{
    public static void main(final String[] args)
    {
        HistoryVariable hv = new HistoryVariable("a");
        hv.update(90);
        hv.update(12.1D);
        System.out.println(hv.toString());
        System.out.println(hv.undo());
        System.out.println(hv.undo());
        System.out.println(hv.undo());
        System.out.println(hv.undo());
        System.out.println(hv.toString());
        hv.dispose();
        System.out.println(hv.toString());
    }
}

```

### java_code_4.txt
```java
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

/**
 * A class for an "Integer with a history".
 * <p>
 * Note that it is not possible to create an empty Variable (so there is no "null") with this type. This is a design
 * choice, because if "empty" variables were allowed, reading of empty variables must return a value. Null is a
 * bad idea, and Java 8's Optional<T> (which is somewhat like the the official fix for the null-bad-idea) would
 * make things more complicated than an example should be.
 */
public class IntegerWithHistory {

    /**
     * The "storage Backend" is a list of all values that have been ever assigned to this variable. The List is
     * populated front to back, so a new value is inserted at the start (position 0), and older values move toward the end.
     */
    private final List<Integer> history;

    /**
     * Creates this variable and assigns the initial value
     *
     * @param value initial value
     */
    public IntegerWithHistory(Integer value) {
        history = new LinkedList<>();
        history.add(value);
    }

    /**
     * Sets a new value, pushing the older ones back in the history
     *
     * @param value the new value to be assigned
     */
    public void set(Integer value) {
        //History is populated from the front to the back, so the freshest value is stored a position 0
        history.add(0, value);
    }

    /**
     * Gets the current value. Since history is populuated front to back, the current value is the first element
     * of the history.
     *
     * @return the current value
     */
    public Integer get() {
        return history.get(0);
    }

    /**
     * Gets the entire history all values that have been assigned to this variable.
     *
     * @return a List of all values, including the current one, ordered new to old
     */
    public List<Integer> getHistory() {
        return Collections.unmodifiableList(this.history);
    }

    /**
     * Rolls back the history one step, so the current value is removed from the history and replaced by it's predecessor.
     * This is a destructive operation! It is not possible to rollback() beyond the initial value!
     *
     * @return the value that had been the current value until history was rolled back.
     */
    public Integer rollback() {
        if (history.size() > 1) {
            return history.remove(0);
        } else {
            return history.get(0);
        }
    }
}

```

### java_code_5.txt
```java
public class TestIntegerWithHistory {

    public static void main(String[] args) {

        //creating and setting three different values
        IntegerWithHistory i = new IntegerWithHistory(3);
        i.set(42);
        i.set(7);

        //looking at current value and history
        System.out.println("The current value of i is :" + i.get());
        System.out.println("The history of i is :" + i.getHistory());

        //demonstrating rollback
        System.out.println("Rolling back:");
        System.out.println("returns what was the current value: " + i.rollback());
        System.out.println("after rollback: " + i.get());
        System.out.println("returns what was the current value: " + i.rollback());
        System.out.println("after rollback: " + i.get());
        System.out.println("Rolling back only works to the original value: " + i.rollback());
        System.out.println("Rolling back only works to the original value: " + i.rollback());
        System.out.println("So there is no way to 'null' the variable: " + i.get());

    }
}

```

### java_code_6.txt
```java
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

/**
 * A Generic class for an "Anything with a history".
 * <p>
 * Note that it is not possible to create an empty Variable (so there is no "null") with this type. This is a design
 * choice, because if "empty" variables were allowed, reading of empty variables must return a value. Null is a
 * bad idea, and Java 8's Optional<T> (which is somewhat like the the official fix for the null-bad-idea) would
 * make things more complicated than an example should be.
 * <p>
 * Also note that this "really works" only with constant Ts. If somebody keeps a reference to an assigned value,
 * and is able to modify the state of this value through the reference , this will not be reflected in the history!
 */
public class WithHistory<T> {

    /**
     * The "storage Backend" is a list of all values that have been ever assigned to this variable. The List is
     * populated front to back, so a new value is inserted at the start (position 0), and older values move toward the end.
     */
    private final List<T> history;

    /**
     * Creates this variable and assigns the initial value
     *
     * @param value initial value
     */
    public WithHistory(T value) {
        history = new LinkedList<>();
        history.add(value);
    }

    /**
     * Sets a new value, pushing the older ones back in the history
     *
     * @param value the new value to be assigned
     */
    public void set(T value) {
        //History is populated from the front to the back, so the freshest value is stored a position 0
        history.add(0, value);
    }

    /**
     * Gets the current value. Since history is populuated front to back, the current value is the first element
     * of the history.
     *
     * @return the current value
     */
    public T get() {
        return history.get(0);
    }

    /**
     * Gets the entire history all values that have been assigned to this variable.
     *
     * @return a List of all values, including the current one, ordered new to old
     */
    public List<T> getHistory() {
        return Collections.unmodifiableList(this.history);
    }

    /**
     * Rolls back the history one step, so the current value is removed from the history and replaced by it's predecessor.
     * This is a destructive operation! It is not possible to rollback() beyond the initial value!
     *
     * @return the value that had been the cueent value until history was rolled back.
     */
    public T rollback() {
        if (history.size() > 1) {
            return history.remove(0);
        } else {
            return history.get(0);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import sys

HIST = {}

def trace(frame, event, arg):
    for name,val in frame.f_locals.items():
        if name not in HIST:
            HIST[name] = []
        else:
            if HIST[name][-1] is val:
                continue
        HIST[name].append(val)
    return trace

def undo(name):
    HIST[name].pop(-1)
    return HIST[name][-1]

def main():
    a = 10
    a = 20

    for i in range(5):
        c = i

    print "c:", c, "-> undo x3 ->",
    c = undo('c')
    c = undo('c')
    c = undo('c')
    print c
    print 'HIST:', HIST

sys.settrace(trace)
main()

```

