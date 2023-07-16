# N'th

## Task Link
[Rosetta Code - N'th](https://rosettacode.org/wiki/N%27th)

## Java Code
### java_code_1.txt
```java
public class Nth {
	public static String ordinalAbbrev(int n){
		String ans = "th"; //most of the time it should be "th"
		if(n % 100 / 10 == 1) return ans; //teens are all "th"
		switch(n % 10){
			case 1: ans = "st"; break;
			case 2: ans = "nd"; break;
			case 3: ans = "rd"; break;
		}
		return ans;
	}
	
	public static void main(String[] args){
		for(int i = 0; i <= 25;i++){
			System.out.print(i + ordinalAbbrev(i) + " ");
		}
		System.out.println();
		for(int i = 250; i <= 265;i++){
			System.out.print(i + ordinalAbbrev(i) + " ");
		}
		System.out.println();
		for(int i = 1000; i <= 1025;i++){
			System.out.print(i + ordinalAbbrev(i) + " ");
		}
	}
}

```

### java_code_2.txt
```java
package nth;

import java.util.stream.IntStream;
import java.util.stream.Stream;

public interface Nth {
  public static String suffix(int n){
    if(n % 100 / 10 == 1){
      return "th"; //teens are all "th"
    }
    switch(n % 10){
      case 1: return "st";
      case 2: return "nd";
      case 3: return "rd";
      default: return "th"; //most of the time it should be "th"
    }
  }

  public static void print(int start, int end) {
    IntStream.rangeClosed(start, end)
      .parallel()
      .mapToObj(i -> i + suffix(i) + " ")
      .reduce(String::concat)
      .ifPresent(System.out::println)
    ;
  }

  public static void print(int[] startAndEnd) {
    print(startAndEnd[0], startAndEnd[1]);
  }

  public static int[] startAndEnd(int start, int end) {
    return new int[] {
      start,
      end
    };
  }
 
  public static void main(String... arguments){
    Stream.of(
      startAndEnd(0, 25),
      startAndEnd(250, 265),
      startAndEnd(1000, 1025)
    )
      .forEach(Nth::print)
    ;
  }
}

```

## Python Code
### python_code_1.txt
```python
_suffix = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']

def nth(n):
    return "%i'%s" % (n, _suffix[n%10] if n % 100 <= 10 or n % 100 > 20 else 'th')

if __name__ == '__main__':
    for j in range(0,1001, 250):
        print(' '.join(nth(i) for i in list(range(j, j+25))))

```

### python_code_2.txt
```python
#!/usr/bin/env python3

def ord(n):
    try:
        s = ['st', 'nd', 'rd'][(n-1)%10]
        if (n-10)%100//10:
            return str(n)+s
    except IndexError:
        pass
    return str(n)+'th'

if __name__ == '__main__':
    print(*(ord(n) for n in range(26)))
    print(*(ord(n) for n in range(250,266)))
    print(*(ord(n) for n in range(1000,1026)))

```

