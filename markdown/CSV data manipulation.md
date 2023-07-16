# CSV data manipulation

## Task Link
[Rosetta Code - CSV data manipulation](https://rosettacode.org/wiki/CSV_data_manipulation)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

```

### java_code_2.txt
```java
public class CSV {
    public static void main(String[] args) throws IOException {
        CSV csv = new CSV("data.csv");
        csv.sumAllRows();
        csv.write();
    }

    private final File file;
    private List<List<String>> data;

    public CSV(File file) throws IOException {
        this.file = file;
        open();
    }

    /* convenience constructor */
    public CSV(String path) throws IOException {
        this(new File(path));
    }

    public void sumAllRows() {
        appendColumn("SUM");
        int sum;
        int length;
        for (int index = 1; index < data.size(); index++) {
            sum = sum(data.get(index));
            length = data.get(index).size();
            data.get(index).set(length - 1, String.valueOf(sum));
        }
    }

    private int sum(List<String> row) {
        int sum = 0;
        for (int index = 0; index < row.size() - 1; index++)
            sum += Integer.parseInt(row.get(index));
        return sum;
    }

    private void appendColumn(String title) {
        List<String> titles = data.get(0);
        titles.add(title);
        /* append an empty cell to each row */
        for (int index = 1; index < data.size(); index++)
            data.get(index).add("");
    }

    private void open() throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            data = new ArrayList<>();
            String line;
            while ((line = reader.readLine()) != null) {
                /* using a limit of -1 will preserve trailing commas */
                data.add(new ArrayList<>(List.of(line.split(",", -1))));
            }
        }
    }

    public void write() throws IOException {
        try (FileWriter writer = new FileWriter(file)) {
            String newline = System.lineSeparator();
            for (List<String> row : data) {
                writer.write(String.join(",", row));
                writer.write(newline);
            }
            writer.flush();
        }
    }
}

```

### java_code_3.txt
```java
import java.io.*;
import java.awt.Point;
import java.util.HashMap;
import java.util.Scanner;

public class CSV {

    private HashMap<Point, String> _map = new HashMap<Point, String>();
    private int _cols;
    private int _rows;

    public void open(File file) throws FileNotFoundException, IOException {
        open(file, ',');
    }

    public void open(File file, char delimiter)
            throws FileNotFoundException, IOException {
        Scanner scanner = new Scanner(file);
        scanner.useDelimiter(Character.toString(delimiter));

        clear();

        while(scanner.hasNextLine()) {
            String[] values = scanner.nextLine().split(Character.toString(delimiter));

            int col = 0;
            for ( String value: values ) {
                _map.put(new Point(col, _rows), value);
                _cols = Math.max(_cols, ++col);
            }
            _rows++;
        }
        scanner.close();
    }

    public void save(File file) throws IOException {
        save(file, ',');
    }

    public void save(File file, char delimiter) throws IOException {
        FileWriter fw = new FileWriter(file);
        BufferedWriter bw = new BufferedWriter(fw);

        for (int row = 0; row < _rows; row++) {
            for (int col = 0; col < _cols; col++) {
                Point key = new Point(col, row);
                if (_map.containsKey(key)) {
                    bw.write(_map.get(key));
                }

                if ((col + 1) < _cols) {
                    bw.write(delimiter);
                }
            }
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }

    public String get(int col, int row) {
        String val = "";
        Point key = new Point(col, row);
        if (_map.containsKey(key)) {
            val = _map.get(key);
        }
        return val;
    }

    public void put(int col, int row, String value) {
        _map.put(new Point(col, row), value);
        _cols = Math.max(_cols, col+1);
        _rows = Math.max(_rows, row+1);
    }

    public void clear() {
        _map.clear();
        _cols = 0;
        _rows = 0;
    }

    public int rows() {
        return _rows;
    }

    public int cols() {
        return _cols;
    }

    public static void main(String[] args) {
        try {
            CSV csv = new CSV();

            csv.open(new File("test_in.csv"));
            csv.put(0, 0, "Column0");
            csv.put(1, 1, "100");
            csv.put(2, 2, "200");
            csv.put(3, 3, "300");
            csv.put(4, 4, "400");
            csv.save(new File("test_out.csv"));
        } catch (Exception e) {
        }
    }
}

```

### java_code_4.txt
```java
import java.io.*;
import java.util.*;

import org.apache.commons.csv.*;

public class RCsv {
  private static final String NL = System.getProperty("line.separator");
  private static final String FILENAME_IR = "data/csvtest_in.csv";
  private static final String FILENAME_OR = "data/csvtest_sum.csv";
  private static final String COL_NAME_SUM = "SUM, \"integers\""; // demonstrate white space, comma & quote handling

  public static void main(String[] args) {
    Reader iCvs = null;
    Writer oCvs = null;
    System.out.println(textFileContentsToString(FILENAME_IR));
    try {
      iCvs = new BufferedReader(new FileReader(FILENAME_IR));
      oCvs = new BufferedWriter(new FileWriter(FILENAME_OR));
      processCsv(iCvs, oCvs);
    }
    catch (IOException ex) {
      ex.printStackTrace();
    }
    finally {
      try {
        if (iCvs != null) { iCvs.close(); }
        if (oCvs != null) { oCvs.close(); }
      }
      catch (IOException ex) {
        ex.printStackTrace();
      }
    }
    System.out.println(textFileContentsToString(FILENAME_OR));
    return;
  }

  public static void processCsv(Reader iCvs, Writer oCvs) throws IOException {
    CSVPrinter printer = null;
    try {
      printer = new CSVPrinter(oCvs, CSVFormat.DEFAULT.withRecordSeparator(NL));
      List<String> oCvsHeaders;
      List<String> oCvsRecord;
      CSVParser records = CSVFormat.DEFAULT.withHeader().parse(iCvs);
      Map<String, Integer> irHeader = records.getHeaderMap();
      oCvsHeaders = new ArrayList<String>(Arrays.asList((irHeader.keySet()).toArray(new String[0])));
      oCvsHeaders.add(COL_NAME_SUM);
      printer.printRecord(oCvsHeaders);
      for (CSVRecord record : records) {
        oCvsRecord = record2list(record, oCvsHeaders);
        printer.printRecord(oCvsRecord);
      }
    }
    finally {
      if (printer != null) {
        printer.close();
      }
    }
    return;
  }

  private static List<String> record2list(CSVRecord record, List<String> oCvsHeaders) {
    List<String> cvsRecord;
    Map<String, String> rMap = record.toMap();
    long recNo = record.getRecordNumber();
    rMap = alterRecord(rMap, recNo);
    int sum = 0;
    sum = summation(rMap);
    rMap.put(COL_NAME_SUM, String.valueOf(sum));
    cvsRecord = new ArrayList<String>();
    for (String key : oCvsHeaders) {
      cvsRecord.add(rMap.get(key));
    }
    return cvsRecord;
  }

  private static Map<String, String> alterRecord(Map<String, String> rMap, long recNo) {
    int rv;
    Random rg = new Random(recNo);
    rv = rg.nextInt(50);
    String[] ks = rMap.keySet().toArray(new String[0]);
    int ix = rg.nextInt(ks.length);
    long yv = 0;
    String ky = ks[ix];
    String xv = rMap.get(ky);
    if (xv != null && xv.length() > 0) {
      yv = Long.valueOf(xv) + rv;
      rMap.put(ks[ix], String.valueOf(yv));
    }
    return rMap;
  }

  private static int summation(Map<String, String> rMap) {
    int sum = 0;
    for (String col : rMap.keySet()) {
      String nv = rMap.get(col);
      sum += nv != null && nv.length() > 0 ? Integer.valueOf(nv) : 0;
    }
    return sum;
  }

  private static String textFileContentsToString(String filename) {
    StringBuilder lineOut = new StringBuilder();
    Scanner fs = null;
    try {
      fs = new Scanner(new File(filename));
      lineOut.append(filename);
      lineOut.append(NL);
      while (fs.hasNextLine()) {
        String line = fs.nextLine();
        lineOut.append(line);
        lineOut.append(NL);
      }
    }
    catch (FileNotFoundException ex) {
      // TODO Auto-generated catch block
      ex.printStackTrace();
    }
    finally {
      if (fs != null) {
        fs.close();
      }
    }
    return lineOut.toString();
  }
}

```

### java_code_5.txt
```java
public static void main(String[] args) throws IOException {

        // 1st, config the CSV reader with line separator
        CsvParserSettings settings = new CsvParserSettings();
        settings.getFormat().setLineSeparator("\n");

        // 2nd, config the CSV reader with row processor attaching the bean definition
        BeanListProcessor<Employee> rowProcessor = new BeanListProcessor<Employee>(Employee.class);
        settings.setRowProcessor(rowProcessor);

        // 3rd, creates a CSV parser with the configs
        CsvParser parser = new CsvParser(settings);

        // 4th, parse all rows from the CSF file into the list of beans you defined
        parser.parse(new FileReader("/examples/employees.csv"));
        List<Employee> resolvedBeans = rowProcessor.getBeans();

        // 5th, Store, Delete duplicates, Re-arrange the words in specific order
        // ......

        // 6th, Write the listed of processed employee beans out to a CSV file.
        CsvWriterSettings writerSettings = new CsvWriterSettings();

        // 6.1 Creates a BeanWriterProcessor that handles annotated fields in the Employee class.
        writerSettings.setRowWriterProcessor(new BeanWriterProcessor<Employee>(Employee.class));

        // 6.2 persistent the employee beans to a CSV file.
        CsvWriter writer = new CsvWriter(new FileWriter("/examples/processed_employees.csv"), writerSettings);
        writer.processRecords(resolvedBeans);
        writer.writeRows(new ArrayList<List<Object>>());
    }

```

## Python Code
### python_code_1.txt
```python
import fileinput

changerow, changecolumn, changevalue = 2, 4, '"Spam"'

with fileinput.input('csv_data_manipulation.csv', inplace=True) as f:
    for line in f:
        if fileinput.filelineno() == changerow:
            fields = line.rstrip().split(',')
            fields[changecolumn-1] = changevalue
            line = ','.join(fields) + '\n'
        print(line, end='')

```

### python_code_2.txt
```python
import csv
from pathlib import Path
from tempfile import NamedTemporaryFile

filepath = Path('data.csv')
temp_file = NamedTemporaryFile('w',
                               newline='',
                               delete=False)

with filepath.open() as csv_file, temp_file:
    reader = csv.reader(csv_file)
    writer = csv.writer(temp_file)

    header = next(reader)
    writer.writerow(header + ['SUM'])

    for row in reader:
        row_sum = sum(map(int, row))
        writer.writerow(row + [row_sum])

temp_file_path = Path(temp_file.name)
temp_file_path.replace(filepath)

```

### python_code_3.txt
```python
import pandas as pd

filepath = 'data.csv'

df = pd.read_csv(filepath)
rows_sums = df.sum(axis=1)
df['SUM'] = rows_sums
df.to_csv(filepath, index=False)

```

