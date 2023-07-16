# ABC problem

## Task Link
[Rosetta Code - ABC problem](https://rosettacode.org/wiki/ABC_problem)

## Java Code
### java_code_1.txt
```java
static Boolean canMakeWord(List<String> src_blocks, String word) {
    if (String.isEmpty(word)) {
        return true;
    }

    List<String> blocks = new List<String>();
    for (String block : src_blocks) {
        blocks.add(block.toUpperCase());
    }
    
    for (Integer i = 0; i < word.length(); i++) {
        Integer blockIndex = -1;
        String c = word.mid(i, 1).toUpperCase();
        
        for (Integer j = 0; j < blocks.size(); j++) {
            if (blocks.get(j).contains(c)) {
                blockIndex = j;
                break;
            }
        }
        
        if (blockIndex == -1) {
            return false;
        } else {
            blocks.remove(blockIndex);
        }
    }
        
    return true;
}

List<String> blocks = new List<String>{
    'BO', 'XK', 'DQ', 'CP', 'NA',
    'GT', 'RE', 'TG', 'QD', 'FS', 
    'JW', 'HU', 'VI', 'AN', 'OB', 
    'ER', 'FS', 'LY', 'PC', 'ZM'
};
System.debug('"": ' + canMakeWord(blocks, ''));
System.debug('"A": ' + canMakeWord(blocks, 'A'));
System.debug('"BARK": ' + canMakeWord(blocks, 'BARK'));
System.debug('"book": ' + canMakeWord(blocks, 'book'));
System.debug('"treat": ' + canMakeWord(blocks, 'treat'));
System.debug('"COMMON": ' + canMakeWord(blocks, 'COMMON'));
System.debug('"SQuAd": ' + canMakeWord(blocks, 'SQuAd'));
System.debug('"CONFUSE": ' + canMakeWord(blocks, 'CONFUSE'));

```

### java_code_2.txt
```java
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ABC {

    public static void main(String[] args) {
        List<String> blocks = Arrays.asList(
                "BO", "XK", "DQ", "CP", "NA",
                "GT", "RE", "TG", "QD", "FS",
                "JW", "HU", "VI", "AN", "OB",
                "ER", "FS", "LY", "PC", "ZM");

        for (String word : Arrays.asList("", "A", "BARK", "BOOK", "TREAT", "COMMON", "SQUAD", "CONFUSE")) {
            System.out.printf("%s: %s%n", word.isEmpty() ? "\"\"" : word, canMakeWord(word, blocks));
        }
    }

    public static boolean canMakeWord(String word, List<String> blocks) {
        if (word.isEmpty())
            return true;

        char c = word.charAt(0);
        for (int i = 0; i < blocks.size(); i++) {
            String b = blocks.get(i);
            if (b.charAt(0) != c && b.charAt(1) != c)
                continue;
            Collections.swap(blocks, 0, i);
            if (canMakeWord(word.substring(1), blocks.subList(1, blocks.size())))
                return true;
            Collections.swap(blocks, 0, i);
        }

        return false;
    }
}

```

## Python Code
### python_code_1.txt
```python
    >>> can_make_word("A")
    True
    >>> can_make_word("BARK")
    True
    >>> can_make_word("BOOK")
    False
    >>> can_make_word("TREAT")
    True
    >>> can_make_word("COMMON")
    False
    >>> can_make_word("SQUAD")
    True
    >>> can_make_word("CONFUSE")
    True

```

### python_code_3.txt
```python
'''
Note that this code is broken, e.g., it won't work when 
blocks = [("A", "B"), ("A","C")] and the word is "AB", where the answer
should be True, but the code returns False.
'''
blocks = [("B", "O"),
          ("X", "K"),
          ("D", "Q"),
          ("C", "P"),
          ("N", "A"),
          ("G", "T"),
          ("R", "E"),
          ("T", "G"),
          ("Q", "D"),
          ("F", "S"),
          ("J", "W"),
          ("H", "U"),
          ("V", "I"),
          ("A", "N"),
          ("O", "B"),
          ("E", "R"),
          ("F", "S"),
          ("L", "Y"),
          ("P", "C"),
          ("Z", "M")]


def can_make_word(word, block_collection=blocks):
    """
    Return True if `word` can be made from the blocks in `block_collection`.

    >>> can_make_word("")
    False
    >>> can_make_word("a")
    True
    >>> can_make_word("bark")
    True
    >>> can_make_word("book")
    False
    >>> can_make_word("treat")
    True
    >>> can_make_word("common")
    False
    >>> can_make_word("squad")
    True
    >>> can_make_word("coNFused")
    True
    """
    if not word:
        return False

    blocks_remaining = block_collection[:]
    for char in word.upper():
        for block in blocks_remaining:
            if char in block:
                blocks_remaining.remove(block)
                break
        else:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(", ".join("'%s': %s" % (w, can_make_word(w)) for w in
                    ["", "a", "baRk", "booK", "treat", 
                     "COMMON", "squad", "Confused"]))

```

### python_code_4.txt
```python
BLOCKS = 'BO XK DQ CP NA GT RE TG QD FS JW HU VI AN OB ER FS LY PC ZM'.split()

def _abc(word, blocks):
    for i, ch in enumerate(word):
        for blk in (b for b in blocks if ch in b):
            whatsleft = word[i + 1:]
            blksleft = blocks[:]
            blksleft.remove(blk)
            if not whatsleft: 
                return True, blksleft
            if not blksleft: 
                return False, blksleft
            ans, blksleft = _abc(whatsleft, blksleft)
            if ans:
                return ans, blksleft
        else:
            break
    return False, blocks

def abc(word, blocks=BLOCKS):
    return _abc(word.upper(), blocks)[0]

if __name__ == '__main__':
    for word in [''] + 'A BARK BoOK TrEAT COmMoN SQUAD conFUsE'.split():
        print('Can we spell %9r? %r' % (word, abc(word)))

```

### python_code_5.txt
```python
def mkword(w, b):
    if not w: return []

    c,w = w[0],w[1:]
    for i in range(len(b)):
        if c in b[i]:
            m = mkword(w, b[0:i] + b[i+1:])
            if m != None: return [b[i]] + m

def abc(w, blk):
    return mkword(w.upper(), [a.upper() for a in blk])

blocks = 'BO XK DQ CP NA GT RE TG QD FS JW HU VI AN OB ER FS LY PC ZM'.split()

for w in ", A, bark, book, treat, common, SQUAD, conFUsEd".split(', '):
    print '\'' + w + '\'' + ' ->', abc(w, blocks)

```

