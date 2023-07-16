# Distance and Bearing

## Task Link
[Rosetta Code - Distance and Bearing](https://rosettacode.org/wiki/Distance_and_Bearing)

## Java Code
### java_code_1.txt
```java
// The Airport class holds each airport object
package distanceAndBearing;
public class Airport {
	private String airport;
	private String country;
	private String icao;
	private double lat;
	private double lon;
	public String getAirportName() {	return this.airport;	}
	public void setAirportName(String airport) {	this.airport = airport; }
	public String getCountry() {	return this.country;	}
	public void setCountry(String country) {	this.country = country;	}
	public String getIcao() { return this.icao; }
	public void setIcao(String icao) { this.icao = icao;	}
	public double getLat() {	return this.lat; }
	public void setLat(double lat) {	this.lat = lat;	}
	public double getLon() {	return this.lon; }
	public void setLon(double lon) {	this.lon = lon;	}
	@Override
	public String toString() {return "Airport: " + getAirportName() + ": ICAO: " + getIcao();}
}

// The DistanceAndBearing class does all the work.
package distanceAndBearing;
import java.io.File;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;
public class DistanceAndBearing {
	private final double earthRadius = 6371;
	private File datFile;
	private List<Airport> airports;
	public DistanceAndBearing() { this.airports = new ArrayList<Airport>(); }
	public boolean readFile(String filename) {
		this.datFile = new File(filename);
		try {
			Scanner fileScanner = new Scanner(datFile);
			String line;
			while (fileScanner.hasNextLine()) {
				line = fileScanner.nextLine();
				line = line.replace(", ", "; "); // There are some commas in airport names in the dat
													// file
				line = line.replace(",\",\"", "\",\""); // There are some airport names that
														// end in a comma in the dat file
				String[] parts = line.split(",");
				Airport airport = new Airport();
				airport.setAirportName(parts[1].replace("\"", "")); // Remove the double quotes from the string
				airport.setCountry(parts[3].replace("\"", "")); // Remove the double quotes from the string
				airport.setIcao(parts[5].replace("\"", "")); // Remove the double quotes from the string
				airport.setLat(Double.valueOf(parts[6]));
				airport.setLon(Double.valueOf(parts[7]));
				this.airports.add(airport);
			}
			fileScanner.close();
			return true; // Return true if the read was successful
		} catch (Exception e) {
			e.printStackTrace();
			return false; // Return false if the read was not successful
		}}
	public double[] calculate(double lat1, double lon1, double lat2, double lon2) {
		double[] results = new double[2];
		double dLat = Math.toRadians(lat2 - lat1);
		double dLon = Math.toRadians(lon2 - lon1);
		double rlat1 = Math.toRadians(lat1);
		double rlat2 = Math.toRadians(lat2);
		double a = Math.pow(Math.sin(dLat / 2), 2)
				+ Math.pow(Math.sin(dLon / 2), 2) * Math.cos(rlat1) * Math.cos(rlat2);
		double c = 2 * Math.asin(Math.sqrt(a));
		double distance = earthRadius * c;
		DecimalFormat df = new DecimalFormat("#0.00");
		distance = Double.valueOf(df.format(distance));
		results[0] = distance;
		double X = Math.cos(rlat2) * Math.sin(dLon);
		double Y = Math.cos(rlat1) * Math.sin(rlat2) - Math.sin(rlat1) * Math.cos(rlat2) * Math.cos(dLon);
		double heading = Math.atan2(X, Y);
		heading = Math.toDegrees(heading);
		results[1] = heading;
		return results;
	}
	public Airport searchByName(final String name) {
		Airport airport = new Airport();
		List<Airport> results = this.airports.stream().filter(ap -> ap.getAirportName().contains(name))
				.collect(Collectors.toList());
		airport = results.get(0);
		return airport;
	}
	public List<Airport> findClosestAirports(double lat, double lon) {
		// TODO Auto-generated method stub
		Map<Double, Airport> airportDistances = new HashMap<>();
		Map<Double, Airport> airportHeading = new HashMap<>();
		List<Airport> closestAirports = new ArrayList<Airport>();
		// This loop finds the distance and heading for every airport and saves them
		// into two separate Maps
		for (Airport ap : this.airports) {
			double[] result = calculate(lat, lon, ap.getLat(), ap.getLon());
			airportDistances.put(result[0], ap);
			airportHeading.put(result[1], ap);
		}
		// Get the keyset from the distance map and sort it.
		ArrayList<Double> distances = new ArrayList<>(airportDistances.keySet());
		Collections.sort(distances);
		// Get the first 20 airports by finding the value in the distance map for
		// each distance in the sorted Arraylist. Then get the airport name, and
		// use that to search for the airport in the airports List.
		// Save that into a new List
		for (int i = 0; i < 20; i++) { closestAirports.add(searchByName((airportDistances.get(distances.get(i)).getAirportName())));}
		// Find the distance and heading for each of the top 20 airports.
		Map<String, Double> distanceMap = new HashMap<>();
		for (Double d : airportDistances.keySet()) {	distanceMap.put(airportDistances.get(d).getAirportName(), d);}
		Map<String, Double> headingMap = new HashMap<>();
		for (Double d : airportHeading.keySet()) { 
            double d2 = d;
            if(d2<0){d2+=360'}
            headingMap.put(airportHeading.get(d).getAirportName(), d2); }

		// Print the results.
		System.out.printf("%-4s %-40s %-25s %-6s %12s %15s\n", "Num", "Airport", "Country", "ICAO", "Distance", "Bearing");
		System.out.println("-----------------------------------------------------------------------------------------------------------");
		int i = 0;
		for (Airport a : closestAirports) {
			System.out.printf("%-4s %-40s %-25s %-6s %12.1f %15.0f\n", ++i, a.getAirportName(), a.getCountry(), a.getIcao(), distanceMap.get(a.getAirportName())*0.5399568, headingMap.get(a.getAirportName()));
		}
		return closestAirports;
	}
}

```

### java_code_2.txt
```java
import distanceAndBearing.DistanceAndBearing;
public class MyClass {

	public static void main(String[] args) {
		DistanceAndBearing dandb = new DistanceAndBearing();
		dandb.readFile("airports.txt");
		dandb.findClosestAirports(51.514669,2.198581);
	}
}

```

## Python Code
### python_code_1.txt
```python
''' Rosetta Code task Distance_and_Bearing '''

from math import radians, degrees, sin, cos, asin, atan2, sqrt
from pandas import read_csv


EARTH_RADIUS_KM = 6372.8
TASK_CONVERT_NM =  0.0094174
AIRPORT_DATA_FILE = 'airports.dat.txt'

QUERY_LATITUDE, QUERY_LONGITUDE = 51.514669, 2.198581


def haversine(lat1, lon1, lat2, lon2):
    '''
    Given two latitude, longitude pairs in degrees for two points on the Earth,
    get distance (nautical miles) and initial direction of travel (degrees)
    for travel from lat1, lon1 to lat2, lon2
    '''
    rlat1, rlon1, rlat2, rlon2 = [radians(x) for x in [lat1, lon1, lat2, lon2]]
    dlat = rlat2 - rlat1
    dlon = rlon2 - rlon1
    arc = sin(dlat / 2) ** 2 + cos(rlat1) * cos(rlat2) * sin(dlon / 2) ** 2
    clen = 2.0 * degrees(asin(sqrt(arc)))
    theta = atan2(sin(dlon) * cos(rlat2),
                  cos(rlat1) * sin(rlat2) - sin(rlat1) * cos(rlat2) * cos(dlon))
    theta = (degrees(theta) + 360) % 360
    return EARTH_RADIUS_KM * clen * TASK_CONVERT_NM, theta


def find_nearest_airports(latitude, longitude, wanted=20, csv=AIRPORT_DATA_FILE):
    ''' Given latitude and longitude, find `wanted` closest airports in database file csv. '''
    airports = read_csv(csv, header=None, usecols=[1, 3, 5, 6, 7], names=[
                        'Name', 'Country', 'ICAO', 'Latitude', 'Longitude'])
    airports['Distance'] = 0.0
    airports['Bearing'] = 0
    for (idx, row) in enumerate(airports.itertuples()):
        distance, bearing = haversine(
            latitude, longitude, row.Latitude, row.Longitude)
        airports.at[idx, 'Distance'] = round(distance, ndigits=1)
        airports.at[idx, 'Bearing'] = int(round(bearing))

    airports.sort_values(by=['Distance'], ignore_index=True, inplace=True)
    return airports.loc[0:wanted-1, ['Name', 'Country', 'ICAO', 'Distance', 'Bearing']]


print(find_nearest_airports(QUERY_LATITUDE, QUERY_LONGITUDE))

```

