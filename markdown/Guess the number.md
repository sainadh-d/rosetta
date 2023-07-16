# Guess the number

## Task Link
[Rosetta Code - Guess the number](https://rosettacode.org/wiki/Guess_the_number)

## Java Code
### java_code_1.txt
```java
public class Guessing {
    public static void main(String[] args) throws NumberFormatException{
        int n = (int)(Math.random() * 10 + 1);
        System.out.print("Guess the number between 1 and 10: ");
        while(Integer.parseInt(System.console().readLine()) != n){
            System.out.print("Wrong! Guess again: ");
        }
        System.out.println("Well guessed!");
    }
}

```

## Python Code
### python_code_1.txt
```python
import random
t,g=random.randint(1,10),0
g=int(input("Guess a number that's between 1 and 10: "))
while t!=g:g=int(input("Guess again! "))
print("That's right!")

```

### python_code_2.txt
```python
import random #milliard.py
h1 = 0; h2 = 10**16; t = 0; f=0
c = random.randrange(0,h2) #comp
h = random.randrange(0,h2) #human DANILIN

while f<1:
    print(t,c,h)

    if h<c:
        print('MORE')
        a=h
        h=int((h+h2)/2)
        h1=a

    elif h>c:
        print('less')
        a=h
        h=int((h1+h)/2)
        h2=a

    else:
        print('win by', t, 'steps')
        f=1
    t=t+1

```

