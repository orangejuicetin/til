# Anagram of `a` is substring of `b`

This was a fun one that took a bit of time to think through with Eric Barch and Mathew Estafanous, but spent a bit of time after our jam on-call to fully iron out the best way to do it (optimized the solution a bit more to be linear time thanks to [this S/O post](https://stackoverflow.com/a/32071284) but cleaned it up in my version).

The additional function just to abstract away a littttle bit of repetitiveness felt like a bit much at first, but figured since this was interview prep it was worth to just call out as I was practicing and trying to abstract it away into a function quickly.

But yes, solution works, woot.

```python
import collections

def is_substring_anagram(substring, string) -> bool:
    n = len(substring)
    m = len(string)

    counts = collections.Counter(substring)
    difference = 0
    for i in range(m):
        curr_char = string[i]
        if i < n:
            if curr_char in counts:
                counts[curr_char] -= 1
        else:
            if i == n:
                difference = sum(abs(counts[num]) for num in counts)
            if difference == 0:
                return True
            leaving, entering = string[i - n], string[i]
            difference += increment_diff(counts, leaving, is_entering=False)
            difference += increment_diff(counts, entering, is_entering=True)

    return difference == 0

def increment_diff(counts: collections.Counter, char: str, is_entering: bool = True) -> int:
    if char in counts:
        incr = -1 if is_entering else 1
        counts[char] += incr
        return 1 if (is_entering and counts[char] < 0) or (not is_entering and counts[char] > 0) else -1
    return 0



print(is_substring_anagram("get", "eeetageek"))
```
