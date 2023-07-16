# Last letter-first letter

## Task Link
[Rosetta Code - Last letter-first letter](https://rosettacode.org/wiki/Last_letter-first_letter)

## Java Code
### java_code_1.txt
```java
// derived from C
final class LastLetterFirstLetter {
    static int maxPathLength = 0;
    static int maxPathLengthCount = 0;
    static final StringBuffer maxPathExample = new StringBuffer(500);

    static final String[] names = {"audino", "bagon", "baltoy", "banette",
        "bidoof", "braviary", "bronzor", "carracosta", "charmeleon",
        "cresselia", "croagunk", "darmanitan", "deino", "emboar",
        "emolga", "exeggcute", "gabite", "girafarig", "gulpin",
        "haxorus", "heatmor", "heatran", "ivysaur", "jellicent",
        "jumpluff", "kangaskhan", "kricketune", "landorus", "ledyba",
        "loudred", "lumineon", "lunatone", "machamp", "magnezone",
        "mamoswine", "nosepass", "petilil", "pidgeotto", "pikachu",
        "pinsir", "poliwrath", "poochyena", "porygon2", "porygonz",
        "registeel", "relicanth", "remoraid", "rufflet", "sableye",
        "scolipede", "scrafty", "seaking", "sealeo", "silcoon",
        "simisear", "snivy", "snorlax", "spoink", "starly", "tirtouga",
        "trapinch", "treecko", "tyrogue", "vigoroth", "vulpix",
        "wailord", "wartortle", "whismur", "wingull", "yamask"};

    static void recursive(String[] part, int offset) {
        if (offset > maxPathLength) {
            maxPathLength = offset;
            maxPathLengthCount = 1;
        } else if (offset == maxPathLength) {
            maxPathLengthCount++;
            maxPathExample.setLength(0);
            for (int i = 0; i < offset; i++) {
                maxPathExample.append((i % 5 == 0 ? "\n  " : " "));
                maxPathExample.append(part[i]);
            }
        }
        final char lastChar = part[offset - 1].charAt(part[offset - 1].length()-1);
        for (int i = offset; i < part.length; i++) {
            if (part[i].charAt(0) == lastChar) {
                String tmp = names[offset];
                names[offset] = names[i];
                names[i] = tmp;
                recursive(names, offset+1);
                names[i] = names[offset];
                names[offset] = tmp;
            }
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < names.length; i++) {
            String tmp = names[0];
            names[0] = names[i];
            names[i] = tmp;
            recursive(names, 1);
            names[i] = names[0];
            names[0] = tmp;
       }
       System.out.println("maximum path length        : " + maxPathLength);
       System.out.println("paths of that length       : " + maxPathLengthCount);
       System.out.println("example path of that length:" + maxPathExample);
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import defaultdict

def order_words(words):
    byfirst = defaultdict(set)
    for word in words:
        byfirst[word[0]].add( word )
    #byfirst = dict(byfirst)
    return byfirst

def linkfirst(byfirst, sofar):
    '''\
    For all words matching last char of last word in sofar as FIRST char and not in sofar,
    return longest chain as sofar + chain
    '''

    assert sofar
    chmatch = sofar[-1][-1]
    options = byfirst[chmatch] - set(sofar)
    #print('  linkfirst options: %r %r' % (chmatch, options))
    if not options:
        return sofar
    else:
        alternatives = ( linkfirst(byfirst, list(sofar) + [word])
                         for word in options )
        mx = max( alternatives, key=len )
        #input('linkfirst: %r' % mx)
        return mx

def llfl(words):

    byfirst = order_words(words)
    return max( (linkfirst(byfirst, [word]) for word in words), key=len )

if __name__ == '__main__':
    pokemon = '''audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'''
    pokemon = pokemon.strip().lower().split()
    pokemon = sorted(set(pokemon))    
    l = llfl(pokemon)
    for i in range(0, len(l), 8): print(' '.join(l[i:i+8]))
    print(len(l))

```

### python_code_2.txt
```python
import psyco

nsolutions = 0

def search(sequences, ord_minc, curr_word, current_path,
           current_path_len, longest_path):
    global nsolutions

    current_path[current_path_len] = curr_word
    current_path_len += 1

    if current_path_len == len(longest_path):
        nsolutions += 1
    elif current_path_len > len(longest_path):
        nsolutions = 1
        longest_path[:] = current_path[:current_path_len]

    # recursive search
    last_char_index = ord(curr_word[-1]) - ord_minc
    if last_char_index >= 0 and last_char_index < len(sequences):
        for pair in sequences[last_char_index]:
            if not pair[1]:
                pair[1] = True
                search(sequences, ord_minc, pair[0], current_path,
                       current_path_len, longest_path)
                pair[1] = False


def find_longest_chain(words):
    ord_minc = ord(min(word[0] for word in words))
    ord_maxc = ord(max(word[0] for word in words))
    sequences = [[] for _ in xrange(ord_maxc - ord_minc + 1)]
    for word in words:
        sequences[ord(word[0]) - ord_minc].append([word, False])

    current_path = [None] * len(words)
    longest_path = []

    # try each item as possible start
    for seq in sequences:
        for pair in seq:
            pair[1] = True
            search(sequences, ord_minc, pair[0],
                   current_path, 0, longest_path)
            pair[1] = False

    return longest_path


def main():
    global nsolutions

    pokemon = """audino bagon baltoy banette bidoof braviary
bronzor carracosta charmeleon cresselia croagunk darmanitan deino
emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor
heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus
ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass
petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede
scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly
tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle
whismur wingull yamask""".lower().split()

    # remove duplicates
    pokemon = sorted(set(pokemon))

    sol = find_longest_chain(pokemon)
    print "Maximum path length:", len(sol)
    print "Paths of that length:", nsolutions
    print "Example path of that length:"
    for i in xrange(0, len(sol), 7):
        print " ", " ".join(sol[i : i+7])

psyco.full()
main()

```

