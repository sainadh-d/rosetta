# Create an HTML table

## Task Link
[Rosetta Code - Create an HTML table](https://rosettacode.org/wiki/Create_an_HTML_table)

## Java Code
### java_code_1.txt
```java
import java.util.Random;

```

### java_code_2.txt
```java
String generateHTMLTable() {
    StringBuilder string = new StringBuilder();
    string.append("<table border=\"1\">");
    string.append(System.lineSeparator());
    string.append("<tr>".indent(2));
    string.append("<th width=\"40\"></th>".indent(4));
    string.append("<th width=\"50\">X</th>".indent(4));
    string.append("<th width=\"50\">Y</th>".indent(4));
    string.append("<th width=\"50\">Z</th>".indent(4));
    string.append("</tr>".indent(2));
    Random random = new Random();
    int number;
    for (int countA = 0; countA < 10; countA++) {
        string.append("<tr>".indent(2));
        string.append("<td>%d</td>".formatted(countA).indent(4));
        for (int countB = 0; countB < 3; countB++) {
            number = random.nextInt(1, 9999);
            string.append("<td>%,d</td>".formatted(number).indent(4));
        }
        string.append("</tr>".indent(2));
    }
    string.append("</table>");
    return string.toString();
}

```

### java_code_3.txt
```java
public class HTML {

	public static String array2HTML(Object[][] array){
		StringBuilder html = new StringBuilder(
				"<table>");
		for(Object elem:array[0]){
			html.append("<th>" + elem.toString() + "</th>");
		}
		for(int i = 1; i < array.length; i++){
			Object[] row = array[i];
			html.append("<tr>");
			for(Object elem:row){
				html.append("<td>" + elem.toString() + "</td>");
			}
			html.append("</tr>");
		}
		html.append("</table>");
		return html.toString();
	}
	
	public static void main(String[] args){
		Object[][] ints = {{"","X","Y","Z"},{1,1,2,3},{2,4,5,6},{3,7,8,9},{4,10,11,12}};
		System.out.println(array2HTML(ints));
	}
}

```

## Python Code
### python_code_1.txt
```python
import random

def rand9999():
    return random.randint(1000, 9999)

def tag(attr='', **kwargs):
    for tag, txt in kwargs.items():
        return '<{tag}{attr}>{txt}</{tag}>'.format(**locals())

if __name__ == '__main__':
    header = tag(tr=''.join(tag(th=txt) for txt in ',X,Y,Z'.split(','))) + '\n'
    rows = '\n'.join(tag(tr=tag(' style="font-weight: bold;"', td=i)
                                    + ''.join(tag(td=rand9999())
                                              for j in range(3)))
                     for i in range(1, 6))
    table = tag(table='\n' + header + rows + '\n')
    print(table)

```

### python_code_2.txt
```python
from functools import (reduce)
import itertools
import random


# HTML RENDERING ----------------------------------------

# treeHTML :: tree
#      {tag :: String, text :: String, kvs :: Dict}
#      -> HTML String
def treeHTML(tree):
    return foldTree(
        lambda x: lambda xs: (
            f"<{x['tag'] + attribString(x)}>" + (
                str(x['text']) if 'text' in x else '\n'
            ) + ''.join(xs) + f"</{x['tag']}>\n"
        )
    )(tree)


# attribString :: Dict -> String
def attribString(dct):
    kvs = dct['kvs'] if 'kvs' in dct else None
    return ' ' + reduce(
        lambda a, k: a + k + '="' + kvs[k] + '" ',
        kvs.keys(), ''
    ).strip() if kvs else ''


# HTML TABLE FROM GENERATED DATA ------------------------


def main():
    # Number of columns and rows to generate.
    n = 3

    # Table details -------------------------------------
    strCaption = 'Table generated with Python'
    colNames = take(n)(enumFrom('A'))
    dataRows = map(
        lambda x: (x, map(
            lambda _: random.randint(100, 9999),
            colNames
        )), take(n)(enumFrom(1)))
    tableStyle = {
        'style': "width:25%; border:2px solid silver;"
    }
    trStyle = {
        'style': "border:1px solid silver;text-align:right;"
    }

    # TREE STRUCTURE OF TABLE ---------------------------
    tableTree = Node({'tag': 'table', 'kvs': tableStyle})([
        Node({
            'tag': 'caption',
            'text': strCaption
        })([]),

        # HEADER ROW --------------------------------
        (Node({'tag': 'tr'})(
            Node({
                'tag': 'th',
                'kvs': {'style': 'text-align:right;'},
                'text': k
            })([]) for k in ([''] + colNames)
        ))
    ] +
        # DATA ROWS ---------------------------------
        list(Node({'tag': 'tr', 'kvs': trStyle})(
            [Node({'tag': 'th', 'text': tpl[0]})([])] +
            list(Node(
                {'tag': 'td', 'text': str(v)})([]) for v in tpl[1]
            )
        ) for tpl in dataRows)
    )

    print(
        treeHTML(tableTree)
        # dataRows
    )


# GENERIC -----------------------------------------------

# Node :: a -> [Tree a] -> Tree a
def Node(v):
    return lambda xs: {'type': 'Node', 'root': v, 'nest': xs}


# enumFrom :: Enum a => a -> [a]
def enumFrom(x):
    return itertools.count(x) if type(x) is int else (
        map(chr, itertools.count(ord(x)))
    )


# foldTree :: (a -> [b] -> b) -> Tree a -> b
def foldTree(f):
    def go(node):
        return f(node['root'])(
            list(map(go, node['nest']))
        )
    return lambda tree: go(tree)


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(itertools.islice(xs, n))
    )


if __name__ == '__main__':
    main()

```

