# Active Directory/Connect

## Task Link
[Rosetta Code - Active Directory/Connect](https://rosettacode.org/wiki/Active_Directory/Connect)

## Java Code
### java_code_1.txt
```java
import java.io.IOException;
import org.apache.directory.api.ldap.model.exception.LdapException;
import org.apache.directory.ldap.client.api.LdapConnection;
import org.apache.directory.ldap.client.api.LdapNetworkConnection;

public class LdapConnectionDemo {

    public static void main(String[] args) throws LdapException, IOException {
        try (LdapConnection connection = new LdapNetworkConnection("localhost", 10389)) {
            connection.bind();
            connection.unBind();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import ldap

l = ldap.initialize("ldap://ldap.example.com")
try:
    l.protocol_version = ldap.VERSION3
    l.set_option(ldap.OPT_REFERRALS, 0)

    bind = l.simple_bind_s("me@example.com", "password")
finally:
    l.unbind()

```

