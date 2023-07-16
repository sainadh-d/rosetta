# Execute a system command

## Task Link
[Rosetta Code - Execute a system command](https://rosettacode.org/wiki/Execute_a_system_command)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;
import java.io.*;

public class Program {
    public static void main(String[] args) {    	
    	try {
    		Process p = Runtime.getRuntime().exec("cmd /C dir");//Windows command, use "ls -oa" for UNIX
    		Scanner sc = new Scanner(p.getInputStream());    		
    		while (sc.hasNext()) System.out.println(sc.nextLine());
    	}
    	catch (IOException e) {
    		System.out.println(e.getMessage());
    	}
    }
}

```

### java_code_2.txt
```java
import java.io.IOException;
import java.io.InputStream;

public class MainEntry {
    public static void main(String[] args) {
        executeCmd("ls -oa");
    }

    private static void executeCmd(String string) {
        InputStream pipedOut = null;
        try {
            Process aProcess = Runtime.getRuntime().exec(string);
            aProcess.waitFor();

            pipedOut = aProcess.getInputStream();
            byte buffer[] = new byte[2048];
            int read = pipedOut.read(buffer);
            // Replace following code with your intends processing tools
            while(read >= 0) {
                System.out.write(buffer, 0, read);
                
                read = pipedOut.read(buffer);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException ie) {
            ie.printStackTrace();
        } finally {
            if(pipedOut != null) {
                try {
                    pipedOut.close();
                } catch (IOException e) {
                }
            }
        }
    }
    
    
}

```

### java_code_3.txt
```java
import java.io.IOException;
import java.io.InputStream;

public class MainEntry {
    public static void main(String[] args) {
        // the command to execute
        executeCmd("ls -oa");
    }

    private static void executeCmd(String string) {
        InputStream pipedOut = null;
        try {
            Process aProcess = Runtime.getRuntime().exec(string);

            // These two thread shall stop by themself when the process end
            Thread pipeThread = new Thread(new StreamGobber(aProcess.getInputStream()));
            Thread errorThread = new Thread(new StreamGobber(aProcess.getErrorStream()));
            
            pipeThread.start();
            errorThread.start();
            
            aProcess.waitFor();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException ie) {
            ie.printStackTrace();
        }
    }
}

//Replace the following thread with your intends reader
class StreamGobber implements Runnable {

    private InputStream Pipe;

    public StreamGobber(InputStream pipe) {
        if(pipe == null) {
            throw new NullPointerException("bad pipe");
        }
        Pipe = pipe;
    }

    public void run() {
        try {
            byte buffer[] = new byte[2048];

            int read = Pipe.read(buffer);
            while(read >= 0) {
                System.out.write(buffer, 0, read);

                read = Pipe.read(buffer);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if(Pipe != null) {
                try {
                    Pipe.close();
                } catch (IOException e) {
                }
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import os
exit_code = os.system('ls')       # Just execute the command, return a success/fail code
output    = os.popen('ls').read() # If you want to get the output data. Deprecated.

```

### python_code_2.txt
```python
import subprocess
# if the exit code was non-zero these commands raise a CalledProcessError
exit_code = subprocess.check_call(['ls', '-l'])   # Python 2.5+
assert exit_code == 0
output    = subprocess.check_output(['ls', '-l']) # Python 2.7+

```

### python_code_3.txt
```python
from subprocess import PIPE, Popen, STDOUT
p = Popen('ls', stdout=PIPE, stderr=STDOUT)
print p.communicate()[0]

```

### python_code_4.txt
```python
import commands
stat, out = commands.getstatusoutput('ls')
if not stat:
    print out

```

