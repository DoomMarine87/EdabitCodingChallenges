"""You are given a list of strings consisting of grocery items, with prices in parentheses. Return a list of prices in float format.
Examples

get_prices(["salad ($4.99)"]) ➞ [4.99]

get_prices([
  "artichokes ($1.99)",
  "rotiserrie chicken ($5.99)",
  "gum ($0.75)"
])

➞ [1.99, 5.99, 0.75]

get_prices([
  "ice cream ($5.99)",
  "banana ($0.20)",
  "sandwich ($8.50)",
  "soup ($1.99)"
])

➞ [5.99, 0.2, 8.50, 1.99]

Notes

See if you can use RegExp to solve (but it's not necessary)."""

#import re
def get_prices(lst):
  #return list(map(float, re.findall(r'\d+.\d+', "".join(lst))))

  return list(map(lambda x: float(x.split()[-1][2:-1]),lst))



print(get_prices(["salad ($4.99)"])) # ➞ [4.99]

print(get_prices([
  "artichokes ($1.99)",
  "rotiserrie chicken ($5.99)",
  "gum ($0.75)"
])) #➞ [1.99, 5.99, 0.75]

print(get_prices([
  "ice cream ($5.99)",
  "banana ($0.20)",
  "sandwich ($8.50)",
  "soup ($1.99)"
])) #➞ [5.99, 0.2, 8.50, 1.99]

print(get_prices(['pizza ($2.99)', 'shampoo ($15.75)', 'trash bags ($15.00)'])), # [2.99, 15.75, 15])