# Word ladder

## Task Link
[Rosetta Code - Word ladder](https://rosettacode.org/wiki/Word_ladder)

## Java Code
### java_code_1.txt
```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.stream.IntStream;

public class WordLadder {
    private static int distance(String s1, String s2) {
        assert s1.length() == s2.length();
        return (int) IntStream.range(0, s1.length())
            .filter(i -> s1.charAt(i) != s2.charAt(i))
            .count();
    }

    private static void wordLadder(Map<Integer, Set<String>> words, String fw, String tw) {
        wordLadder(words, fw, tw, 8);
    }

    private static void wordLadder(Map<Integer, Set<String>> words, String fw, String tw, int limit) {
        if (fw.length() != tw.length()) {
            throw new IllegalArgumentException("From word and to word must have the same length");
        }

        Set<String> ws = words.get(fw.length());
        if (ws.contains(fw)) {
            List<String> primeList = new ArrayList<>();
            primeList.add(fw);

            PriorityQueue<List<String>> queue = new PriorityQueue<>((chain1, chain2) -> {
                int cmp1 = Integer.compare(chain1.size(), chain2.size());
                if (cmp1 == 0) {
                    String last1 = chain1.get(chain1.size() - 1);
                    int d1 = distance(last1, tw);

                    String last2 = chain2.get(chain2.size() - 1);
                    int d2 = distance(last2, tw);

                    return Integer.compare(d1, d2);
                }
                return cmp1;
            });
            queue.add(primeList);

            while (queue.size() > 0) {
                List<String> curr = queue.remove();
                if (curr.size() > limit) {
                    continue;
                }

                String last = curr.get(curr.size() - 1);
                for (String word : ws) {
                    if (distance(last, word) == 1) {
                        if (word.equals(tw)) {
                            curr.add(word);
                            System.out.println(String.join(" -> ", curr));
                            return;
                        }

                        if (!curr.contains(word)) {
                            List<String> cp = new ArrayList<>(curr);
                            cp.add(word);
                            queue.add(cp);
                        }
                    }
                }
            }
        }

        System.err.printf("Cannot turn `%s` into `%s`%n", fw, tw);
    }

    public static void main(String[] args) throws IOException {
        Map<Integer, Set<String>> words = new HashMap<>();
        for (String line : Files.readAllLines(Path.of("unixdict.txt"))) {
            Set<String> wl = words.computeIfAbsent(line.length(), HashSet::new);
            wl.add(line);
        }

        wordLadder(words, "boy", "man");
        wordLadder(words, "girl", "lady");
        wordLadder(words, "john", "jane");
        wordLadder(words, "child", "adult");
        wordLadder(words, "cat", "dog");
        wordLadder(words, "lead", "gold");
        wordLadder(words, "white", "black");
        wordLadder(words, "bubble", "tickle", 12);
    }
}

```

### java_code_2.txt
```java
import java.io.*;
import java.util.*;

public class WordLadder {
    public static void main(String[] args) {
        try {
            Map<Integer, List<String>> words = new HashMap<>();
            try (BufferedReader reader = new BufferedReader(new FileReader("unixdict.txt"))) {
                String line;
                while ((line = reader.readLine()) != null)
                    words.computeIfAbsent(line.length(), k -> new ArrayList<String>()).add(line);
            }
            wordLadder(words, "boy", "man");
            wordLadder(words, "girl", "lady");
            wordLadder(words, "john", "jane");
            wordLadder(words, "child", "adult");
            wordLadder(words, "cat", "dog");
            wordLadder(words, "lead", "gold");
            wordLadder(words, "white", "black");
            wordLadder(words, "bubble", "tickle");
        } catch (Exception e)  {
            e.printStackTrace();
        }   
    }

    // Returns true if strings s1 and s2 differ by one character.
    private static boolean oneAway(String s1, String s2) {
        if (s1.length() != s2.length())
            return false;
        boolean result = false;
        for (int i = 0, n = s1.length(); i != n; ++i) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (result)
                    return false;
                result = true;
            }
        }
        return result;
    }

    // If possible, print the shortest chain of single-character modifications that
    // leads from "from" to "to", with each intermediate step being a valid word.
    // This is an application of breadth-first search.
    private static void wordLadder(Map<Integer, List<String>> words, String from, String to) {
        List<String> w = words.get(from.length());
        if (w != null) {
            Deque<String> poss = new ArrayDeque<>(w);
            Deque<String> f = new ArrayDeque<String>();
            f.add(from);
            Deque<Deque<String>> queue = new ArrayDeque<>();
            queue.add(f);
            while (!queue.isEmpty()) {
                Deque<String> curr = queue.poll();
                for (Iterator<String> i = poss.iterator(); i.hasNext(); ) {
                    String str = i.next();
                    if (!oneAway(str, curr.getLast()))
                        continue;
                    if (to.equals(str)) {
                        curr.add(to);
                        System.out.println(String.join(" -> ", curr));
                        return;
                    }
                    Deque<String> temp = new ArrayDeque<>(curr);
                    temp.add(str);
                    queue.add(temp);
                    i.remove();
                }
            }
        }
        System.out.printf("%s into %s cannot be done.\n", from, to);
    }
}

```

## Python Code
### python_code_1.txt
```python
import os,sys,zlib,urllib.request

def h ( str,x=9 ):
    for c in str :
        x = ( x*33 + ord( c )) & 0xffffffffff
    return x  

def cache ( func,*param ):
    n = 'cache_%x.bin'%abs( h( repr( param )))
    try    : return eval( zlib.decompress( open( n,'rb' ).read()))
    except : pass
    s = func( *param )
    open( n,'wb' ).write( zlib.compress( bytes( repr( s ),'ascii' )))
    return s

dico_url  = 'https://raw.githubusercontent.com/quinnj/Rosetta-Julia/master/unixdict.txt'
read_url  = lambda url   : urllib.request.urlopen( url ).read()
load_dico = lambda url   : tuple( cache( read_url,url ).split( b'\n'))
isnext    = lambda w1,w2 : len( w1 ) == len( w2 ) and len( list( filter( lambda l : l[0]!=l[1] , zip( w1,w2 )))) == 1

def build_map ( words ):
    map = [(w.decode('ascii'),[]) for w in words]
    for i1,(w1,n1) in enumerate( map ):
        for i2,(w2,n2) in enumerate( map[i1+1:],i1+1 ):
            if isnext( w1,w2 ):
                n1.append( i2 )
                n2.append( i1 )
    return map

def find_path ( words,w1,w2 ):
    i = [w[0] for w in words].index( w1 )
    front,done,res  = [i],{i:-1},[]
    while front :
        i = front.pop(0)
        word,next = words[i]
        for n in next :
            if n in done : continue
            done[n] = i
            if words[n][0] == w2 :
                while n >= 0 :
                    res = [words[n][0]] + res
                    n = done[n]
                return ' '.join( res )
            front.append( n )
    return '%s can not be turned into %s'%( w1,w2 )

for w in ('boy man','girl lady','john jane','alien drool','child adult'):
    print( find_path( cache( build_map,load_dico( dico_url )),*w.split()))

```

