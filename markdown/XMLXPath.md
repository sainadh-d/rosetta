# XML/XPath

## Task Link
[Rosetta Code - XML/XPath](https://rosettacode.org/wiki/XML/XPath)

## Java Code
### java_code_1.txt
```java
import java.io.StringReader;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;

public class XMLParser {
	final static String xmlStr = 
			  "<inventory title=\"OmniCorp Store #45x10^3\">"
			+ "  <section name=\"health\">"
			+ "    <item upc=\"123456789\" stock=\"12\">"
			+ "      <name>Invisibility Cream</name>"
			+ "      <price>14.50</price>"
			+ "      <description>Makes you invisible</description>"
			+ "    </item>"
			+ "    <item upc=\"445322344\" stock=\"18\">"
			+ "      <name>Levitation Salve</name>"
			+ "      <price>23.99</price>"
			+ "      <description>Levitate yourself for up to 3 hours per application</description>"
			+ "    </item>"
			+ "  </section>"
			+ "  <section name=\"food\">"
			+ "    <item upc=\"485672034\" stock=\"653\">"
			+ "      <name>Blork and Freen Instameal</name>"
			+ "      <price>4.95</price>"
			+ "      <description>A tasty meal in a tablet; just add water</description>"
			+ "    </item>"
			+ "    <item upc=\"132957764\" stock=\"44\">"
			+ "      <name>Grob winglets</name>"
			+ "      <price>3.56</price>"
			+ "      <description>Tender winglets of Grob. Just add priwater</description>"
			+ "    </item>"
			+ "  </section>" 
			+ "</inventory>";

	public static void main(String[] args) {
		try {
			Document doc = DocumentBuilderFactory.newInstance()
					.newDocumentBuilder()
					.parse(new InputSource(new StringReader(xmlStr)));
			XPath xpath = XPathFactory.newInstance().newXPath();
			// 1
			System.out.println(((Node) xpath.evaluate(
					"/inventory/section/item[1]", doc, XPathConstants.NODE))
					.getAttributes().getNamedItem("upc"));
			// 2, 3
			NodeList nodes = (NodeList) xpath.evaluate(
					"/inventory/section/item/price", doc,
					XPathConstants.NODESET);
			for (int i = 0; i < nodes.getLength(); i++)
				System.out.println(nodes.item(i).getTextContent());
		} catch (Exception e) {
			System.out.println("Error ocurred while parsing XML.");
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
# Python has basic xml parsing built in

from xml.dom import minidom

xmlfile = file("test3.xml") # load xml document from file 
xmldoc = minidom.parse(xmlfile).documentElement # parse from file stream or...
xmldoc = minidom.parseString("<inventory title="OmniCorp Store #45x10^3">...</inventory>").documentElement # alternatively, parse a string
	
#  1st Task: Retrieve the first "item" element
i = xmldoc.getElementsByTagName("item") # get a list of all "item" tags
firstItemElement = i[0] # get the first element

# 2nd task: Perform an action on each "price" element (print it out)
for j in xmldoc.getElementsByTagName("price"): # get a list of all "price" tags
	print j.childNodes[0].data # XML Element . TextNode . data of textnode

# 3rd Task: Get an array of all the "name" elements
namesArray = xmldoc.getElementsByTagName("name")

```

### python_code_2.txt
```python
import xml.etree.ElementTree as ET

xml = open('inventory.xml').read()
doc = ET.fromstring(xml)

doc = ET.parse('inventory.xml')  # or load it directly

# Note, ElementTree's root is the top level element. So you need ".//" to really start searching from top

# Return first Item
item1 = doc.find("section/item")  # or ".//item"

# Print each price
for p in doc.findall("section/item/price"):  # or ".//price"
    print "{0:0.2f}".format(float(p.text))  # could raise exception on missing text or invalid float() conversion

# list of names
names = doc.findall("section/item/name")  # or ".//name"

```

### python_code_3.txt
```python
from lxml import etree

xml = open('inventory.xml').read()
doc = etree.fromstring(xml)

doc = etree.parse('inventory.xml')  # or load it directly

# Return first item
item1 = doc.xpath("//section[1]/item[1]")

# Print each price
for p in doc.xpath("//price"):
    print "{0:0.2f}".format(float(p.text))  # could raise exception on missing text or invalid float() conversion

names = doc.xpath("//name")  # list of names

```

