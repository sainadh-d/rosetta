# Fixed length records

## Task Link
[Rosetta Code - Fixed length records](https://rosettacode.org/wiki/Fixed_length_records)

## Java Code
## Python Code
### python_code_1.txt
```python
infile = open('infile.dat', 'rb')
outfile = open('outfile.dat', 'wb')

while True:
    onerecord = infile.read(80)
    if len(onerecord) < 80:
        break
    onerecordreversed = bytes(reversed(onerecord))
    outfile.write(onerecordreversed)

infile.close()
outfile.close()

```

