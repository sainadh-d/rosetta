# Display an outline as a nested table

## Task Link
[Rosetta Code - Display an outline as a nested table](https://rosettacode.org/wiki/Display_an_outline_as_a_nested_table)

## Java Code
## Python Code
### python_code_1.txt
```python
"""Display an outline as a nested table. Requires Python >=3.6."""

import itertools
import re
import sys

from collections import deque
from typing import NamedTuple


RE_OUTLINE = re.compile(r"^((?: |\t)*)(.+)$", re.M)

COLORS = itertools.cycle(
    [
        "#ffffe6",
        "#ffebd2",
        "#f0fff0",
        "#e6ffff",
        "#ffeeff",
    ]
)


class Node:
    def __init__(self, indent, value, parent, children=None):
        self.indent = indent
        self.value = value
        self.parent = parent
        self.children = children or []

        self.color = None

    def depth(self):
        if self.parent:
            return self.parent.depth() + 1
        return -1

    def height(self):
        """Height of the subtree rooted at this node."""
        if not self.children:
            return 0
        return max(child.height() for child in self.children) + 1

    def colspan(self):
        if self.leaf:
            return 1
        return sum(child.colspan() for child in self.children)

    @property
    def leaf(self):
        return not bool(self.children)

    def __iter__(self):
        # Level order tree traversal.
        q = deque()
        q.append(self)
        while q:
            node = q.popleft()
            yield node
            q.extend(node.children)


class Token(NamedTuple):
    indent: int
    value: str


def tokenize(outline):
    """Generate ``Token``s from the given outline."""
    for match in RE_OUTLINE.finditer(outline):
        indent, value = match.groups()
        yield Token(len(indent), value)


def parse(outline):
    """Return the given outline as a tree of ``Node``s."""
    # Split the outline into lines and count the level of indentation.
    tokens = list(tokenize(outline))

    # Parse the tokens into a tree of nodes.
    temp_root = Node(-1, "", None)
    _parse(tokens, 0, temp_root)

    # Pad the tree so that all branches have the same depth.
    root = temp_root.children[0]
    pad_tree(root, root.height())

    return root


def _parse(tokens, index, node):
    """Recursively build a tree of nodes.

    Args:
        tokens (list): A collection of ``Token``s.
        index (int): Index of the current token.
        node (Node): Potential parent or sibling node.
    """
    # Base case. No more lines.
    if index >= len(tokens):
        return

    token = tokens[index]

    if token.indent == node.indent:
        # A sibling of node
        current = Node(token.indent, token.value, node.parent)
        node.parent.children.append(current)
        _parse(tokens, index + 1, current)

    elif token.indent > node.indent:
        # A child of node
        current = Node(token.indent, token.value, node)
        node.children.append(current)
        _parse(tokens, index + 1, current)

    elif token.indent < node.indent:
        # Try the node's parent until we find a sibling.
        _parse(tokens, index, node.parent)


def pad_tree(node, height):
    """Pad the tree with blank nodes so all branches have the same depth."""
    if node.leaf and node.depth() < height:
        pad_node = Node(node.indent + 1, "", node)
        node.children.append(pad_node)

    for child in node.children:
        pad_tree(child, height)


def color_tree(node):
    """Walk the tree and color each node as we go."""
    if not node.value:
        node.color = "#F9F9F9"
    elif node.depth() <= 1:
        node.color = next(COLORS)
    else:
        node.color = node.parent.color

    for child in node.children:
        color_tree(child)


def table_data(node):
    """Return an HTML table data element for the given node."""
    indent = "    "

    if node.colspan() > 1:
        colspan = f'colspan="{node.colspan()}"'
    else:
        colspan = ""

    if node.color:
        style = f'style="background-color: {node.color};"'
    else:
        style = ""

    attrs = " ".join([colspan, style])
    return f"{indent}<td{attrs}>{node.value}</td>"


def html_table(tree):
    """Return the tree as an HTML table."""
    # Number of columns in the table.
    table_cols = tree.colspan()

    # Running count of columns in the current row.
    row_cols = 0

    # HTML buffer
    buf = ["<table style='text-align: center;'>"]

    # Breadth first iteration.
    for node in tree:
        if row_cols == 0:
            buf.append("  <tr>")

        buf.append(table_data(node))
        row_cols += node.colspan()

        if row_cols == table_cols:
            buf.append("  </tr>")
            row_cols = 0

    buf.append("</table>")
    return "\n".join(buf)


def wiki_table_data(node):
    """Return an wiki table data string for the given node."""
    if not node.value:
        return "|  |"

    if node.colspan() > 1:
        colspan = f"colspan={node.colspan()}"
    else:
        colspan = ""

    if node.color:
        style = f'style="background: {node.color};"'
    else:
        style = ""

    attrs = " ".join([colspan, style])
    return f"| {attrs} | {node.value}"


def wiki_table(tree):
    """Return the tree as a wiki table."""
    # Number of columns in the table.
    table_cols = tree.colspan()

    # Running count of columns in the current row.
    row_cols = 0

    # HTML buffer
    buf = ['{| class="wikitable" style="text-align: center;"']

    for node in tree:
        if row_cols == 0:
            buf.append("|-")

        buf.append(wiki_table_data(node))
        row_cols += node.colspan()

        if row_cols == table_cols:
            row_cols = 0

    buf.append("|}")
    return "\n".join(buf)


def example(table_format="wiki"):
    """Write an example table to stdout in either HTML or Wiki format."""

    outline = (
        "Display an outline as a nested table.\n"
        "    Parse the outline to a tree,\n"
        "        measuring the indent of each line,\n"
        "        translating the indentation to a nested structure,\n"
        "        and padding the tree to even depth.\n"
        "    count the leaves descending from each node,\n"
        "        defining the width of a leaf as 1,\n"
        "        and the width of a parent node as a sum.\n"
        "            (The sum of the widths of its children)\n"
        "    and write out a table with 'colspan' values\n"
        "        either as a wiki table,\n"
        "        or as HTML."
    )

    tree = parse(outline)
    color_tree(tree)

    if table_format == "wiki":
        print(wiki_table(tree))
    else:
        print(html_table(tree))


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 1:
        table_format = args[0]
    else:
        table_format = "wiki"

    example(table_format)

```

### python_code_2.txt
```python
'''Display an outline as a nested table'''

from itertools import chain, cycle, takewhile
from functools import reduce
from operator import add


# wikiTablesFromOutline :: [String] -> String -> String
def wikiTablesFromOutline(colorSwatch):
    '''Wikitable markup for (colspan) tables representing
       the indentation of a given outline.
       Each key-line point (child of a tree root) has a
       distinct color, inherited by all its descendants.
       The first color in the swatch is for the root node.
       A sequence of tables is generated where the outline
       represents a forest rather than a singly-rooted tree.
    '''
    def go(outline):
        return '\n\n'.join([
            wikiTableFromTree(colorSwatch)(tree) for tree in
            forestFromLevels(
                indentLevelsFromLines(
                    outline.splitlines()
                )
            )
        ])
    return go


#  wikiTableFromTree :: [String] -> Tree String -> String
def wikiTableFromTree(colorSwatch):
    '''A wikitable rendered from a single tree.
    '''
    return compose(
        wikiTableFromRows,
        levels,
        paintedTree(colorSwatch),
        widthMeasuredTree,
        ap(paddedTree(""))(treeDepth)
    )


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''A colored wikitable rendering of a given outline'''

    outline = '''Display an outline as a nested table.
    Parse the outline to a tree,
        measuring the indent of each line,
        translating the indentation to a nested structure,
        and padding the tree to even depth.
    count the leaves descending from each node,
        defining the width of a leaf as 1,
        and the width of a parent node as a sum.
            (The sum of the widths of its children)
    and write out a table with 'colspan' values
        either as a wiki table,
        or as HTML.'''

    print(
        wikiTablesFromOutline([
            "#ffffe6",
            "#ffebd2",
            "#f0fff0",
            "#e6ffff",
            "#ffeeff"
        ])(outline)
    )


# ------------------ TREE FROM OUTLINE -------------------

# indentLevelsFromLines :: [String] -> [(Int, String)]
def indentLevelsFromLines(xs):
    '''Each input line stripped of leading
       white space, and tupled with a preceding integer
       giving its level of indentation from 0 upwards.
    '''
    indentTextPairs = [
        (n, s[n:]) for (n, s)
        in (
            (len(list(takewhile(isSpace, x))), x)
            for x in xs
        )
    ]
    indentUnit = len(next(
        x for x in indentTextPairs if x[0]
    )) or 1
    return [
        (x[0] // indentUnit, x[1])
        for x in indentTextPairs
    ]


# forestFromLevels :: [(Int, String)] -> [Tree a]
def forestFromLevels(levelValuePairs):
    '''A list of trees derived from a list of values paired
       with integers giving their levels of indentation.
    '''
    def go(xs):
        if xs:
            level, v = xs[0]
            children, rest = span(
                lambda x: level < x[0]
            )(xs[1:])
            return [Node(v)(go(children))] + go(rest)
        else:
            return []
    return go(levelValuePairs)


# -------------- TREE PADDED TO EVEN DEPTH ---------------

# paddedTree :: a -> (Int, Node a) -> Node a
def paddedTree(padValue):
    '''A tree vertically padded to a given depth,
       with additional nodes, containing padValue,
       where needed.
    '''
    def go(tree):
        def pad(n):
            prev = n - 1
            return Node(tree.get('root'))([
                go(x)(prev) for x in (
                    tree.get('nest') or [Node(padValue)([])]
                )
            ]) if prev else tree
        return pad
    return go


# treeDepth :: Tree a -> Int
def treeDepth(tree):
    '''Maximum number of distinct levels in the tree.
    '''
    def go(_, xs):
        return 1 + max(xs) if xs else 1
    return foldTree(go)(tree)


# ------------ SPANNING WIDTH OF EACH SUBTREE ------------

# widthMeasuredTree :: Tree a -> Tree (a, Int)
def widthMeasuredTree(tree):
    '''A tree in which each node value is tupled
       with the width of the subtree.
    '''
    def go(x, xs):
        return Node((x, 1))([]) if not xs else (
            Node((x, reduce(
                lambda a, child: a + (
                    child.get('root')[1]
                ),
                xs,
                0
            )))(xs)
        )
    return foldTree(go)(tree)


# ----------------- COLOR SWATCH APPLIED -----------------

# paintedTree :: [String] -> Tree a -> Tree (String, a)
def paintedTree(swatch):
    '''A tree in which every node value is tupled with
       a hexadecimal color string taken from a swatch list.
       The first colour is used for the root node.
       The next n colours paint the root's n children.
       All descendants of those children are painted with
       the same color as their non-root ancestor.
    '''
    colors = cycle(swatch)

    def go(tree):
        return fmapTree(
            lambda x: ("", x)
        )(tree) if not swatch else (
            Node(
                (next(colors), tree.get('root'))
            )(
                list(map(
                    lambda k, child: fmapTree(
                        lambda v: (k, v)
                    )(child),
                    colors,
                    tree.get('nest')
                ))
            )
        )
    return go


# ---------------- GENERIC TREE FUNCTIONS ----------------

# Node :: a -> [Tree a] -> Tree a
def Node(v):
    '''Constructor for a Tree node which connects a
       value of some kind to a list of zero or
       more child trees.
    '''
    return lambda xs: {'root': v, 'nest': xs}


# fmapTree :: (a -> b) -> Tree a -> Tree b
def fmapTree(f):
    '''A new tree holding the results of
       an application of f to each root in
       the existing tree.
    '''
    def go(x):
        return Node(
            f(x.get('root'))
        )([go(v) for v in x.get('nest')])
    return go


# foldTree :: (a -> [b] -> b) -> Tree a -> b
def foldTree(f):
    '''The catamorphism on trees. A summary
       value defined by a depth-first fold.
    '''
    def go(node):
        return f(
            node.get('root'),
            [go(x) for x in node.get('nest')]
        )
    return go


# levels :: Tree a -> [[a]]
def levels(tree):
    '''A list of lists, grouping the root
       values of each level of the tree.
    '''
    return [[tree.get('root')]] + list(
        reduce(
            zipWithLong(add),
            map(levels, tree.get('nest')),
            []
        )
    )


# ----------------- WIKITABLE RENDERING ------------------

# wikiTableFromRows :: [[(String, (String, Int))]] -> String
def wikiTableFromRows(rows):
    '''A wiki table rendering of rows in which each cell
       has the form (hexColorString, (text, colspan))
    '''
    def cw(color, width):
        def go(w):
            return f' colspan={w}' if 1 < w else ''
        return f'style="background: {color}; "{go(width)}'

    def cellText(cell):
        color, (txt, width) = cell
        return f'| {cw(color,width) if txt else ""} | {txt}'

    def go(row):
        return '\n'.join([cellText(cell) for cell in row])

    return '{| class="wikitable" ' + (
        'style="text-align: center;"\n|-\n'
    ) + '\n|-\n'.join([go(row) for row in rows]) + '\n|}'


# ----------------------- GENERIC ------------------------

# ap :: (a -> b -> c) -> (a -> b) -> a -> c
def ap(f):
    '''Applicative instance for functions.
    '''
    def go(g):
        return lambda x: f(x)(g(x))
    return go

# compose :: ((a -> a), ...) -> (a -> a)


def compose(*fs):
    '''Composition, from right to left,
       of a series of functions.
    '''
    def go(f, g):
        def fg(x):
            return f(g(x))
        return fg
    return reduce(go, fs, lambda x: x)


# head :: [a] -> a
def head(xs):
    '''The first element of a non-empty list.
    '''
    return xs[0] if isinstance(xs, list) else next(xs)


# isSpace :: Char -> Bool
# isSpace :: String -> Bool
def isSpace(s):
    '''True if s is not empty, and
       contains only white space.
    '''
    return s.isspace()


# span :: (a -> Bool) -> [a] -> ([a], [a])
def span(p):
    '''The longest (possibly empty) prefix of xs that
       contains only elements satisfying p, tupled with the
       remainder of xs.  span p xs is equivalent to
       (takeWhile p xs, dropWhile p xs).
    '''
    def match(ab):
        b = ab[1]
        return not b or not p(b[0])

    def f(ab):
        a, b = ab
        return a + [b[0]], b[1:]

    def go(xs):
        return until(match)(f)(([], xs))
    return go


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of repeatedly applying f until p holds.
       The initial seed value is x.
    '''
    def go(f):
        def g(x):
            v = x
            while not p(v):
                v = f(v)
            return v
        return g
    return go


# zipWithLong :: ((a, a) -> a) -> ([a], [a]) -> [a]
def zipWithLong(f):
    '''Analogous to map(f, xs, ys)
       but returns a list with the length of the *longer*
       of xs and ys, taking any surplus values unmodified.
    '''
    def go(xs, ys):
        lxs = list(xs)
        lys = list(ys)
        i = min(len(lxs), len(lys))
        return chain.from_iterable([
            map(f, lxs, lys),
            lxs[i:],
            lys[i:]
        ])
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

