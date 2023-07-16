# Read a configuration file

## Task Link
[Rosetta Code - Read a configuration file](https://rosettacode.org/wiki/Read_a_configuration_file)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ConfigReader {
    private static final Pattern             LINE_PATTERN = Pattern.compile( "([^ =]+)[ =]?(.*)" );
    private static final Map<String, Object> DEFAULTS     = new HashMap<String, Object>() {{
        put( "needspeeling", false );
        put( "seedsremoved", false );
    }};

    public static void main( final String[] args ) {
        System.out.println( parseFile( args[ 0 ] ) );
    }

    public static Map<String, Object> parseFile( final String fileName ) {
        final Map<String, Object> result = new HashMap<String, Object>( DEFAULTS );
        /*v*/ BufferedReader      reader = null;

        try {
            reader = new BufferedReader( new FileReader( fileName ) );
            for ( String line; null != ( line = reader.readLine() );  ) {
                parseLine( line, result );
            }
        } catch ( final IOException x ) {
            throw new RuntimeException( "Oops: " + x, x );
        } finally {
            if ( null != reader ) try {
                reader.close();
            } catch ( final IOException x2 ) {
                System.err.println( "Could not close " + fileName + " - " + x2 );
            }
        }

        return result;
    }

    private static void parseLine( final String line, final Map<String, Object> map ) {
        if ( "".equals( line.trim() ) || line.startsWith( "#" ) || line.startsWith( ";" ) )
            return;

        final Matcher matcher = LINE_PATTERN.matcher( line );

        if ( ! matcher.matches() ) {
            System.err.println( "Bad config line: " + line );
            return;
        }

        final String key   = matcher.group( 1 ).trim().toLowerCase();
        final String value = matcher.group( 2 ).trim();

        if ( "".equals( value ) ) {
            map.put( key, true );
        } else if ( -1 == value.indexOf( ',' ) ) {
            map.put( key, value );
        } else {
            final String[] values = value.split( "," );

            for ( int i = 0; i < values.length; i++ ) {
                values[ i ] = values[ i ].trim();
            }
            map.put( key, Arrays.asList( values ) );
        }
    }
}

```

### java_code_2.txt
```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class ConfigReader {
    private static final Pattern LINE_PATTERN = Pattern.compile("([^ =]+)[ =]?(.*)");

    public static void main(final String[] args) throws IOException {
        System.out.println(parseFile(args[0]));
    }

    public static Map<String, Object> parseFile(final String fileName) throws IOException {
        final Map<String, Object> result = new HashMap<>();
        result.put("needspeeling", false);
        result.put("seedsremoved", false);
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            result.putAll(reader.lines()
                .filter(line -> !"".equals(line.trim()) && !line.startsWith("#") && !line.startsWith(";"))
                .map(LINE_PATTERN::matcher)
                .filter(Matcher::matches)
                .collect(Collectors.toMap(matcher -> matcher.group(1).trim().toLowerCase(), matcher -> {
                    final String value = matcher.group(2).trim();
                    if ("".equals(value)) {
                        return true;
                    } else if (-1 == value.indexOf(',')) {
                        return value;
                    }
                    return Arrays.asList(value.split(",")).stream().map(String::trim).collect(Collectors.toList());
                }))
            );
        }

        return result;
    }
}

```

## Python Code
### python_code_1.txt
```python
def readconf(fn):
    ret = {}
    with file(fn) as fp:
        for line in fp:
            # Assume whitespace is ignorable
            line = line.strip()
            if not line or line.startswith('#'): continue
            
            boolval = True
            # Assume leading ";" means a false boolean
            if line.startswith(';'):
                # Remove one or more leading semicolons
                line = line.lstrip(';')
                # If more than just one word, not a valid boolean
                if len(line.split()) != 1: continue
                boolval = False
            
            bits = line.split(None, 1)
            if len(bits) == 1:
                # Assume booleans are just one standalone word
                k = bits[0]
                v = boolval
            else:
                # Assume more than one word is a string value
                k, v = bits
            ret[k.lower()] = v
    return ret


if __name__ == '__main__':
    import sys
    conf = readconf(sys.argv[1])
    for k, v in sorted(conf.items()):
        print k, '=', v

```

