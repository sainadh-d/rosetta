# Abbreviations, simple

## Task Link
[Rosetta Code - Abbreviations, simple](https://rosettacode.org/wiki/Abbreviations,_simple)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class Abbreviations {
    public static void main(String[] args) {
        CommandList commands = new CommandList(commandTable);
        String input = "riG   rePEAT copies  put mo   rest    types   fup.    6       poweRin";
        System.out.println(" input: " + input);
        System.out.println("output: " + test(commands, input));
    }

    private static String test(CommandList commands, String input) {
        StringBuilder output = new StringBuilder();
        Scanner scanner = new Scanner(input);
        while (scanner.hasNext()) {
            String word = scanner.next();
            if (output.length() > 0)
                output.append(' ');
            Command cmd = commands.findCommand(word);
            if (cmd != null)
                output.append(cmd.cmd);
            else
                output.append("*error*");
        }
        return output.toString();
    }

    private static String commandTable =
        "add 1  alter 3  backup 2  bottom 1  Cappend 2  change 1  Schange  Cinsert 2  Clast 3 " +
        "compress 4 copy 2 count 3 Coverlay 3 cursor 3  delete 3 Cdelete 2  down 1  duplicate " +
        "3 xEdit 1 expand 3 extract 3  find 1 Nfind 2 Nfindup 6 NfUP 3 Cfind 2 findUP 3 fUP 2 " +
        "forward 2  get  help 1 hexType 4  input 1 powerInput 3  join 1 split 2 spltJOIN load " +
        "locate 1 Clocate 2 lowerCase 3 upperCase 3 Lprefix 2  macro  merge 2 modify 3 move 2 " +
        "msg  next 1 overlay 1 parse preserve 4 purge 3 put putD query 1 quit  read recover 3 " +
        "refresh renum 3 repeat 3 replace 1 Creplace 2 reset 3 restore 4 rgtLEFT right 2 left " +
        "2  save  set  shift 2  si  sort  sos  stack 3 status 4 top  transfer 3  type 1  up 1";

    private static class Command {
        private Command(String cmd, int minLength) {
             this.cmd = cmd;
             this.minLength = minLength;
        }
        private boolean match(String str) {
            int olen = str.length();
            return olen >= minLength && olen <= cmd.length()
                && cmd.regionMatches(true, 0, str, 0, olen);
        }
        private String cmd;
        private int minLength;
    }

    private static Integer parseInteger(String word) {
        try {
            return Integer.valueOf(word);
        } catch (NumberFormatException ex) {
            return null;
        }
    }

    private static class CommandList {
        private CommandList(String table) {
            Scanner scanner = new Scanner(table);
            List<String> words = new ArrayList<>();
            while (scanner.hasNext()) {
                String word = scanner.next();
                words.add(word.toUpperCase());
            }
            for (int i = 0, n = words.size(); i < n; ++i) {
                String word = words.get(i);
                // if there's an integer following this word, it specifies the minimum
                // length for the command, otherwise the minimum length is the length
                // of the command string
                int len = word.length();
                if (i + 1 < n) {
                    Integer number = parseInteger(words.get(i + 1));
                    if (number != null) {
                        len = number.intValue();
                        ++i;
                    }
                }
                commands.add(new Command(word, len));
            }
        }
        private Command findCommand(String word) {
            for (Command command : commands) {
                if (command.match(word))
                    return command;
            }
            return null;
        }
        private List<Command> commands = new ArrayList<>();
    }
}

```

## Python Code
### python_code_1.txt
```python
command_table_text = """add 1  alter 3  backup 2  bottom 1  Cappend 2  change 1  Schange  Cinsert 2  Clast 3
   compress 4 copy 2 count 3 Coverlay 3 cursor 3  delete 3 Cdelete 2  down 1  duplicate
   3 xEdit 1 expand 3 extract 3  find 1 Nfind 2 Nfindup 6 NfUP 3 Cfind 2 findUP 3 fUP 2
   forward 2  get  help 1 hexType 4  input 1 powerInput 3  join 1 split 2 spltJOIN load
   locate 1 Clocate 2 lowerCase 3 upperCase 3 Lprefix 2  macro  merge 2 modify 3 move 2
   msg  next 1 overlay 1 parse preserve 4 purge 3 put putD query 1 quit  read recover 3
   refresh renum 3 repeat 3 replace 1 Creplace 2 reset 3 restore 4 rgtLEFT right 2 left
   2  save  set  shift 2  si  sort  sos  stack 3 status 4 top  transfer 3  type 1  up 1"""

user_words = "riG   rePEAT copies  put mo   rest    types   fup.    6       poweRin"


def find_abbreviations_length(command_table_text):
    """ find the minimal abbreviation length for each word.
        a word that does not have minimum abbreviation length specified
        gets it's full lengths as the minimum.
    """
    command_table = dict()
    input_iter = iter(command_table_text.split())

    word = None
    try:
        while True:
            if word is None:
                word = next(input_iter)
            abbr_len = next(input_iter, len(word))
            try:
                command_table[word] = int(abbr_len)
                word = None
            except ValueError:
                command_table[word] = len(word)
                word = abbr_len
    except StopIteration:
        pass
    return command_table


def find_abbreviations(command_table):
    """ for each command insert all possible abbreviations"""
    abbreviations = dict()
    for command, min_abbr_len in command_table.items():
        for l in range(min_abbr_len, len(command)+1):
            abbr = command[:l].lower()
            abbreviations[abbr] = command.upper()
    return abbreviations


def parse_user_string(user_string, abbreviations):
    user_words = [word.lower() for word in user_string.split()]
    commands = [abbreviations.get(user_word, "*error*") for user_word in user_words]
    return " ".join(commands)


command_table = find_abbreviations_length(command_table_text)
abbreviations_table = find_abbreviations(command_table)

full_words = parse_user_string(user_words, abbreviations_table)

print("user words:", user_words)
print("full words:", full_words)

```

### python_code_2.txt
```python
'''Simple abbreviations'''

from functools import reduce
import re


# withExpansions :: [(String, Int)] -> String -> String
def withExpansions(table):
    '''A string in which all words are either
       expanded (if they match abbreviations in
       a supplied table), or replaced with an
       '*error*' string.
    '''
    return lambda s: unwords(map(
        expanded(table), words(s)
    ))


# expanded :: [(String, Int)] -> String -> String
def expanded(table):
    '''An abbreviation (or error string) for
       a given word, based on a table of full
       strings and minimum abbreviation lengths.
    '''
    def expansion(k):
        u = k.upper()
        lng = len(k)

        def p(wn):
            w, n = wn
            return w.startswith(u) and lng >= n
        return find(p)(table) if k else Just(('', 0))

    return lambda s: maybe('*error*')(fst)(expansion(s))


# cmdsFromString :: String -> [(String, Int)]
def cmdsFromString(s):
    '''A simple rule-base consisting of a
       list of tuples [(
          upper case expansion string,
          minimum character count of abbreviation
       )],
       obtained by a parse of single input string.
    '''
    def go(a, x):
        xs, n = a
        return (xs, int(x)) if x.isdigit() else (
            ([(x.upper(), n)] + xs, 0)
        )
    return fst(reduce(
        go,
        reversed(re.split(r'\s+', s)),
        ([], 0)
    ))


# TEST -------------------------------------------------
def main():
    '''Tests of abbreviation expansions'''

    # table :: [(String, Int)]
    table = cmdsFromString(
        '''add 1  alter 3  backup 2  bottom 1  Cappend 2  change 1
            Schange Cinsert 2  Clast 3 compress 4 copy 2 count 3 Coverlay 3
            cursor 3  delete 3 Cdelete 2  down 1  duplicate 3 xEdit 1 expand 3
            extract 3  find 1 Nfind 2 Nfindup 6 NfUP 3 Cfind 2 findUP 3 fUP 2
            forward 2  get  help 1 hexType 4 input 1 powerInput 3  join 1
            split 2 spltJOIN load locate 1 Clocate 2 lowerCase 3 upperCase 3
            Lprefix 2  macro  merge 2 modify 3 move 2 msg  next 1 overlay 1
            parse preserve 4 purge 3 put putD query 1 quit read recover 3
            refresh renum 3 repeat 3 replace 1 Creplace 2 reset 3 restore 4
            rgtLEFT right 2 left 2  save  set  shift 2  si  sort  sos stack 3
            status 4 top  transfer 3  type 1  up 1'''
    )

    # tests :: [String]
    tests = [
        'riG   rePEAT copies  put mo   rest    types   fup.    6      poweRin',
        ''
    ]

    print(
        fTable(__doc__ + ':\n')(lambda s: "'" + s + "'")(
            lambda s: "\n\t'" + s + "'"
        )(withExpansions(table))(tests)
    )


# GENERIC -------------------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# Just :: a -> Maybe a
def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.'''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


# Nothing :: Maybe a
def Nothing():
    '''Constructor for an empty Maybe (option type) value.'''
    return {'type': 'Maybe', 'Nothing': True}


# find :: (a -> Bool) -> [a] -> Maybe a
def find(p):
    '''Just the first element in the list that matches p,
       or Nothing if no elements match.'''
    def go(xs):
        for x in xs:
            if p(x):
                return Just(x)
        return Nothing()
    return lambda xs: go(xs)


# fst :: (a, b) -> a
def fst(tpl):
    '''First member of a pair.'''
    return tpl[0]


# fTable :: String -> (a -> String)
#                  -> (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function ->
                 fx display function ->
          f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join([
            xShow(x).rjust(w, ' ') + (' -> ') + fxShow(f(x))
            for x in xs
        ])
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(v):
    '''Either the default value v, if m is Nothing,
       or the application of f to x,
       where m is Just(x).'''
    return lambda f: lambda m: v if m.get('Nothing') else (
        f(m.get('Just'))
    )


# unwords :: [String] -> String
def unwords(xs):
    '''A space-separated string derived from
       a list of words.'''
    return ' '.join(xs)


# words :: String -> [String]
def words(s):
    '''A list of words delimited by characters
       representing white space.'''
    return re.split(r'\s+', s)


# MAIN ---
if __name__ == '__main__':
    main()

```

