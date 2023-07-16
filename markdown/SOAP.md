# SOAP

## Task Link
[Rosetta Code - SOAP](https://rosettacode.org/wiki/SOAP)

## Java Code
## Python Code
### python_code_1.txt
```python
from SOAPpy import WSDL 
proxy = WSDL.Proxy("http://example.com/soap/wsdl")
result = proxy.soapFunc("hello")
result = proxy.anotherSoapFunc(34234)

```

