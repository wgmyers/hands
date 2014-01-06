#!/usr/bin/env python

# hands.py

# Print out a chart of poker hands and their % to win against
# any other hand HU over n iterations (n to be determined)

import random

suits = ['s', 'h', 'd', 'c']
values = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

hands = ['STFL', 'FOUR', 'FULL', 'FLSH', 'STRT', 'TRIP', 'TWOP', 'ONEP', 'HIGH']

fresh_pack = [v+s for s in suits for v in values]

def shuffled_pack():
    """Return a freshly shuffled pack of cards"""

    # random has a shuffle function. May as well use it.
    pack = list(fresh_pack)
    random.shuffle(pack)
    return pack

def rank_cards(cards):
    """Take list of cards, return sorted list in descending order of rank"""

    ranked = sorted(cards, key = lambda c: values.index(c[0]))
    return ranked

def count_cards(hand):
    """Take hand, return dict with count of each card value"""
    d = {}
    for c in hand:
        if c[0] in d.keys():
            d[c[0]] += 1
        else:
            d[c[0]] = 1
    return d

def count_suits(hand):
    """Take hand, return dict with count of each suit value"""
    s = {}
    for c in hand:
        if c[1] in s.keys():
            s[c[1]] += 1
        else:
            s[c[1]] = 1
    return s

def has_n(d, n):
    """True if hand contains n cards the same, false otherwise"""

    for v in d.values():
        if v == n:
            return True

    return False

def has_pair(d):
    """True if hand contains a pair, false otherwise"""

    return has_n(d, 2)

def has_three(d):
    """True if hand contains three of a kind, false otherwise"""

    return has_n(d, 3)

def has_four(d):
    """True if hand contains quads, false otherwise"""

    return has_n(d, 4)

def has_two_pair(d):
    """True if hand contains two pair (or more), false otherwise"""

    pairs = 0

    for v in d.values():
        if v == 2:
            pairs += 1

    if pairs > 1:
        return True

    return False

def has_full_house(d):
    """True if hand contains full house, false otherwise"""

    three = False
    two = False

    for v in d.values():
        if v == 2:
            two = True
        if v == 3:
            # Handle extreme edge case of two sets of three
            if three == True:
                two = True
            else:
                three = True

    if three == True and two == True:
        return True

    return False

def has_flush(s):
    """True if hand contains flush, false otherwise"""

    for v in s.values():
        if v > 4:
            return True

    return False

def has_straight(hand):
    """True if hand contains straight, false otherwise"""

    run = 0
    last_card = -1
    this_card = -1

    for c in hand:
        if last_card == -1:
            last_card = values.index(c[0])
            this_card = values.index(c[0])
        else:
            last_card = this_card
            this_card = values.index(c[0])
            if this_card - last_card == 1:
                run += 1
                if run > 3:
                    break
            elif this_card - last_card == 0:
                # Ignore pairs etc
                continue
            else:
                run = 0

    # run counts the number of times the gap between cards is 1, ignoring
    # pairs. So for a straight we need run to be at least 4.
    if run > 3:
        return True

    return False

def has_straight_flush(hand, s):
    """True if hand contains straight flush, false otherwise"""

    # First check we have a flush
    if has_flush(s) == False:
        return False

    # Get flush suit
    for k in s.keys():
        if s[k] > 4:
            fsuit = k

    # Populate test_hand with cards of that suit
    test_hand = []
    for c in hand:
        if c[1] == fsuit:
            test_hand.append(c)

    # Now if has_straight returns true on test_hand, we have straight flush
    if has_straight(test_hand) == True:
        return True

    return False


def get_n(hand, d, n):
    """Take seven card hand containing n = 2,3 or 4, return five card poker hand"""

    best = []
    kickers = []

    # Find the n cards
    nval = d.keys()[d.values().index(n)]

    for c in hand:
        if c[0] == nval:
            best.append(c)
    for c in hand:
        if c[0] != nval:
            kickers.append(c)
    
    return (best + kickers[:5-n])

def get_pair(hand, d):
    """Take seven card hand containing pair, return five card poker hand"""
    return get_n(hand, d, 2)

def get_three(hand, d):
    """Take seven card hand containg three of kind, return five card hand"""
    return get_n(hand, d, 3)

def get_four(hand, d):
    """Take seven card hand containing quads, return five card hand"""
    return get_n(hand, d, 4)

def get_two_pair(hand, d):
    """Take seven card hand containing minimum two pairs, return five card poker hand"""

    best = []
    pairs = []
    kickers = []

    for k in d.keys():
        if d[k] == 2:
            pairs.append(k)

    pairs = rank_cards(pairs)

    # We only want the first two pairs - any lower pair is dropped
    for c in hand:
        if c[0] == pairs[0]:
            best.append(c)
    for c in hand:
        if c[0] == pairs[1]:
            best.append(c)
    for c in hand:
        if (c[0] != pairs[0] and c[0] != pairs[1]):
            kickers.append(c)

    return (best + kickers[0:1])

def get_full_house(hand, d):
    """Take seven card hand containing full house, return five card poker hand"""

    best = []
    pairs = []
    threes = []

    # May be more than one pair, we want the best pair
    for k in d.keys():
        if d[k] == 2:
            pairs.append(k)
    pairs = rank_cards(pairs)

    # Find the threes
    for k in d.keys():
        if d[k] == 3:
            threes.append(k)
    threes = rank_cards(threes)

    # Weird edge case with two sets of three
    if len(threes) > 1:
        # Handle case
        for c in hand:
            if c[0] == threes[0]:
                best.append(c)
            if c[0] == threes[1]:
                best.append(c)
        # Lose the last card
        best = best[:5]

    else:
        # Normal full house
        for c in hand:
            if c[0] == threes[0]:
                best.append(c)
        for c in hand:
            if c[0] == pairs[0]:
                best.append(c)

    return best

def get_flush(hand, s):
    """Take seven card hand containing flush, return it"""

    best = []
    suit = ""

    # Find flush suit
    for k in s.keys():
        if s[k] > 4:
            suit = k

    for c in hand:
        if c[1] == suit:
            best.append(c)

    # Return only first five
    return best[:5]

def get_straight(hand):
    """Take hand containing straight, return best straight"""

    best = []

    # Copy hand to best, eliminating pairs or sets
    last = ""
    for c in hand:
        if c[0] == last:
            continue
        last = c[0]
        best.append(c)

    # best now contains 5, 6 or 7 cards and no duplicates
    if len(best) == 5:
        # We're done
        return best

    # It's XXSSSSS, XSSSSS?, SSSSS??, SSSSS? or XSSSSS 

    # First check gap between second and third card 

    if values.index(best[2][0]) - values.index(best[1][0]) > 1:
        # Gap between two and three, lose first two cards
        best = best[2:]
    elif values.index(best[1][0]) - values.index(best[0][0]) > 1:
        # Gap between one and two, lose first card
        best = best[1:]

    # Best straight is now the first five remaining cards
    return best[:5]

def get_straight_flush(hand, s):
    """Take hand containing straight flush, return best straight flush"""

    # Find flush suit
    for k in s.keys():
        if s[k] > 4:
            fsuit = k

    # Eliminate cards not of that suit
    flush = []
    for c in hand:
        if c[1] == fsuit:
            flush.append(c)

    # Get straight from that flush and return it
    return get_straight(flush)

def best_hand(hand, board):
    """Take hole cards and a board and make best five card poker hand.
       Return it with prepended four character hand code."""

    # First sort seven cards in descending order of rank
    ranked = rank_cards(hand + board)

    # count cards
    d = count_cards(ranked)

    suits = count_suits(ranked)

    # Check for straight flush
    if has_straight_flush(ranked, suits):
        return ['STFL'] + get_straight_flush(ranked, suits)

    # Check for quads
    if has_four(d):
        return ['FOUR'] + get_four(ranked, d)
    
    # Check for full house
    if has_full_house(d):
        return ['FULL'] + get_full_house(ranked, d)

    # Check for flush
    if has_flush(suits):
        return ['FLSH'] + get_flush(ranked, suits)

    # Check for straight
    if has_straight(ranked):
        return ['STRT'] + get_straight(ranked)

    # Check for three of a kind
    if has_three(d):
        return ['TRIP'] + get_three(ranked, d)

    # Check for two pairs
    if has_two_pair(d):
        return ['TWOP'] + get_two_pair(ranked, d)

    # Check for pairs
    if has_pair(d):
        return ['ONEP'] + get_pair(ranked, d)

    # Return high-card five card hand
    return ['HIGH'] + ranked[:5]

def compare_high_cards(h1, h2):
    """Take two hands, return True if h1 has the high card or ties, False otherwise"""

    for p in zip(h1, h2):
        if values.index(p[0][0]) < values.index(p[1][0]):
            return True
        if values.index(p[0][0]) > values.index(p[1][0]):
            return False

    # A tie. Return True
    return True

def compare_hands(h1, h2):
    """Take two scored five card hands, return True if h1 wins, False otherwise"""

    if hands.index(h1[0]) < hands.index(h2[0]):
        return True
    elif hands.index(h1[0]) > hands.index(h2[0]):
        return False
    else:

        # Does this work for all possible hand types
        # assuming winning combinations are sorted to
        # the front and remaining cards sorted by rank?

        return compare_high_cards(h1[1:], h2[1:])

def play_hands(h1, h2):
    """Take two hole hands, play a round of poker, and return True if h1 wins, False otherwise"""

    pack = shuffled_pack()

    # Remove the dealt cards from the pack
    for c in h1 + h2:
        pack.remove(c)

    if len(h2) == 0:
        # If we haven't been given a second hand, deal it now
        # Also get the board
        h2 = pack[:2]
        board = pack[2:7]
    else:
        # Otherwise, just get the board
        board = pack[:5]

    # Get best combined hand for h1 and h2
    h1best = best_hand(h1, board)
    h2best = best_hand(h2, board)

    # Compare them and return result
    return compare_hands(h1best, h2best)

def compare_hole_hands(hero, vill):
    """Take two hole hands and see how often one beats the other.
       If vill not given, see how often hero wins against random hand."""

    max = 20000
    c = 0

    hwon = 0

    while c < max:
        if play_hands(hero, vill) == True:
            hwon += 1
        c += 1

    percent = (hwon * 100.0) / max

    if len(vill) == 2:
        print "%s%s beats %s%s %d%% of the time.\n" % (hero[0], hero[1], vill[0], vill[1], percent)
    else:
        print "%s%s wins %d%% of the time.\n" % (hero[0], hero[1], percent)

if __name__ == "__main__":

    h = ['7d', '2c']
    #v = ['Qc', '2s']
    v = []

    compare_hole_hands(h, v)

    #if play_hands(h, v) == True:
    #    print "h wins"
    #else:
    #    print "v wins"
