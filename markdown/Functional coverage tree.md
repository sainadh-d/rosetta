# Functional coverage tree

## Task Link
[Rosetta Code - Functional coverage tree](https://rosettacode.org/wiki/Functional_coverage_tree)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public final class FunctionalCoverageTree {

	public static void main(String[] aArgs) {		
		FCNode cleaning = new FCNode("Cleaning", 1, 0.0);
		
		List<FCNode> houses = Arrays.asList(
			new FCNode("House_1", 40, 0.0),
			new FCNode("House_2", 60, 0.0) );		
		cleaning.addChildren(houses);
		
		List<FCNode> house_1 = Arrays.asList( 
			new FCNode("Bedrooms", 1, 0.25), 
			new FCNode("Bathrooms", 1, 0.0), 
			new FCNode("Attic", 1, 0.75),
			new FCNode("Kitchen", 1, 0.1),
			new FCNode("Living_rooms", 1, 0.0),
			new FCNode("Basement", 1, 0.0),
			new FCNode("Garage", 1, 0.0),
			new FCNode("Garden",1, 0.8) );		
		houses.get(0).addChildren(house_1);
		
		List<FCNode> bathrooms_house_1 = Arrays.asList(
			new FCNode("Bathroom_1", 1, 0.5),
			new FCNode("Bathroom_2", 1, 0.0),
			new FCNode("Outside_lavatory", 1, 1.0) );
		house_1.get(1).addChildren(bathrooms_house_1);
		
		List<FCNode> living_rooms_house_1 = Arrays.asList( 
			new FCNode("lounge", 1, 0.0),
			new FCNode("Dining_room", 1, 0.0),
			new FCNode("Conservatory", 1, 0.0),
			new FCNode("Playroom", 1, 1.0) );
		house_1.get(4).addChildren(living_rooms_house_1);
		
		List<FCNode> house_2 = Arrays.asList(
			new FCNode("Upstairs", 1, 0.15),
			new FCNode("Ground_floor", 1, 0.316667),
			new FCNode("Basement", 1, 0.916667));
		houses.get(1).addChildren(house_2);
		
		List<FCNode> upstairs = Arrays.asList(
			new FCNode("Bedrooms", 1, 0.0),
			new FCNode("Bathroom", 1, 0.0),
			new FCNode("Toilet", 1, 0.0),
			new FCNode("Attics", 1, 0.6) );
		house_2.get(0).addChildren(upstairs);
		
		List<FCNode> ground_floor = Arrays.asList(
			new FCNode("Kitchen", 1, 0.0),
			new FCNode("Living_rooms", 1, 0.0), 
			new FCNode("Wet_room_&_toilet", 1, 0.0),
			new FCNode("Garage", 1, 0.0),
			new FCNode("Garden", 1, 0.9),
			new FCNode("Hot_tub_suite", 1, 1.0) );
		house_2.get(1).addChildren(ground_floor);
		
		List<FCNode> basement = Arrays.asList( 
			new FCNode("Cellars", 1, 1.0),
			new FCNode("Wine_cellar", 1, 1.0),
			new FCNode("Cinema", 1, 0.75) );
		house_2.get(2).addChildren(basement);
		
		List<FCNode> bedrooms = Arrays.asList(
			new FCNode("Suite_1", 1, 0.0),
			new FCNode("Suite_2", 1, 0.0),
			new FCNode("Bedroom_3",1, 0.0),
			new FCNode("Bedroom_4",1, 0.0) );
		upstairs.get(0).addChildren(bedrooms);
		
		List<FCNode> living_rooms_house_2 = Arrays.asList(
			new FCNode("lounge", 1, 0.0),
			new FCNode("Dining_room", 1, 0.0),
			new FCNode("Conservatory", 1, 0.0),
			new FCNode("Playroom", 1, 0.0) );
		ground_floor.get(1).addChildren(living_rooms_house_2);		
		
		final double overallCoverage = cleaning.getCoverage();
		System.out.println("OVERALL COVERAGE = " + String.format("%.6f", overallCoverage) + System.lineSeparator());
		System.out.println("NAME HIERARCHY                  | WEIGHT | COVERAGE |" );
		System.out.println("--------------------------------|--------|----------|");
		cleaning.display();
		System.out.println();
		
		basement.get(2).setCoverage(1.0); // Change House_2 Cinema node coverage to 1.0		
		final double updatedCoverage = cleaning.getCoverage();
	    final double difference = updatedCoverage - overallCoverage;
	    System.out.println("If the coverage of the House_2 Cinema node were increased from 0.75 to 1.0");
	    System.out.print("the overall coverage would increase by ");
	    System.out.println(String.format("%.6f%s%.6f", difference, " to ", updatedCoverage));;   
	    basement.get(2).setCoverage(0.75); // Restore to House_2 Cinema node coverage to its original value
	}

}

final class FCNode {
	
	public FCNode(String aName, int aWeight, double aCoverage) {
		name = aName;
		weight = aWeight;
		coverage = aCoverage;
	}
	
	public void addChildren(List<FCNode> aNodes) {
	    for ( FCNode node : aNodes ) {
	    	node.parent = this;
	    	children.add(node);
	    	updateCoverage();
	    }
	}	
	
	public double getCoverage() {
		return coverage;
	}
	
	public void setCoverage(double aCoverage) {
		if ( coverage != aCoverage ) {
		    coverage = aCoverage;
		    if ( parent != null ) {
		    	parent.updateCoverage();
		    }
		}		
	}
	
	public void display() {
		display(0);
	}
	
	private void updateCoverage() {
		double value1 = 0.0;
	    int value2 = 0;
	    for ( FCNode node : children ) {
	    	value1 += node.weight * node.coverage;
	    	value2 += node.weight;
	    }
	    
	    setCoverage(value1 / value2);
	}	
	
	private void display(int aLevel) {		
		final String initial = " ".repeat(4 * aLevel) + name;
		final String padding = " ".repeat(NAME_FIELD_WIDTH - initial.length()); 
		System.out.print(initial + padding + "|");
		System.out.print("  " + String.format("%3d", weight) + "   |");
		System.out.println(" " + String.format("%.6f", coverage) + " |");

		for ( FCNode child : children ) {
			child.display(aLevel + 1);
		}
	}	
	
	private String name;
	private int weight;
	private double coverage;
	private FCNode parent;
	private List<FCNode> children = new ArrayList<FCNode>();
	
	private static final int NAME_FIELD_WIDTH = 32;
	
}

```

## Python Code
### python_code_1.txt
```python
from itertools import zip_longest


fc2 = '''\
cleaning,,
    house1,40,
        bedrooms,,.25
        bathrooms,,
            bathroom1,,.5
            bathroom2,,
            outside_lavatory,,1
        attic,,.75
        kitchen,,.1
        living_rooms,,
            lounge,,
            dining_room,,
            conservatory,,
            playroom,,1
        basement,,
        garage,,
        garden,,.8
    house2,60,
        upstairs,,
            bedrooms,,
                suite_1,,
                suite_2,,
                bedroom_3,,
                bedroom_4,,
            bathroom,,
            toilet,,
            attics,,.6
        groundfloor,,
            kitchen,,
            living_rooms,,
                lounge,,
                dining_room,,
                conservatory,,
                playroom,,
            wet_room_&_toilet,,
            garage,,
            garden,,.9
            hot_tub_suite,,1
        basement,,
            cellars,,1
            wine_cellar,,1
            cinema,,.75

'''

NAME, WT, COV = 0, 1, 2

def right_type(txt):
    try:
        return float(txt)
    except ValueError:
        return txt

def commas_to_list(the_list, lines, start_indent=0):
    '''
    Output format is a nest of lists and tuples
    lists are for coverage leaves without children items in the list are name, weight, coverage
    tuples are 2-tuples for nodes with children. The first element is a list representing the
    name, weight, coverage of the node (some to be calculated); the second element is a list of
    child elements which may be 2-tuples or lists as above.
    
    the_list is modified in-place
    lines must be a generator of successive lines of input like fc2
    '''
    for n, line in lines:
        indent = 0
        while line.startswith(' ' * (4 * indent)):
            indent += 1
        indent -= 1
        fields = [right_type(f) for f in line.strip().split(',')]
        if indent == start_indent:
            the_list.append(fields)
        elif indent > start_indent:
            lst = [fields]
            sub = commas_to_list(lst, lines, indent)
            the_list[-1] = (the_list[-1], lst)
            if sub not in (None, ['']) :
                the_list.append(sub)
        else:
            return fields if fields else None
    return None


def pptreefields(lst, indent=0, widths=['%-32s', '%-8g', '%-10g']):
    '''
    Pretty prints the format described from function commas_to_list as a table with 
    names in the first column suitably indented and all columns having a fixed 
    minimum column width.
    '''
    lhs = ' ' * (4 * indent)
    for item in lst:
        if type(item) != tuple:
            name, *rest = item
            print(widths[0] % (lhs + name), end='|')
            for width, item in zip_longest(widths[1:len(rest)], rest, fillvalue=widths[-1]):
                if type(item) == str:
                    width = width[:-1] + 's'
                print(width % item, end='|')
            print()
        else:
            item, children = item
            name, *rest = item
            print(widths[0] % (lhs + name), end='|')
            for width, item in zip_longest(widths[1:len(rest)], rest, fillvalue=widths[-1]):
                if type(item) == str:
                    width = width[:-1] + 's'
                print(width % item, end='|')
            print()
            pptreefields(children, indent+1)


def default_field(node_list):
    node_list[WT] = node_list[WT] if node_list[WT] else 1.0
    node_list[COV] = node_list[COV] if node_list[COV] else 0.0

def depth_first(tree, visitor=default_field):
    for item in tree:
        if type(item) == tuple:
            item, children = item
            depth_first(children, visitor)
        visitor(item)
            

def covercalc(tree):
    '''
    Depth first weighted average of coverage
    '''
    sum_covwt, sum_wt = 0, 0
    for item in tree:
        if type(item) == tuple:
            item, children = item
            item[COV] = covercalc(children)
        sum_wt  += item[WT]
        sum_covwt += item[COV] * item[WT]
    cov = sum_covwt / sum_wt
    return cov

if __name__ == '__main__':        
    lstc = []
    commas_to_list(lstc, ((n, ln) for n, ln in enumerate(fc2.split('\n'))))
    #pp(lstc, width=1, indent=4, compact=1)
    
    #print('\n\nEXPANDED DEFAULTS\n')
    depth_first(lstc)
    #pptreefields(['NAME_HIERARCHY WEIGHT COVERAGE'.split()] + lstc)
    
    print('\n\nTOP COVERAGE = %f\n' % covercalc(lstc))
    depth_first(lstc)
    pptreefields(['NAME_HIERARCHY WEIGHT COVERAGE'.split()] + lstc)

```

### python_code_2.txt
```python
# -*- coding: utf-8 -*-

SPACES = 4
class Node:
    path2node = {}
    
    def add_node(self, pathname, wt, cov):
        path2node = self.path2node
        path, name = pathname.strip().rsplit('/', 1)
        node = Node(name, wt, cov)
        path2node[pathname] = node
        path2node[path].child.append(node) # Link the tree

    def __init__(self, name="", wt=1, cov=0.0, child=None):
        if child is None:
            child = []
        self.name, self.wt, self.cov, self.child = name, wt, cov, child
        self.delta = None
        self.sum_wt = wt
        if name == "": 
            # designate the top of the tree
            self.path2node[name] = self
    
    
    def __repr__(self, indent=0):
        name, wt, cov, delta, child = (self.name, self.wt, self.cov, 
                                       self.delta, self.child)
        lhs = ' ' * (SPACES * indent) + "Node(%r," % name
        txt = '%-40s wt=%2g, cov=%-8.5g, delta=%-10s, child=[' \
              % (lhs, wt, cov, ('n/a' if delta is None else '%-10.7f' % delta))
        if not child:
            txt += (']),\n')
        else:
            txt += ('\n')
            for c in child:
                txt += c.__repr__(indent + 1)
            txt += (' ' * (SPACES * indent) + "]),\n")
        return txt

    def covercalc(self):
        '''
        Depth first weighted average of coverage
        '''
        child = self.child
        if not child:
            return self.cov
        sum_covwt, sum_wt = 0, 0
        for node in child:
            nwt = node.wt
            ncov = node.covercalc()
            sum_wt += nwt
            sum_covwt += ncov * nwt
        cov = sum_covwt / sum_wt
        self.sum_wt = sum_wt
        self.cov = cov
        return cov

    def deltacalc(self, power=1.0):
        '''
        Top down distribution of weighted residuals
        '''
        sum_wt = self.sum_wt
        self.delta = delta = (1 - self.cov) * power
        for node in self.child:
            node.deltacalc(power * node.wt / sum_wt)
        return delta


def isclose(a, b, rel_tol=1e-9, abs_tol=1e-9):
    return abs(a-b) <= max( rel_tol * max(abs(a), abs(b)), abs_tol )
    
    
if __name__ == '__main__': 
    top = Node()    # Add placeholder for top of tree
    add_node = top.add_node
    
    add_node('/cleaning', 1, 0)
    add_node('/cleaning/house1', 40, 0)
    add_node('/cleaning/house1/bedrooms', 1, 0.25)
    add_node('/cleaning/house1/bathrooms', 1, 0)
    add_node('/cleaning/house1/bathrooms/bathroom1', 1, 0.5)
    add_node('/cleaning/house1/bathrooms/bathroom2', 1, 0)
    add_node('/cleaning/house1/bathrooms/outside_lavatory', 1, 1)
    add_node('/cleaning/house1/attic', 1, 0.75)
    add_node('/cleaning/house1/kitchen', 1, 0.1)
    add_node('/cleaning/house1/living_rooms', 1, 0)
    add_node('/cleaning/house1/living_rooms/lounge', 1, 0)
    add_node('/cleaning/house1/living_rooms/dining_room', 1, 0)
    add_node('/cleaning/house1/living_rooms/conservatory', 1, 0)
    add_node('/cleaning/house1/living_rooms/playroom', 1, 1)
    add_node('/cleaning/house1/basement', 1, 0)
    add_node('/cleaning/house1/garage', 1, 0)
    add_node('/cleaning/house1/garden', 1, 0.8)
    add_node('/cleaning/house2', 60, 0)
    add_node('/cleaning/house2/upstairs', 1, 0)
    add_node('/cleaning/house2/upstairs/bedrooms', 1, 0)
    add_node('/cleaning/house2/upstairs/bedrooms/suite_1', 1, 0)
    add_node('/cleaning/house2/upstairs/bedrooms/suite_2', 1, 0)
    add_node('/cleaning/house2/upstairs/bedrooms/bedroom_3', 1, 0)
    add_node('/cleaning/house2/upstairs/bedrooms/bedroom_4', 1, 0)
    add_node('/cleaning/house2/upstairs/bathroom', 1, 0)
    add_node('/cleaning/house2/upstairs/toilet', 1, 0)
    add_node('/cleaning/house2/upstairs/attics', 1, 0.6)
    add_node('/cleaning/house2/groundfloor', 1, 0)
    add_node('/cleaning/house2/groundfloor/kitchen', 1, 0)
    add_node('/cleaning/house2/groundfloor/living_rooms', 1, 0)
    add_node('/cleaning/house2/groundfloor/living_rooms/lounge', 1, 0)
    add_node('/cleaning/house2/groundfloor/living_rooms/dining_room', 1, 0)
    add_node('/cleaning/house2/groundfloor/living_rooms/conservatory', 1, 0)
    add_node('/cleaning/house2/groundfloor/living_rooms/playroom', 1, 0)
    add_node('/cleaning/house2/groundfloor/wet_room_&_toilet', 1, 0)
    add_node('/cleaning/house2/groundfloor/garage', 1, 0)
    add_node('/cleaning/house2/groundfloor/garden', 1, 0.9)
    add_node('/cleaning/house2/groundfloor/hot_tub_suite', 1, 1)
    add_node('/cleaning/house2/basement', 1, 0)
    add_node('/cleaning/house2/basement/cellars', 1, 1)
    add_node('/cleaning/house2/basement/wine_cellar', 1, 1)
    add_node('/cleaning/house2/basement/cinema', 1, 0.75)

    top = top.child[0]  # Remove artificial top
    cover = top.covercalc()
    delta = top.deltacalc()
    print('TOP COVERAGE = %g\n' % cover)
    print(top)
    assert isclose((delta + cover), 1.0), "Top level delta + coverage should " \
                                          "equal 1 instead of (%f + %f)" % (delta, cover)

```

### python_code_3.txt
```python
'''Functional coverage tree'''

from itertools import chain, product
from functools import reduce


# main :: IO ()
def main():
    '''Tabular outline serialisation of a parse tree
       decorated with computations of:
       1. Weighted coverage of each tree node.
       2. Each node's share of the total project's
          remaining work.
    '''
    columnWidths = [31, 9, 9, 9]
    delimiter = '|'

    reportLines = REPORT.splitlines()
    columnTitles = init(columnNames(delimiter)(reportLines[0]))

    # ------ SERIALISATION OF DECORATED PARSE TREE -------
    print(titleLine(delimiter)(columnWidths)(
        columnTitles + ['share of residue']
    ))
    print(indentedLinesFromTree('    ', tabulation(columnWidths))(

        # -------- TWO COMPUTATIONS BY TRAVERSAL ---------
        withResidueShares(1.0)(
            foldTree(weightedCoverage)(

                # --- TREE FROM PARSE OF OUTLINE TEXT ----
                fmapTree(
                    recordFromKeysDefaultsDelimiterAndLine(
                        columnTitles
                    )(
                        [str, float, float])([
                            '?', 1.0, 0.0
                        ])(delimiter)
                )(
                    forestFromIndentLevels(
                        indentLevelsFromLines(
                            reportLines[1:]
                        )
                    )[0]
                )
            )
        )
    ))


# ---- WEIGHTED COVERAGE, AND SHARE OF TOTAL RESIDUE -----

# weightedCoverage :: Tree Dict ->
# [Tree Dict] -> Tree Dict
def weightedCoverage(x):
    '''The weighted coverage of a tree node,
       as a function of the weighted averages
       of its children.
    '''
    def go(xs):
        cws = [
            (r['coverage'], r['weight']) for r
            in [root(x) for x in xs]
        ]
        totalWeight = reduce(lambda a, x: a + x[1], cws, 0)
        return Node(dict(
            x, **{
                'coverage': round(reduce(
                    lambda a, cw: a + (cw[0] * cw[1]),
                    cws, x['coverage']
                ) / (totalWeight if 0 < totalWeight else 1), 5)
            }
        ))(xs)
    return go


# withResidueShares :: Float -> Tree Dict -> Tree Dict
def withResidueShares(shareOfTotal):
    '''A Tree of dictionaries additionally decorated with each
       node's proportion of the total project's outstanding work.
    '''
    def go(fraction, node):
        [nodeRoot, nodeNest] = ap([root, nest])([node])
        weights = [root(x)['weight'] for x in nodeNest]
        siblingsTotal = sum(weights)
        return Node(
            insertDict('residual_share')(
                round(fraction * (1 - nodeRoot['coverage']), 5)
            )(nodeRoot)
        )(
            map(
                go,
                [fraction * (w / siblingsTotal) for w in weights],
                nodeNest
            )
        )
    return lambda tree: go(shareOfTotal, tree)


# ------------------ OUTLINE TABULATION ------------------

# tabulation :: [Int] -> String -> Dict -> String
def tabulation(columnWidths):
    '''Indented string representation of a node
       in a functional coverage tree.
    '''
    return lambda indent, dct: '| '.join(map(
        lambda k, w: (
            (indent if 10 < w else '') + str(dct.get(k, ''))
        ).ljust(w, ' '),
        dct.keys(),
        columnWidths
    ))


# titleLine :: String -> [Int] -> [String] -> String
def titleLine(delimiter):
    '''A string consisting of a spaced and delimited
       series of upper-case column titles.
    '''
    return lambda columnWidths: lambda ks: (
        delimiter + ' '
    ).join(map(
        lambda k, w: k.ljust(w, ' '),
        [k.upper() for k in ks],
        columnWidths
    ))


# ------------ GENERIC AND REUSABLE FUNCTIONS ------------

# Node :: a -> [Tree a] -> Tree a
def Node(v):
    '''Constructor for a Tree node which connects a
       value of some kind to a list of zero or
       more child trees.
    '''
    return lambda xs: {'type': 'Tree', 'root': v, 'nest': xs}


# ap (<*>) :: [(a -> b)] -> [a] -> [b]
def ap(fs):
    '''The application of each of a list of functions,
       to each of a list of values.
    '''
    def go(xs):
        return [
            f(x) for (f, x)
            in product(fs, xs)
        ]
    return go


# columnNames :: String -> String -> [String]
def columnNames(delimiter):
    '''A list of lower-case keys derived from
       a header line and a delimiter character.
    '''
    return compose(
        fmapList(compose(toLower, strip)),
        splitOn(delimiter)
    )


# compose :: ((a -> a), ...) -> (a -> a)
def compose(*fs):
    '''Composition, from right to left,
       of a series of functions.
    '''
    return lambda x: reduce(
        lambda a, f: f(a),
        fs[::-1], x
    )


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been mapped.
       The list monad can be derived by using a function f which
       wraps its output in a list,
       (using an empty list to represent computational failure).
    '''
    def go(xs):
        return chain.from_iterable(map(f, xs))
    return go


# div :: Int -> Int -> Int
def div(x):
    '''Integer division.'''
    return lambda y: x // y


# first :: (a -> b) -> ((a, c) -> (b, c))
def first(f):
    '''A simple function lifted to a function over a tuple,
       with f applied only the first of two values.
    '''
    return lambda xy: (f(xy[0]), xy[1])


# flip :: (a -> b -> c) -> b -> a -> c
def flip(f):
    '''The (curried or uncurried) function f with its
       arguments reversed.
    '''
    return lambda a: lambda b: f(b)(a)


# fmapList :: (a -> b) -> [a] -> [b]
def fmapList(f):
    '''fmap over a list.
       f lifted to a function over a list.
    '''
    return lambda xs: [f(x) for x in xs]


# fmapTree :: (a -> b) -> Tree a -> Tree b
def fmapTree(f):
    '''A new tree holding the results of
       an application of f to each root in
       the existing tree.
    '''
    def go(x):
        return Node(
            f(x['root'])
        )([go(v) for v in x['nest']])
    return go


# foldTree :: (a -> [b] -> b) -> Tree a -> b
def foldTree(f):
    '''The catamorphism on trees. A summary
       value defined by a depth-first fold.
    '''
    def go(node):
        return f(root(node))([
            go(x) for x in nest(node)
        ])
    return go


# forestFromIndentLevels :: [(Int, a)] -> [Tree a]
def forestFromIndentLevels(tuples):
    '''A list of trees derived from a list of values paired
       with integers giving their levels of indentation.
    '''
    def go(xs):
        if xs:
            intIndent, v = xs[0]
            firstTreeLines, rest = span(
                lambda x: intIndent < x[0]
            )(xs[1:])
            return [Node(v)(go(firstTreeLines))] + go(rest)
        else:
            return []
    return go(tuples)


# fst :: (a, b) -> a
def fst(tpl):
    '''First member of a pair.'''
    return tpl[0]


# indentLevelsFromLines :: [String] -> [(Int, String)]
def indentLevelsFromLines(xs):
    '''Each input line stripped of leading
       white space, and tupled with a preceding integer
       giving its level of indentation from 0 upwards.
    '''
    indentTextPairs = list(map(
        compose(first(len), span(isSpace)),
        xs
    ))
    indentUnit = min(concatMap(
        lambda x: [x[0]] if x[0] else []
    )(indentTextPairs))
    return list(map(
        first(flip(div)(indentUnit)),
        indentTextPairs
    ))


# indentedLinesFromTree :: String -> (String -> a -> String) ->
# [Tree a] -> String
def indentedLinesFromTree(strTab, f):
    '''An indented line rendering of a tree, in which
       the function f stringifies a root value.
    '''
    def go(indent):
        return lambda node: [f(indent, node['root'])] + list(
            concatMap(
                go(strTab + indent)
            )(node['nest'])
        )
    return lambda tree: '\n'.join(go('')(tree))


# init :: [a] -> [a]
def init(xs):
    '''A list containing all the elements
       of xs except the last.
    '''
    return xs[:-1]


# insertDict :: String -> a -> Dict -> Dict
def insertDict(k):
    '''A new dictionary updated with a (k, v) pair.'''
    def go(v, dct):
        return dict(dct, **{k: v})
    return lambda v: lambda dct: go(v, dct)


# isSpace :: Char -> Bool
# isSpace :: String -> Bool
def isSpace(s):
    '''True if s is not empty, and
       contains only white space.
    '''
    return s.isspace()


# lt (<) :: Ord a => a -> a -> Bool
def lt(x):
    '''True if x < y.'''
    return lambda y: (x < y)


# nest :: Tree a -> [Tree a]
def nest(t):
    '''Accessor function for children of tree node.'''
    return t['nest'] if 'nest' in t else None


# recordFromKeysDefaultsAndLine :: String ->
# { name :: String, weight :: Float, completion :: Float }
def recordFromKeysDefaultsDelimiterAndLine(columnTitles):
    '''A dictionary of key-value pairs, derived from a
       delimited string, together with ordered lists of
       key-names, types, default values, and a delimiter.
    '''
    return lambda ts: lambda vs: lambda delim: lambda s: dict(
        map(
            lambda k, t, v, x: (k, t(x) if x else v),
            columnTitles, ts, vs,
            map(strip, splitOn(delim)(s))
        )
    )


# root :: Tree a -> a
def root(t):
    '''Accessor function for data of tree node.'''
    return t['root'] if 'root' in t else None


# strip :: String -> String
def strip(s):
    '''A copy of s without any leading or trailling
       white space.
    '''
    return s.strip()


# span :: (a -> Bool) -> [a] -> ([a], [a])
def span(p):
    '''The longest (possibly empty) prefix of xs
       that contains only elements satisfying p,
       tupled with the remainder of xs.
       span p xs is equivalent to (takeWhile p xs, dropWhile p xs).
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


# splitOn :: String -> String -> [String]
def splitOn(pat):
    '''A list of the strings delimited by
       instances of a given pattern in s.
    '''
    return lambda xs: (
        xs.split(pat) if isinstance(xs, str) else None
    )


# toLower :: String -> String
def toLower(s):
    '''String in lower case.'''
    return s.lower()


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


# MAIN ----------------------------------------------------
if __name__ == '__main__':
    REPORT = '''NAME_HIERARCHY                  |WEIGHT  |COVERAGE  |
    cleaning                        |        |          |
        house1                      |40      |          |
            bedrooms                |        |0.25      |
            bathrooms               |        |          |
                bathroom1           |        |0.5       |
                bathroom2           |        |          |
                outside_lavatory    |        |1         |
            attic                   |        |0.75      |
            kitchen                 |        |0.1       |
            living_rooms            |        |          |
                lounge              |        |          |
                dining_room         |        |          |
                conservatory        |        |          |
                playroom            |        |1         |
            basement                |        |          |
            garage                  |        |          |
            garden                  |        |0.8       |
        house2                      |60      |          |
            upstairs                |        |          |
                bedrooms            |        |          |
                    suite_1         |        |          |
                    suite_2         |        |          |
                    bedroom_3       |        |          |
                    bedroom_4       |        |          |
                bathroom            |        |          |
                toilet              |        |          |
                attics              |        |0.6       |
            groundfloor             |        |          |
                kitchen             |        |          |
                living_rooms        |        |          |
                    lounge          |        |          |
                    dining_room     |        |          |
                    conservatory    |        |          |
                    playroom        |        |          |
                wet_room_&_toilet   |        |          |
                garage              |        |          |
                garden              |        |0.9       |
                hot_tub_suite       |        |1         |
            basement                |        |          |
                cellars             |        |1         |
                wine_cellar         |        |1         |
                cinema              |        |0.75      |'''
    main()

```

