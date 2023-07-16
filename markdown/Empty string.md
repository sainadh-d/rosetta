# Empty string

## Task Link
[Rosetta Code - Empty string](https://rosettacode.org/wiki/Empty_string)

## Java Code
### java_code_1.txt
```java
String s = "";
if(s != null && s.isEmpty()){//optionally, instead of "s.isEmpty()": "s.length() == 0" or "s.equals("")"
   System.out.println("s is empty");
}else{
   System.out.println("s is not empty");
}

```

## Python Code
### python_code_1.txt
```python
s = ''
# or:
s = str()

if not s or s == '':
   print("String is empty")

if len(s) == 0:
    print("String is empty")
else:
    print("String not empty")


# boolean test function for python2 and python3
# test for regular (non-unicode) strings
# unicode strings
# None 
def emptystring(s):
   if isinstance(s, (''.__class__ , u''.__class__) ):
      if len(s) == 0: 
         return True
      else 
         return False

   elif s is None:
        return True

```

