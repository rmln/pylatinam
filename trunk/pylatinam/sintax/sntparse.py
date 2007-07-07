"""Sentence parser - pyLatinam

This module creates class with sentence lists from
text.

"""

class Text:
    def __init__(self, text, norm=False):
        text = text.split(".")
        self.text = strip(text)

def strip(text):
    new = []
    for item in text:
        new.append(item.strip())
    return new
