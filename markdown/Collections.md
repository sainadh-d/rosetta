# Collections

## Task Link
[Rosetta Code - Collections](https://rosettacode.org/wiki/Collections)

## Java Code
### java_code_1.txt
```java
List arrayList = new ArrayList();
arrayList.add(new Integer(0));
// alternative with primitive autoboxed to an Integer object automatically
arrayList.add(0); 

//other features of ArrayList
//define the type in the arraylist, you can substitute a proprietary class in the "<>"
List<Integer> myarrlist = new ArrayList<Integer>();

//add several values to the arraylist to be summed later
int sum;
for(int i = 0; i < 10; i++) {
    myarrlist.add(i);
}

```

### java_code_2.txt
```java
//loop through myarrlist to sum each entry
for ( i = 0; i < myarrlist.size(); i++) {
    sum += myarrlist.get(i);
}

```

### java_code_3.txt
```java
for(int i : myarrlist) {
    sum += i;
}

```

### java_code_4.txt
```java
//remove the last entry in the ArrayList
myarrlist.remove(myarrlist.size()-1)

//clear the ArrayList
myarrlist.clear();

```

### java_code_5.txt
```java
import scala.Tuple2;
import scala.collection.concurrent.TrieMap;
import scala.collection.immutable.HashSet;
import scala.collection.mutable.ArrayBuffer;

public class Collections {

	public static void main(String[] args) {
		ArrayBuffer<Integer> myarrlist = new ArrayBuffer<Integer>();
		ArrayBuffer<Integer> myarrlist2 = new ArrayBuffer<Integer>(20);

		myarrlist.$plus$eq(new Integer(42)); // $plus$eq is Scala += operator
		myarrlist.$plus$eq(13); // to add an element.
		myarrlist.$plus$eq(-1);

		myarrlist2 = (ArrayBuffer<Integer>) myarrlist2.$minus(-1);

		for (int i = 0; i < 10; i++)
			myarrlist2.$plus$eq(i);

		// loop through myarrlist to sum each entry
		int sum = 0;
		for (int i = 0; i < myarrlist2.size(); i++) {
			sum += myarrlist2.apply(i);
		}
		System.out.println("List is: " + myarrlist2 + " with head: "
				+ myarrlist2.head() + " sum is: " + sum);
		System.out.println("Third element is: " + myarrlist2.apply$mcII$sp(2));

		Tuple2<String, String> tuple = new Tuple2<String, String>("US",
				"Washington");
		System.out.println("Tuple2 is : " + tuple);

		ArrayBuffer<Tuple2<String, String>> capList = new ArrayBuffer<Tuple2<String, String>>();
		capList.$plus$eq(new Tuple2<String, String>("US", "Washington"));
		capList.$plus$eq(new Tuple2<String, String>("France", "Paris"));
		System.out.println(capList);

		TrieMap<String, String> trieMap = new TrieMap<String, String>();
		trieMap.put("US", "Washington");
		trieMap.put("France", "Paris");

		HashSet<Character> set = new HashSet<Character>();

		ArrayBuffer<Tuple2<String, String>> capBuffer = new ArrayBuffer<Tuple2<String, String>>();
		trieMap.put("US", "Washington");

		System.out.println(trieMap);
	}
}

```

## Python Code
### python_code_1.txt
```python
collection = [0, '1']                 # Lists are mutable (editable) and can be sorted in place
x = collection[0]                     # accessing an item (which happens to be a numeric 0 (zero)
collection.append(2)                  # adding something to the end of the list
collection.insert(0, '-1')            # inserting a value into the beginning
y = collection[0]                     # now returns a string of "-1"
collection.extend([2,'3'])            # same as [collection.append(i) for i in [2,'3']] ... but faster
collection += [2,'3']                 # same as previous line
collection[2:6]                       # a "slice" (collection of the list elements from the third up to but not including the sixth)
len(collection)                       # get the length of (number of elements in) the collection
collection = (0, 1)                   # Tuples are immutable (not editable)
collection[:]                         # ... slices work on these too; and this is equivalent to collection[0:len(collection)]
collection[-4:-1]                     # negative slices count from the end of the string
collection[::2]                       # slices can also specify a stride --- this returns all even elements of the collection
collection="some string"              # strings are treated as sequences of characters
x = collection[::-1]                  # slice with negative step returns reversed sequence (string in this case).
collection[::2] == "some string"[::2] # True, literal objects don't need to be bound to name/variable to access slices or object methods
collection.__getitem__(slice(0,len(collection),2))  # same as previous expressions.
collection = {0: "zero", 1: "one"}    # Dictionaries (Hash)
collection['zero'] = 2                # Dictionary members accessed using same syntax as list/array indexes.
collection = set([0, '1'])            # sets (Hash)

```

