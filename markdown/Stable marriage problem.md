# Stable marriage problem

## Task Link
[Rosetta Code - Stable marriage problem](https://rosettacode.org/wiki/Stable_marriage_problem)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class Stable {
    static List<String> guys = Arrays.asList(
            new String[]{
        "abe", "bob", "col", "dan", "ed", "fred", "gav", "hal", "ian", "jon"});
    static List<String> girls = Arrays.asList(
            new String[]{
        "abi", "bea", "cath", "dee", "eve", "fay", "gay", "hope", "ivy", "jan"});
    static Map<String, List<String>> guyPrefers =
            new HashMap<String, List<String>>(){{
        put("abe",
            Arrays.asList("abi", "eve", "cath", "ivy", "jan", "dee", "fay",
            "bea", "hope", "gay"));
        put("bob",
            Arrays.asList("cath", "hope", "abi", "dee", "eve", "fay", "bea",
            "jan", "ivy", "gay"));
        put("col",
            Arrays.asList("hope", "eve", "abi", "dee", "bea", "fay", "ivy",
            "gay", "cath", "jan"));
        put("dan",
            Arrays.asList("ivy", "fay", "dee", "gay", "hope", "eve", "jan",
            "bea", "cath", "abi"));
        put("ed",
            Arrays.asList("jan", "dee", "bea", "cath", "fay", "eve", "abi",
            "ivy", "hope", "gay"));
        put("fred",
            Arrays.asList("bea", "abi", "dee", "gay", "eve", "ivy", "cath",
            "jan", "hope", "fay"));
        put("gav",
            Arrays.asList("gay", "eve", "ivy", "bea", "cath", "abi", "dee",
            "hope", "jan", "fay"));
        put("hal",
            Arrays.asList("abi", "eve", "hope", "fay", "ivy", "cath", "jan",
            "bea", "gay", "dee"));
        put("ian",
            Arrays.asList("hope", "cath", "dee", "gay", "bea", "abi", "fay",
            "ivy", "jan", "eve"));
        put("jon",
            Arrays.asList("abi", "fay", "jan", "gay", "eve", "bea", "dee",
            "cath", "ivy", "hope"));
    }};
    static Map<String, List<String>> girlPrefers =
            new HashMap<String, List<String>>(){{
        put("abi",
            Arrays.asList("bob", "fred", "jon", "gav", "ian", "abe", "dan",
            "ed", "col", "hal"));
        put("bea",
            Arrays.asList("bob", "abe", "col", "fred", "gav", "dan", "ian",
            "ed", "jon", "hal"));
        put("cath",
            Arrays.asList("fred", "bob", "ed", "gav", "hal", "col", "ian",
            "abe", "dan", "jon"));
        put("dee",
            Arrays.asList("fred", "jon", "col", "abe", "ian", "hal", "gav",
            "dan", "bob", "ed"));
        put("eve",
            Arrays.asList("jon", "hal", "fred", "dan", "abe", "gav", "col",
            "ed", "ian", "bob"));
        put("fay",
            Arrays.asList("bob", "abe", "ed", "ian", "jon", "dan", "fred",
            "gav", "col", "hal"));
        put("gay",
            Arrays.asList("jon", "gav", "hal", "fred", "bob", "abe", "col",
            "ed", "dan", "ian"));
        put("hope",
            Arrays.asList("gav", "jon", "bob", "abe", "ian", "dan", "hal",
            "ed", "col", "fred"));
        put("ivy",
            Arrays.asList("ian", "col", "hal", "gav", "fred", "bob", "abe",
            "ed", "jon", "dan"));
        put("jan",
            Arrays.asList("ed", "hal", "gav", "abe", "bob", "jon", "col",
            "ian", "fred", "dan"));
    }};
    public static void main(String[] args){
        Map<String, String> matches = match(guys, guyPrefers, girlPrefers);
        for(Map.Entry<String, String> couple:matches.entrySet()){
            System.out.println(
                    couple.getKey() + " is engaged to " + couple.getValue());
        }
        if(checkMatches(guys, girls, matches, guyPrefers, girlPrefers)){
            System.out.println("Marriages are stable");
        }else{
            System.out.println("Marriages are unstable");
        }
        String tmp = matches.get(girls.get(0));
        matches.put(girls.get(0), matches.get(girls.get(1)));
        matches.put(girls.get(1), tmp);
        System.out.println(
                girls.get(0) +" and " + girls.get(1) + " have switched partners");
        if(checkMatches(guys, girls, matches, guyPrefers, girlPrefers)){
            System.out.println("Marriages are stable");
        }else{
            System.out.println("Marriages are unstable");
        }
    }

    private static Map<String, String> match(List<String> guys,
            Map<String, List<String>> guyPrefers,
            Map<String, List<String>> girlPrefers){
        Map<String, String> engagedTo = new TreeMap<String, String>();
        List<String> freeGuys = new LinkedList<String>();
        freeGuys.addAll(guys);
        while(!freeGuys.isEmpty()){
            String thisGuy = freeGuys.remove(0); //get a load of THIS guy
            List<String> thisGuyPrefers = guyPrefers.get(thisGuy);
            for(String girl:thisGuyPrefers){
                if(engagedTo.get(girl) == null){//girl is free
                    engagedTo.put(girl, thisGuy); //awww
                    break;
                }else{
                    String otherGuy = engagedTo.get(girl);
                    List<String> thisGirlPrefers = girlPrefers.get(girl);
                    if(thisGirlPrefers.indexOf(thisGuy) <
                            thisGirlPrefers.indexOf(otherGuy)){
                        //this girl prefers this guy to the guy she's engaged to
                        engagedTo.put(girl, thisGuy);
                        freeGuys.add(otherGuy);
                        break;
                    }//else no change...keep looking for this guy
                }
            }
        }
        return engagedTo;
    }

    private static boolean checkMatches(List<String> guys, List<String> girls,
            Map<String, String> matches, Map<String, List<String>> guyPrefers,
            Map<String, List<String>> girlPrefers) {
        if(!matches.keySet().containsAll(girls)){
            return false;
        }

        if(!matches.values().containsAll(guys)){
            return false;
        }

        Map<String, String> invertedMatches = new TreeMap<String, String>();
        for(Map.Entry<String, String> couple:matches.entrySet()){
            invertedMatches.put(couple.getValue(), couple.getKey());
        }

        for(Map.Entry<String, String> couple:matches.entrySet()){
            List<String> shePrefers = girlPrefers.get(couple.getKey());
            List<String> sheLikesBetter = new LinkedList<String>();
            sheLikesBetter.addAll(shePrefers.subList(0, shePrefers.indexOf(couple.getValue())));
            List<String> hePrefers = guyPrefers.get(couple.getValue());
            List<String> heLikesBetter = new LinkedList<String>();
            heLikesBetter.addAll(hePrefers.subList(0, hePrefers.indexOf(couple.getKey())));

            for(String guy : sheLikesBetter){
                String guysFinace = invertedMatches.get(guy);
                List<String> thisGuyPrefers = guyPrefers.get(guy);
                if(thisGuyPrefers.indexOf(guysFinace) >
                        thisGuyPrefers.indexOf(couple.getKey())){
                    System.out.printf("%s likes %s better than %s and %s"
                            + " likes %s better than their current partner\n",
                       couple.getKey(), guy, couple.getValue(),
                       guy, couple.getKey());
                    return false;
                }
            }

            for(String girl : heLikesBetter){
                String girlsFinace = matches.get(girl);
                List<String> thisGirlPrefers = girlPrefers.get(girl);
                if(thisGirlPrefers.indexOf(girlsFinace) >
                        thisGirlPrefers.indexOf(couple.getValue())){
                    System.out.printf("%s likes %s better than %s and %s"
                            + " likes %s better than their current partner\n",
                       couple.getValue(), girl, couple.getKey(),
                       girl, couple.getValue());
                    return false;
                }
            }
        }
        return true;
    }
}

```

## Python Code
### python_code_1.txt
```python
import copy

guyprefers = {
 'abe':  ['abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
 'bob':  ['cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
 'col':  ['hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
 'dan':  ['ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
 'ed':   ['jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
 'fred': ['bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
 'gav':  ['gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
 'hal':  ['abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
 'ian':  ['hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
 'jon':  ['abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope']}
galprefers = {
 'abi':  ['bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
 'bea':  ['bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
 'cath': ['fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
 'dee':  ['fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed'],
 'eve':  ['jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob'],
 'fay':  ['bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal'],
 'gay':  ['jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian'],
 'hope': ['gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred'],
 'ivy':  ['ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan'],
 'jan':  ['ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan']}

guys = sorted(guyprefers.keys())
gals = sorted(galprefers.keys())


def check(engaged):
    inverseengaged = dict((v,k) for k,v in engaged.items())
    for she, he in engaged.items():
        shelikes = galprefers[she]
        shelikesbetter = shelikes[:shelikes.index(he)]
        helikes = guyprefers[he]
        helikesbetter = helikes[:helikes.index(she)]
        for guy in shelikesbetter:
            guysgirl = inverseengaged[guy]
            guylikes = guyprefers[guy]
            if guylikes.index(guysgirl) > guylikes.index(she):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (she, guy, he, guysgirl))
                return False
        for gal in helikesbetter:
            girlsguy = engaged[gal]
            gallikes = galprefers[gal]
            if gallikes.index(girlsguy) > gallikes.index(he):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (he, gal, she, girlsguy))
                return False
    return True

def matchmaker():
    guysfree = guys[:]
    engaged  = {}
    guyprefers2 = copy.deepcopy(guyprefers)
    galprefers2 = copy.deepcopy(galprefers)
    while guysfree:
        guy = guysfree.pop(0)
        guyslist = guyprefers2[guy]
        gal = guyslist.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            # She's free
            engaged[gal] = guy
            print("  %s and %s" % (guy, gal))
        else:
            # The bounder proposes to an engaged lass!
            galslist = galprefers2[gal]
            if galslist.index(fiance) > galslist.index(guy):
                # She prefers new guy
                engaged[gal] = guy
                print("  %s dumped %s for %s" % (gal, fiance, guy))
                if guyprefers2[fiance]:
                    # Ex has more girls to try
                    guysfree.append(fiance)
            else:
                # She is faithful to old fiance
                if guyslist:
                    # Look again
                    guysfree.append(guy)
    return engaged


print('\nEngagements:')
engaged = matchmaker()

print('\nCouples:')
print('  ' + ',\n  '.join('%s is engaged to %s' % couple
                          for couple in sorted(engaged.items())))
print()
print('Engagement stability check PASSED'
      if check(engaged) else 'Engagement stability check FAILED')

print('\n\nSwapping two fiances to introduce an error')
engaged[gals[0]], engaged[gals[1]] = engaged[gals[1]], engaged[gals[0]]
for gal in gals[:2]:
    print('  %s is now engaged to %s' % (gal, engaged[gal]))
print()
print('Engagement stability check PASSED'
      if check(engaged) else 'Engagement stability check FAILED')

```

