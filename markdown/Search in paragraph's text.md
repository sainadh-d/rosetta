# Search in paragraph's text

## Task Link
[Rosetta Code - Search in paragraph's text](https://rosettacode.org/wiki/Search_in_paragraph%27s_text)

## Java Code
## Python Code
### python_code_1.txt
```python
with open('Traceback.txt', 'r' ) as f:
    rawText = f.read()

paragraphs = rawText.split( "\n\n" )

for p in paragraphs:
    if "SystemError" in p:

        index = p.find( "Traceback (most recent call last):" )

        if -1 != index:
            print( p[index:] )
            print( "----------------" )

```

