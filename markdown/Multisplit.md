# Multisplit

## Task Link
[Rosetta Code - Multisplit](https://rosettacode.org/wiki/Multisplit)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class MultiSplit {

    public static void main(String[] args) {
        System.out.println("Regex split:");
        System.out.println(Arrays.toString("a!===b=!=c".split("==|!=|=")));

        System.out.println("\nManual split:");
        for (String s : multiSplit("a!===b=!=c", new String[]{"==", "!=", "="}))
            System.out.printf("\"%s\" ", s);
    }

    static List<String> multiSplit(String txt, String[] separators) {
        List<String> result = new ArrayList<>();
        int txtLen = txt.length(), from = 0;

        for (int to = 0; to < txtLen; to++) {
            for (String sep : separators) {
                int sepLen = sep.length();
                if (txt.regionMatches(to, sep, 0, sepLen)) {
                    result.add(txt.substring(from, to));
                    from = to + sepLen;
                    to = from - 1; // compensate for the increment
                    break;
                }
            }
        }
        if (from < txtLen)
            result.add(txt.substring(from));
        return result;
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> import re
>>> def ms2(txt="a!===b=!=c", sep=["==", "!=", "="]):
	if not txt or not sep:
		return []
	ans = m = []
	for m in re.finditer('(.*?)(?:' + '|'.join('('+re.escape(s)+')' for s in sep) + ')', txt):
		ans += [m.group(1), (m.lastindex-2, m.start(m.lastindex))]
	if m and txt[m.end(m.lastindex):]:
		ans += [txt[m.end(m.lastindex):]]
	return ans

>>> ms2()
['a', (1, 1), '', (0, 3), 'b', (2, 6), '', (1, 7), 'c']
>>> ms2(txt="a!===b=!=c", sep=["=", "!=", "=="])
['a', (1, 1), '', (0, 3), '', (0, 4), 'b', (0, 6), '', (1, 7), 'c']

```

### python_code_2.txt
```python
def multisplit(text, sep):
    lastmatch = i = 0
    matches = []
    while i < len(text):
        for j, s in enumerate(sep):
            if text[i:].startswith(s):
                if i > lastmatch:
                    matches.append(text[lastmatch:i])
                matches.append((j, i))  # Replace the string containing the matched separator with a tuple of which separator and where in the string the match occured
                lastmatch = i + len(s)
                i += len(s)
                break
        else:
            i += 1
    if i > lastmatch:
        matches.append(text[lastmatch:i])
    return matches

>>> multisplit('a!===b=!=c', ['==', '!=', '='])
['a', (1, 1), (0, 3), 'b', (2, 6), (1, 7), 'c']
>>> multisplit('a!===b=!=c', ['!=', '==', '='])
['a', (0, 1), (1, 3), 'b', (2, 6), (0, 7), 'c']

```

### python_code_3.txt
```python
def min_pos(List):
	return List.index(min(List))

def find_all(S, Sub, Start = 0, End = -1, IsOverlapped = 0):
	Res = []
	if End == -1:
		End = len(S)
	if IsOverlapped:
		DeltaPos = 1
	else:
		DeltaPos = len(Sub)
	Pos = Start
	while True:
		Pos = S.find(Sub, Pos, End)
		if Pos == -1:
			break
		Res.append(Pos)
		Pos += DeltaPos
	return Res

def multisplit(S, SepList):
	SepPosListList = []
	SLen = len(S)
	SepNumList = []
	ListCount = 0
	for i, Sep in enumerate(SepList):
		SepPosList = find_all(S, Sep, 0, SLen, IsOverlapped = 1)
		if SepPosList != []:
			SepNumList.append(i)
			SepPosListList.append(SepPosList)
			ListCount += 1
	if ListCount == 0:
		return [S]
	MinPosList = []
	for i in range(ListCount):
		MinPosList.append(SepPosListList[i][0])
	SepEnd = 0
	MinPosPos = min_pos(MinPosList)
	Res = []
	while True:
		Res.append( S[SepEnd : MinPosList[MinPosPos]] )
		Res.append([SepNumList[MinPosPos], MinPosList[MinPosPos]])
		SepEnd = MinPosList[MinPosPos] + len(SepList[SepNumList[MinPosPos]])
		while True:
			MinPosPos = min_pos(MinPosList)
			if MinPosList[MinPosPos] < SepEnd:
				del SepPosListList[MinPosPos][0]
				if len(SepPosListList[MinPosPos]) == 0:
					del SepPosListList[MinPosPos]
					del MinPosList[MinPosPos]
					del SepNumList[MinPosPos]
					ListCount -= 1
					if ListCount == 0:
						break
				else:
					MinPosList[MinPosPos] = SepPosListList[MinPosPos][0]
			else:
				break
		if ListCount == 0:
			break
	Res.append(S[SepEnd:])
	return Res


S = "a!===b=!=c"
multisplit(S, ["==", "!=", "="]) # output: ['a', [1, 1], '', [0, 3], 'b', [2, 6], '', [1, 7], 'c']
multisplit(S, ["=", "!=", "=="]) # output: ['a', [1, 1], '', [0, 3], '', [0, 4], 'b', [0, 6], '', [1, 7], 'c']

```

### python_code_4.txt
```python
'''Multisplit'''


from functools import reduce


# multiSplit :: [String] -> String -> [(String, String, Int)]
def multiSplit(separators):
    '''List of triples:
       [(token, separator, start index of separator].
    '''
    def go(s):
        def f(tokensPartsOffset, ic):
            tokens, parts, offset = tokensPartsOffset
            i, c = ic
            inDelim = offset > i
            return maybe(
                (
                    tokens if inDelim
                    else c + tokens, parts, offset
                )
            )(
                lambda x: (
                    '',
                    [(tokens, x, i)] + parts,
                    i + len(x)
                )
            )(
                None if inDelim else find(
                    s[i:].startswith
                )(separators)
            )
        ts, ps, _ = reduce(f, enumerate(s), ('', [], 0))
        return list(reversed(ps)) + [(ts, '', len(s))]
    return go


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''String split on three successive separators.'''
    print(
        multiSplit(['==', '!=', '='])(
            'a!===b=!=c'
        )
    )


# ------------------ GENERIC FUNCTIONS -------------------

# find :: (a -> Bool) -> [a] -> (a | None)
def find(p):
    '''Just the first element in the list that matches p,
       or None if no elements match.
    '''
    def go(xs):
        try:
            return next(x for x in xs if p(x))
        except StopIteration:
            return None
    return go


# maybe :: b -> (a -> b) -> (a | None) -> b
def maybe(v):
    '''Either the default value v, if m is None,
       or the application of f to x.
    '''
    return lambda f: lambda m: v if (
        None is m
    ) else f(m)


# MAIN ---
if __name__ == '__main__':
    main()

```

