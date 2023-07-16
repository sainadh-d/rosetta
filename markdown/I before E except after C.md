# I before E except after C

## Task Link
[Rosetta Code - I before E except after C](https://rosettacode.org/wiki/I_before_E_except_after_C)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;

```

### java_code_2.txt
```java
public static void main(String[] args) throws URISyntaxException, IOException {
    count();
    System.out.printf("%-10s %,d%n", "total", total);
    System.out.printf("%-10s %,d%n", "'cei'", cei);
    System.out.printf("%-10s %,d%n", "'cie'", cie);
    System.out.printf("%,d > (%,d * 2) = %b%n", cei, cie, cei > (cie * 2));
    System.out.printf("%,d > (%,d * 2) = %b", cie, cei, cie > (cei * 2));
}

static int total = 0;
static int cei = 0;
static int cie = 0;

static void count() throws URISyntaxException, IOException {
    URL url = new URI("http://wiki.puzzlers.org/pub/wordlists/unixdict.txt").toURL();
    try (BufferedReader reader = new BufferedReader(new InputStreamReader(url.openStream()))) {
        String line;
        while ((line = reader.readLine()) != null) {
            if (line.matches(".*?(?:[^c]ie|cei).*")) {
                cei++;
            } else if (line.matches(".*?(?:[^c]ei|cie).*")) {
                cie++;
            }
            total++;
        }
    }
}

```

### java_code_3.txt
```java
import java.io.BufferedReader;
import java.io.FileReader;

public class IbeforeE 
{
	public static void main(String[] args)
	{
		IbeforeE now=new IbeforeE();
		String wordlist="unixdict.txt";
		if(now.isPlausibleRule(wordlist))
			System.out.println("Rule is plausible.");
		else
			System.out.println("Rule is not plausible.");
	}
	boolean isPlausibleRule(String filename)
	{
		int truecount=0,falsecount=0;
		try
		{
			BufferedReader br=new BufferedReader(new FileReader(filename));
			String word;
			while((word=br.readLine())!=null)
			{
				if(isPlausibleWord(word))
					truecount++;
				else if(isOppPlausibleWord(word))
					falsecount++;
			}
			br.close();
		}
		catch(Exception e)
		{
			System.out.println("Something went horribly wrong: "+e.getMessage());
		}
		
		System.out.println("Plausible count: "+truecount);
		System.out.println("Implausible count: "+falsecount);
		if(truecount>2*falsecount)
			return true;
		return false;
	}
	boolean isPlausibleWord(String word)
	{
		if(!word.contains("c")&&word.contains("ie"))
			return true;
		else if(word.contains("cei"))
			return true;
		return false;
	}
	boolean isOppPlausibleWord(String word)
	{
		if(!word.contains("c")&&word.contains("ei"))
			return true;
		else if(word.contains("cie"))
			return true;
		return false;
	}
}

```

## Python Code
### python_code_1.txt
```python
import urllib.request
import re

PLAUSIBILITY_RATIO = 2

def plausibility_check(comment, x, y):
    print('\n  Checking plausibility of: %s' % comment)
    if x > PLAUSIBILITY_RATIO * y:
        print('    PLAUSIBLE. As we have counts of %i vs %i, a ratio of %4.1f times'
              % (x, y, x / y))
    else:
        if x > y:
            print('    IMPLAUSIBLE. As although we have counts of %i vs %i, a ratio of %4.1f times does not make it plausible'
                  % (x, y, x / y))
        else:
            print('    IMPLAUSIBLE, probably contra-indicated. As we have counts of %i vs %i, a ratio of %4.1f times'
                  % (x, y, x / y))
    return x > PLAUSIBILITY_RATIO * y

def simple_stats(url='http://wiki.puzzlers.org/pub/wordlists/unixdict.txt'):
    words = urllib.request.urlopen(url).read().decode().lower().split()
    cie = len({word for word in words if 'cie' in word})
    cei = len({word for word in words if 'cei' in word})
    not_c_ie = len({word for word in words if re.search(r'(^ie|[^c]ie)', word)})
    not_c_ei = len({word for word in words if re.search(r'(^ei|[^c]ei)', word)})
    return cei, cie, not_c_ie, not_c_ei

def print_result(cei, cie, not_c_ie, not_c_ei):
    if ( plausibility_check('I before E when not preceded by C', not_c_ie, not_c_ei)
         & plausibility_check('E before I when preceded by C', cei, cie) ):
        print('\nOVERALL IT IS PLAUSIBLE!')
    else:
        print('\nOVERALL IT IS IMPLAUSIBLE!')
    print('(To be plausible, one count must exceed another by %i times)' % PLAUSIBILITY_RATIO)

print('Checking plausibility of "I before E except after C":')
print_result(*simple_stats())

```

### python_code_2.txt
```python
def stretch_stats(url='http://ucrel.lancs.ac.uk/bncfreq/lists/1_2_all_freq.txt'):
    freq = [line.strip().lower().split()
            for line in urllib.request.urlopen(url)
            if len(line.strip().split()) == 3]
    wordfreq = [(word.decode(), int(frq))
                for word, pos, frq in freq[1:]
                if (b'ie' in word) or (b'ei' in word)]
    cie = sum(frq for word, frq in wordfreq if 'cie' in word)
    cei = sum(frq for word, frq in wordfreq if 'cei' in word)
    not_c_ie = sum(frq for word, frq in wordfreq if re.search(r'(^ie|[^c]ie)', word))
    not_c_ei = sum(frq for word, frq in wordfreq if re.search(r'(^ei|[^c]ei)', word))
    return cei, cie, not_c_ie, not_c_ei

print('\n\nChecking plausibility of "I before E except after C"')
print('And taking account of word frequencies in British English:')
print_result(*stretch_stats())

```

