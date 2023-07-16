# SQL-based authentication

## Task Link
[Rosetta Code - SQL-based authentication](https://rosettacode.org/wiki/SQL-based_authentication)

## Java Code
### java_code_1.txt
```java
import java.io.UnsupportedEncodingException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.math.BigInteger;


class UserManager {
    private Connection dbConnection;

    public UserManager() {
    }

    private String md5(String aString) throws NoSuchAlgorithmException, UnsupportedEncodingException {
        MessageDigest md;
        String hex;
        StringBuffer hexString;
        byte[] bytesOfMessage;
        byte[] theDigest;

        hexString = new StringBuffer();
        bytesOfMessage = aString.getBytes("UTF-8");
        md = MessageDigest.getInstance("MD5");
        theDigest = md.digest(bytesOfMessage);

        for (int i = 0; i < theDigest.length; i++) {
            hex = Integer.toHexString(0xff & theDigest[i]);
            if (hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex);
        }

        return hexString.toString();
    }

    public void connectDB(String host, int port, String db, String user, String password)
      throws ClassNotFoundException, SQLException {

        Class.forName("com.mysql.jdbc.Driver");

        this.dbConnection =  DriverManager.getConnection("jdbc:mysql://"
                                + host
                                + ":"
                                + port
                                + "/"
                                + db, user, password);
    }

    public boolean createUser(String user, String password) {
        SecureRandom random;
        String insert;
        String salt;

        random = new SecureRandom();
        salt =  new BigInteger(130, random).toString(16);

        insert = "INSERT INTO users "
            + "(username, pass_salt, pass_md5) "
            + "VALUES (?, ?, ?)";

        try (PreparedStatement pstmt = this.dbConnection.prepareStatement(insert)) {
            pstmt.setString(1, user);
            pstmt.setString(2, salt);
            pstmt.setString(3, this.md5(salt + password));
            pstmt.executeUpdate();

            return true;
        } catch(NoSuchAlgorithmException | SQLException | UnsupportedEncodingException ex) {
            return false;
        }
    }

    public boolean authenticateUser(String user, String password) {
        String pass_md5;
        String pass_salt;
        String select;
        ResultSet res;

        select = "SELECT pass_salt, pass_md5 FROM users WHERE username = ?";
        res = null;

        try(PreparedStatement pstmt = this.dbConnection.prepareStatement(select)) {
            pstmt.setString(1, user);
            res = pstmt.executeQuery();

            res.next(); // We assume that username is unique

            pass_salt = res.getString(1);
            pass_md5 = res.getString(2);

            if (pass_md5.equals(this.md5(pass_salt + password))) {
                return true;
            } else {
                return false;
            }

        } catch(NoSuchAlgorithmException | SQLException | UnsupportedEncodingException ex) {
            return false;
        } finally {
            try {
                if (res instanceof ResultSet && !res.isClosed()) {
                    res.close();
                }
            } catch(SQLException ex) {
            }
        }
    }

    public void closeConnection() {
        try {
            this.dbConnection.close();
        } catch(NullPointerException | SQLException ex) {
        }
    }

    public static void main(String[] args) {
        UserManager um;

        um = new UserManager();
        try {
            um.connectDB("localhost", 3306, "test", "root", "admin");

            if (um.createUser("johndoe", "test")) {
                System.out.println("User created");
            }

            if (um.authenticateUser("johndoe", "test")) {
                System.out.println("User authenticated");
            }
        } catch(ClassNotFoundException | SQLException ex) {
            ex.printStackTrace();
        } finally {
            um.closeConnection();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import mysql.connector 
import hashlib
 
import sys	 
import random	 
 
DB_HOST = "localhost"	 
DB_USER = "devel" 
DB_PASS = "devel"	 
DB_NAME = "test"	 
 
def connect_db():	 
    ''' Try to connect DB and return DB instance, if not, return False '''	 
    try:	 
        return mysql.connector.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS, db=DB_NAME)	 
    except:	 
        return False	 
 
def create_user(username, passwd):	 
    ''' if user was successfully created, returns its ID; returns None on error '''	 
    db = connect_db()	 
    if not db:	 
        print "Can't connect MySQL!"
        return None
 
    cursor = db.cursor()	 
 
    salt = randomValue(16)	 	 
    passwd_md5 = hashlib.md5(salt+passwd).hexdigest()	 
 
    # If username already taken, inform it	 
    try:	 
        cursor.execute("INSERT INTO users (`username`, `pass_salt`, `pass_md5`) VALUES (%s, %s, %s)", (username, salt, passwd_md5)) 
        cursor.execute("SELECT userid FROM users WHERE username=%s", (username,) ) 
        id = cursor.fetchone()
        db.commit()
        cursor.close()
        db.close()
        return id[0]	 
    except:	 
        print 'Username was already taken. Please select another'	 
        return None
 
def authenticate_user(username, passwd):	 
    db = connect_db()	 
    if not db:	 
        print "Can't connect MySQL!"
        return False
 
    cursor = db.cursor()	 
 
    cursor.execute("SELECT pass_salt, pass_md5 FROM users WHERE username=%s", (username,))

    row = cursor.fetchone()
    cursor.close()
    db.close()
    if row is None:     # username not found
        return False
    salt = row[0]
    correct_md5 = row[1]
    tried_md5 = hashlib.md5(salt+passwd).hexdigest()
    return correct_md5 == tried_md5
 
def randomValue(length):	 
    ''' Creates random value with given length'''	 
    salt_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

    return ''.join(random.choice(salt_chars) for x in range(length))
 
if __name__ == '__main__':	 
    user = randomValue(10)
    passwd = randomValue(16)	 
 
    new_user_id = create_user(user, passwd)
    if new_user_id is None:
        print 'Failed to create user %s' % user
        sys.exit(1)
    auth = authenticate_user(user, passwd)	 
    if auth:	 
        print 'User %s authenticated successfully' % user	 
    else:	 
        print 'User %s failed' % user

```

