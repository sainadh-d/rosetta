# CSV to HTML translation

## Task Link
[Rosetta Code - CSV to HTML translation](https://rosettacode.org/wiki/CSV_to_HTML_translation)

## Java Code
### java_code_1.txt
```java
//  Create an HTML Table from comma seperated values
//  Nigel Galloway - June 2nd., 2013
grammar csv2html;
dialog : {System.out.println("<HTML><Table>");}header body+{System.out.println("</Table></HTML>");} ;
header : {System.out.println("<THEAD align=\"center\"><TR bgcolor=\"blue\">");}row{System.out.println("</TR></THEAD");};
body   : {System.out.println("<TBODY><TR>");}row{System.out.println("</TR></TBODY");};
row    : field ',' field '\r'? '\n';
field  : Field{System.out.println("<TD>" + $Field.text.replace("<","&lt;").replace(">","&gt;") + "</TD>");};
Field  : ~[,\n\r]+;

```

### java_code_2.txt
```java
String csv = "...";
// Use Collectors.joining(...) for streaming, otherwise StringJoiner
StringBuilder html = new StringBuilder("<table>\n");
Collector collector = Collectors.joining("</td><td>", "  <tr><td>", "</td></tr>\n");
for (String row : csv.split("\n") ) {
    html.append(Arrays.stream(row.split(",")).collect(collector));
}
html.append("</table>\n");

```

### java_code_3.txt
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintStream;

class Csv2Html {

	public static String escapeChars(String lineIn) {
		StringBuilder sb = new StringBuilder();
		int lineLength = lineIn.length();
		for (int i = 0; i < lineLength; i++) {
			char c = lineIn.charAt(i);
			switch (c) {
				case '"': 
					sb.append("&quot;");
					break;
				case '&':
					sb.append("&amp;");
					break;
				case '\'':
					sb.append("&apos;");
					break;
				case '<':
					sb.append("&lt;");
					break;
				case '>':
					sb.append("&gt;");
					break;
				default: sb.append(c);
			}
		}
		return sb.toString();
	}

	public static void tableHeader(PrintStream ps, String[] columns) {
		ps.print("<tr>");
		for (int i = 0; i < columns.length; i++) {
			ps.print("<th>");
			ps.print(columns[i]);
			ps.print("</th>");
		}
		ps.println("</tr>");
	}
	
	public static void tableRow(PrintStream ps, String[] columns) {
		ps.print("<tr>");
		for (int i = 0; i < columns.length; i++) {
			ps.print("<td>");
			ps.print(columns[i]);
			ps.print("</td>");
		}
		ps.println("</tr>");
	}
	
	public static void main(String[] args) throws Exception {
		boolean withTableHeader = (args.length != 0);
		
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		PrintStream stdout = System.out;
		
		stdout.println("<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">");
		stdout.println("<html xmlns=\"http://www.w3.org/1999/xhtml\">");
		stdout.println("<head><meta http-equiv=\"Content-type\" content=\"text/html;charset=UTF-8\"/>");
		stdout.println("<title>Csv2Html</title>");
		stdout.println("<style type=\"text/css\">");
		stdout.println("body{background-color:#FFF;color:#000;font-family:OpenSans,sans-serif;font-size:10px;}");
		stdout.println("table{border:0.2em solid #2F6FAB;border-collapse:collapse;}");
		stdout.println("th{border:0.15em solid #2F6FAB;padding:0.5em;background-color:#E9E9E9;}");
		stdout.println("td{border:0.1em solid #2F6FAB;padding:0.5em;background-color:#F9F9F9;}</style>");
		stdout.println("</head><body><h1>Csv2Html</h1>");

		stdout.println("<table>");
		String stdinLine;
		boolean firstLine = true;
		while ((stdinLine = br.readLine()) != null) {
			String[] columns = escapeChars(stdinLine).split(",");
			if (withTableHeader == true && firstLine == true) {
				tableHeader(stdout, columns);
				firstLine = false;
			} else {
				tableRow(stdout, columns);
			}
		}
		stdout.println("</table></body></html>");
	}
}

```

## Python Code
### python_code_1.txt
```python
csvtxt = '''\
Character,Speech
The multitude,The messiah! Show us the messiah!
Brians mother,<angry>Now you listen here! He's not the messiah; he's a very naughty boy! Now go away!</angry>
The multitude,Who are you?
Brians mother,I'm his mother; that's who!
The multitude,Behold his mother! Behold his mother!\
'''

from cgi import escape

def _row2tr(row, attr=None):
    cols = escape(row).split(',')
    return ('<TR>'
            + ''.join('<TD>%s</TD>' % data for data in cols)
            + '</TR>')

def csv2html(txt):
    htmltxt = '<TABLE summary="csv2html program output">\n'
    for rownum, row in enumerate(txt.split('\n')):
        htmlrow = _row2tr(row)
        htmlrow = '  <TBODY>%s</TBODY>\n' % htmlrow
        htmltxt += htmlrow
    htmltxt += '</TABLE>\n'
    return htmltxt

htmltxt = csv2html(csvtxt)
print(htmltxt)

```

### python_code_2.txt
```python
def _row2trextra(row, attr=None):
    cols = escape(row).split(',')
    attr_tr = attr.get('TR', '')
    attr_td = attr.get('TD', '')
    return (('<TR%s>' % attr_tr)
            + ''.join('<TD%s>%s</TD>' % (attr_td, data) for data in cols)
            + '</TR>')

def csv2htmlextra(txt, header=True, attr=None):
    ' attr is a dictionary mapping tags to attributes to add to that tag'
    
    attr_table = attr.get('TABLE', '')
    attr_thead = attr.get('THEAD', '')
    attr_tbody = attr.get('TBODY', '')
    htmltxt = '<TABLE%s>\n' % attr_table
    for rownum, row in enumerate(txt.split('\n')):
        htmlrow = _row2trextra(row, attr)
        rowclass = ('THEAD%s' % attr_thead) if (header and rownum == 0) else ('TBODY%s' % attr_tbody)
        htmlrow = '  <%s>%s</%s>\n' % (rowclass, htmlrow, rowclass[:5])
        htmltxt += htmlrow
    htmltxt += '</TABLE>\n'
    return htmltxt

htmltxt = csv2htmlextra(csvtxt, True,
                        dict(TABLE=' border="1" summary="csv2html extra program output"',
                             THEAD=' bgcolor="yellow"',
                             TBODY=' bgcolor="orange"' 
                             )
                        )
print(htmltxt)

```

### python_code_3.txt
```python
from csv import DictReader
from xml.etree import ElementTree as ET

def csv2html_robust(txt, header=True, attr=None):
    # Use DictReader because, despite what the docs say, reader() doesn't
    # return an object with .fieldnames
    # (DictReader expects an iterable that returns lines, so split on \n)
    reader = DictReader(txt.split('\n'))

    table = ET.Element("TABLE", **attr.get('TABLE', {}))
    thead_tr = ET.SubElement(
        ET.SubElement(table, "THEAD", **attr.get('THEAD', {})),
        "TR")
    tbody = ET.SubElement(table, "TBODY", **attr.get('TBODY', {}))

    if header:
        for name in reader.fieldnames:
            ET.SubElement(thead_tr, "TD").text = name

    for row in reader:
        tr_elem = ET.SubElement(tbody, "TR", **attr.get('TR', {}))

        # Use reader.fieldnames to query `row` in the correct order.
        # (`row` isn't an OrderedDict prior to Python 3.6)
        for field in reader.fieldnames:
            td_elem = ET.SubElement(tr_elem, "TD", **attr.get('TD', {}))
            td_elem.text = row[field]

    return ET.tostring(table, method='html')

htmltxt = csv2html_robust(csvtxt, True, {
    'TABLE': {'border': "1", 'summary': "csv2html extra program output"},
    'THEAD': {'bgcolor': "yellow"},
    'TBODY': {'bgcolor': "orange"}
})

print(htmltxt.decode('utf8'))

```

