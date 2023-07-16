# List rooted trees

## Task Link
[Rosetta Code - List rooted trees](https://rosettacode.org/wiki/List_rooted_trees)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class ListRootedTrees {
    private static final List<Long> TREE_LIST = new ArrayList<>();

    private static final List<Integer> OFFSET = new ArrayList<>();

    static {
        for (int i = 0; i < 32; i++) {
            if (i == 1) {
                OFFSET.add(1);
            } else {
                OFFSET.add(0);
            }
        }
    }

    private static void append(long t) {
        TREE_LIST.add(1 | (t << 1));
    }

    private static void show(long t, int l) {
        while (l-- > 0) {
            if (t % 2 == 1) {
                System.out.print('(');
            } else {
                System.out.print(')');
            }
            t = t >> 1;
        }
    }

    private static void listTrees(int n) {
        for (int i = OFFSET.get(n); i < OFFSET.get(n + 1); i++) {
            show(TREE_LIST.get(i), n * 2);
            System.out.println();
        }
    }

    private static void assemble(int n, long t, int sl, int pos, int rem) {
        if (rem == 0) {
            append(t);
            return;
        }

        var pp = pos;
        var ss = sl;

        if (sl > rem) {
            ss = rem;
            pp = OFFSET.get(ss);
        } else if (pp >= OFFSET.get(ss + 1)) {
            ss--;
            if (ss == 0) {
                return;
            }
            pp = OFFSET.get(ss);
        }

        assemble(n, t << (2 * ss) | TREE_LIST.get(pp), ss, pp, rem - ss);
        assemble(n, t, ss, pp + 1, rem);
    }

    private static void makeTrees(int n) {
        if (OFFSET.get(n + 1) != 0) {
            return;
        }
        if (n > 0) {
            makeTrees(n - 1);
        }
        assemble(n, 0, n - 1, OFFSET.get(n - 1), n - 1);
        OFFSET.set(n + 1, TREE_LIST.size());
    }

    private static void test(int n) {
        if (n < 1 || n > 12) {
            throw new IllegalArgumentException("Argument must be between 1 and 12");
        }

        append(0);

        makeTrees(n);
        System.out.printf("Number of %d-trees: %d\n", n, OFFSET.get(n + 1) - OFFSET.get(n));
        listTrees(n);
    }

    public static void main(String[] args) {
        test(5);
    }
}

```

## Python Code
### python_code_1.txt
```python
def bags(n,cache={}):
	if not n: return [(0, "")]

	upto = sum([bags(x) for x in range(n-1, 0, -1)], [])
	return [(c+1, '('+s+')') for c,s in bagchain((0, ""), n-1, upto)]

def bagchain(x, n, bb, start=0):
	if not n: return [x]

	out = []
	for i in range(start, len(bb)):
		c,s = bb[i]
		if c <= n: out += bagchain((x[0] + c, x[1] + s), n-c, bb, i)
	return out

# Maybe this lessens eye strain. Maybe not.
def replace_brackets(s):
	depth,out = 0,[]
	for c in s:
		if c == '(':
			out.append("([{"[depth%3])
			depth += 1
		else:
			depth -= 1
			out.append(")]}"[depth%3])
	return "".join(out)

for x in bags(5): print(replace_brackets(x[1]))

```

### python_code_2.txt
```python
treeid = {(): 0}

'''
Successor of a tree.  The predecessor p of a tree t is:

  1. if the smallest subtree of t is a single node, then p is t minus that node
  2. otherwise, p is t with its smalles subtree "m" replaced by m's predecessor

Here "smaller" means the tree is generated earlier, as recorded by treeid. Obviously,
predecessor to a tree is unique.  Since every degree n tree has a
unique degree (n-1) predecessor, inverting the process leads to the successors
to tree t:

  1. append a single node tree to t's root, or
  2. replace t's smallest subtree by its successors

We need to keep the trees so generated canonical, so when replacing a subtree,
the replacement must not be larger than the next smallest subtree.

Note that trees can be compared by other means, as long as trees with fewer nodes
are considered smaller, and trees with the same number of nodes have a fixed order.
'''
def succ(x):
    yield(((),) + x)
    if not x: return

    if len(x) == 1:
        for i in succ(x[0]): yield((i,))
        return

    head,rest = x[0],tuple(x[1:])
    top = treeid[rest[0]]

    for i in [i for i in succ(head) if treeid[i] <= top]:
        yield((i,) + rest)

def trees(n):
    if n == 1:
        yield()
        return

    global treeid
    for x in trees(n-1):
        for a in succ(x):
            if not a in treeid: treeid[a] = len(treeid)
            yield(a)

def tostr(x): return "(" + "".join(map(tostr, x)) + ")"

for x in trees(5): print(tostr(x))

```

