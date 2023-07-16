# Inverted index

## Task Link
[Rosetta Code - Inverted index](https://rosettacode.org/wiki/Inverted_index)

## Java Code
### java_code_1.txt
```java
package org.rosettacode;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class InvertedIndex {

    List<String> stopwords = Arrays.asList("a", "able", "about",
            "across", "after", "all", "almost", "also", "am", "among", "an",
            "and", "any", "are", "as", "at", "be", "because", "been", "but",
            "by", "can", "cannot", "could", "dear", "did", "do", "does",
            "either", "else", "ever", "every", "for", "from", "get", "got",
            "had", "has", "have", "he", "her", "hers", "him", "his", "how",
            "however", "i", "if", "in", "into", "is", "it", "its", "just",
            "least", "let", "like", "likely", "may", "me", "might", "most",
            "must", "my", "neither", "no", "nor", "not", "of", "off", "often",
            "on", "only", "or", "other", "our", "own", "rather", "said", "say",
            "says", "she", "should", "since", "so", "some", "than", "that",
            "the", "their", "them", "then", "there", "these", "they", "this",
            "tis", "to", "too", "twas", "us", "wants", "was", "we", "were",
            "what", "when", "where", "which", "while", "who", "whom", "why",
            "will", "with", "would", "yet", "you", "your");

    Map<String, List<Tuple>> index = new HashMap<String, List<Tuple>>();
    List<String> files = new ArrayList<String>();

    public void indexFile(File file) throws IOException {
        int fileno = files.indexOf(file.getPath());
        if (fileno == -1) {
            files.add(file.getPath());
            fileno = files.size() - 1;
        }

        int pos = 0;
        BufferedReader reader = new BufferedReader(new FileReader(file));
        for (String line = reader.readLine(); line != null; line = reader
                .readLine()) {
            for (String _word : line.split("\\W+")) {
                String word = _word.toLowerCase();
                pos++;
                if (stopwords.contains(word))
                    continue;
                List<Tuple> idx = index.get(word);
                if (idx == null) {
                    idx = new LinkedList<Tuple>();
                    index.put(word, idx);
                }
                idx.add(new Tuple(fileno, pos));
            }
        }
        System.out.println("indexed " + file.getPath() + " " + pos + " words");
    }

    public void search(List<String> words) {
        for (String _word : words) {
            Set<String> answer = new HashSet<String>();
            String word = _word.toLowerCase();
            List<Tuple> idx = index.get(word);
            if (idx != null) {
                for (Tuple t : idx) {
                    answer.add(files.get(t.fileno));
                }
            }
            System.out.print(word);
            for (String f : answer) {
                System.out.print(" " + f);
            }
            System.out.println("");
        }
    }

    public static void main(String[] args) {
        try {
            InvertedIndex idx = new InvertedIndex();
            for (int i = 1; i < args.length; i++) {
                idx.indexFile(new File(args[i]));
            }
            idx.search(Arrays.asList(args[0].split(",")));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private class Tuple {
        private int fileno;
        private int position;

        public Tuple(int fileno, int position) {
            this.fileno = fileno;
            this.position = position;
        }
    }
}

```

### java_code_2.txt
```java
java -cp bin org.rosettacode.InvertedIndex "huntsman,merit,dog,the,gutenberg,lovecraft,olympian" pg30637.txt pg7025.txt pg82.txt pg9090.txt
indexed pg30637.txt 106473 words
indexed pg7025.txt 205714 words
indexed pg82.txt 205060 words
indexed pg9090.txt 68962 words
huntsman pg82.txt pg7025.txt
merit pg9090.txt pg30637.txt pg82.txt pg7025.txt
dog pg30637.txt pg82.txt pg7025.txt
the
gutenberg pg9090.txt pg30637.txt pg82.txt pg7025.txt
lovecraft pg30637.txt
olympian pg30637.txt

```

## Python Code
### python_code_1.txt
```python
'''
This implements: http://en.wikipedia.org/wiki/Inverted_index of 28/07/10
'''

from pprint import pprint as pp
from glob import glob
try: reduce
except: from functools import reduce
try:    raw_input
except: raw_input = input


def parsetexts(fileglob='InvertedIndex/T*.txt'):
    texts, words = {}, set()
    for txtfile in glob(fileglob):
        with open(txtfile, 'r') as f:
            txt = f.read().split()
            words |= set(txt)
            texts[txtfile.split('\\')[-1]] = txt
    return texts, words

def termsearch(terms): # Searches simple inverted index
    return reduce(set.intersection,
                  (invindex[term] for term in terms),
                  set(texts.keys()))

texts, words = parsetexts()
print('\nTexts')
pp(texts)
print('\nWords')
pp(sorted(words))

invindex = {word:set(txt
                        for txt, wrds in texts.items() if word in wrds)
            for word in words}
print('\nInverted Index')
pp({k:sorted(v) for k,v in invindex.items()})

terms = ["what", "is", "it"]
print('\nTerm Search for: ' + repr(terms))
pp(sorted(termsearch(terms)))

```

### python_code_2.txt
```python
from collections import Counter


def termsearch(terms): # Searches full inverted index
    if not set(terms).issubset(words):
        return set()
    return reduce(set.intersection,
                  (set(x[0] for x in txtindx)
                   for term, txtindx in finvindex.items()
                   if term in terms),
                  set(texts.keys()) )

def phrasesearch(phrase):
    wordsinphrase = phrase.strip().strip('"').split()
    if not set(wordsinphrase).issubset(words):
        return set()
    #firstword, *otherwords = wordsinphrase # Only Python 3
    firstword, otherwords = wordsinphrase[0], wordsinphrase[1:]
    found = []
    for txt in termsearch(wordsinphrase):
        # Possible text files
        for firstindx in (indx for t,indx in finvindex[firstword]
                          if t == txt):
            # Over all positions of the first word of the phrase in this txt
            if all( (txt, firstindx+1 + otherindx) in finvindex[otherword]
                    for otherindx, otherword in enumerate(otherwords) ):
                found.append(txt)
    return found


finvindex = {word:set((txt, wrdindx)
                      for txt, wrds in texts.items()
                      for wrdindx in (i for i,w in enumerate(wrds) if word==w)
                      if word in wrds)
             for word in words}
print('\nFull Inverted Index')
pp({k:sorted(v) for k,v in finvindex.items()})

print('\nTerm Search on full inverted index for: ' + repr(terms))
pp(sorted(termsearch(terms)))

phrase = '"what is it"'
print('\nPhrase Search for: ' + phrase)
print(phrasesearch(phrase))

# Show multiple match capability
phrase = '"it is"'
print('\nPhrase Search for: ' + phrase)
ans = phrasesearch(phrase)
print(ans)
ans = Counter(ans)
print('  The phrase is found most commonly in text: ' + repr(ans.most_common(1)[0][0]))

```

