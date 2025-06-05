import csv
from io import StringIO

def parse_profile(csv_text):
    profile = []
    reader = csv.reader(StringIO(csv_text.strip()))
    for row in reader:
        vote = [alt.strip() for alt in row if alt.strip()]
        profile.append(vote)
    print("Parsed Voter Profile:", profile)
    return profile

def find_bottom(profile, remaining):
    bottoms = set()
    for vote in profile:
        for candidate in reversed(vote):
            if candidate in remaining:
                bottoms.add(candidate)
                break
    return bottoms

def top_candidate(vote, remaining):
    for alt in vote:
        if alt in remaining:
            return alt
    return None

def check_single_peaked(profile):
    from collections import deque

    alternatives = set(alt for vote in profile for alt in vote)
    left = deque()
    right = deque()
    A = set(alternatives)

    # Stage 1: fill outermost positions until two bottom-ranked found
    while A and not right:
        B = find_bottom(profile, A)
        if len(B) > 2:
            return "No"
        B = list(B)
        if len(B) == 1:
            left.append(B[0])
        elif len(B) == 2:
            left.append(B[0])
            right.appendleft(B[1])
        A -= set(B)

    # Stage 2: place remaining candidates inward
    while len(A) >= 2:
        l = left[-1]
        r = right[0]
        B = find_bottom(profile, A)
        if len(B) > 2:
            return "No"

        L, R = set(), set()
        for x in B:
            for vote in profile:
                if top_candidate(vote, A) != x:
                    # ranking positions
                    try:
                        pos_l = vote.index(l)
                        pos_r = vote.index(r)
                        pos_x = vote.index(x)
                    except ValueError:
                        continue  # skip if any of l, r, or x is missing

                    if pos_r < pos_x < pos_l:
                        L.add(x)
                    elif pos_l < pos_x < pos_r:
                        R.add(x)

        if len(L) > 1 or len(R) > 1:
            return "No"
        if L & R:
            return "No"
        undecided = set(B) - (L | R)
        for x in undecided:
            if not L:
                L.add(x)
            else:
                R.add(x)

        if L:
            left.append(L.pop())
        if R:
            right.appendleft(R.pop())
        A -= set(B)

    return "Axis: " + " < ".join(list(left) + list(A) + list(right))
