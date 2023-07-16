# Find common directory path

## Task Link
[Rosetta Code - Find common directory path](https://rosettacode.org/wiki/Find_common_directory_path)

## Java Code
### java_code_1.txt
```java
public class CommonPath {
	public static String commonPath(String... paths){
		String commonPath = "";
		String[][] folders = new String[paths.length][];
		for(int i = 0; i < paths.length; i++){
			folders[i] = paths[i].split("/"); //split on file separator
		}
		for(int j = 0; j < folders[0].length; j++){
			String thisFolder = folders[0][j]; //grab the next folder name in the first path
			boolean allMatched = true; //assume all have matched in case there are no more paths
			for(int i = 1; i < folders.length && allMatched; i++){ //look at the other paths
				if(folders[i].length < j){ //if there is no folder here
					allMatched = false; //no match
					break; //stop looking because we've gone as far as we can
				}
				//otherwise
				allMatched &= folders[i][j].equals(thisFolder); //check if it matched
			}
			if(allMatched){ //if they all matched this folder name
				commonPath += thisFolder + "/"; //add it to the answer
			}else{//otherwise
				break;//stop looking
			}
		}
		return commonPath;
	}
	
	public static void main(String[] args){
		String[] paths = { "/home/user1/tmp/coverage/test",
				 "/home/user1/tmp/covert/operator",
				 "/home/user1/tmp/coven/members"};
		System.out.println(commonPath(paths));
		
		String[] paths2 = { "/hame/user1/tmp/coverage/test",
				 "/home/user1/tmp/covert/operator",
				 "/home/user1/tmp/coven/members"};
		System.out.println(commonPath(paths2));
	}
}

```

### java_code_2.txt
```java
	static String commonPath(String...  paths){
		String commonPath = "";
		String[][] folders = new String[paths.length][];
		
		for(int i=0; i<paths.length; i++){
			folders[i] = paths[i].split("/");
		}
			
		for(int j = 0; j< folders[0].length; j++){
			String s = folders[0][j];
			for(int i=1; i<paths.length; i++){
				if(!s.equals(folders[i][j]))
					return commonPath;
			}
			commonPath += s + "/";
		}
		return commonPath;		
	}

```

## Python Code
### python_code_1.txt
```python
>>> import os
>>> os.path.commonpath(['/home/user1/tmp/coverage/test', 
                        '/home/user1/tmp/covert/operator', '/home/user1/tmp/coven/members'])
'/home/user1/tmp'

```

### python_code_2.txt
```python
>>> import os
>>> os.path.commonprefix(['/home/user1/tmp/coverage/test', 
                          '/home/user1/tmp/covert/operator', '/home/user1/tmp/coven/members'])
'/home/user1/tmp/cove'

```

### python_code_3.txt
```python
>>> def commonprefix(args, sep='/'):
	return os.path.commonprefix(args).rpartition(sep)[0]

>>> commonprefix(['/home/user1/tmp/coverage/test', 
                  '/home/user1/tmp/covert/operator', '/home/user1/tmp/coven/members'])
'/home/user1/tmp'

```

### python_code_4.txt
```python
>>> paths = ['/home/user1/tmp/coverage/test', '/home/user1/tmp/covert/operator', '/home/user1/tmp/coven/members']
>>> os.path.dirname(os.path.commonprefix(paths))
'/home/user1/tmp'

```

### python_code_5.txt
```python
>>> from itertools import takewhile
>>> def allnamesequal(name):
	return all(n==name[0] for n in name[1:])

>>> def commonprefix(paths, sep='/'):
	bydirectorylevels = zip(*[p.split(sep) for p in paths])
	return sep.join(x[0] for x in takewhile(allnamesequal, bydirectorylevels))

>>> commonprefix(['/home/user1/tmp/coverage/test', 
                  '/home/user1/tmp/covert/operator', '/home/user1/tmp/coven/members'])
'/home/user1/tmp'
>>> # And also
>>> commonprefix(['/home/user1/tmp', '/home/user1/tmp/coverage/test',
                  '/home/user1/tmp/covert/operator', '/home/user1/tmp/coven/members'])
'/home/user1/tmp'
>>>

```

