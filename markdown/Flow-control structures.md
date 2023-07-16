# Flow-control structures

## Task Link
[Rosetta Code - Flow-control structures](https://rosettacode.org/wiki/Flow-control_structures)

## Java Code
### java_code_1.txt
```java
switch (xx) {
  case 1:
  case 2:
    /* 1 & 2 both come here... */
    ...
    break;
  case 4:
    /* 4 comes here... */
    ...
    break;
  case 5:
    /* 5 comes here... */
    ...
    break;
  default:
    /* everything else */
    break;
}

for (int i = 0; i < 10; ++i) {
  ...
  if (some_condition) { break; }
  ...
}

_Time_: do {
  for (int i = 0; i < 10; ++i) {
    ...
    if (some_condition) { break _Time_; /* terminate the do-while loop */}
    ...
    }
  ...
} while (thisCondition);

```

### java_code_2.txt
```java
while (condition) {
  ...
  if (someCondition) { continue; /* skip to beginning of this loop */ }
  ...
}

top: for (int 1 = 0; i < 10; ++i) {
  ...
  middle: for (int j = 0; j < 10; ++j) {
    ...
    bottom: for (int k = 0; k < 10; ++k) {
    ...
    if (top_condition) { continue top; /* restart outer loop */ }
    ...
    if (middle_condition) { continue middle; /* restart middle loop */ }
    ...
    if (bottom_condition) { continue bottom; /* restart bottom loop */ }
    ...
    if (bottom_condition) { continue; /* this will also restart bottom loop */ }
    ...
    }
    ... 
  }
  ....
}

```

## Python Code
### python_code_1.txt
```python
# Search for an odd factor of a using brute force:
for i in range(n):
    if (n%2) == 0:
        continue
    if (n%i) == 0:
        result = i
        break
else:
    result = None
    print "No odd factors found"

```

### python_code_10.txt
```python
# Let's call our custom error "StupidError"; it inherits from the Exception class

class StupidError(Exception): pass
        
# Try it out.
try:
    raise StupidError("Segfault") # here, we manually 'raise' the error within the try block
except StupidError, details: # 'details' is the StupidError object we create in the try block.
    print 'Something stupid occurred:', details # so we access the value we had stored for it...
        

# Output :
# Something stupid occurred: Segfault

```

### python_code_11.txt
```python
    i = 101
    for i in range(4): # loop 4 times
        print "I will always be seen."
        if i % 2 == 0:
            continue # continue goes back to the loop beginning for a new iteration.
        print "I'll only be seen every other time."
    else:
        print "Loop done"
    
    # Output:
    # I will always be seen.
    # I will always be seen.
    # I'll only be seen every other time.
    # I will always be seen.
    # I will always be seen.
    # I'll only be seen every other time.
    # Loop done
        
if(__name__ == "__main__"):
    main()

```

### python_code_12.txt
```python
class Quitting(Exception): pass
max = 10 
with open("some_file") as myfile:
    exit_counter = 0
    for line in myfile:
        exit_counter += 1
        if exit_counter > max:
            raise Quitting 
        print line,

```

### python_code_2.txt
```python
class MyException(Exception): pass

```

### python_code_3.txt
```python
class MyVirtual(object):
    def __init__(self):
        raise NotImplementedError

```

### python_code_4.txt
```python
try:
    temp = 0/0
# 'except' catches any errors that may have been raised between the code of 'try' and 'except'
except:   # Note: catch all handler ... NOT RECOMMENDED
    print "An error occurred."
# Output : "An error occurred"

```

### python_code_5.txt
```python
try:
    temp = 0/0
# here, 'except' catches a specific type of error raised within the try block.
except ZeroDivisionError:
    print "You've divided by zero!"
# Output : "You've divided by zero!"

```

### python_code_6.txt
```python
try:
    temp = 0/0
except:
    print "An error occurred."
# here, 'finally' executes when the try - except block ends, regardless of whether an error was raised or not    
# useful in areas such as closing opened file streams in the try block whether they were successfully opened or not
finally:
    print "End of 'try' block..."
# Output :
# An error occurred
# End of 'try' block...

```

### python_code_7.txt
```python
try:
    try:
        pass
    except (MyException1, MyOtherException):
        pass
    except SomeOtherException:
finally:
    do_some_cleanup() # run in any case, whether any exceptions were thrown or not

```

### python_code_8.txt
```python
try:
    temp = 1/1 # not a division by zero error
except ZeroDivisionError: # so... it is not caught
    print "You've divided by zero."
# here, 'else' executes when no exceptions are caught...
else:
    print "No apparent error occurred."
# Output :
# No apparent error occurred.

```

### python_code_9.txt
```python
i = 0
while 1: # infinite loop
    try:
       temp2 = 0/i # will raise a ZeroDivisionError first.
       temp = math.sqrt(i)
       
       break # 'break' will break out of the while loop
    except ValueError: #
        print "Imaginary Number! Breaking out of loop"
        break # 'break' out of while loop
    except ZeroDivisionError:
        print "You've divided by zero. Decrementing i and continuing..."
        i-=1 # we decrement i.
        # we 'continue', everything within the try - except block will be executed again, 
        # this time however, ZeroDivisionError would not be raised again.
        continue # Note that removing it, replacing it with 'pass' would perform the equivalent
                 # see below for a better example
# Output :
# You've divided by zero. Decrementing i and continuing...
# Imaginary Number! Breaking out of loop

```

