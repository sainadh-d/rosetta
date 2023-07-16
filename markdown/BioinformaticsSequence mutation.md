# Bioinformatics/Sequence mutation

## Task Link
[Rosetta Code - Bioinformatics/Sequence mutation](https://rosettacode.org/wiki/Bioinformatics/Sequence_mutation)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class Program {
    List<Character> sequence;
    Random random;

    SequenceMutation() {
        sequence = new ArrayList<>();
        random = new Random();
    }

    void generate(int amount) {
        for (int count = 0; count < amount; count++)
            sequence.add(randomBase());
    }

    void mutate(int amount) {
        int index;
        for (int count = 0; count < amount; count++) {
            index = random.nextInt(0, sequence.size());
            switch (random.nextInt(0, 3)) {
                case 0 -> sequence.set(index, randomBase());
                case 1 -> sequence.remove(index);
                case 2 -> sequence.add(index, randomBase());
            }
        }
    }

    private char randomBase() {
        return switch (random.nextInt(0, 4)) {
            case 0 -> 'A';
            case 1 -> 'C';
            case 2 -> 'G';
            case 3 -> 'T';
            default -> '?';
        };
    }

    private Base count(String string) {
        int a = 0, c = 0, g = 0, t = 0;
        for (char base : string.toCharArray()) {
            switch (base) {
                case 'A' -> a++;
                case 'C' -> c++;
                case 'G' -> g++;
                case 'T' -> t++;
            }
        }
        return new Base(a, c, g, t);
    }

    /* used exclusively for count totals */
    private record Base(int a, int c, int g, int t) {
        int total() {
            return a + c + g + t;
        }

        @Override
        public String toString() {
            return "[A %2d, C %2d, G %2d, T %2d]".formatted(a, c, g, t);
        }
    }

    @Override
    public String toString() {
        StringBuilder string = new StringBuilder();
        StringBuilder stringB = new StringBuilder();
        String newline = System.lineSeparator();
        for (int index = 0; index < sequence.size(); index++) {
            if (index != 0 && index % 50 == 0)
                string.append(newline);
            string.append(sequence.get(index));
            stringB.append(sequence.get(index));
        }
        try {
            BufferedReader reader = new BufferedReader(new StringReader(string.toString()));
            string = new StringBuilder();
            int count = 0;
            String line;
            while ((line = reader.readLine()) != null) {
                string.append(count++);
                string.append(" %-50s ".formatted(line));
                string.append(count(line));
                string.append(newline);
            }
        } catch (IOException exception) {
            /* ignore */
        }
        string.append(newline);
        Base bases = count(stringB.toString());
        int total = bases.total();
        string.append("Total of %d bases%n".formatted(total));
        string.append("A %3d (%.2f%%)%n".formatted(bases.a, ((double) bases.a / total) * 100));
        string.append("C %3d (%.2f%%)%n".formatted(bases.c, ((double) bases.c / total) * 100));
        string.append("G %3d (%.2f%%)%n".formatted(bases.g, ((double) bases.g / total) * 100));
        string.append("T %3d (%.2f%%)%n".formatted(bases.t, ((double) bases.t / total) * 100));
        return string.toString();
    }
}

```

### java_code_2.txt
```java
import java.util.Arrays;
import java.util.Random;

public class SequenceMutation {
    public static void main(String[] args) {
        SequenceMutation sm = new SequenceMutation();
        sm.setWeight(OP_CHANGE, 3);
        String sequence = sm.generateSequence(250);
        System.out.println("Initial sequence:");
        printSequence(sequence);
        int count = 10;
        for (int i = 0; i < count; ++i)
            sequence = sm.mutateSequence(sequence);
        System.out.println("After " + count + " mutations:");
        printSequence(sequence);
    }

    public SequenceMutation() {
        totalWeight_ = OP_COUNT;
        Arrays.fill(operationWeight_, 1);
    }

    public String generateSequence(int length) {
        char[] ch = new char[length];
        for (int i = 0; i < length; ++i)
            ch[i] = getRandomBase();
        return new String(ch);
    }

    public void setWeight(int operation, int weight) {
        totalWeight_ -= operationWeight_[operation];
        operationWeight_[operation] = weight;
        totalWeight_ += weight;
    }

    public String mutateSequence(String sequence) {
        char[] ch = sequence.toCharArray();
        int pos = random_.nextInt(ch.length);
        int operation = getRandomOperation();
        if (operation == OP_CHANGE) {
            char b = getRandomBase();
            System.out.println("Change base at position " + pos + " from "
                               + ch[pos] + " to " + b);
            ch[pos] = b;
        } else if (operation == OP_ERASE) {
            System.out.println("Erase base " + ch[pos] + " at position " + pos);
            char[] newCh = new char[ch.length - 1];
            System.arraycopy(ch, 0, newCh, 0, pos);
            System.arraycopy(ch, pos + 1, newCh, pos, ch.length - pos - 1);
            ch = newCh;
        } else if (operation == OP_INSERT) {
            char b = getRandomBase();
            System.out.println("Insert base " + b + " at position " + pos);
            char[] newCh = new char[ch.length + 1];
            System.arraycopy(ch, 0, newCh, 0, pos);
            System.arraycopy(ch, pos, newCh, pos + 1, ch.length - pos);
            newCh[pos] = b;
            ch = newCh;
        }
        return new String(ch);
    }

    public static void printSequence(String sequence) {
        int[] count = new int[BASES.length];
        for (int i = 0, n = sequence.length(); i < n; ++i) {
            if (i % 50 == 0) {
                if (i != 0)
                    System.out.println();
                System.out.printf("%3d: ", i);
            }
            char ch = sequence.charAt(i);
            System.out.print(ch);
            for (int j = 0; j < BASES.length; ++j) {
                if (BASES[j] == ch) {
                    ++count[j];
                    break;
                }
            }
        }
        System.out.println();
        System.out.println("Base counts:");
        int total = 0;
        for (int j = 0; j < BASES.length; ++j) {
            total += count[j];
            System.out.print(BASES[j] + ": " + count[j] + ", ");
        }
        System.out.println("Total: " + total);
    }

    private char getRandomBase() {
        return BASES[random_.nextInt(BASES.length)];
    }

    private int getRandomOperation() {
        int n = random_.nextInt(totalWeight_), op = 0;
        for (int weight = 0; op < OP_COUNT; ++op) {
            weight += operationWeight_[op];
            if (n < weight)
                break;
        }
        return op;
    }

    private final Random random_ = new Random();
    private int[] operationWeight_ = new int[OP_COUNT];
    private int totalWeight_ = 0;

    private static final int OP_CHANGE = 0;
    private static final int OP_ERASE = 1;
    private static final int OP_INSERT = 2;
    private static final int OP_COUNT = 3;
    private static final char[] BASES = {'A', 'C', 'G', 'T'};
}

```

## Python Code
### python_code_1.txt
```python
import random
from collections import Counter

def basecount(dna):
    return sorted(Counter(dna).items())

def seq_split(dna, n=50):
    return [dna[i: i+n] for i in range(0, len(dna), n)]

def seq_pp(dna, n=50):
    for i, part in enumerate(seq_split(dna, n)):
        print(f"{i*n:>5}: {part}")
    print("\n  BASECOUNT:")
    tot = 0
    for base, count in basecount(dna):
        print(f"    {base:>3}: {count}")
        tot += count
    base, count = 'TOT', tot
    print(f"    {base:>3}= {count}")

def seq_mutate(dna, count=1, kinds="IDSSSS", choice="ATCG" ):
    mutation = []
    k2txt = dict(I='Insert', D='Delete', S='Substitute')
    for _ in range(count):
        kind = random.choice(kinds)
        index = random.randint(0, len(dna))
        if kind == 'I':    # Insert
            dna = dna[:index] + random.choice(choice) + dna[index:]
        elif kind == 'D' and dna:  # Delete
            dna = dna[:index] + dna[index+1:]
        elif kind == 'S' and dna:  # Substitute
            dna = dna[:index] + random.choice(choice) + dna[index+1:]
        mutation.append((k2txt[kind], index))
    return dna, mutation

if __name__ == '__main__':
    length = 250
    print("SEQUENCE:")
    sequence = ''.join(random.choices('ACGT', weights=(1, 0.8, .9, 1.1), k=length))
    seq_pp(sequence)
    print("\n\nMUTATIONS:")
    mseq, m = seq_mutate(sequence, 10)
    for kind, index in m:
        print(f" {kind:>10} @{index}")
    print()
    seq_pp(mseq)

```

