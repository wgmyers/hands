Hands
=====

A pure python poker hand evaluator.

Why?
----

I have a bad case of Not Written By Me Syndrome

Why Not Just Use Pokerstove?
----------------------------

Good question. Haven't tried to get it running under wine yet, but can't
see why it wouldn't. You should almost certainly use that instead.

So What Is The Point Of This?
-----------------------------

I enjoyed writing it. I also learned quite a few things about poker I had
not previously realised, such as the fact that you can get two three of a
kinds in a single hand, though it will in that case count as a full house.

What Is It Doing On Github?
---------------------------

Offsite backup.

Why Doesn't It Do Much?
-----------------------

hands.py is mainly just a library. I haven't written a front-end for it yet.

Will You?
---------

Let's see how the evening progresses and take it from there.

What Does It Do Then?
---------------------

The library contains functions that compare poker hands in various ways. One
of them emits a table of dubious utility, purporting to be the % of the time
that each hand will win against random other hands in heads-up NL Texas
Hold'em. So far all of the figures I have checked against other hand evaluators
seem to be in the same ballpark. I haven't done any rigorous testing yet.

Show Me The Table
-----------------

Here you go:

```
    | A  | K  | Q  | J  | T  | 9  | 8  | 7  | 6  | 5  | 4  | 3  | 2  |
 A: | 85 | 67 | 67 | 66 | 65 | 64 | 63 | 63 | 62 | 61 | 60 | 59 | 58 |
 K: | 66 | 83 | 64 | 64 | 63 | 61 | 59 | 59 | 58 | 58 | 56 | 56 | 55 |
 Q: | 65 | 62 | 80 | 61 | 61 | 59 | 57 | 56 | 55 | 54 | 54 | 53 | 52 |
 J: | 65 | 61 | 59 | 78 | 59 | 57 | 56 | 54 | 53 | 52 | 52 | 50 | 49 |
 T: | 63 | 61 | 58 | 58 | 75 | 56 | 54 | 53 | 51 | 49 | 49 | 48 | 46 |
 9: | 62 | 59 | 57 | 55 | 53 | 73 | 53 | 51 | 49 | 47 | 46 | 45 | 45 |
 8: | 61 | 57 | 55 | 53 | 51 | 50 | 70 | 50 | 48 | 47 | 44 | 43 | 42 |
 7: | 61 | 57 | 53 | 52 | 50 | 48 | 48 | 67 | 48 | 46 | 44 | 42 | 40 |
 6: | 59 | 56 | 53 | 49 | 48 | 47 | 45 | 45 | 64 | 46 | 44 | 43 | 40 |
 5: | 59 | 56 | 52 | 49 | 46 | 45 | 43 | 43 | 43 | 60 | 43 | 40 | 39 |
 4: | 57 | 54 | 51 | 48 | 46 | 43 | 42 | 41 | 41 | 40 | 58 | 40 | 38 |
 3: | 57 | 53 | 50 | 47 | 45 | 42 | 39 | 39 | 39 | 38 | 36 | 54 | 37 |
 2: | 56 | 52 | 49 | 47 | 44 | 41 | 39 | 37 | 37 | 35 | 34 | 33 | 51 |
```

Top right corner is suited combinations, bottom left is offsuit.

Hmmm...
-------

That's what I was thinking.

Wayne Myers, 2014-01-06
