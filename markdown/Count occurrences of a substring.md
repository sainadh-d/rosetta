# Count occurrences of a substring

## Task Link
[Rosetta Code - Count occurrences of a substring](https://rosettacode.org/wiki/Count_occurrences_of_a_substring)

## Java Code
### java_code_1.txt
```java
int countSubstring(String string, String substring) {
    substring = Pattern.quote(substring);
    Pattern pattern = Pattern.compile(substring);
    Matcher matcher = pattern.matcher(string);
    int count = 0;
    while (matcher.find())
        count++;
    return count;
}

```

### java_code_2.txt
```java
public class CountSubstring {
	public static int countSubstring(String subStr, String str){
		return (str.length() - str.replace(subStr, "").length()) / subStr.length();
	}
	
	public static void main(String[] args){
		System.out.println(countSubstring("th", "the three truths"));
		System.out.println(countSubstring("abab", "ababababab"));
		System.out.println(countSubstring("a*b", "abaabba*bbaba*bbab"));
	}
}

```

### java_code_3.txt
```java
import java.util.regex.Pattern;

public class CountSubstring {
	public static int countSubstring(String subStr, String str){
		// the result of split() will contain one more element than the delimiter
		// the "-1" second argument makes it not discard trailing empty strings
		return str.split(Pattern.quote(subStr), -1).length - 1;
	}
	
	public static void main(String[] args){
		System.out.println(countSubstring("th", "the three truths"));
		System.out.println(countSubstring("abab", "ababababab"));
		System.out.println(countSubstring("a*b", "abaabba*bbaba*bbab"));
	}
}

```

### java_code_4.txt
```java
public class CountSubstring {
	public static int countSubstring(String subStr, String str){
		int count = 0;
		for (int loc = str.indexOf(subStr); loc != -1;
		     loc = str.indexOf(subStr, loc + subStr.length()))
			count++;
		return count;
	}
	
	public static void main(String[] args){
		System.out.println(countSubstring("th", "the three truths"));
		System.out.println(countSubstring("abab", "ababababab"));
		System.out.println(countSubstring("a*b", "abaabba*bbaba*bbab"));
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> "the three truths".count("th")
3
>>> "ababababab".count("abab")
2

```

