# Text processing/Max licenses in use

## Task Link
[Rosetta Code - Text processing/Max licenses in use](https://rosettacode.org/wiki/Text_processing/Max_licenses_in_use)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;

public class License {
  public static void main(String[] args) throws FileNotFoundException, IOException{
    BufferedReader in = new BufferedReader(new FileReader(args[0]));
    int max = Integer.MIN_VALUE;
    LinkedList<String> dates = new LinkedList<String>();
    String line;
    int count = 0;
    while((line = in.readLine()) != null){
      if(line.startsWith("License OUT ")) count++;
      if(line.startsWith("License IN ")) count--;
      if(count > max){
        max = count;
        String date = line.split(" ")[3];
        dates.clear();
        dates.add(date);
      }else if(count == max){
        String date = line.split(" ")[3];
        dates.add(date);
      }
    }
    System.out.println("Max licenses out: "+max);
    System.out.println("At time(s): "+dates);
  }
}

```

## Python Code
### python_code_1.txt
```python
out, max_out, max_times = 0, -1, []
for job in open('mlijobs.txt'):
    out += 1 if "OUT" in job else -1
    if out > max_out:
        max_out, max_times = out, []
    if out == max_out:
        max_times.append(job.split()[3])
        
print("Maximum simultaneous license use is %i at the following times:" % max_out)
print('  ' + '\n  '.join(max_times))

```

