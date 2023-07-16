# Parameterized SQL statement

## Task Link
[Rosetta Code - Parameterized SQL statement](https://rosettacode.org/wiki/Parameterized_SQL_statement)

## Java Code
### java_code_1.txt
```java
import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.PreparedStatement;
 
public class DBDemo{
   private String protocol; //set this to some connection protocol like "jdbc:sqlserver://"
   private String dbName;   //set this to the name of your database
   private String username;
   private String password;

   PreparedStatement query;
 
   public int setUpAndExecPS(){
      try {
         Connection conn = DriverManager.getConnection(protocol + dbName, username, password);

         query = conn.prepareStatement(
            "UPDATE players SET name = ?, score = ?, active = ? WHERE jerseyNum = ?");
 
         query.setString(1, "Smith, Steve");//automatically sanitizes and adds quotes
         query.setInt(2, 42);
         query.setBoolean(3, true);
         query.setInt(4, 99);
         //there are similar methods for other SQL types in PerparedStatement
         return query.executeUpdate();//returns the number of rows changed
         //PreparedStatement.executeQuery() will return a java.sql.ResultSet,
         //execute() will simply return a boolean saying whether it succeeded or not

      } catch (Exception e) {
         e.printStackTrace();
      }

      return 0;
   }
}

```

## Python Code
### python_code_1.txt
```python
import sqlite3

db = sqlite3.connect(':memory:')

# setup
db.execute('create temp table players (name, score, active, jerseyNum)')
db.execute('insert into players values ("name",0,"false",99)')
db.execute('insert into players values ("name",0,"false",100)')

# demonstrate parameterized SQL

# example 1 -- simple placeholders
db.execute('update players set name=?, score=?, active=? where jerseyNum=?', ('Smith, Steve', 42, True, 99))

# example 2 -- named placeholders
db.execute('update players set name=:name, score=:score, active=:active where jerseyNum=:num',
    {'num': 100,
     'name': 'John Doe',
     'active': False,
     'score': -1}
)

# and show the results
for row in db.execute('select * from players'):
   print(row)

```

