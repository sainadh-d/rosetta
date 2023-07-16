# Web scraping

## Task Link
[Rosetta Code - Web scraping](https://rosettacode.org/wiki/Web_scraping)

## Java Code
### java_code_1.txt
```java
String scrapeUTC() throws URISyntaxException, IOException {
    String address = "http://tycho.usno.navy.mil/cgi-bin/timer.pl";
    URL url = new URI(address).toURL();
    try (BufferedReader reader = new BufferedReader(new InputStreamReader(url.openStream()))) {
        Pattern pattern = Pattern.compile("^.+? UTC");
        Matcher matcher;
        String line;
        while ((line = reader.readLine()) != null) {
            matcher = pattern.matcher(line);
            if (matcher.find())
                return matcher.group().replaceAll("<.+?>", "");
        }
    }
    return null;
}

```

### java_code_2.txt
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;

public final class WebScraping {
	
    public static void main(String[] aArgs) {
	    try {
	        URI uri = new URI("https://www.rosettacode.org/wiki/Talk:Web_scraping").parseServerAuthority();	      
	        URL address = uri.toURL();
	        HttpURLConnection connection = (HttpURLConnection) address.openConnection();
	        BufferedReader reader = new BufferedReader( new InputStreamReader(connection.getInputStream()) );
	        
	        final int responseCode = connection.getResponseCode();
	        System.out.println("Response code: " + responseCode);
	        
	        String line;
	        while ( ! ( line = reader.readLine() ).contains("UTC") ) {
	        	/* Empty block */
	        }
	        
	        final int index = line.indexOf("UTC");	        
	        System.out.println(line.substring(index - 16, index + 4));
	        
	        reader.close();
	        connection.disconnect();
	    } catch (IOException ioe) {
	        System.err.println("Error connecting to server: " + ioe.getCause());
	    } catch (URISyntaxException use) {
	    	System.err.println("Unable to connect to URI: " + use.getCause());
		} 
	}
    
}

```

## Python Code
### python_code_1.txt
```python
import urllib
page = urllib.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl')
for line in page:
    if ' UTC' in line:
        print line.strip()[4:]
        break
page.close()

```

