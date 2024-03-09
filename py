# Define your functions
def coffee_bot():
  print('Welcome to the cafe!')
  size=get_size()
  drink_type=get_drink_type()
  temp_type=get_temp_type()
  print ('Alright, that\'s a {} {} {}!'.format (temp_type, size, drink_type))  
  name=input('Can I get your name please? \n>')
  print ('Thanks, {}! Your drink will be ready shortly.'.format(name))
  cup_type=get_cup_type()
  add_order=get_add_order()

def thank_message():
  print ('Thank you!')

def print_message():
  print ('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res== 'a':
    return 'small'
  elif res== 'b':
    return 'medium'
  elif res== 'c':
    return 'large'
  else:
    return print_message()
  return get_size()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Lattee \n>')
  if res== 'a':
    return 'brewed coffee'
  elif res== 'b':
    return 'mocha'
  elif res== 'c':
    return get_order_latte()
  else:
    return print_message()
  return get_drink_type()

def get_order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>')
  if res== 'a':
    return '2% milk latte';
  if res== 'b':
    return 'Non-fat milk latte';      
  if res== 'c':
    return 'Soy milk latte';
  else:
    return print_message()
  return get_order_latte()    

def get_cup_type():
  res = input('would like a plastic cup or to use your own reusable cup? \n[a] plastic cup \n[b] reusable cup \n>')
  if res== 'a':
    return 'plastic cup';
  if res== 'b':
    return 'reusable cup';   
  else:
    return print_message()
  return get_cup_type()

def get_temp_type():
  res = input('How about if they\'d like their drink hot or iced? \n[a] hot \n[b] iced \n>')
  if res== 'a':
    return 'hot';
  if res== 'b':
    return 'iced';   
  else:
    return print_message()
  return get_temp_type()

def get_add_order():
  res = input('Would you like to order an additional drink? \n[a] Yes \n[b] No \n>')
  if res== 'a':
    return get_drink_type()
  if res== 'b':
    return thank_message()  
  else:
    return print_message()
  return get_add_order()

#Call coffee_bot()!
coffee_bot()
