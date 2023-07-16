# Rosetta Code/Fix code tags

## Task Link
[Rosetta Code - Rosetta Code/Fix code tags](https://rosettacode.org/wiki/Rosetta_Code/Fix_code_tags)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;

public class FixCodeTags 
{
	public static void main(String[] args)
	{
		String sourcefile=args[0];
		String convertedfile=args[1];
		convert(sourcefile,convertedfile);
	}
		static String[] languages = {"abap", "actionscript", "actionscript3",
			"ada", "apache", "applescript", "apt_sources", "asm", "asp",
			"autoit", "avisynth", "bar", "bash", "basic4gl", "bf",
			"blitzbasic", "bnf", "boo", "c", "caddcl", "cadlisp", "cfdg",
			"cfm", "cil", "c_mac", "cobol", "cpp", "cpp-qt", "csharp", "css",
			"d", "delphi", "diff", "_div", "dos", "dot", "eiffel", "email",
			"foo", "fortran", "freebasic", "genero", "gettext", "glsl", "gml",
			"gnuplot", "go", "groovy", "haskell", "hq9plus", "html4strict",
			"idl", "ini", "inno", "intercal", "io", "java", "java5",
			"javascript", "kixtart", "klonec", "klonecpp", "latex", "lisp",
			"lolcode", "lotusformulas", "lotusscript", "lscript", "lua",
			"m68k", "make", "matlab", "mirc", "modula3", "mpasm", "mxml",
			"mysql", "nsis", "objc", "ocaml", "ocaml-brief", "oobas",
			"oracle11", "oracle8", "pascal", "per", "perl", "php", "php-brief",
			"pic16", "pixelbender", "plsql", "povray", "powershell",
			"progress", "prolog", "providex", "python", "qbasic", "rails",
			"reg", "robots", "ruby", "sas", "scala", "scheme", "scilab",
			"sdlbasic", "smalltalk", "smarty", "sql", "tcl", "teraterm",
			"text", "thinbasic", "tsql", "typoscript", "vb", "vbnet",
			"verilog", "vhdl", "vim", "visualfoxpro", "visualprolog",
			"whitespace", "winbatch", "xml", "xorg_conf", "xpp", "z80"};
	static void convert(String sourcefile,String convertedfile)
	{
		try
		{
			BufferedReader br=new BufferedReader(new FileReader(sourcefile));
			//String buffer to store contents of the file
			StringBuffer sb=new StringBuffer("");
			String line;
			while((line=br.readLine())!=null)
			{
				for(int i=0;i<languages.length;i++)
				{
					String lang=languages[i];
					line=line.replaceAll("<"+lang+">", "<lang "+lang+">");
					line=line.replaceAll("</"+lang+">", "</"+"lang>");
					line=line.replaceAll("<code "+lang+">", "<lang "+lang+">");
					line=line.replaceAll("</code>", "</"+"lang>");
				}
				sb.append(line);
			}
			br.close();
			
			FileWriter fw=new FileWriter(new File(convertedfile));
			//Write entire string buffer into the file
			fw.write(sb.toString());
			fw.close();
		}
		catch (Exception e)
		{
			System.out.println("Something went horribly wrong: "+e.getMessage());
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
""" Rosetta Code task rosettacode.org/wiki/Rosetta_Code/Fix_code_tags """

from re import sub

testtexts = [
"""<lang AutoHotkey>; usage: > fixtags.ahk input.txt ouput.txt
FileRead, text, %1%
langs = ada,awk,autohotkey,etc
slang = /lang
slang := "<" . slang . "/>"
Loop, Parse, langs, `,
{
  tag1 = <%A_LoopField%>
  tag2 = </%A_LoopField%>
  text := RegExReplace(text, tag1, "<lang " . A_LoopField . ">")
  text := RegExReplace(text, tag2, slang)
  text := RegExReplace(text, "<code (.+?)>(.*?)</code>"
          , "<lang $1>$2" . slang)
}
FileAppend, % text, %2%
</lang>""",
    """<lang perl>my @langs = qw(ada cpp-qt pascal lscript z80 visualprolog
html4strict cil objc asm progress teraterm hq9plus genero tsql
email pic16 tcl apt_sources io apache vhdl avisynth winbatch
vbnet ini scilab ocaml-brief sas actionscript3 qbasic perl bnf
cobol powershell php kixtart visualfoxpro mirc make javascript
cpp sdlbasic cadlisp php-brief rails verilog xml csharp
actionscript nsis bash typoscript freebasic dot applescript
haskell dos oracle8 cfdg glsl lotusscript mpasm latex sql klonec
ruby ocaml smarty python oracle11 caddcl robots groovy smalltalk
diff fortran cfm lua modula3 vb autoit java text scala
lotusformulas pixelbender reg _div whitespace providex asp css
lolcode lisp inno mysql plsql matlab oobas vim delphi xorg_conf
gml prolog bf per scheme mxml d basic4gl m68k gnuplot idl abap
intercal c_mac thinbasic java5 xpp boo klonecpp blitzbasic eiffel
povray c gettext);

my $text = join "", <STDIN>;
my $slang="/lang";
for (@langs) {
    $text =~ s|<$_>|<lang $_>|g;
    $text =~ s|</$_>|<$slang>|g;
}

$text =~ s|<code (.+?)>(.*?)</code>|<lang $1>$2<$slang>|sg;

print $text;</lang>""",
    """<lang>HAI 1.3

I HAS A bottles ITZ 99 I HAS A plural ITZ "Z" I HAS A lyric ITZ "99 BOTTLZ OV BEER"

IM IN YR song

   VISIBLE lyric " ON TEH WALL"
   VISIBLE lyric
   VISIBLE "TAEK 1 DOWN, PAZ IT AROUN"
   bottles R DIFF OF bottles AN 1
   NOT bottles, O RLY?
       YA RLY, VISIBLE "NO MOAR BOTTLZ OV BEER ON TEH WALL", GTFO
   OIC
   BOTH SAEM bottles AN 1, O RLY?
       YA RLY, plural R ""
   OIC
   lyric R SMOOSH bottles " BOTTL" plural " OV BEER" MKAY
   VISIBLE lyric " ON TEH WALL:)"
IM OUTTA YR song

KTHXBYE</lang>
"""]

for txt in testtexts:
    text2 = sub(r'<lang\s+\"?([\w\d\s]+)\"?\s?>', r'<syntaxhighlight lang=\1>', txt)
    text2 = sub(r'<lang\s*>', r'<syntaxhighlight lang=text>', text2)
    text2 = sub(r'</lang\s*>', r'

```

### python_code_2.txt
```python
import "./pattern" for Pattern

var source1 = """
<lang AutoHotkey>; usage: > fixtags.ahk input.txt ouput.txt
FileRead, text, %1%
langs = ada,awk,autohotkey,etc
slang = /lang
slang := "<" . slang . "/>"
Loop, Parse, langs, `,
{
  tag1 = <%A_LoopField%>
  tag2 = </%A_LoopField%>
  text := RegExReplace(text, tag1, "<lang " . A_LoopField . ">")
  text := RegExReplace(text, tag2, slang)
  text := RegExReplace(text, "<code (.+?)>(.*?)</code>"
          , "<lang $1>$2" . slang)
}
FileAppend, % text, %2%
</lang>
"""

var source2 = """
<lang perl>my @langs = qw(ada cpp-qt pascal lscript z80 visualprolog
html4strict cil objc asm progress teraterm hq9plus genero tsql
email pic16 tcl apt_sources io apache vhdl avisynth winbatch
vbnet ini scilab ocaml-brief sas actionscript3 qbasic perl bnf
cobol powershell php kixtart visualfoxpro mirc make javascript
cpp sdlbasic cadlisp php-brief rails verilog xml csharp
actionscript nsis bash typoscript freebasic dot applescript
haskell dos oracle8 cfdg glsl lotusscript mpasm latex sql klonec
ruby ocaml smarty python oracle11 caddcl robots groovy smalltalk
diff fortran cfm lua modula3 vb autoit java text scala
lotusformulas pixelbender reg _div whitespace providex asp css
lolcode lisp inno mysql plsql matlab oobas vim delphi xorg_conf
gml prolog bf per scheme mxml d basic4gl m68k gnuplot idl abap
intercal c_mac thinbasic java5 xpp boo klonecpp blitzbasic eiffel
povray c gettext);

my $text = join "", <STDIN>;
my $slang="/lang";
for (@langs) {
    $text =~ s|<$_>|<lang $_>|g;
    $text =~ s|</$_>|<$slang>|g;
}

$text =~ s|<code (.+?)>(.*?)</code>|<lang $1>$2<$slang>|sg;

print $text;</lang>
"""

var source3 = """
<lang>HAI 1.3

I HAS A bottles ITZ 99 I HAS A plural ITZ "Z" I HAS A lyric ITZ "99 BOTTLZ OV BEER"

IM IN YR song

   VISIBLE lyric " ON TEH WALL"
   VISIBLE lyric
   VISIBLE "TAEK 1 DOWN, PAZ IT AROUN"
   bottles R DIFF OF bottles AN 1
   NOT bottles, O RLY?
       YA RLY, VISIBLE "NO MOAR BOTTLZ OV BEER ON TEH WALL", GTFO
   OIC
   BOTH SAEM bottles AN 1, O RLY?
       YA RLY, plural R ""
   OIC
   lyric R SMOOSH bottles " BOTTL" plural " OV BEER" MKAY
   VISIBLE lyric " ON TEH WALL:)"
IM OUTTA YR song

KTHXBYE</lang>
"""

var p = Pattern.new("<lang [+1^>]>")
var sh = "syntaxhighlight"
var repl = "<%(sh) lang=\"$1\">"
for (source in [source1, source2, source3]) {
    source = p.replace(source, repl, 1, 0).
             replace("<lang>", "<%(sh) lang=\"text\">").
             replace("</lang>", "</%(sh)>")
    System.print(source)
    System.print()
}

```

