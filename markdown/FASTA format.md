# FASTA format

## Task Link
[Rosetta Code - FASTA format](https://rosettacode.org/wiki/FASTA_format)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

```

### java_code_2.txt
```java
public static void main(String[] args) throws IOException {
    List<FASTA> fastas = readFile("fastas.txt");
    for (FASTA fasta : fastas)
        System.out.println(fasta);
}

static List<FASTA> readFile(String path) throws IOException {
    try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
        List<FASTA> list = new ArrayList<>();
        StringBuilder lines = null;
        String newline = System.lineSeparator();
        String line;
        while ((line = reader.readLine()) != null) {
            if (line.startsWith(">")) {
                if (lines != null)
                    list.add(parseFASTA(lines.toString()));
                lines = new StringBuilder();
                lines.append(line).append(newline);
            } else {
                lines.append(line);
            }
        }
        list.add(parseFASTA(lines.toString()));
        return list;
    }
}

static FASTA parseFASTA(String string) {
    String description;
    char[] sequence;
    int indexOf = string.indexOf(System.lineSeparator());
    description = string.substring(1, indexOf);
    /* using 'stripLeading' will remove any additional line-separators */
    sequence = string.substring(indexOf + 1).stripLeading().toCharArray();
    return new FASTA(description, sequence);
}

/* using a 'char' array seems more logical */
record FASTA(String description, char[] sequence) {
    @Override
    public String toString() {
        return "%s: %s".formatted(description, new String(sequence));
    }
}

```

### java_code_3.txt
```java
import java.io.*;
import java.util.Scanner;

public class ReadFastaFile {

    public static void main(String[] args) throws FileNotFoundException {

        boolean first = true;

        try (Scanner sc = new Scanner(new File("test.fasta"))) {
            while (sc.hasNextLine()) {
                String line = sc.nextLine().trim();
                if (line.charAt(0) == '>') {
                    if (first)
                        first = false;
                    else
                        System.out.println();
                    System.out.printf("%s: ", line.substring(1));
                } else {
                    System.out.print(line);
                }
            }
        }
        System.out.println();
    }
}

```

## Python Code
### python_code_1.txt
```python
import io

FASTA='''\
>Rosetta_Example_1
THERECANBENOSPACE
>Rosetta_Example_2
THERECANBESEVERAL
LINESBUTTHEYALLMUST
BECONCATENATED'''

infile = io.StringIO(FASTA)

def fasta_parse(infile):
    key = ''
    for line in infile:
        if line.startswith('>'):
            if key:
                yield key, val
            key, val = line[1:].rstrip().split()[0], ''
        elif key:
            val += line.rstrip()
    if key:
        yield key, val

print('\n'.join('%s: %s' % keyval for keyval in fasta_parse(infile)))

```

