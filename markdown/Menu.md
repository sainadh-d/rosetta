# Menu

## Task Link
[Rosetta Code - Menu](https://rosettacode.org/wiki/Menu)

## Java Code
### java_code_1.txt
```java
public static String select(List<String> list, String prompt){
    if(list.size() == 0) return "";
    Scanner sc = new Scanner(System.in);
    String ret = null;
    do{
        for(int i=0;i<list.size();i++){
            System.out.println(i + ": "+list.get(i));
        }
        System.out.print(prompt);
        int index = sc.nextInt();
        if(index >= 0 && index < list.size()){
            ret = list.get(index);
        }
    }while(ret == null);
    return ret;
}

```

## Python Code
### python_code_1.txt
```python
def _menu(items):
    for indexitem in enumerate(items):
        print ("  %2i) %s" % indexitem)

def _ok(reply, itemcount):
    try:
        n = int(reply)
        return 0 <= n < itemcount
    except:
        return False
    
def selector(items, prompt):
    'Prompt to select an item from the items'
    if not items: return ''
    reply = -1
    itemcount = len(items)
    while not _ok(reply, itemcount):
        _menu(items)
        # Use input instead of raw_input for Python 3.x
        reply = raw_input(prompt).strip()
    return items[int(reply)]

if __name__ == '__main__':
    items = ['fee fie', 'huff and puff', 'mirror mirror', 'tick tock']
    item = selector(items, 'Which is from the three pigs: ')
    print ("You chose: " + item)

```

