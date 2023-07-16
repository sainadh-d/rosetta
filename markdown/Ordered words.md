# Ordered words

## Task Link
[Rosetta Code - Ordered words](https://rosettacode.org/wiki/Ordered_words)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

public class Ordered {

	private static boolean isOrderedWord(String word){
		char[] sortedWord = word.toCharArray();
		Arrays.sort(sortedWord);
		return word.equals(new String(sortedWord));
	}
	
	public static void main(String[] args) throws IOException{
		List<String> orderedWords = new LinkedList<String>();
		BufferedReader in = new BufferedReader(new FileReader(args[0]));
		while(in.ready()){
			String word = in.readLine();
			if(isOrderedWord(word)) orderedWords.add(word);
		}
		in.close();
		
		Collections.<String>sort(orderedWords, new Comparator<String>() {
			@Override
			public int compare(String o1, String o2) {
				return new Integer(o2.length()).compareTo(o1.length());
			}
		});
		
		int maxLen = orderedWords.get(0).length();
		for(String word: orderedWords){
			if(word.length() == maxLen){
				System.out.println(word);
			}else{
				break;
			}
		}
	}
}

```

### java_code_2.txt
```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public final class OrderedWords {

	public static void main(String[] aArgs) throws IOException {
		List<String> ordered = Files.lines(Path.of("unixdict.txt"))
				                    .filter( word -> isOrdered(word) ).toList();
	    	    
	    final int maxLength = ordered.stream().map( word -> word.length() ).max(Integer::compare).get();
	    ordered.stream().filter( word -> word.length() == maxLength ).forEach(System.out::println);	   
	}
	
	private static boolean isOrdered(String aWord) {
		return aWord.chars()
				    .mapToObj( i -> (char) i )
				    .sorted()
				    .map(String::valueOf)
				    .reduce("", String::concat)
				    .equals(aWord);
	}

}

```

## Python Code
### python_code_1.txt
```python
import urllib.request

url = 'http://www.puzzlers.org/pub/wordlists/unixdict.txt'
words = urllib.request.urlopen(url).read().decode("utf-8").split()
ordered = [word for word in words if word==''.join(sorted(word))]
maxlen = len(max(ordered, key=len))
maxorderedwords = [word for word in ordered if len(word) == maxlen]
print(' '.join(maxorderedwords))

```

### python_code_2.txt
```python
import urllib.request

mx, url = 0, 'http://www.puzzlers.org/pub/wordlists/unixdict.txt'

for word in urllib.request.urlopen(url).read().decode("utf-8").split():
    lenword = len(word)
    if lenword >= mx and word==''.join(sorted(word)):
        if lenword > mx:
            words, mx = [], lenword
        words.append(word)
print(' '.join(words))

```

### python_code_3.txt
```python
'''The longest ordered words in a list'''

from functools import reduce
from operator import le
import urllib.request


# longestOrds :: [String] -> [String]
def longestOrds(ws):
    '''The longest ordered words in a given list.
    '''
    return reduce(triage, ws, (0, []))[1]


# triage :: (Int, [String]) -> String -> (Int, [String])
def triage(nxs, w):
    '''The maximum length seen for an ordered word,
       and the ordered words of this length seen so far.
    '''
    n, xs = nxs
    lng = len(w)
    return (
        (lng, ([w] if n != lng else xs + [w])) if (
            ordered(w)
        ) else nxs
    ) if lng >= n else nxs


# ordered :: String -> Bool
def ordered(w):
    '''True if the word w is ordered.'''
    return all(map(le, w, w[1:]))


# ------------------------- TEST -------------------------
if __name__ == '__main__':
    print(
        '\n'.join(longestOrds(
            urllib.request.urlopen(
                'http://wiki.puzzlers.org/pub/wordlists/unixdict.txt'
            ).read().decode("utf-8").split()
        ))
    )

```

