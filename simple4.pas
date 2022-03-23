import random

def Grammar(**grammar):
  "Create a dictionary mapping symbols to alternatives."
  for (cat, rhs) in grammar.items():
    grammar[cat] = [alt.split() for alt in rhs.split('|')]
  return grammar
  
grammar = Grammar(
  S   = 'NP VP | S and S',
  NP  = 'Art N | Name',
  VP  = 'V NP',
  Art = 'the | a | every | some',
  N   = 'man | ball | woman | table | dog | cat | wombat',
  V   = 'hit | took | saw | liked | worshiped | remembered',
  Name= 'Alice | Bob | Carlos | Dan | Eve'
  )

def generate(symbol='S'):
  "Replace symbol with a random entry in grammar (recursively); join into a string."
  if symbol not in grammar:
    return symbol
  else:
    return ' '.join(map(generate, random.choice(grammar[symbol])))

def generate_tree(symbol='S'):
  "Replace symbol with a random entry in grammar (recursively); return a tree."
  if symbol not in grammar:
    return symbol
  else:
    return {symbol: [generate_tree(x) for x in random.choice(grammar[symbol])]}
