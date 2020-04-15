"""
Complete the function that accepts a string parameter,
and reverses each word in the string. All spaces in
the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""

def reverse_words(text):
  str_list = []
  for word in text.split(' '):
      str_list.append(word[::-1])
  return ' '.join(str_list)
