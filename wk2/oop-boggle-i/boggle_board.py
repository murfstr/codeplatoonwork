import string
import random

class BoggleBoard:

  def __init__(self):
    print(self)
    user_input = input("say shake!")

    if user_input == 'shake':
      self.shake()
    else:
      print("that wasn't shake!")
    


  
  def __repr__(self):
    return '____\n____\n____\n____'


  def shake(self):
    for _ in range(4):
      row = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
      print(row)



# print(BoggleBoard())
BoggleBoard()