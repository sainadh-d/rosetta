# JSON

## Task Link
[Rosetta Code - JSON](https://rosettacode.org/wiki/JSON)

## Java Code
### java_code_1.txt
```java
//  Parse JSON
//
//  Nigel Galloway - April 27th., 2012
//
grammar JSON ;
@members {
String Indent = "";
}
Number	:	(('0')|('-'? ('1'..'9') ('0'..'9')*)) ('.' ('0'..'9')+)? (('e'|'E') ('+'|'-')? ('0'..'9')+)?;
WS	:	(' ' | '\t' | '\r' |'\n') {skip();};
Tz	:	' ' .. '!' | '#' .. '[' | ']' .. '~';
Control	:	'\\' ('"'|'\\'|'/'|'b'|'f'|'n'|'r'|'t'|UCode);
UCode	:	'u' ('0'..'9'|'a'..'f'|'A'..'F') ('0'..'9'|'a'..'f'|'A'..'F') ('0'..'9'|'a'..'f'|'A'..'F') ('0'..'9'|'a'..'f'|'A'..'F');
Keyword	:	'true' | 'false' | 'null';
String	:	'"' (Control? Tz)* '"';
object	:       '{' {System.out.println(Indent + "{Object}"); Indent += "    ";} (pair (',' pair*)*)? '}' {Indent = Indent.substring(4);};
pair	:	e = String {System.out.println(Indent + "{Property}\t" + $e.text);} ':' value;
value	:	Number             {System.out.println(Indent + "{Number}  \t" + $Number.text);}
	|	object
	|	String             {System.out.println(Indent + "{String}  \t" + $String.text);}
	|	Keyword            {System.out.println(Indent + "{Keyword} \t" + $Keyword.text);}
	|	array;
array	:	'[' {System.out.println(Indent + "Array"); Indent += "    ";} (value (',' value)*)? ']' {Indent = Indent.substring(4);};

```

### java_code_2.txt
```java
import com.google.gson.Gson;

public class JsonExample {

	public static void main(String[] args) {
		Gson gson = new Gson();
		String json = "{ \"foo\": 1, \"bar\": [ \"10\", \"apples\"] }";
		
		MyJsonObject obj = gson.fromJson(json, MyJsonObject.class);
		
		System.out.println(obj.getFoo());

		for(String bar : obj.getBar()) {
			System.out.println(bar);
		}
		
		obj = new MyJsonObject(2, new String[] { "20", "oranges" });
		json = gson.toJson(obj);
		
		System.out.println(json);
	}
	
}

class MyJsonObject {
	
	private int foo;
	private String[] bar;
	
	public MyJsonObject(int foo, String[] bar) {
		this.foo = foo;
		this.bar = bar;
	}
	
	public int getFoo() {
		return foo;
	}
	
	public String[] getBar() {
		return bar;
	}
	
}

```

## Python Code
### python_code_1.txt
```python
>>> import json
>>> data = json.loads('{ "foo": 1, "bar": [10, "apples"] }')
>>> sample = { "blue": [1,2], "ocean": "water" }
>>> json_string = json.dumps(sample)
>>> json_string
'{"blue": [1, 2], "ocean": "water"}'
>>> sample
{'blue': [1, 2], 'ocean': 'water'}
>>> data
{'foo': 1, 'bar': [10, 'apples']}

```

### python_code_2.txt
```python
>>> true = True; false = False; null = None
>>> data = eval('{ "foo": 1, "bar": [10, "apples"] }')
>>> data
{'foo': 1, 'bar': [10, 'apples']}

```

