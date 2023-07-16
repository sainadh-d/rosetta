# Simulate input/Keyboard

## Task Link
[Rosetta Code - Simulate input/Keyboard](https://rosettacode.org/wiki/Simulate_input/Keyboard)

## Java Code
### java_code_1.txt
```java
import java.awt.Robot
public static void type(String str){
   Robot robot = new Robot();
   for(char ch:str.toCharArray()){
      if(Character.isUpperCase(ch)){
         robot.keyPress(KeyEvent.VK_SHIFT);
         robot.keyPress((int)ch);
         robot.keyRelease((int)ch);
         robot.keyRelease(KeyEvent.VK_SHIFT);
      }else{
         char upCh = Character.toUpperCase(ch);
         robot.keyPress((int)upCh);
         robot.keyRelease((int)upCh);
      }
   }
}

```

## Python Code
### python_code_1.txt
```python
import autopy
autopy.key.type_string("Hello, world!") # Prints out "Hello, world!" as quickly as OS will allow.
autopy.key.type_string("Hello, world!", wpm=60) # Prints out "Hello, world!" at 60 WPM.
autopy.key.tap(autopy.key.Code.RETURN)
autopy.key.tap(autopy.key.Code.F1)
autopy.key.tap(autopy.key.Code.LEFT_ARROW)

```

### python_code_2.txt
```python
>>> import pyautogui
>>> pyautogui.typewrite('Hello world!')                 # prints out "Hello world!" instantly
>>> pyautogui.typewrite('Hello world!', interval=0.25)  # prints out "Hello world!" with a quarter second delay after each character
>>> pyautogui.press('enter')  # press the Enter key
>>> pyautogui.press('f1')     # press the F1 key
>>> pyautogui.press('left')   # press the left arrow key
>>> pyautogui.keyDown('shift')  # hold down the shift key
>>> pyautogui.press('left')     # press the left arrow key
>>> pyautogui.keyUp('shift')    # release the shift key
>>> pyautogui.hotkey('ctrl', 'shift', 'esc')

```

