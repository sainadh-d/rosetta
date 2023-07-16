# Text processing/2

## Task Link
[Rosetta Code - Text processing/2](https://rosettacode.org/wiki/Text_processing/2)

## Java Code
### java_code_1.txt
```java
import java.util.*;
import java.util.regex.*;
import java.io.*;

public class DataMunging2 {

    public static final Pattern e = Pattern.compile("\\s+");

    public static void main(String[] args) {
        try {
            BufferedReader infile = new BufferedReader(new FileReader(args[0]));
            List<String> duplicates = new ArrayList<String>();
            Set<String> datestamps = new HashSet<String>(); //for the datestamps

            String eingabe;
            int all_ok = 0;//all_ok for lines in the given pattern e
            while ((eingabe = infile.readLine()) != null) { 
                String[] fields = e.split(eingabe); //we tokenize on empty fields
                if (fields.length != 49) //we expect 49 fields in a record
                    System.out.println("Format not ok!");
                if (datestamps.add(fields[0])) { //not duplicated
                    int howoften = (fields.length - 1) / 2 ; //number of measurement
                                                             //devices and values
                    for (int n = 1; Integer.parseInt(fields[2*n]) >= 1; n++) {
                        if (n == howoften) {
                            all_ok++ ;
                            break ;
                        }
                    }
                } else {
                    duplicates.add(fields[0]); //first field holds datestamp
                }
            }
            infile.close();
            System.out.println("The following " + duplicates.size() + " datestamps were duplicated:");
            for (String x : duplicates)
                System.out.println(x);
            System.out.println(all_ok + " records were complete and ok!");
        } catch (IOException e) {
            System.err.println("Can't open file " + args[0]);
            System.exit(1);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import re
import zipfile
import StringIO

def munge2(readings):

   datePat = re.compile(r'\d{4}-\d{2}-\d{2}')
   valuPat = re.compile(r'[-+]?\d+\.\d+')
   statPat = re.compile(r'-?\d+')
   allOk, totalLines = 0, 0
   datestamps = set([])
   for line in readings:
      totalLines += 1
      fields = line.split('\t')
      date = fields[0]
      pairs = [(fields[i],fields[i+1]) for i in range(1,len(fields),2)]

      lineFormatOk = datePat.match(date) and \
         all( valuPat.match(p[0]) for p in pairs ) and \
         all( statPat.match(p[1]) for p in pairs )
      if not lineFormatOk:
         print 'Bad formatting', line
         continue
		
      if len(pairs)!=24 or any( int(p[1]) < 1 for p in pairs ):
         print 'Missing values', line
         continue

      if date in datestamps:
         print 'Duplicate datestamp', line
         continue
      datestamps.add(date)
      allOk += 1

   print 'Lines with all readings: ', allOk
   print 'Total records: ', totalLines

#zfs = zipfile.ZipFile('readings.zip','r')
#readings = StringIO.StringIO(zfs.read('readings.txt'))
readings = open('readings.txt','r')
munge2(readings)

```

### python_code_2.txt
```python
import re
import zipfile
import StringIO
 
def munge2(readings, debug=False):
 
   datePat = re.compile(r'\d{4}-\d{2}-\d{2}')
   valuPat = re.compile(r'[-+]?\d+\.\d+')
   statPat = re.compile(r'-?\d+')
   totalLines = 0
   dupdate, badform, badlen, badreading = set(), set(), set(), 0
   datestamps = set([])
   for line in readings:
      totalLines += 1
      fields = line.split('\t')
      date = fields[0]
      pairs = [(fields[i],fields[i+1]) for i in range(1,len(fields),2)]
 
      lineFormatOk = datePat.match(date) and \
         all( valuPat.match(p[0]) for p in pairs ) and \
         all( statPat.match(p[1]) for p in pairs )
      if not lineFormatOk:
         if debug: print 'Bad formatting', line
         badform.add(date)
         
      if len(pairs)!=24 or any( int(p[1]) < 1 for p in pairs ):
         if debug: print 'Missing values', line
      if len(pairs)!=24: badlen.add(date)
      if any( int(p[1]) < 1 for p in pairs ): badreading += 1
 
      if date in datestamps:
         if debug: print 'Duplicate datestamp', line
         dupdate.add(date)

      datestamps.add(date)

   print 'Duplicate dates:\n ', '\n  '.join(sorted(dupdate)) 
   print 'Bad format:\n ', '\n  '.join(sorted(badform)) 
   print 'Bad number of fields:\n ', '\n  '.join(sorted(badlen)) 
   print 'Records with good readings: %i = %5.2f%%\n' % (
      totalLines-badreading, (totalLines-badreading)/float(totalLines)*100 )
   print 'Total records: ', totalLines
 
readings = open('readings.txt','r')
munge2(readings)

```

