def A():
  from fractions import Fraction
  def result(first, op, second):
    assert len(op) == 1
    expr = float(Fraction(eval("first"+op+"second")).limit_denominator())
    return op.join(("\tfirst ",
                    " second = {0} ",
                    " {1} = {2}")).format(first, second, expr)
  first, second = 7, 44.3
  print("A.")
  print(result(first, '+', second))
  print(result(first, '*', second))
  print(result(first, '/', second))

def B():
  print("B.")
  print("\ta = 9")
  print(f"\tc = {9+6}")
  print("\tb = 8")

def C():
  print("C.")
  if "john" == 'john':
    print("\tthere is NO difference.")
  else:
    raise NotImplementedError
  my_number = 5+5
  try:
    print("\tresult is: "+my_number)
  except TypeError:
    print("\tresult is:", my_number)

def D():
  print("D.")
  print("\tx + int(y) ==", 5+int(2.36))

def E():
  X, Y = "X", "Y"
  print("E.")
  if X > Y:
    print("\tBIG")
  elif X < Y:
    print("\tsmall")

def F():
  from random import randint
  seasonEnum = randint(1, 4)
  seasons = ('summer', 'winter',
             'fall', 'spring')
  print("F.")
  print('\t'+seasons[seasonEnum-1])

def G():
  from ast import literal_eval
  a = 8
  b = "123"
  print("G.")
  print('\t'+str(a+literal_eval(b)))
  

if __name__ == '__main__':
  A()
  B()
  C()
  D()
  E()
  F()
  G()
