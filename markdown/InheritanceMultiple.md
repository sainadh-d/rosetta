# Inheritance/Multiple

## Task Link
[Rosetta Code - Inheritance/Multiple](https://rosettacode.org/wiki/Inheritance/Multiple)

## Java Code
### java_code_1.txt
```java
public interface Camera{
   //functions here with no definition...
   //ex:
   //public void takePicture();
}

```

### java_code_2.txt
```java
public interface MobilePhone{
   //functions here with no definition...
   //ex:
   //public void makeCall();
}

```

### java_code_3.txt
```java
public class CameraPhone implements Camera, MobilePhone{
   //functions here...
}

```

## Python Code
### python_code_1.txt
```python
class Camera:
  pass #functions go here...

```

### python_code_2.txt
```python
class MobilePhone:
  pass #functions go here...

```

### python_code_3.txt
```python
class CameraPhone(Camera, MobilePhone):
  pass #functions go here...

```

