import re

sentence = """
I went to the shop and bought \
30 apple at $50.0 each 20 mangoes at \
$60.0 each and came back with balance of $20 dollars
"""
searchable = sentence.strip()
search = r"[0-9]+"

print(re.findall(search,searchable))
