# HTTPS/Client-authenticated

## Task Link
[Rosetta Code - HTTPS/Client-authenticated](https://rosettacode.org/wiki/HTTPS/Client-authenticated)

## Java Code
## Python Code
### python_code_1.txt
```python
import httplib

connection = httplib.HTTPSConnection('www.example.com',cert_file='myCert.PEM')
connection.request('GET','/index.html')
response = connection.getresponse()
data = response.read()

```

