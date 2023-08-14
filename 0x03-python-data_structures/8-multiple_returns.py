#!/usr/bin/python3
def multiple_returns(sentence):
    if str(sentence) == "":
        first_character = None
        return (len(sentence), first_character)
    else:
        first_character = sentence[0]
        return (len(sentence), first_character)
