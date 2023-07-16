# Strip block comments

## Task Link
[Rosetta Code - Strip block comments](https://rosettacode.org/wiki/Strip_block_comments)

## Java Code
### java_code_1.txt
```java
import java.io.*;

public class StripBlockComments{
    public static String readFile(String filename) {
	BufferedReader reader = new BufferedReader(new FileReader(filename));
	try {
	    StringBuilder fileContents = new StringBuilder();
	    char[] buffer = new char[4096];
	    while (reader.read(buffer, 0, 4096) > 0) {
		fileContents.append(buffer);
	    }
	    return fileContents.toString();
	} finally {
	    reader.close();
	}
    }

    public static String stripComments(String beginToken, String endToken,
				       String input) {
	StringBuilder output = new StringBuilder();
	while (true) {
	    int begin = input.indexOf(beginToken);
	    int end = input.indexOf(endToken, begin+beginToken.length());
	    if (begin == -1 || end == -1) {
		output.append(input);
		return output.toString();
	    }
	    output.append(input.substring(0, begin));
	    input = input.substring(end + endToken.length());
	}
    }

    public static void main(String[] args) {
	if (args.length < 3) {
	    System.out.println("Usage: BeginToken EndToken FileToProcess");
	    System.exit(1);
	}

	String begin = args[0];
	String end = args[1];
	String input = args[2];

	try {
	    System.out.println(stripComments(begin, end, readFile(input)));
	} catch (Exception e) {
	    e.printStackTrace();
	    System.exit(1);
	}
    }
}

```

## Python Code
### python_code_1.txt
```python
def _commentstripper(txt, delim):
    'Strips first nest of block comments'
    
    deliml, delimr = delim
    out = ''
    if deliml in txt:
        indx = txt.index(deliml)
        out += txt[:indx]
        txt = txt[indx+len(deliml):]
        txt = _commentstripper(txt, delim)
        assert delimr in txt, 'Cannot find closing comment delimiter in ' + txt
        indx = txt.index(delimr)
        out += txt[(indx+len(delimr)):]
    else:
        out = txt
    return out

def commentstripper(txt, delim=('/*', '*/')):
    'Strips nests of block comments'
    
    deliml, delimr = delim
    while deliml in txt:
        txt = _commentstripper(txt, delim)
    return txt

```

### python_code_2.txt
```python
def test():
    print('\nNON-NESTED BLOCK COMMENT EXAMPLE:')
    sample = '''  /**
   * Some comments
   * longer comments here that we can parse.
   *
   * Rahoo 
   */
   function subroutine() {
    a = /* inline comment */ b + c ;
   }
   /*/ <-- tricky comments */

   /**
    * Another comment.
    */
    function something() {
    }'''
    print(commentstripper(sample))

    print('\nNESTED BLOCK COMMENT EXAMPLE:')
    sample = '''  /**
   * Some comments
   * longer comments here that we can parse.
   *
   * Rahoo 
   *//*
   function subroutine() {
    a = /* inline comment */ b + c ;
   }
   /*/ <-- tricky comments */
   */
   /**
    * Another comment.
    */
    function something() {
    }'''
    print(commentstripper(sample))
    
if __name__ == '__main__':
    test()

```

