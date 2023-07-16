# Align columns

## Task Link
[Rosetta Code - Align columns](https://rosettacode.org/wiki/Align_columns)

## Java Code
### java_code_1.txt
```java
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.lang3.StringUtils;

/**
 * Aligns fields into columns, separated by "|"
 */
public class ColumnAligner {
    private List<String[]> words = new ArrayList<>();
    private int columns = 0;
    private List<Integer> columnWidths = new ArrayList<>();

    /**
     * Initialize columns aligner from lines in a single string
     * 
     * @param s
     *            lines in a single string. Empty string does form a column.
     */
    public ColumnAligner(String s) {
        String[] lines = s.split("\\n");
        for (String line : lines) {
            processInputLine(line);
        }
    }

    /**
     * Initialize columns aligner from lines in a list of strings
     * 
     * @param lines
     *            lines in a single string. Empty string does form a column.
     */
    public ColumnAligner(List<String> lines) {
        for (String line : lines) {
            processInputLine(line);
        }
    }

    private void processInputLine(String line) {
        String[] lineWords = line.split("\\$");
        words.add(lineWords);
        columns = Math.max(columns, lineWords.length);
        for (int i = 0; i < lineWords.length; i++) {
            String word = lineWords[i];
            if (i >= columnWidths.size()) {
                columnWidths.add(word.length());
            } else {
                columnWidths.set(i, Math.max(columnWidths.get(i), word.length()));
            }
        }
    }

    interface AlignFunction {
        String align(String s, int length);
    }

    /**
     * Left-align all columns
     * 
     * @return Lines, terminated by "\n" of columns, separated by "|"
     */
    public String alignLeft() {
        return align(new AlignFunction() {
            @Override
            public String align(String s, int length) {
                return StringUtils.rightPad(s, length);
            }
        });
    }

    /**
     * Right-align all columns
     * 
     * @return Lines, terminated by "\n" of columns, separated by "|"
     */
    public String alignRight() {
        return align(new AlignFunction() {
            @Override
            public String align(String s, int length) {
                return StringUtils.leftPad(s, length);
            }
        });
    }

    /**
     * Center-align all columns
     * 
     * @return Lines, terminated by "\n" of columns, separated by "|"
     */
    public String alignCenter() {
        return align(new AlignFunction() {
            @Override
            public String align(String s, int length) {
                return StringUtils.center(s, length);
            }
        });
    }

    private String align(AlignFunction a) {
        StringBuilder result = new StringBuilder();
        for (String[] lineWords : words) {
            for (int i = 0; i < lineWords.length; i++) {
                String word = lineWords[i];
                if (i == 0) {
                    result.append("|");
                }
                result.append(a.align(word, columnWidths.get(i)) + "|");
            }
            result.append("\n");
        }
        return result.toString();
    }

    public static void main(String args[]) throws IOException {
        if (args.length < 1) {
            System.out.println("Usage: ColumnAligner file [left|right|center]");
            return;
        }
        String filePath = args[0];
        String alignment = "left";
        if (args.length >= 2) {
            alignment = args[1];
        }
        ColumnAligner ca = new ColumnAligner(Files.readAllLines(Paths.get(filePath), StandardCharsets.UTF_8));
        switch (alignment) {
        case "left":
            System.out.print(ca.alignLeft());
            break;
        case "right":
            System.out.print(ca.alignRight());
            break;
        case "center":
            System.out.print(ca.alignCenter());
            break;
        default:
            System.err.println(String.format("Error! Unknown alignment: '%s'", alignment));
            break;
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import zip_longest

txt = """Given$a$txt$file$of$many$lines,$where$fields$within$a$line$
are$delineated$by$a$single$'dollar'$character,$write$a$program
that$aligns$each$column$of$fields$by$ensuring$that$words$in$each$
column$are$separated$by$at$least$one$space.
Further,$allow$for$each$word$in$a$column$to$be$either$left$
justified,$right$justified,$or$center$justified$within$its$column."""
 
parts = [line.rstrip("$").split("$") for line in txt.splitlines()]
widths = [max(len(word) for word in col) 
          for col in zip_longest(*parts, fillvalue='')]
 
for justify in "<_Left ^_Center >_Right".split():
    j, jtext = justify.split('_')
    print(f"{jtext} column-aligned output:\n")
    for line in parts:
        print(' '.join(f"{wrd:{j}{wdth}}" for wdth, wrd in zip(widths, line)))
    print("- " * 52)

```

### python_code_2.txt
```python
from StringIO import StringIO
 
textinfile = '''Given$a$text$file$of$many$lines,$where$fields$within$a$line$
are$delineated$by$a$single$'dollar'$character,$write$a$program
that$aligns$each$column$of$fields$by$ensuring$that$words$in$each$
column$are$separated$by$at$least$one$space.
Further,$allow$for$each$word$in$a$column$to$be$either$left$
justified,$right$justified,$or$center$justified$within$its$column.'''
 
j2justifier = dict(L=str.ljust, R=str.rjust, C=str.center)
 
def aligner(infile, justification = 'L'):
  ''' \
  Justify columns of textual tabular input where the row separator is the newline
  and the field separator is a 'dollar' character.
  justification can be L, R, or C; (Left, Right, or Centered).
 
  Return the justified output as a string
  '''
  assert justification in j2justifier, "justification can be L, R, or C; (Left, Right, or Centered)."
  justifier = j2justifier[justification]
 
  fieldsbyrow= [line.strip().split('$') for line in infile]
  # pad to same number of fields per row
  maxfields = max(len(row) for row in fieldsbyrow)
  fieldsbyrow = [fields + ['']*(maxfields - len(fields))
                    for fields in fieldsbyrow]
  # rotate
  fieldsbycolumn = zip(*fieldsbyrow)
  # calculate max fieldwidth per column
  colwidths = [max(len(field) for field in column)
               for column in fieldsbycolumn]
  # pad fields in columns to colwidth with spaces
  fieldsbycolumn = [ [justifier(field, width) for field in column]
                     for width, column in zip(colwidths, fieldsbycolumn) ]
  # rotate again
  fieldsbyrow = zip(*fieldsbycolumn)
 
  return "\n".join( " ".join(row) for row in fieldsbyrow)
 
 
for align in 'Left Right Center'.split():
  infile = StringIO(textinfile)
  print "\n# %s Column-aligned output:" % align
  print aligner(infile, align[0])

```

### python_code_3.txt
```python
'''
cat <<'EOF' > align_columns.dat
Given$a$text$file$of$many$lines,$where$fields$within$a$line$
are$delineated$by$a$single$'dollar'$character,$write$a$program
that$aligns$each$column$of$fields$by$ensuring$that$words$in$each$
column$are$separated$by$at$least$one$space.
Further,$allow$for$each$word$in$a$column$to$be$either$left$
justified,$right$justified,$or$center$justified$within$its$column.
EOF
'''

for align in '<^>':
  rows = [ line.strip().split('$') for line in open('align_columns.dat') ]
  fmts = [ '{:%s%d}' % (align, max( len(row[i]) if i < len(row) else 0 for row in rows ))
           for i in range(max(map(len, rows))) ]
  for row in rows:
    print(' '.join(fmts).format(*(row + [''] * len(fmts))))
  print('')

```

### python_code_4.txt
```python
txt = """Given$a$txt$file$of$many$lines,$where$fields$within$a$line$
are$delineated$by$a$single$'dollar'$character,$write$a$program
that$aligns$each$column$of$fields$by$ensuring$that$words$in$each$
column$are$separated$by$at$least$one$space.
Further,$allow$for$each$word$in$a$column$to$be$either$left$
justified,$right$justified,$or$center$justified$within$its$column."""
 
parts = [line.rstrip("$").split("$") for line in txt.splitlines()]
 
max_widths = {}
for line in parts:
    for i, word in enumerate(line):
        max_widths[i] = max(max_widths.get(i, 0), len(word))
 
for i, justify in enumerate([str.ljust, str.center, str.rjust]):
    print(["Left", "Center", "Right"][i], " column-aligned output:\n")
    for line in parts:
        for j, word in enumerate(line):
            print(justify(word, max_widths[j]), end=' ')
        print()
    print("- " * 52)

```

### python_code_5.txt
```python
'''Variously aligned columns
   from delimited text.
'''

from functools import reduce
from itertools import repeat


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Test of three alignments.'''

    txt = '''Given$a$text$file$of$many$lines,$where$fields$within$a$line$
are$delineated$by$a$single$'dollar'$character,$write$a$program
that$aligns$each$column$of$fields$by$ensuring$that$words$in$each$
column$are$separated$by$at$least$one$space.
Further,$allow$for$each$word$in$a$column$to$be$either$left$
justified,$right$justified,$or$center$justified$within$its$column.'''

    rows = [x.split('$') for x in txt.splitlines()]
    table = paddedRows(max(map(len, rows)))('')(rows)

    print('\n\n'.join(map(
        alignedTable(table)('  '),
        [-1, 0, 1]  # Left, Center, Right
    )))


# alignedTable :: [[String]] -> Alignment -> String -> String
def alignedTable(rows):
    '''Tabulation of rows of cells, with cell alignment
       specified by:
           eAlign -1 = left
           eAlign  0 = center
           eAlign  1 = right
       and separator between columns
       supplied by the `sep` argument.
    '''
    def go(sep, eAlign):
        lcr = ['ljust', 'center', 'rjust'][1 + eAlign]

        # nextAlignedCol :: [[String]] -> [String] -> [[String]]
        def nextAlignedCol(cols, col):
            w = max(len(cell) for cell in col)
            return cols + [
                [getattr(s, lcr)(w, ' ') for s in col]
            ]

        return '\n'.join([
            sep.join(cells) for cells in
            zip(*reduce(nextAlignedCol, zip(*rows), []))
        ])
    return lambda sep: lambda eAlign: go(sep, eAlign)


# GENERIC -------------------------------------------------

# paddedRows :: Int -> a -> [[a]] -> [[a]]
def paddedRows(n):
    '''A list of rows of even length,
       in which each may be padded (but
       not truncated) to length n with
       appended copies of value v.'''
    def go(v, xs):
        def pad(x):
            d = n - len(x)
            return (x + list(repeat(v, d))) if 0 < d else x
        return [pad(row) for row in xs]
    return lambda v: lambda xs: go(v, xs) if xs else []


# MAIN ---
if __name__ == '__main__':
    main()

```

