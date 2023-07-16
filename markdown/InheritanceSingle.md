# Inheritance/Single

## Task Link
[Rosetta Code - Inheritance/Single](https://rosettacode.org/wiki/Inheritance/Single)

## Java Code
### java_code_1.txt
```java
public class Animal{
   //functions go here...
}

```

### java_code_2.txt
```java
public class Dog extends Animal{
   //functions go here...
}

```

### java_code_3.txt
```java
public class Cat extends Animal{
   //functions go here...
}

```

### java_code_4.txt
```java
public class Lab extends Dog{
   //functions go here...
}

```

### java_code_5.txt
```java
public class Collie extends Dog{
   //functions go here...
}

```

## Python Code
### python_code_1.txt
```python
class Animal:
  pass #functions go here...

class Dog(Animal):
  pass #functions go here...

class Cat(Animal):
  pass #functions go here...

class Lab(Dog):
  pass #functions go here...

class Collie(Dog):
  pass #functions go here...

```

### python_code_2.txt
```python
import time

class Animal(object):
    def __init__(self, birth=None, alive=True):
        self.birth = birth if birth else time.time()
        self.alive = alive
    def age(self):
        return time.time() - self.birth
    def kill(self):
        self.alive = False

class Dog(Animal):
    def __init__(self, bones_collected=0, **kwargs):
        self.bone_collected = bones_collected
        super(Dog, self).__init__(**kwargs)

class Cat(Animal):
    max_lives = 9
    def __init__(self, lives=max_lives, **kwargs):
        self.lives = lives
        super(Cat, self).__init__(**kwargs)
    def kill(self):
        if self.lives>0:
            self.lives -= 1
            if self.lives == 0:
                super(Cat, self).kill()
        else:
            raise ValueError
        return self

class Labrador(Dog):
    def __init__(self, guide_dog=False, **kwargs):
        self.guide_dog=False
        super(Labrador, self).__init__(**kwargs)

class Collie(Dog):
    def __init__(self, sheep_dog=False, **kwargs):
        self.sheep_dog=False
        super(Collie, self).__init__(**kwargs)

lassie = Collie()
felix = Cat()
felix.kill().kill().kill()
mr_winkle = Dog()
buddy = Labrador()
buddy.kill()
print "Felix has",felix.lives, "lives, ","Buddy is %salive!"%("" if buddy.alive else "not ")

```

