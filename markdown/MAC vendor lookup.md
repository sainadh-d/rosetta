# MAC vendor lookup

## Task Link
[Rosetta Code - MAC vendor lookup](https://rosettacode.org/wiki/MAC_vendor_lookup)

## Java Code
### java_code_1.txt
```java
package com.jamesdonnell.MACVendor;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

/** MAC Vendor Lookup class.
 * www.JamesDonnell.com
 * @author James A. Donnell Jr. */
public class Lookup {
	/** Base URL for API. The API from www.macvendors.com was chosen. */
	private static final String baseURL = "http://api.macvendors.com/";

	/** Performs lookup on MAC address(es) supplied in arguments.
	 * @param args MAC address(es) to lookup. */
	public static void main(String[] args) {
		for (String arguments : args)
			System.out.println(arguments + ": " + get(arguments));
	}

	/** Performs lookup on supplied MAC address.
	 * @param macAddress MAC address to lookup.
	 * @return Manufacturer of MAC address. */
	private static String get(String macAddress) {
		try {
			StringBuilder result = new StringBuilder();
			URL url = new URL(baseURL + macAddress);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");
			BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
			String line;
			while ((line = rd.readLine()) != null) {
				result.append(line);
			}
			rd.close();
			return result.toString();
		} catch (FileNotFoundException e) {
			// MAC not found
			return "N/A";
		} catch (IOException e) {
			// Error during lookup, either network or API.
			return null;
		}
	}
}

```

### java_code_2.txt
```java
 
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.List;
import java.util.concurrent.TimeUnit;

public final class MacVendorLookup {

	public static void main(String[] aArgs) throws InterruptedException, IOException {		
		for ( String macAddress : macAddresses ) {
			HttpResponse<String> response = getMacVendor(macAddress);
			System.out.println(macAddress + "  " + response.statusCode() + "  " + response.body());
			
			TimeUnit.SECONDS.sleep(2);
		}		
	}

	private static HttpResponse<String> getMacVendor(String aMacAddress) throws IOException, InterruptedException {				
		URI uri = URI.create(BASE_URL + aMacAddress);
		HttpClient client = HttpClient.newHttpClient();
		HttpRequest request = HttpRequest
			.newBuilder()
		    .uri(uri)
		    .header("accept", "application/json")
		    .GET()
		    .build();
		
		HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
		
		return response;
	}
	
	private static final String BASE_URL = "http://api.macvendors.com/";
	
	private static final List<String> macAddresses = List.of("88:53:2E:67:07:BE",
															 "D4:F4:6F:C9:EF:8D",
															 "FC:FB:FB:01:FA:21",
															 "4c:72:b9:56:fe:bc",
															 "00-14-22-01-23-45"
															 );	
	
}

```

## Python Code
### python_code_1.txt
```python
import requests

for addr in ['88:53:2E:67:07:BE', 'FC:FB:FB:01:FA:21',
        'D4:F4:6F:C9:EF:8D', '23:45:67']:
    vendor = requests.get('http://api.macvendors.com/' + addr).text
    print(addr, vendor)

```

