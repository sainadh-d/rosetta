# SHA-1

## Task Link
[Rosetta Code - SHA-1](https://rosettacode.org/wiki/SHA-1)

## Java Code
## Python Code
### python_code_1.txt
```python
import crypto { sha1 }
let hash = sha1.hexdigest('Ars longa, vita brevis')
print hash

```

### python_code_2.txt
```python
import hashlib
h = hashlib.sha1()
h.update(bytes("Ars longa, vita brevis", encoding="ASCII"))
h.hexdigest()
# "e640d285242886eb96ab80cbf858389b3df52f43"

```

