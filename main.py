#functions with outputs

def format_name(first, last):
  f_name = list(first.lower())
  l_name = list(last.lower())
  f_name[0] = f_name[0].upper()
  l_name[0] = l_name[0].upper()
  whole_name = ""
  for x in f_name:
    whole_name += x
  whole_name += " "
  for y in l_name:
    whole_name += y
  return whole_name

'''
def format_name(first, last):
  f_name = first.title()
  l_name = last.title()

  return f"{f_name} {l_name}"
'''


print(format_name("joElle", "carbonell"))
