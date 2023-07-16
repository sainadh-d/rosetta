# Old lady swallowed a fly

## Task Link
[Rosetta Code - Old lady swallowed a fly](https://rosettacode.org/wiki/Old_lady_swallowed_a_fly)

## Java Code
### java_code_1.txt
```java
public class OldLadySwallowedAFly {

    final static String[] data = {
        "_ha _c _e _p,/Quite absurd_f_p;_`cat,/Fancy that_fcat;_j`dog,/What a hog"
        + "_fdog;_l`pig,/Her mouth_qso big_fpig;_d_r,/She just opened her throat_f_"
        + "r;_icow,/_mhow she_ga cow;_k_o,/It_qrather wonky_f_o;_a_o_bcow,_khorse.."
        + "./She's dead, of course!/", "_a_p_b_e ", "/S_t ", " to catch the ", "fly,/Bu"
        + "t _mwhy s_t fly,/Perhaps she'll die!//_ha", "_apig_bdog,_l`", "spider,/Tha"
        + "t wr_nj_ntickled inside her;_aspider_b_c", ", to_s a ", "_sed ", "There_qan"
        + " old lady who_g", "_a_r_bpig,_d", "_acat_b_p,_", "_acow_b_r,_i", "_adog_bcat"
        + ",_j", "I don't know ", "iggled and ", "donkey", "bird", " was ", "goat", " swal"
        + "low", "he_gthe"};

    static boolean oldLady(String part, boolean s) {
        for (char c : part.toCharArray()) {
            if (s)
                s = oldLady(data[c - '_'], false);
            else if (c == '_')
                s = true;
            else
                System.out.print(c == '/' ? '\n' : c);
        }
        return s;
    }

    public static void main(String[] args) {
        oldLady(data[0], false);
    }
}

```

## Python Code
### python_code_1.txt
```python
import zlib, base64

b64 = b'''
eNrtVE1rwzAMvedXaKdeRn7ENrb21rHCzmrs1m49K9gOJv9+cko/HBcGg0LHcpOfnq2np0QL
2FuKgBbICDAoeoiKwEc0hqIUgLAxfV0tQJCdhQM7qh68kheswKeBt5ROYetTemYMCC3rii//
WMS3WkhXVyuFAaLT261JuBWwu4iDbvYp1tYzHVS68VEIObwFgaDB0KizuFs38aSdqKv3TgcJ
uPYdn2B1opwIpeKE53qPftxRd88Y6uoVbdPzWxznrQ3ZUi3DudQ/bcELbevqM32iCIrj3IIh
W6plOJf6L6xaajZjzqW/qAsKIvITBGs9Nm3glboZzkVP5l6Y+0bHLnedD0CttIyrpEU5Kv7N
Mz3XkPBc/TSN3yxGiqMiipHRekycK0ZwMhM8jerGC9zuZaoTho3kMKSfJjLaF8v8wLzmXMqM
zJvGew/jnZPzclA08yAkikegDTTUMfzwDXBcwoE='''
print(zlib.decompress(base64.b64decode(b64)).decode("utf-8", "strict"))

```

### python_code_2.txt
```python
animals = [
        ("fly", "I don't know why she swallowed a fly, perhaps she'll die."),
        ("spider", "It wiggled and jiggled and tickled inside her."),
        ("bird", "How absurd, to swallow a bird."),
        ("cat", "Imagine that, she swallowed a cat."),
        ("dog", "What a hog, to swallow a dog."),
        ("goat", "She just opened her throat and swallowed a goat."),
        ("cow", "I don't know how she swallowed a cow."),
        ("horse", "She's dead, of course.")]

for i, (animal, lyric) in enumerate(animals):
    print("There was an old lady who swallowed a {}.\n{}".format(animal, lyric))

    if animal == "horse": break

    for (predator, _), (prey, _) in zip(animals[i:0:-1], animals[i-1::-1]):
        print("\tShe swallowed the {} to catch the {}".format(predator, prey))

    if animal != "fly": print(animals[0][1])  # fly lyric
    print()  # new line

```

