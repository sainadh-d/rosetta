# Doubly-linked list/Element insertion

## Task Link
[Rosetta Code - Doubly-linked list/Element insertion](https://rosettacode.org/wiki/Doubly-linked_list/Element_insertion)

## Java Code
### java_code_1.txt
```java
import java.util.LinkedList;

@SuppressWarnings("serial")
public class DoublyLinkedListInsertion<T> extends LinkedList<T> {
   
    public static void main(String[] args) {
        DoublyLinkedListInsertion<String> list = new DoublyLinkedListInsertion<String>();
        list.addFirst("Add First 1");
        list.addFirst("Add First 2");
        list.addFirst("Add First 3");
        list.addFirst("Add First 4");
        list.addFirst("Add First 5");
        traverseList(list);
        
        list.addAfter("Add First 3", "Add New");
        traverseList(list);
    }
    
    /*
     * Add after indicated node.  If not in the list, added as the last node.
     */
    public void addAfter(T after, T element) {
        int index = indexOf(after);
        if ( index >= 0 ) {
            add(index + 1, element);
        }
        else {
            addLast(element);
        }
    }
    
    private static void traverseList(LinkedList<String> list) {
        System.out.println("Traverse List:");
        for ( int i = 0 ; i < list.size() ; i++ ) {
            System.out.printf("Element number %d - Element value = '%s'%n", i, list.get(i));
        }
        System.out.println();
    }
    
}

```

## Python Code
### python_code_1.txt
```python
def insert(anchor, new):
    new.next = anchor.next
    new.prev = anchor
    anchor.next.prev = new
    anchor.next = new

```

