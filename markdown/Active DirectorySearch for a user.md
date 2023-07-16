# Active Directory/Search for a user

## Task Link
[Rosetta Code - Active Directory/Search for a user](https://rosettacode.org/wiki/Active_Directory/Search_for_a_user)

## Java Code
### java_code_1.txt
```java
import java.io.IOException;
import org.apache.directory.api.ldap.model.cursor.CursorException;
import org.apache.directory.api.ldap.model.cursor.EntryCursor;
import org.apache.directory.api.ldap.model.entry.Entry;
import org.apache.directory.api.ldap.model.exception.LdapException;
import org.apache.directory.api.ldap.model.message.SearchScope;
import org.apache.directory.ldap.client.api.LdapConnection;
import org.apache.directory.ldap.client.api.LdapNetworkConnection;

public class LdapSearchDemo {

    public static void main(String[] args) throws IOException, LdapException, CursorException {
        new LdapSearchDemo().demonstrateSearch();
    }

    private void demonstrateSearch() throws IOException, LdapException, CursorException {
        try (LdapConnection conn = new LdapNetworkConnection("localhost", 11389)) {
            conn.bind("uid=admin,ou=system", "********");
            search(conn, "*mil*");
            conn.unBind();
        }
    }

    private void search(LdapConnection connection, String uid) throws LdapException, CursorException {
        String baseDn = "ou=users,o=mojo";
        String filter = "(&(objectClass=person)(&(uid=" + uid + ")))";
        SearchScope scope = SearchScope.SUBTREE;
        String[] attributes = {"dn", "cn", "sn", "uid"};
        int ksearch = 0;

        EntryCursor cursor = connection.search(baseDn, filter, scope, attributes);
        while (cursor.next()) {
            ksearch++;
            Entry entry = cursor.get();
            System.out.printf("Search entry %d = %s%n", ksearch, entry);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
Import-Module ActiveDirectory

$searchData = "user name"
$searchBase = "DC=example,DC=com"

#searches by some of the most common unique identifiers
get-aduser -Filter((DistinguishedName -eq $searchdata) -or (UserPrincipalName -eq $searchdata) -or (SamAccountName -eq $searchdata)) -SearchBase $searchBase

```

### python_code_2.txt
```python
import ldap

l = ldap.initialize("ldap://ldap.example.com")
try:
    l.protocol_version = ldap.VERSION3
    l.set_option(ldap.OPT_REFERRALS, 0)

    bind = l.simple_bind_s("me@example.com", "password")
    
    base = "dc=example, dc=com"
    criteria = "(&(objectClass=user)(sAMAccountName=username))"
    attributes = ['displayName', 'company']
    result = l.search_s(base, ldap.SCOPE_SUBTREE, criteria, attributes)

    results = [entry for dn, entry in result if isinstance(entry, dict)]
    print results
finally:
    l.unbind()

```

