# De Bruijn sequences

## Task Link
[Rosetta Code - De Bruijn sequences](https://rosettacode.org/wiki/De_Bruijn_sequences)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.BiConsumer;

public class DeBruijn {
    public interface Recursable<T, U> {
        void apply(T t, U u, Recursable<T, U> r);
    }

    public static <T, U> BiConsumer<T, U> recurse(Recursable<T, U> f) {
        return (t, u) -> f.apply(t, u, f);
    }

    private static String deBruijn(int k, int n) {
        byte[] a = new byte[k * n];
        Arrays.fill(a, (byte) 0);

        List<Byte> seq = new ArrayList<>();

        BiConsumer<Integer, Integer> db = recurse((t, p, f) -> {
            if (t > n) {
                if (n % p == 0) {
                    for (int i = 1; i < p + 1; ++i) {
                        seq.add(a[i]);
                    }
                }
            } else {
                a[t] = a[t - p];
                f.apply(t + 1, p, f);
                int j = a[t - p] + 1;
                while (j < k) {
                    a[t] = (byte) (j & 0xFF);
                    f.apply(t + 1, t, f);
                    j++;
                }
            }
        });
        db.accept(1, 1);

        StringBuilder sb = new StringBuilder();
        for (Byte i : seq) {
            sb.append("0123456789".charAt(i));
        }

        sb.append(sb.subSequence(0, n - 1));
        return sb.toString();
    }

    private static boolean allDigits(String s) {
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            if (!Character.isDigit(c)) {
                return false;
            }
        }
        return true;
    }

    private static void validate(String db) {
        int le = db.length();
        int[] found = new int[10_000];
        Arrays.fill(found, 0);
        List<String> errs = new ArrayList<>();

        // Check all strings of 4 consecutive digits within 'db'
        // to see if all 10,000 combinations occur without duplication.
        for (int i = 0; i < le - 3; ++i) {
            String s = db.substring(i, i + 4);
            if (allDigits(s)) {
                int n = Integer.parseInt(s);
                found[n]++;
            }
        }

        for (int i = 0; i < 10_000; ++i) {
            if (found[i] == 0) {
                errs.add(String.format("    PIN number %d is missing", i));
            } else if (found[i] > 1) {
                errs.add(String.format("    PIN number %d occurs %d times", i, found[i]));
            }
        }

        if (errs.isEmpty()) {
            System.out.println("    No errors found");
        } else {
            String pl = (errs.size() == 1) ? "" : "s";
            System.out.printf("  %d error%s found:\n", errs.size(), pl);
            errs.forEach(System.out::println);
        }
    }

    public static void main(String[] args) {
        String db = deBruijn(10, 4);

        System.out.printf("The length of the de Bruijn sequence is %d\n\n", db.length());
        System.out.printf("The first 130 digits of the de Bruijn sequence are: %s\n\n", db.substring(0, 130));
        System.out.printf("The last 130 digits of the de Bruijn sequence are: %s\n\n", db.substring(db.length() - 130));

        System.out.println("Validating the de Bruijn sequence:");
        validate(db);

        StringBuilder sb = new StringBuilder(db);
        String rdb = sb.reverse().toString();
        System.out.println();
        System.out.println("Validating the de Bruijn sequence:");
        validate(rdb);

        sb = new StringBuilder(db);
        sb.setCharAt(4443, '.');
        System.out.println();
        System.out.println("Validating the overlaid de Bruijn sequence:");
        validate(sb.toString());
    }
}

```

## Python Code
### python_code_1.txt
```python
# from https://en.wikipedia.org/wiki/De_Bruijn_sequence

def de_bruijn(k, n):
    """
    de Bruijn sequence for alphabet k
    and subsequences of length n.
    """
    try:
        # let's see if k can be cast to an integer;
        # if so, make our alphabet a list
        _ = int(k)
        alphabet = list(map(str, range(k)))

    except (ValueError, TypeError):
        alphabet = k
        k = len(k)

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return "".join(alphabet[i] for i in sequence)
    
def validate(db):
    """
    
    Check that all 10,000 combinations of 0-9 are present in 
    De Bruijn string db.
    
    Validating the reversed deBruijn sequence:
      No errors found
    
    Validating the overlaid deBruijn sequence:
      4 errors found:
        PIN number 1459 missing
        PIN number 4591 missing
        PIN number 5814 missing
        PIN number 8145 missing
    
    """
    
    dbwithwrap = db+db[0:3]
    
    digits = '0123456789'
    
    errorstrings = []
    
    for d1 in digits:
        for d2 in digits:
            for d3 in digits:
                for d4 in digits:
                    teststring = d1+d2+d3+d4
                    if teststring not in dbwithwrap:
                        errorstrings.append(teststring)
                        
    if len(errorstrings) > 0:
        print("  "+str(len(errorstrings))+" errors found:")
        for e in errorstrings:
            print("  PIN number "+e+"  missing")
    else:
        print("  No errors found")

db = de_bruijn(10, 4)

print(" ")
print("The length of the de Bruijn sequence is ", str(len(db)))
print(" ")
print("The first 130 digits of the de Bruijn sequence are: "+db[0:130])
print(" ")
print("The last 130 digits of the de Bruijn sequence are: "+db[-130:])
print(" ")
print("Validating the deBruijn sequence:")
validate(db)
dbreversed = db[::-1]
print(" ")
print("Validating the reversed deBruijn sequence:")
validate(dbreversed)
dboverlaid = db[0:4443]+'.'+db[4444:]
print(" ")
print("Validating the overlaid deBruijn sequence:")
validate(dboverlaid)

```

