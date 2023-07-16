# Higher-order functions

## Task Link
[Rosetta Code - Higher-order functions](https://rosettacode.org/wiki/Higher-order_functions)

## Java Code
### java_code_1.txt
```java
public class NewClass {
   
   public NewClass() {
       first(new AnEventOrCallback() {
           public void call() {
               second();
           }
       });
   }
   
   public void first(AnEventOrCallback obj) {
       obj.call();
   }
   
   public void second() {
       System.out.println("Second");
   }
   
   public static void main(String[] args) {
       new NewClass();
   }
}

interface AnEventOrCallback {
   public void call();
}

```

### java_code_2.txt
```java
public class ListenerTest {
   public static void main(String[] args) {   
     JButton testButton = new JButton("Test Button");
     testButton.addActionListener(new ActionListener(){
     @Override public void actionPerformed(ActionEvent ae){
         System.out.println("Click Detected by Anon Class");
       }
     });
     
     testButton.addActionListener(e -> System.out.println("Click Detected by Lambda Listner"));
     
     // Swing stuff
     JFrame frame = new JFrame("Listener Test");
     frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
     frame.add(testButton, BorderLayout.CENTER);
     frame.pack();
     frame.setVisible(true);     
   }
}

```

## Python Code
### python_code_1.txt
```python
def first(function):
    return function()

def second():
    return "second"

result = first(second)

```

### python_code_2.txt
```python
  result = first(lambda: "second")

```

