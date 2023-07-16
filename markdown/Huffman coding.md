# Huffman coding

## Task Link
[Rosetta Code - Huffman coding](https://rosettacode.org/wiki/Huffman_coding)

## Java Code
### java_code_1.txt
```java
import java.util.*;

abstract class HuffmanTree implements Comparable<HuffmanTree> {
    public final int frequency; // the frequency of this tree
    public HuffmanTree(int freq) { frequency = freq; }

    // compares on the frequency
    public int compareTo(HuffmanTree tree) {
        return frequency - tree.frequency;
    }
}

class HuffmanLeaf extends HuffmanTree {
    public final char value; // the character this leaf represents
   
    public HuffmanLeaf(int freq, char val) {
        super(freq);
        value = val;
    }
}

class HuffmanNode extends HuffmanTree {
    public final HuffmanTree left, right; // subtrees
   
    public HuffmanNode(HuffmanTree l, HuffmanTree r) {
        super(l.frequency + r.frequency);
        left = l;
        right = r;
    }
}

public class HuffmanCode {
    // input is an array of frequencies, indexed by character code
    public static HuffmanTree buildTree(int[] charFreqs) {
        PriorityQueue<HuffmanTree> trees = new PriorityQueue<HuffmanTree>();
        // initially, we have a forest of leaves
        // one for each non-empty character
        for (int i = 0; i < charFreqs.length; i++)
            if (charFreqs[i] > 0)
                trees.offer(new HuffmanLeaf(charFreqs[i], (char)i));

        assert trees.size() > 0;
        // loop until there is only one tree left
        while (trees.size() > 1) {
            // two trees with least frequency
            HuffmanTree a = trees.poll();
            HuffmanTree b = trees.poll();

            // put into new node and re-insert into queue
            trees.offer(new HuffmanNode(a, b));
        }
        return trees.poll();
    }

    public static void printCodes(HuffmanTree tree, StringBuffer prefix) {
        assert tree != null;
        if (tree instanceof HuffmanLeaf) {
            HuffmanLeaf leaf = (HuffmanLeaf)tree;

            // print out character, frequency, and code for this leaf (which is just the prefix)
            System.out.println(leaf.value + "\t" + leaf.frequency + "\t" + prefix);

        } else if (tree instanceof HuffmanNode) {
            HuffmanNode node = (HuffmanNode)tree;

            // traverse left
            prefix.append('0');
            printCodes(node.left, prefix);
            prefix.deleteCharAt(prefix.length()-1);

            // traverse right
            prefix.append('1');
            printCodes(node.right, prefix);
            prefix.deleteCharAt(prefix.length()-1);
        }
    }

    public static void main(String[] args) {
        String test = "this is an example for huffman encoding";

        // we will assume that all our characters will have
        // code less than 256, for simplicity
        int[] charFreqs = new int[256];
        // read each character and record the frequencies
        for (char c : test.toCharArray())
            charFreqs[c]++;

        // build tree
        HuffmanTree tree = buildTree(charFreqs);

        // print out results
        System.out.println("SYMBOL\tWEIGHT\tHUFFMAN CODE");
        printCodes(tree, new StringBuffer());
    }
}

```

## Python Code
### python_code_1.txt
```python
from heapq import heappush, heappop, heapify
from collections import defaultdict

def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

txt = "this is an example for huffman encoding"
symb2freq = defaultdict(int)
for ch in txt:
    symb2freq[ch] += 1
# in Python 3.1+:
# symb2freq = collections.Counter(txt)
huff = encode(symb2freq)
print "Symbol\tWeight\tHuffman Code"
for p in huff:
    print "%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1])

```

### python_code_2.txt
```python
"""Huffman encoding and decoding. Requires Python >= 3.7."""
from __future__ import annotations

from collections import Counter

from heapq import heapify
from heapq import heappush
from heapq import heappop

from itertools import chain
from itertools import islice

from typing import BinaryIO
from typing import Dict
from typing import Iterable
from typing import Optional
from typing import Tuple


LEFT_BIT = "0"
RIGHT_BIT = "1"
WORD_SIZE = 8  # Assumed to be a multiple of 8.
READ_SIZE = WORD_SIZE // 8
P_EOF = 1 << WORD_SIZE


class Node:
    """Huffman tree node."""

    def __init__(
        self,
        weight: int,
        symbol: Optional[int] = None,
        left: Optional[Node] = None,
        right: Optional[Node] = None,
    ):
        self.weight = weight
        self.symbol = symbol
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        """Return `True` if this node is a leaf node, or `False` otherwise."""
        return self.left is None and self.right is None

    def __lt__(self, other: Node) -> bool:
        return self.weight < other.weight


def huffman_tree(weights: Dict[int, int]) -> Node:
    """Build a prefix tree from a map of symbol frequencies."""
    heap = [Node(v, k) for k, v in weights.items()]
    heapify(heap)

    # Pseudo end-of-file with a weight of 1.
    heappush(heap, Node(1, P_EOF))

    while len(heap) > 1:
        left, right = heappop(heap), heappop(heap)
        node = Node(weight=left.weight + right.weight, left=left, right=right)
        heappush(heap, node)

    return heappop(heap)


def huffman_table(tree: Node) -> Dict[int, str]:
    """Build a table of prefix codes by visiting every leaf node in `tree`."""
    codes: Dict[int, str] = {}

    def walk(node: Optional[Node], code: str = ""):
        if node is None:
            return

        if node.is_leaf():
            assert node.symbol
            codes[node.symbol] = code
            return

        walk(node.left, code + LEFT_BIT)
        walk(node.right, code + RIGHT_BIT)

    walk(tree)
    return codes


def huffman_encode(data: bytes) -> Tuple[Iterable[bytes], Node]:
    """Encode the given byte string using Huffman coding.

    Returns the encoded byte stream and the Huffman tree required to
    decode those bytes.
    """
    weights = Counter(data)
    tree = huffman_tree(weights)
    table = huffman_table(tree)
    return _encode(data, table), tree


def huffman_decode(data: Iterable[bytes], tree: Node) -> bytes:
    """Decode the given byte stream using a Huffman tree."""
    return bytes(_decode(_bits_from_bytes(data), tree))


def _encode(stream: Iterable[int], codes: Dict[int, str]) -> Iterable[bytes]:
    bits = chain(chain.from_iterable(codes[s] for s in stream), codes[P_EOF])

    # Pack bits (stream of 1s and 0s) one word at a time.
    while True:
        word = "".join(islice(bits, WORD_SIZE))  # Most significant bit first.
        if not word:
            break

        # Pad last bits if they don't align to a whole word.
        if len(word) < WORD_SIZE:
            word = word.ljust(WORD_SIZE, "0")

        # Byte order becomes relevant when READ_SIZE > 1.
        yield int(word, 2).to_bytes(READ_SIZE, byteorder="big", signed=False)


def _decode(bits: Iterable[str], tree: Node) -> Iterable[int]:
    node = tree

    for bit in bits:
        if bit == LEFT_BIT:
            assert node.left
            node = node.left
        else:
            assert node.right
            node = node.right

        if node.symbol == P_EOF:
            break

        if node.is_leaf():
            assert node.symbol
            yield node.symbol
            node = tree  # Back to the top of the tree.


def _word_to_bits(word: bytes) -> str:
    """Return the binary representation of a word given as a byte string,
    including leading zeros up to WORD_SIZE.

    For example, when WORD_SIZE is 8:
        _word_to_bits(b'65') == '01000001'
    """
    i = int.from_bytes(word, "big")
    return bin(i)[2:].zfill(WORD_SIZE)


def _bits_from_file(file: BinaryIO) -> Iterable[str]:
    """Generate a stream of bits (strings of either "0" or "1") from file-like
    object `file`, opened in binary mode."""
    word = file.read(READ_SIZE)
    while word:
        yield from _word_to_bits(word)
        word = file.read(READ_SIZE)


def _bits_from_bytes(stream: Iterable[bytes]) -> Iterable[str]:
    """Generate a stream of bits (strings of either "0" or "1") from an
    iterable of single byte byte-strings."""
    return chain.from_iterable(_word_to_bits(byte) for byte in stream)


def main():
    """Example usage."""
    s = "this is an example for huffman encoding"
    data = s.encode()  # Need a byte string
    encoded, tree = huffman_encode(data)

    # Pretty print the Huffman table
    print(f"Symbol Code\n------ ----")
    for k, v in sorted(huffman_table(tree).items(), key=lambda x: len(x[1])):
        print(f"{chr(k):<6} {v}")

    # Print the bit pattern of the encoded data
    print("".join(_bits_from_bytes(encoded)))

    # Encode then decode
    decoded = huffman_decode(*huffman_encode(data))
    print(decoded.decode())


if __name__ == "__main__":
    main()

```

