# Text processing/1

## Task Link
[Rosetta Code - Text processing/1](https://rosettacode.org/wiki/Text_processing/1)

## Java Code
### java_code_1.txt
```java
import java.io.File;
import java.util.*;
import static java.lang.System.out;

public class TextProcessing1 {

    public static void main(String[] args) throws Exception {
        Locale.setDefault(new Locale("en", "US"));
        Metrics metrics = new Metrics();

        int dataGap = 0;
        String gapBeginDate = null;
        try (Scanner lines = new Scanner(new File("readings.txt"))) {
            while (lines.hasNextLine()) {

                double lineTotal = 0.0;
                int linePairs = 0;
                int lineInvalid = 0;
                String lineDate;

                try (Scanner line = new Scanner(lines.nextLine())) {

                    lineDate = line.next();

                    while (line.hasNext()) {
                        final double value = line.nextDouble();
                        if (line.nextInt() <= 0) {
                            if (dataGap == 0)
                                gapBeginDate = lineDate;
                            dataGap++;
                            lineInvalid++;
                            continue;
                        }
                        lineTotal += value;
                        linePairs++;

                        metrics.addDataGap(dataGap, gapBeginDate, lineDate);
                        dataGap = 0;
                    }
                }
                metrics.addLine(lineTotal, linePairs);
                metrics.lineResult(lineDate, lineInvalid, linePairs, lineTotal);
            }
            metrics.report();
        }
    }

    private static class Metrics {
        private List<String[]> gapDates;
        private int maxDataGap = -1;
        private double total;
        private int pairs;
        private int lineResultCount;

        void addLine(double tot, double prs) {
            total += tot;
            pairs += prs;
        }

        void addDataGap(int gap, String begin, String end) {
            if (gap > 0 && gap >= maxDataGap) {
                if (gap > maxDataGap) {
                    maxDataGap = gap;
                    gapDates = new ArrayList<>();
                }
                gapDates.add(new String[]{begin, end});
            }
        }

        void lineResult(String date, int invalid, int prs, double tot) {
            if (lineResultCount >= 3)
                return;
            out.printf("%10s  out: %2d  in: %2d  tot: %10.3f  avg: %10.3f%n",
                    date, invalid, prs, tot, (prs > 0) ? tot / prs : 0.0);
            lineResultCount++;
        }

        void report() {
            out.printf("%ntotal    = %10.3f%n", total);
            out.printf("readings = %6d%n", pairs);
            out.printf("average  = %010.3f%n", total / pairs);
            out.printf("%nmaximum run(s) of %d invalid measurements: %n",
                    maxDataGap);
            for (String[] dates : gapDates)
                out.printf("begins at %s and ends at %s%n", dates[0], dates[1]);

        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import fileinput
import sys

nodata = 0;             # Current run of consecutive flags<0 in lines of file
nodata_max=-1;          # Max consecutive flags<0 in lines of file
nodata_maxline=[];      # ... and line number(s) where it occurs

tot_file = 0            # Sum of file data
num_file = 0            # Number of file data items with flag>0

infiles = sys.argv[1:]

for line in fileinput.input():
  tot_line=0;             # sum of line data
  num_line=0;             # number of line data items with flag>0

  # extract field info
  field = line.split()
  date  = field[0]
  data  = [float(f) for f in field[1::2]]
  flags = [int(f)   for f in field[2::2]]

  for datum, flag in zip(data, flags):
    if flag<1:
      nodata += 1
    else:
      # check run of data-absent fields
      if nodata_max==nodata and nodata>0:
        nodata_maxline.append(date)
      if nodata_max<nodata and nodata>0:
        nodata_max=nodata
        nodata_maxline=[date]
      # re-initialise run of nodata counter
      nodata=0; 
      # gather values for averaging
      tot_line += datum
      num_line += 1

  # totals for the file so far
  tot_file += tot_line
  num_file += num_line

  print "Line: %11s  Reject: %2i  Accept: %2i  Line_tot: %10.3f  Line_avg: %10.3f" % (
        date, 
        len(data) -num_line, 
        num_line, tot_line, 
        tot_line/num_line if (num_line>0) else 0)

print ""
print "File(s)  = %s" % (", ".join(infiles),)
print "Total    = %10.3f" % (tot_file,)
print "Readings = %6i" % (num_file,)
print "Average  = %10.3f" % (tot_file / num_file,)

print "\nMaximum run(s) of %i consecutive false readings ends at line starting with date(s): %s" % (
    nodata_max, ", ".join(nodata_maxline))

```

