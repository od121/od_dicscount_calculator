print('Welcome, this program will tell you your discounted price!')

def discountcalc(prediscount,discount):
  discount = 1 - discount/100
  discount_price = round(prediscount * discount,2)
  return discount_price

while True:
  
  print()
  prediscount = input('Please enter item price:  ')

  while True:

    try:
      prediscount = int(prediscount)
      if prediscount <= 0: 
        print('Error, please enter a valid input!')
        break
  

    except:
      print('Error, please enter a valid input!')
      break
    
    print()
    discount = input('Please enter discount percentage without the percent sign:  ')


    try:
      discount = int(discount)
      if discount < 0:
        print('Error, please enter a valid input!')
        continue
      elif discount == 0:
        print(f'*** Item price after discount: {prediscount} ***')
        break
      if discount >= 100:
        print('*** Item price after discount: 0 ***')
        break

    except:
      print('Error, please enter a valid input!')
      continue

    print()
    print('*** Item price after discount:',discountcalc(prediscount,discount),'***')
    print()
    break

