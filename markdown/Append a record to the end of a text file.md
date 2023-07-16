# Append a record to the end of a text file

## Task Link
[Rosetta Code - Append a record to the end of a text file](https://rosettacode.org/wiki/Append_a_record_to_the_end_of_a_text_file)

## Java Code
### java_code_1.txt
```java
import java.io.FileOutputStream;
import java.io.IOException;

```

### java_code_2.txt
```java
void append(String path, byte[] data) throws IOException {
    /* the second argument here is for appending bytes */
    try (FileOutputStream output = new FileOutputStream(path, true)) {
        output.write(data);
    }
}

```

### java_code_3.txt
```java
import static java.util.Objects.requireNonNull;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class RecordAppender {
    static class Record {
        private final String account;
        private final String password;
        private final int uid;
        private final int gid;
        private final List<String> gecos;
        private final String directory;
        private final String shell;

        public Record(String account, String password, int uid, int gid, List<String> gecos, String directory, String shell) {
            this.account = requireNonNull(account);
            this.password = requireNonNull(password);
            this.uid = uid;
            this.gid = gid;
            this.gecos = requireNonNull(gecos);
            this.directory = requireNonNull(directory);
            this.shell = requireNonNull(shell);
        }

        @Override
        public String toString() {
            return account + ':' + password + ':' + uid + ':' + gid + ':' + String.join(",", gecos) + ':' + directory + ':' + shell;
        }

        public static Record parse(String text) {
            String[] tokens = text.split(":");
            return new Record(
                    tokens[0],
                    tokens[1],
                    Integer.parseInt(tokens[2]),
                    Integer.parseInt(tokens[3]),
                    Arrays.asList(tokens[4].split(",")),
                    tokens[5],
                    tokens[6]);
        }
    }

    public static void main(String[] args) throws IOException {
        List<String> rawData = Arrays.asList(
                "jsmith:x:1001:1000:Joe Smith,Room 1007,(234)555-8917,(234)555-0077,[email protected]:/home/jsmith:/bin/bash",
                "jdoe:x:1002:1000:Jane Doe,Room 1004,(234)555-8914,(234)555-0044,[email protected]:/home/jdoe:/bin/bash",
                "xyz:x:1003:1000:X Yz,Room 1003,(234)555-8913,(234)555-0033,[email protected]:/home/xyz:/bin/bash"
        );

        List<Record> records = rawData.stream().map(Record::parse).collect(Collectors.toList());

        Path tmp = Paths.get("_rosetta", ".passwd");
        Files.createDirectories(tmp.getParent());
        Files.write(tmp, (Iterable<String>) records.stream().limit(2).map(Record::toString)::iterator);

        Files.write(tmp, Collections.singletonList(records.get(2).toString()), StandardOpenOption.APPEND);

        try (Stream<String> lines = Files.lines(tmp)) {
            lines.map(Record::parse).forEach(System.out::println);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
#############################
# Create a passwd text file
#############################
# note that UID & gid are of type "text"
passwd_list=[
  dict(account='jsmith', password='x', UID=1001, GID=1000, # UID and GID are type int
       GECOS=dict(fullname='Joe Smith', office='Room 1007', extension='(234)555-8917',
                  homephone='(234)555-0077', email='jsmith@rosettacode.org'),
                  directory='/home/jsmith', shell='/bin/bash'),
  dict(account='jdoe', password='x', UID=1002, GID=1000,
       GECOS=dict(fullname='Jane Doe', office='Room 1004', extension='(234)555-8914',
                  homephone='(234)555-0044', email='jdoe@rosettacode.org'),
       directory='/home/jdoe', shell='/bin/bash')
]

passwd_fields="account password UID GID GECOS directory shell".split()
GECOS_fields="fullname office extension homephone email".split()

def passwd_text_repr(passwd_rec):
# convert individual fields to string type
  passwd_rec["GECOS"]=",".join([ passwd_rec["GECOS"][field] for field in GECOS_fields])
  for field in passwd_rec: # convert "int" fields
    if not isinstance(passwd_rec[field], str):
      passwd_rec[field]=`passwd_rec[field]`
  return ":".join([ passwd_rec[field] for field in passwd_fields ])

passwd_text=open("passwd.txt","w")
for passwd_rec in passwd_list:
  print >> passwd_text,passwd_text_repr(passwd_rec)
passwd_text.close()

#################################
# Load text ready for appending
#################################
passwd_text=open("passwd.txt","a+")
new_rec=dict(account='xyz', password='x', UID=1003, GID=1000,
             GECOS=dict(fullname='X Yz', office='Room 1003', extension='(234)555-8913',
                        homephone='(234)555-0033', email='xyz@rosettacode.org'),
             directory='/home/xyz', shell='/bin/bash')
print >> passwd_text,  passwd_text_repr(new_rec)
passwd_text.close()

##############################################
# Finally reopen and check record was appended
##############################################
passwd_list=list(open("passwd.txt","r"))
if "xyz" in passwd_list[-1]:
  print "Appended record:",passwd_list[-1][:-1]

```

