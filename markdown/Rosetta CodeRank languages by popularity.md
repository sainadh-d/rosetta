# Rosetta Code/Rank languages by popularity

## Task Link
[Rosetta Code - Rosetta Code/Rank languages by popularity](https://rosettacode.org/wiki/Rosetta_Code/Rank_languages_by_popularity)

## Java Code
### java_code_1.txt
```java
import  java.net.URL;
import  java.net.URLConnection;
import  java.io.*;
import  java.util.*;

public class GetRCLanguages
{
    // Custom sort Comparator for sorting the language list
    // assumes the first character is the page count and the rest is the language name
    private static class LanguageComparator implements Comparator<String>
    {
        public int compare( String a, String b )
        {
            // as we "know" we will be comparaing languages, we will assume the Strings have the appropriate format
            int result = ( b.charAt( 0 ) - a.charAt( 0 ) );
            if( result == 0 )
            {
                // the counts are the same - compare the names
                result = a.compareTo( b );
            } // if result == 0
        return result;
        } // compare
    } // LanguageComparator

    // get the string following marker in text
    private static String after( String text, int marker )
    {
        String result = "";
        int    pos    = text.indexOf( marker );
        if( pos >= 0 )
        {
            // the marker is in the string
            result = text.substring( pos + 1 );
        } // if pos >= 0
    return result;
    } // after

    // read and parse the content of path
    // results returned in gcmcontinue and languageList
    public static void parseContent( String path
                                   , String[] gcmcontinue
                                   , ArrayList<String> languageList
                                   )
    {
        try
        {

            URL            url = new URL( path );
            URLConnection  rc  = url.openConnection();
            // Rosetta Code objects to the default Java user agant so use a blank one
            rc.setRequestProperty( "User-Agent", "" );
            BufferedReader bfr = new BufferedReader( new InputStreamReader( rc.getInputStream() ) );
    
            gcmcontinue[0]      = "";
            String languageName = "?";
            String line         = bfr.readLine();
            while( line != null )
            {
                line = line.trim();
                if     ( line.startsWith( "[title]" ) )
                {
                    // have a programming language - should look like "[title] => Category:languageName"
                    languageName = after( line, ':' ).trim();
                }
                else if( line.startsWith( "[pages]" ) )
                {
                    // number of pages the language has (probably)
                    String pageCount = after( line, '>' ).trim();
                    if( pageCount.compareTo( "Array" ) != 0 )
                    {
                        // haven't got "[pages] => Array" - must be a number of pages
                        languageList.add( ( (char) Integer.parseInt( pageCount ) ) + languageName );
                        languageName = "?";
                    } // if [pageCount.compareTo( "Array" ) != 0
                }
                else if( line.startsWith( "[gcmcontinue]" ) )
                {
                    // have an indication of wether there is more data or not
                    gcmcontinue[0] = after( line, '>' ).trim();
                } // if various line starts
                line = bfr.readLine();
            } // while line != null
            bfr.close();
        }
        catch( Exception e )
        {
            e.printStackTrace();
        } // try-catch
    } // parseContent

    public static void main( String[] args )
    {
        // get the languages
        ArrayList<String> languageList = new ArrayList<String>( 1000 );
        String[]          gcmcontinue  = new String[1];
        gcmcontinue[0]                 = "";
        do
        {
            String path = ( "http://www.rosettacode.org/mw/api.php?action=query"
                          + "&generator=categorymembers"
                          + "&gcmtitle=Category:Programming%20Languages"
                          + "&gcmlimit=500"
                          + ( gcmcontinue[0].compareTo( "" ) == 0 ? "" : ( "&gcmcontinue=" + gcmcontinue[0] ) )
                          + "&prop=categoryinfo"
                          + "&format=txt"
                          );
            parseContent( path, gcmcontinue, languageList );
        }
        while( gcmcontinue[0].compareTo( "" ) != 0 );
        // sort the languages
        String[] languages = languageList.toArray(new String[]{});
        Arrays.sort( languages, new LanguageComparator() );
        // print the languages
        int    lastTie    = -1;
        int    lastCount  = -1;
        for( int lPos = 0; lPos < languages.length; lPos ++ )
        {
            int    count = (int) ( languages[ lPos ].charAt( 0 ) );
            System.out.format( "%4d: %4d: %s\n"
                             , 1 + ( count == lastCount ? lastTie : lPos )
                             , count
                             , languages[ lPos ].substring( 1 )
                             );
            if( count != lastCount )
            {
                lastTie   = lPos;
                lastCount = count;
            } // if count != lastCount
        } // for lPos
    } // main
} // GetRCLanguages

```

## Python Code
### python_code_1.txt
```python
import requests
import re

response = requests.get("http://rosettacode.org/wiki/Category:Programming_Languages").text
languages = re.findall('title="Category:(.*?)">',response)[:-3] # strip last 3

response = requests.get("http://rosettacode.org/mw/index.php?title=Special:Categories&limit=5000").text
response = re.sub('(\d+),(\d+)',r'\1'+r'\2',response)           # strip ',' from popular languages above 999 members
members  = re.findall('<li><a[^>]+>([^<]+)</a>[^(]*[(](\\d+) member[s]*[)]</li>',response) # find language and members

for cnt, (language, members) in enumerate(sorted(members, key=lambda x: -int(x[1]))[:15]): # show only top 15 languages
    if language in languages:
        print("{:4d} {:4d} - {}".format(cnt+1, int(members), language))

```

### python_code_2.txt
```python
import requests
import operator
import re

api_url    = 'http://rosettacode.org/mw/api.php'
languages  = {}

parameters = {
    'format':       'json',
    'action':       'query',
    'generator':    'categorymembers',
    'gcmtitle':     'Category:Programming Languages',
    'gcmlimit':     '200',
    'gcmcontinue':  '',
    'continue':     '',
    'prop':         'categoryinfo'
}

while(True):
    response = requests.get(api_url, params=parameters).json()
    for k,v in response['query']['pages'].items():
        if 'title' in v and 'categoryinfo' in v:
          languages[v['title']]=v['categoryinfo']['size']
    if 'continue' in response:
        gcmcontinue = response['continue']['gcmcontinue']
#        print(gcmcontinue)
        parameters.update({'gcmcontinue': gcmcontinue})
    else:
        break

# report top 15 languages                        
for i, (language, size) in enumerate(sorted(languages.items(), key=operator.itemgetter(1), reverse=True)[:15]):
    print("{:4d} {:4d} - {}".format(i+1, size, re.sub('Category:','',language))) # strip Category: from language

```

