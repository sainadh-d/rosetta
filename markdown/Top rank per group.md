# Top rank per group

## Task Link
[Rosetta Code - Top rank per group](https://rosettacode.org/wiki/Top_rank_per_group)

## Java Code
### java_code_1.txt
```java
import java.io.File;
import java.util.*;

public class TopRankPerGroup {

    private static class Employee {
        final String name;
        final String id;
        final String department;
        final int salary;

        Employee(String[] rec) {
            name = rec[0];
            id = rec[1];
            salary = Integer.parseInt(rec[2]);
            department = rec[3];
        }

        @Override
        public String toString() {
            return String.format("%s %s %d %s", id, name, salary, department);
        }
    }

    public static void main(String[] args) throws Exception {
        int N = args.length > 0 ? Integer.parseInt(args[0]) : 3;

        Map<String, List<Employee>> records = new TreeMap<>();
        try (Scanner sc = new Scanner(new File("data.txt"))) {
            while (sc.hasNextLine()) {
                String[] rec = sc.nextLine().trim().split(", ");

                List<Employee> lst = records.get(rec[3]);
                if (lst == null) {
                    lst = new ArrayList<>();
                    records.put(rec[3], lst);
                }
                lst.add(new Employee(rec));
            }
        }

        records.forEach((key, val) -> {
            System.out.printf("%nDepartment %s%n", key);
            val.stream()
                .sorted((a, b) -> Integer.compare(b.salary, a.salary))
                .limit(N).forEach(System.out::println);
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import defaultdict
from heapq import nlargest
 
data = [('Employee Name', 'Employee ID', 'Salary', 'Department'),
        ('Tyler Bennett', 'E10297', 32000, 'D101'),
        ('John Rappl', 'E21437', 47000, 'D050'),
        ('George Woltman', 'E00127', 53500, 'D101'),
        ('Adam Smith', 'E63535', 18000, 'D202'),
        ('Claire Buckman', 'E39876', 27800, 'D202'),
        ('David McClellan', 'E04242', 41500, 'D101'),
        ('Rich Holcomb', 'E01234', 49500, 'D202'),
        ('Nathan Adams', 'E41298', 21900, 'D050'),
        ('Richard Potter', 'E43128', 15900, 'D101'),
        ('David Motsinger', 'E27002', 19250, 'D202'),
        ('Tim Sampair', 'E03033', 27000, 'D101'),
        ('Kim Arlich', 'E10001', 57000, 'D190'),
        ('Timothy Grove', 'E16398', 29900, 'D190')]
 
departments = defaultdict(list)
for rec in data[1:]:
    departments[rec[-1]].append(rec)
 
N = 3
format = " %-15s " * len(data[0])
for department, recs in sorted(departments.items()):
    print ("Department %s" % department)
    print (format % data[0])
    for rec in nlargest(N, recs, key=lambda rec: rec[-2]):
        print (format % rec)
    print('')

```

### python_code_2.txt
```python
from collections import namedtuple
from itertools import groupby

N = 2

db = '''Employee Name,Employee ID,Salary,Department
Tyler Bennett,E10297,32000,D101
John Rappl,E21437,47000,D050
George Woltman,E00127,53500,D101
Adam Smith,E63535,18000,D202
Claire Buckman,E39876,27800,D202
David McClellan,E04242,41500,D101
Rich Holcomb,E01234,49500,D202
Nathan Adams,E41298,21900,D050
Richard Potter,E43128,15900,D101
David Motsinger,E27002,19250,D202
Tim Sampair,E03033,27000,D101
Kim Arlich,E10001,57000,D190
Timothy Grove,E16398,29900,D190'''

rows = db.split('\n')
DBRecord = namedtuple('DBRecord', rows[0].replace(' ', '_'))

records = [DBRecord(*row.split(',')) for row in rows[1:]]

records.sort(key=lambda record: (record.Department, -float(record.Salary)))

print('\n\n'.join(
    '\n  '.join([dpt] + [str(g) for g in grp][:N])
    for dpt, grp in groupby(
        records,
        lambda record: record.Department
    )
))

```

