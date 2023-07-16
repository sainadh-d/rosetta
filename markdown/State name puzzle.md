# State name puzzle

## Task Link
[Rosetta Code - State name puzzle](https://rosettacode.org/wiki/State_name_puzzle)

## Java Code
### java_code_1.txt
```java
import java.util.*;
import java.util.stream.*;

public class StateNamePuzzle {

    static String[] states = {"Alabama", "Alaska", "Arizona", "Arkansas",
        "California", "Colorado", "Connecticut", "Delaware", "Florida",
        "Georgia", "hawaii", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
        "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
        "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
        "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
        "New York", "North Carolina ", "North Dakota", "Ohio", "Oklahoma",
        "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
        "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
        "Washington", "West Virginia", "Wisconsin", "Wyoming",
        "New Kory", "Wen Kory", "York New", "Kory New", "New Kory",};

    public static void main(String[] args) {
        solve(Arrays.asList(states));
    }

    static void solve(List<String> input) {
        Map<String, String> orig = input.stream().collect(Collectors.toMap(
                s -> s.replaceAll("\\s", "").toLowerCase(), s -> s, (s, a) -> s));

        input = new ArrayList<>(orig.keySet());

        Map<String, List<String[]>> map = new HashMap<>();
        for (int i = 0; i < input.size() - 1; i++) {
            String pair0 = input.get(i);
            for (int j = i + 1; j < input.size(); j++) {

                String[] pair = {pair0, input.get(j)};
                String s = pair0 + pair[1];
                String key = Arrays.toString(s.chars().sorted().toArray());

                List<String[]> val = map.getOrDefault(key, new ArrayList<>());
                val.add(pair);
                map.put(key, val);
            }
        }

        map.forEach((key, list) -> {
            for (int i = 0; i < list.size() - 1; i++) {
                String[] a = list.get(i);
                for (int j = i + 1; j < list.size(); j++) {
                    String[] b = list.get(j);

                    if (Stream.of(a[0], a[1], b[0], b[1]).distinct().count() < 4)
                        continue;

                    System.out.printf("%s + %s = %s + %s %n", orig.get(a[0]),
                            orig.get(a[1]), orig.get(b[0]), orig.get(b[1]));
                }
            }
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import defaultdict

states = ["Alabama", "Alaska", "Arizona", "Arkansas",
"California", "Colorado", "Connecticut", "Delaware", "Florida",
"Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
"Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
"Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
"Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
"New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
"Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
"South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
"Washington", "West Virginia", "Wisconsin", "Wyoming",
# Uncomment the next line for the fake states.
# "New Kory", "Wen Kory", "York New", "Kory New", "New Kory"
]

states = sorted(set(states))

smap = defaultdict(list)
for i, s1 in enumerate(states[:-1]):
    for s2 in states[i + 1:]:
        smap["".join(sorted(s1 + s2))].append(s1 + " + " + s2)

for pairs in sorted(smap.itervalues()):
    if len(pairs) > 1:
        print " = ".join(pairs)

```

