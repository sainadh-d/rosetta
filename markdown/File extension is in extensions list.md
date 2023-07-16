# File extension is in extensions list

## Task Link
[Rosetta Code - File extension is in extensions list](https://rosettacode.org/wiki/File_extension_is_in_extensions_list)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.Comparator;

public class FileExt{
	public static void main(String[] args){
		String[] tests = {"text.txt", "text.TXT", "test.tar.gz", "test/test2.exe", "test\\test2.exe", "test", "a/b/c\\d/foo"};
		String[] exts = {".txt",".gz","",".bat"};
		
		System.out.println("Extensions: " + Arrays.toString(exts) + "\n");
		
		for(String test:tests){
			System.out.println(test +": " + extIsIn(test, exts));
		}
	}
	
	public static boolean extIsIn(String test, String... exts){
		int lastSlash = Math.max(test.lastIndexOf('/'), test.lastIndexOf('\\')); //whichever one they decide to use today
		String filename = test.substring(lastSlash + 1);//+1 to get rid of the slash or move to index 0 if there's no slash
		
		//end of the name if no dot, last dot index otherwise
		int lastDot = filename.lastIndexOf('.') == -1 ? filename.length() : filename.lastIndexOf('.');
		String ext = filename.substring(lastDot);//everything at the last dot and after is the extension
		
		Arrays.sort(exts);//sort for the binary search
		
		return Arrays.binarySearch(exts, ext, new Comparator<String>() { //just use the built-in binary search method
			@Override                                                //it will let us specify a Comparator and it's fast enough
			public int compare(String o1, String o2) {
				return o1.compareToIgnoreCase(o2);
			}
		}) >= 0;//binarySearch returns negative numbers when it's not found
	}
}

```

### java_code_2.txt
```java
public static boolean extIsIn(String test, String... exts){
	for(int i = 0; i < exts.length; i++){
		exts[i] = exts[i].replaceAll("\\.", "");
	}
	return (new FileNameExtensionFilter("extension test", exts)).accept(new File(test));
}

```

## Python Code
### python_code_1.txt
```python
def isExt(fileName, extensions):
  return True in map(fileName.lower().endswith, ("." + e.lower() for e in extensions))

```

### python_code_2.txt
```python
'''Check for a specific set of file extensions'''


# extensionFound :: [Extension] -> FileName -> Maybe Extension
def extensionFound(xs):
    '''Nothing if no matching extension is found,
       or Just the extension (drawn from xs, and
       a suffix of the filename, immediately following
       a dot character).
    '''
    return lambda fn: find(fn.lower().endswith)(
        ['.' + x.lower() for x in xs]
    )


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Check filenames for a particular set of extensions.'''

    # checkExtension :: FileName -> Maybe Extension
    def checkExtension(fn):
        return extensionFound([
            'zip', 'rar', '7z', 'gz', 'archive', 'A##', 'tar.bz2'
        ])(fn)

    print(
        fTable(__doc__ + ':\n')(str)(str)(
            compose(fromMaybe('n/a'))(checkExtension)
        )([
            'MyData.a##',
            'MyData.tar.Gz',
            'MyData.gzip',
            'MyData.7z.backup',
            'MyData...',
            'MyData',
            'MyData_v1.0.tar.bz2',
            'MyData_v1.0.bz2'
        ])
    )


# GENERIC -------------------------------------------------

# Just :: a -> Maybe a
def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.'''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


# Nothing :: Maybe a
def Nothing():
    '''Constructor for an empty Maybe (option type) value.'''
    return {'type': 'Maybe', 'Nothing': True}


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# find :: (a -> Bool) -> [a] -> Maybe a
def find(p):
    '''Just the first element in the list that matches p,
       or Nothing if no elements match.
    '''
    def go(xs):
        for x in xs:
            if p(x):
                return Just(x)
        return Nothing()
    return lambda xs: go(xs)


# fromMaybe :: a -> Maybe a -> a
def fromMaybe(x):
    '''The default value x if mb is Nothing,
       or the value contained in mb.
    '''
    return lambda mb: x if (
        mb.get('Nothing')
    ) else mb.get('Just')


# DISPLAY -------------------------------------------------

# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
                     f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

