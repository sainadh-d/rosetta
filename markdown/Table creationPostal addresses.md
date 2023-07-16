# Table creation/Postal addresses

## Task Link
[Rosetta Code - Table creation/Postal addresses](https://rosettacode.org/wiki/Table_creation/Postal_addresses)

## Java Code
## Python Code
### python_code_1.txt
```python
>>> import sqlite3
>>> conn = sqlite3.connect(':memory:')
>>> conn.execute('''CREATE TABLE address (
	addrID		INTEGER PRIMARY KEY AUTOINCREMENT,
	addrStreet	TEXT NOT NULL,
	addrCity	TEXT NOT NULL,
	addrState	TEXT NOT NULL,
	addrZIP		TEXT NOT NULL
    )''')
<sqlite3.Cursor object at 0x013265C0>
>>>

```

