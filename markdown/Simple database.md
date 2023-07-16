# Simple database

## Task Link
[Rosetta Code - Simple database](https://rosettacode.org/wiki/Simple_database)

## Java Code
### java_code_1.txt
```java
import java.io.*;
import java.text.*;
import java.util.*;

public class SimpleDatabase {

    final static String filename = "simdb.csv";

    public static void main(String[] args) {
        if (args.length < 1 || args.length > 3) {
            printUsage();
            return;
        }

        switch (args[0].toLowerCase()) {
            case "add":
                addItem(args);
                break;
            case "latest":
                printLatest(args);
                break;
            case "all":
                printAll();
                break;
            default:
                printUsage();
                break;
        }
    }

    private static class Item implements Comparable<Item>{
        final String name;
        final String date;
        final String category;

        Item(String n, String d, String c) {
            name = n;
            date = d;
            category = c;
        }

        @Override
        public int compareTo(Item item){
            return date.compareTo(item.date);
        }

        @Override
        public String toString() {
            return String.format("%s,%s,%s%n", name, date, category);
        }
    }

    private static void addItem(String[] input) {
        if (input.length < 2) {
            printUsage();
            return;
        }
        List<Item> db = load();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String date = sdf.format(new Date());
        String cat = (input.length == 3) ? input[2] : "none";
        db.add(new Item(input[1], date, cat));
        store(db);
    }

    private static void printLatest(String[] a) {
        List<Item> db = load();
        if (db.isEmpty()) {
            System.out.println("No entries in database.");
            return;
        }
        Collections.sort(db);
        if (a.length == 2) {
            for (Item item : db)
                if (item.category.equals(a[1]))
                    System.out.println(item);
        } else {
            System.out.println(db.get(0));
        }
    }

    private static void printAll() {
        List<Item> db = load();
        if (db.isEmpty()) {
            System.out.println("No entries in database.");
            return;
        }
        Collections.sort(db);
        for (Item item : db)
            System.out.println(item);
    }

    private static List<Item> load() {
        List<Item> db = new ArrayList<>();
        try (Scanner sc = new Scanner(new File(filename))) {
            while (sc.hasNext()) {
                String[] item = sc.nextLine().split(",");
                db.add(new Item(item[0], item[1], item[2]));
            }
        } catch (IOException e) {
            System.out.println(e);
        }
        return db;
    }

    private static void store(List<Item> db) {
        try (FileWriter fw = new FileWriter(filename)) {
            for (Item item : db)
                fw.write(item.toString());
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    private static void printUsage() {
         System.out.println("Usage:");
         System.out.println("  simdb cmd [categoryName]");
         System.out.println("  add     add item, followed by optional category");
         System.out.println("  latest  print last added item(s), followed by "
                 + "optional category");
         System.out.println("  all     print all");
         System.out.println("  For instance: add \"some item name\" "
                 + "\"some category name\"");
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/python3

'''\
Simple database for: http://rosettacode.org/wiki/Simple_database

'''

import argparse
from argparse import Namespace
import datetime
import shlex


def parse_args():
    'Set up, parse, and return arguments'
    
    parser = argparse.ArgumentParser(epilog=globals()['__doc__'])

    parser.add_argument('command', choices='add pl plc pa'.split(),
                        help='''\
add: Add a new entry
pl:  Print the latest entry
plc: Print the latest entry for each category/tag
pa:  Print all entries sorted by a date''')
    parser.add_argument('-d', '--description',
                        help='A description of the item. (e.g., title, name)')
    parser.add_argument('-t', '--tag',
                        help=('''A category or tag (genre, topic, relationship '''
                              '''such as “friend” or “family”)'''))
    parser.add_argument('-f', '--field', nargs=2, action='append', 
                        help='Other optional fields with value (can be repeated)')

    return parser

def do_add(args, dbname):
    'Add a new entry'
    if args.description is None:
        args.description = ''
    if args.tag is None:
        args.tag = ''
    del args.command
    print('Writing record to %s' % dbname)
    with open(dbname, 'a') as db:
        db.write('%r\n' % args)
    
def do_pl(args, dbname):
    'Print the latest entry'
    print('Getting last record from %s' % dbname)
    with open(dbname, 'r') as db:
        for line in db: pass
    record = eval(line)
    del record._date
    print(str(record))
    
def do_plc(args, dbname):
    'Print the latest entry for each category/tag'
    print('Getting latest record for each tag from %s' % dbname)
    with open(dbname, 'r') as db:
        records = [eval(line) for line in db]
    tags = set(record.tag for record in records)
    records.reverse()
    for record in records:
        if record.tag in tags:
            del record._date
            print(str(record))
            tags.discard(record.tag)
            if not tags: break

def do_pa(args, dbname):
    'Print all entries sorted by a date'
    print('Getting all records by date from %s' % dbname)
    with open(dbname, 'r') as db:
        records = [eval(line) for line in db]
    for record in records:
        del record._date
        print(str(record))

def test():
    import time
    parser = parse_args()
    for cmdline in [
                    """-d Book -f title 'Windy places' -f type hardback --tag DISCOUNT add""",
                    """-d Book -f title 'RC spammers'  -f type paperback -t   DISCOUNT add""",
                    """-d Book -f title 'Splat it' -f type hardback -f special 'first edition' -t PREMIUM add""",
                    """pl""",
                    """plc""",
                    ]:
        args = parser.parse_args(shlex.split(cmdline))
        now = datetime.datetime.utcnow()
        args._date = now.isoformat()
        do_command[args.command](args, dbname)
        time.sleep(0.5)


    
do_command = dict(add=do_add, pl=do_pl, plc=do_plc, pa=do_pa)
dbname = '_simple_db_db.py'


if __name__ == '__main__':
    if 0:
        test()
    else:
        parser = parse_args()
        args = parser.parse_args()
        now = datetime.datetime.utcnow()
        args._date = now.isoformat()
        do_command[args.command](args, dbname)

```

