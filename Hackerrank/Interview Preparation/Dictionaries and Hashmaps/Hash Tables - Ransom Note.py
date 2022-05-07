from collections import Counter


def ransom_note(magazine, note):
    return not (Counter(note) - Counter(magazine))


def checkMagazine(magazine, note):
    # Write your code here
    if ransom_note(magazine, note):
        print("Yes")
        return
    print("No")


magazine = ["give", "me", "one", "grand", "today", "night"]
note = ["give", "one", "grand", "today"]
checkMagazine(magazine, note)
