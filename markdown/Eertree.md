# Eertree

## Task Link
[Rosetta Code - Eertree](https://rosettacode.org/wiki/Eertree)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Eertree {
    public static void main(String[] args) {
        List<Node> tree = eertree("eertree");
        List<String> result = subPalindromes(tree);
        System.out.println(result);
    }

    private static class Node {
        int length;
        Map<Character, Integer> edges = new HashMap<>();
        int suffix;

        public Node(int length) {
            this.length = length;
        }

        public Node(int length, Map<Character, Integer> edges, int suffix) {
            this.length = length;
            this.edges = edges != null ? edges : new HashMap<>();
            this.suffix = suffix;
        }
    }

    private static final int EVEN_ROOT = 0;
    private static final int ODD_ROOT = 1;

    private static List<Node> eertree(String s) {
        List<Node> tree = new ArrayList<>();
        tree.add(new Node(0, null, ODD_ROOT));
        tree.add(new Node(-1, null, ODD_ROOT));
        int suffix = ODD_ROOT;
        int n, k;
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            for (n = suffix; ; n = tree.get(n).suffix) {
                k = tree.get(n).length;
                int b = i - k - 1;
                if (b >= 0 && s.charAt(b) == c) {
                    break;
                }
            }
            if (tree.get(n).edges.containsKey(c)) {
                suffix = tree.get(n).edges.get(c);
                continue;
            }
            suffix = tree.size();
            tree.add(new Node(k + 2));
            tree.get(n).edges.put(c, suffix);
            if (tree.get(suffix).length == 1) {
                tree.get(suffix).suffix = 0;
                continue;
            }
            while (true) {
                n = tree.get(n).suffix;
                int b = i - tree.get(n).length - 1;
                if (b >= 0 && s.charAt(b) == c) {
                    break;
                }
            }
            tree.get(suffix).suffix = tree.get(n).edges.get(c);
        }
        return tree;
    }

    private static List<String> subPalindromes(List<Node> tree) {
        List<String> s = new ArrayList<>();
        subPalindromes_children(0, "", tree, s);
        for (Map.Entry<Character, Integer> cm : tree.get(1).edges.entrySet()) {
            String ct = String.valueOf(cm.getKey());
            s.add(ct);
            subPalindromes_children(cm.getValue(), ct, tree, s);
        }
        return s;
    }

    // nested methods are a pain, even if lambdas make that possible for Java
    private static void subPalindromes_children(final int n, final String p, final List<Node> tree, List<String> s) {
        for (Map.Entry<Character, Integer> cm : tree.get(n).edges.entrySet()) {
            Character c = cm.getKey();
            Integer m = cm.getValue();
            String pl = c + p + c;
            s.add(pl);
            subPalindromes_children(m, pl, tree, s);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/bin/python
from __future__ import print_function

class Node(object):
	def __init__(self):
		self.edges = {} # edges (or forward links)
		self.link = None # suffix link (backward links)
		self.len = 0 # the length of the node

class Eertree(object):
	def __init__(self):
		self.nodes = []
		# two initial root nodes
		self.rto = Node() #odd length root node, or node -1
		self.rte = Node() #even length root node, or node 0

		# Initialize empty tree
		self.rto.link = self.rte.link = self.rto;
		self.rto.len = -1
		self.rte.len = 0
		self.S = [0] # accumulated input string, T=S[1..i]
		self.maxSufT = self.rte # maximum suffix of tree T

	def get_max_suffix_pal(self, startNode, a):
		# We traverse the suffix-palindromes of T in the order of decreasing length.
		# For each palindrome we read its length k and compare T[i-k] against a
		# until we get an equality or arrive at the -1 node.
		u = startNode
		i = len(self.S)
		k = u.len
		while id(u) != id(self.rto) and self.S[i - k - 1] != a:
			assert id(u) != id(u.link) #Prevent infinte loop
			u = u.link
			k = u.len

		return u
	
	def add(self, a):

		# We need to find the maximum suffix-palindrome P of Ta
		# Start by finding maximum suffix-palindrome Q of T.
		# To do this, we traverse the suffix-palindromes of T
		# in the order of decreasing length, starting with maxSuf(T)
		Q = self.get_max_suffix_pal(self.maxSufT, a)

		# We check Q to see whether it has an outgoing edge labeled by a.
		createANewNode = not a in Q.edges

		if createANewNode:
			# We create the node P of length Q+2
			P = Node()
			self.nodes.append(P)
			P.len = Q.len + 2
			if P.len == 1:
				# if P = a, create the suffix link (P,0)
				P.link = self.rte
			else:
				# It remains to create the suffix link from P if |P|>1. Just
				# continue traversing suffix-palindromes of T starting with the suffix 
				# link of Q.
				P.link = self.get_max_suffix_pal(Q.link, a).edges[a]

			# create the edge (Q,P)
			Q.edges[a] = P

		#P becomes the new maxSufT
		self.maxSufT = Q.edges[a]

		#Store accumulated input string
		self.S.append(a)

		return createANewNode
	
	def get_sub_palindromes(self, nd, nodesToHere, charsToHere, result):
		#Each node represents a palindrome, which can be reconstructed
		#by the path from the root node to each non-root node.

		#Traverse all edges, since they represent other palindromes
		for lnkName in nd.edges:
			nd2 = nd.edges[lnkName] #The lnkName is the character used for this edge
			self.get_sub_palindromes(nd2, nodesToHere+[nd2], charsToHere+[lnkName], result)

		#Reconstruct based on charsToHere characters.
		if id(nd) != id(self.rto) and id(nd) != id(self.rte): #Don't print for root nodes
			tmp = "".join(charsToHere)
			if id(nodesToHere[0]) == id(self.rte): #Even string
				assembled = tmp[::-1] + tmp
			else: #Odd string
				assembled = tmp[::-1] + tmp[1:]
			result.append(assembled)

if __name__=="__main__":
	st = "eertree"
	print ("Processing string", st)
	eertree = Eertree()
	for ch in st:
		eertree.add(ch)

	print ("Number of sub-palindromes:", len(eertree.nodes))

	#Traverse tree to find sub-palindromes
	result = []
	eertree.get_sub_palindromes(eertree.rto, [eertree.rto], [], result) #Odd length words
	eertree.get_sub_palindromes(eertree.rte, [eertree.rte], [], result) #Even length words
	print ("Sub-palindromes:", result)

```

