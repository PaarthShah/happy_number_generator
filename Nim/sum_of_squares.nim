import std/math
import std/sets

const LENLIST = 1_000_000

var
    happy_set: HashSet[uint] = toHashSet([1u])
    sad_set: HashSet[uint] = toHashSet([4u])
    happy_seq: seq[uint]
    count = 1u

proc sum_of_squares(n_in: uint): uint =
    var n = n_in
    while n != 0:
        result += (n mod 10)^2
        n = n div 10

proc happy_smart(n_in: uint): bool =
    var n = n_in
    var past = initHashSet[uint]()
    while n != 1 and n notin sad_set:
        if n in past:
            sad_set.incl(past)
            return false
        past.incl(n)
        n = sum_of_squares(n)
    if n == 1:
        happy_set.incl(past)
        return true
    else:
        sad_set.incl(past)
        return false

proc happy_smarter(n: uint): bool =
    return sum_of_squares(n) in happy_set

while count <= 99:
    if happy_smart(count):
        happy_seq.add(count)
    count += 1

while happy_seq.len < LENLIST:
    if happy_smarter(count):
        happy_set.incl(count)
        happy_seq.add(count)
    count += 1

echo happy_seq[^5..^1]
