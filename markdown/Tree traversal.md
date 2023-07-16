# Tree traversal

## Task Link
[Rosetta Code - Tree traversal](https://rosettacode.org/wiki/Tree_traversal)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class TreeTraversal {

        static class Node<T> {
		T value;
		Node<T> left;
		Node<T> right;

		Node(T value) {
			this.value = value;
		}

		void visit() {
			System.out.print(this.value + " ");
		}
	}

	static enum ORDER {
		PREORDER, INORDER, POSTORDER, LEVEL
	}
        
        static <T> void traverse(Node<T> node, ORDER order) {
		if (node == null) {
			return;
		}
		switch (order) {
		case PREORDER:
			node.visit();
			traverse(node.left, order);
			traverse(node.right, order);
			break;
		case INORDER:
			traverse(node.left, order);
			node.visit();
			traverse(node.right, order);
			break;
		case POSTORDER:
			traverse(node.left, order);
			traverse(node.right, order);
			node.visit();
			break;
		case LEVEL:
			Queue<Node<T>> queue = new LinkedList<>();
			queue.add(node);
			while(!queue.isEmpty()){
				Node<T> next = queue.remove();
				next.visit();
				if(next.left!=null)
					queue.add(next.left);
				if(next.right!=null)
					queue.add(next.right);
			}
		}
	}	

	public static void main(String[] args) {

		Node<Integer> one = new Node<Integer>(1);
		Node<Integer> two = new Node<Integer>(2);
		Node<Integer> three = new Node<Integer>(3);
		Node<Integer> four = new Node<Integer>(4);
		Node<Integer> five = new Node<Integer>(5);
		Node<Integer> six = new Node<Integer>(6);
		Node<Integer> seven = new Node<Integer>(7);
		Node<Integer> eight = new Node<Integer>(8);
		Node<Integer> nine = new Node<Integer>(9);
		
		one.left = two;
		one.right = three;
		two.left = four;
		two.right = five;
		three.left = six;
		four.left = seven;
		six.left = eight;
		six.right = nine;

		traverse(one, ORDER.PREORDER);
		System.out.println(); 
		traverse(one, ORDER.INORDER);
		System.out.println();
		traverse(one, ORDER.POSTORDER);
		System.out.println();
		traverse(one, ORDER.LEVEL);
		
	}
}

```

### java_code_2.txt
```java
import java.util.function.Consumer;
import java.util.Queue;
import java.util.LinkedList;

class TreeTraversal {
  static class EmptyNode {
    void accept(Visitor aVisitor) {}

    void accept(LevelOrder aVisitor, Queue<EmptyNode> data) {}
  }

  static class Node<T> extends EmptyNode {
    T data;
    EmptyNode left = new EmptyNode();
    EmptyNode right = new EmptyNode();

    Node(T data) {
      this.data = data;
    }

    Node<T> left(Node<?> aNode) {
      this.left = aNode;
      return this;
    }

    Node<T> right(Node<?> aNode) {
      this.right = aNode;
      return this;
    }

    void accept(Visitor aVisitor) {
      aVisitor.visit(this);
    }

    void accept(LevelOrder aVisitor, Queue<EmptyNode> data) {
      aVisitor.visit(this, data);
    }
  }

  static abstract class Visitor {
    Consumer<Node<?>> action;

    Visitor(Consumer<Node<?>> action) {
      this.action = action;
    }

    abstract <T> void visit(Node<T> aNode);
  }

  static class PreOrder extends Visitor {
    PreOrder(Consumer<Node<?>> action) {
      super(action);
    }

    <T> void visit(Node<T> aNode) {
      action.accept(aNode);
      aNode.left.accept(this);
      aNode.right.accept(this);
    }
  }

  static class InOrder extends Visitor {
    InOrder(Consumer<Node<?>> action) {
      super(action);
    }

    <T> void visit(Node<T> aNode) {
      aNode.left.accept(this);
      action.accept(aNode);
      aNode.right.accept(this);
    }
  }

  static class PostOrder extends Visitor {
    PostOrder(Consumer<Node<?>> action) {
      super(action);
    }

    <T> void visit(Node<T> aNode) {
      aNode.left.accept(this);
      aNode.right.accept(this);
      action.accept(aNode);
    }
  }

  static class LevelOrder extends Visitor {
    LevelOrder(Consumer<Node<?>> action) {
      super(action);
    }

    <T> void visit(Node<T> aNode) {
      Queue<EmptyNode> queue = new LinkedList<>();
      queue.add(aNode);
      do {
        queue.remove().accept(this, queue);
      } while (!queue.isEmpty());
    }

    <T> void visit(Node<T> aNode, Queue<EmptyNode> queue) {
      action.accept(aNode);
      queue.add(aNode.left);
      queue.add(aNode.right);
    }
  }

  public static void main(String[] args) {
    Node<Integer> tree = new Node<Integer>(1)
                          .left(new Node<Integer>(2)
                            .left(new Node<Integer>(4)
                              .left(new Node<Integer>(7)))
                            .right(new Node<Integer>(5)))
                          .right(new Node<Integer>(3)
                            .left(new Node<Integer>(6)
                              .left(new Node<Integer>(8))
                              .right(new Node<Integer>(9))));
    Consumer<Node<?>> print = aNode -> System.out.print(aNode.data + " ");
    tree.accept(new PreOrder(print));
    System.out.println();
    tree.accept(new InOrder(print));
    System.out.println();
    tree.accept(new PostOrder(print));
    System.out.println();
    tree.accept(new LevelOrder(print));
    System.out.println();
  }
}

```

## Python Code
### python_code_1.txt
```python
from collections import namedtuple
 
Node = namedtuple('Node', 'data, left, right')
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))
 
def printwithspace(i):
    print(i, end=' ')

def dfs(order, node, visitor):
    if node is not None:
        for action in order:
            if action == 'N':
                visitor(node.data)
            elif action == 'L':
                dfs(order, node.left, visitor)
            elif action == 'R':
                dfs(order, node.right, visitor)
                
def preorder(node, visitor = printwithspace):
    dfs('NLR', node, visitor)
 
def inorder(node, visitor = printwithspace):
    dfs('LNR', node, visitor)
 
def postorder(node, visitor = printwithspace):
    dfs('LRN', node, visitor)
 
def ls(node, more, visitor, order='TB'):
    "Level-based Top-to-Bottom or Bottom-to-Top tree search"
    if node:
        if more is None:
            more = []
        more += [node.left, node.right]
    for action in order:
        if action == 'B' and more:
            ls(more[0], more[1:], visitor, order)
        elif action == 'T' and node:
            visitor(node.data)

def levelorder(node, more=None, visitor = printwithspace):
    ls(node, more, visitor, 'TB') 
 
# Because we can
def reverse_preorder(node, visitor = printwithspace):
    dfs('RLN', node, visitor)
    
def bottom_up_order(node, more=None, visitor = printwithspace, order='BT'):
    ls(node, more, visitor, 'BT')


if __name__ == '__main__':
    w = 10
    for traversal in [preorder, inorder, postorder, levelorder, 
                      reverse_preorder, bottom_up_order]:
        if traversal == reverse_preorder:
            w = 20
            print('\nThe generalisation of function dfs allows:')
        if traversal == bottom_up_order:
            print('The generalisation of function ls allows:')
        print(f"{traversal.__name__:>{w}}:", end=' ')
        traversal(tree)
        print()

```

### python_code_2.txt
```python
from collections import namedtuple
from sys import stdout
 
class Node(namedtuple('Node', 'data, left, right')):
    __slots__ = ()

    def preorder(self, visitor):
        if self is not None:
            visitor(self.data)
            Node.preorder(self.left, visitor)
            Node.preorder(self.right, visitor)
     
    def inorder(self, visitor):
        if self is not None:
            Node.inorder(self.left, visitor)
            visitor(self.data)
            Node.inorder(self.right, visitor)
     
    def postorder(self, visitor):
        if self is not None:
            Node.postorder(self.left, visitor)
            Node.postorder(self.right, visitor)
            visitor(self.data)
     
    def levelorder(self, visitor, more=None):
        if self is not None:
            if more is None:
                more = []
            more += [self.left, self.right]
            visitor(self.data)
        if more:    
            Node.levelorder(more[0], visitor, more[1:])


def printwithspace(i):
    stdout.write("%i " % i)
 

tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))


if __name__ == '__main__':
    stdout.write('  preorder: ')
    tree.preorder(printwithspace)
    stdout.write('\n   inorder: ')
    tree.inorder(printwithspace)
    stdout.write('\n postorder: ')
    tree.postorder(printwithspace)
    stdout.write('\nlevelorder: ')
    tree.levelorder(printwithspace)
    stdout.write('\n')

```

### python_code_3.txt
```python
'''Tree traversals'''

from itertools import chain
from functools import reduce
from operator import mul


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


# levels :: Tree a -> [[a]]
def levels(tree):
    '''A list of lists, grouping the root
       values of each level of the tree.
    '''
    def go(a, node):
        h, *t = a if a else ([], [])

        return [[root(node)] + h] + reduce(
            go, nest(node)[::-1], t
        )
    return go([], tree)


# preorder :: a -> [[a]] -> [a]
def preorder(x):
    '''This node followed by the rest.'''
    return lambda xs: [x] + concat(xs)


# inorder :: a -> [[a]] -> [a]
def inorder(x):
    '''Descendants of any first child,
       then this node, then the rest.'''
    return lambda xs: (
        xs[0] + [x] + concat(xs[1:]) if xs else [x]
    )


# postorder :: a -> [[a]] -> [a]
def postorder(x):
    '''Descendants first, then this node.'''
    return lambda xs: concat(xs) + [x]


# levelorder :: Tree a -> [a]
def levelorder(tree):
    '''Top-down concatenation of this node
       with the rows below.'''
    return concat(levels(tree))


# treeSum :: Int -> [Int] -> Int
def treeSum(x):
    '''This node's value + the sum of its descendants.'''
    return lambda xs: x + sum(xs)


# treeProduct :: Int -> [Int] -> Int
def treeProduct(x):
    '''This node's value * the product of its descendants.'''
    return lambda xs: x * numericProduct(xs)


# treeMax :: Ord a => a -> [a] -> a
def treeMax(x):
    '''Maximum value of this node and any descendants.'''
    return lambda xs: max([x] + xs)


# treeMin :: Ord a => a -> [a] -> a
def treeMin(x):
    '''Minimum value of this node and any descendants.'''
    return lambda xs: min([x] + xs)


# nodeCount :: Int -> [Int] -> Int
def nodeCount(_):
    '''One more than the total number of descendants.'''
    return lambda xs: 1 + sum(xs)


# treeWidth :: Int -> [Int] -> Int
def treeWidth(_):
    '''Sum of widths of any children, or a minimum of 1.'''
    return lambda xs: sum(xs) if xs else 1


# treeDepth :: Int -> [Int] -> Int
def treeDepth(_):
    '''One more than that of the deepest child.'''
    return lambda xs: 1 + (max(xs) if xs else 0)


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Tree traversals - accumulating and folding'''

    # tree :: Tree Int
    tree = Node(1)([
        Node(2)([
            Node(4)([
                Node(7)([])
            ]),
            Node(5)([])
        ]),
        Node(3)([
            Node(6)([
                Node(8)([]),
                Node(9)([])
            ])
        ])
    ])

    print(
        fTable(main.__doc__ + ':\n')(fName)(str)(
            lambda f: (
                foldTree(f) if 'levelorder' != fName(f) else f
            )(tree)
        )([
            preorder, inorder, postorder, levelorder,
            treeSum, treeProduct, treeMin, treeMax,
            nodeCount, treeWidth, treeDepth
        ])
    )


# ----------------------- GENERIC ------------------------

# Node :: a -> [Tree a] -> Tree a
def Node(v):
    '''Contructor for a Tree node which connects a
       value of some kind to a list of zero or
       more child trees.'''
    return lambda xs: {
        'type': 'Node', 'root': v, 'nest': xs
    }


# nest :: Tree a -> [Tree a]
def nest(tree):
    '''Accessor function for children of tree node'''
    return tree['nest'] if 'nest' in tree else None


# root :: Dict -> a
def root(tree):
    '''Accessor function for data of tree node'''
    return tree['root'] if 'root' in tree else None


# concat :: [[a]] -> [a]
# concat :: [String] -> String
def concat(xxs):
    '''The concatenation of all the elements in a list.'''
    xs = list(chain.from_iterable(xxs))
    unit = '' if isinstance(xs, str) else []
    return unit if not xs else (
        ''.join(xs) if isinstance(xs[0], str) else xs
    )


# numericProduct :: [Num] -> Num
def numericProduct(xs):
    '''The arithmetic product of all numbers in xs.'''
    return reduce(mul, xs, 1)


# ---------------------- FORMATTING ----------------------

# fName :: (a -> b) -> String
def fName(f):
    '''The name bound to the function.'''
    return f.__name__


# fTable :: String -> (a -> String) ->
#                     (b -> String) ->
#                     (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function ->
       fx display function -> f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + (
                ' -> ' + fxShow(f(x))
            ),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: (
        lambda f: lambda xs: go(
            xShow, fxShow, f, xs
        )
    )


if __name__ == '__main__':
    main()

```

