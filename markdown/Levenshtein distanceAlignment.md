# Levenshtein distance/Alignment

## Task Link
[Rosetta Code - Levenshtein distance/Alignment](https://rosettacode.org/wiki/Levenshtein_distance/Alignment)

## Java Code
### java_code_1.txt
```java
public class LevenshteinAlignment {

    public static String[] alignment(String a, String b) {
        a = a.toLowerCase();
        b = b.toLowerCase();
        // i == 0
        int[][] costs = new int[a.length()+1][b.length()+1];
        for (int j = 0; j <= b.length(); j++)
            costs[0][j] = j;
        for (int i = 1; i <= a.length(); i++) {
            costs[i][0] = i;
            for (int j = 1; j <= b.length(); j++) {
                costs[i][j] = Math.min(1 + Math.min(costs[i-1][j], costs[i][j-1]), a.charAt(i - 1) == b.charAt(j - 1) ? costs[i-1][j-1] : costs[i-1][j-1] + 1);
            }
        }

	// walk back through matrix to figure out path
	StringBuilder aPathRev = new StringBuilder();
	StringBuilder bPathRev = new StringBuilder();
	for (int i = a.length(), j = b.length(); i != 0 && j != 0; ) {
	    if (costs[i][j] == (a.charAt(i - 1) == b.charAt(j - 1) ? costs[i-1][j-1] : costs[i-1][j-1] + 1)) {
		aPathRev.append(a.charAt(--i));
		bPathRev.append(b.charAt(--j));
	    } else if (costs[i][j] == 1 + costs[i-1][j]) {
		aPathRev.append(a.charAt(--i));
		bPathRev.append('-');
	    } else if (costs[i][j] == 1 + costs[i][j-1]) {
		aPathRev.append('-');
		bPathRev.append(b.charAt(--j));
	    }
	}
        return new String[]{aPathRev.reverse().toString(), bPathRev.reverse().toString()};
    }

    public static void main(String[] args) {
	String[] result = alignment("rosettacode", "raisethysword");
	System.out.println(result[0]);
	System.out.println(result[1]);
    }
}

```

## Python Code
### python_code_1.txt
```python
from difflib import ndiff

def levenshtein(str1, str2):
    result = ""
    pos, removed = 0, 0
    for x in ndiff(str1, str2):
        if pos<len(str1) and str1[pos] == x[2]:
          pos += 1
          result += x[2]
          if x[0] == "-":
              removed += 1
          continue
        else:
          if removed > 0:
            removed -=1
          else:
            result += "-"
    print(result)

levenshtein("place","palace")
levenshtein("rosettacode","raisethysword")

```

