class Chef:

    def __init__(self, name):
        self.name = 'Chef %s' % name
        self.basket = []

class Refrigerator:

    def __init__(self, chef):
        self.chef = chef
        self.items = ['bell pepper', 'onion', 'lettuce']

    def look(self):
        print "You look in the refrigerator and see:"
        for item in self.items:
            print '->', item

if __name__ == '__main__':

    print "What's your name?"
    name = raw_input('> ')

    chef = Chef(name)
    refrigerator = Refrigerator(chef)

    refrigerator.look()

    choice = raw_input('-> ')
    if choice.lower() == 'take onion':
        refrigerator.take('onion')  
        chef.basket.append('onion')
"""

    kitchen = Kitchen(chef)
    bowl = Bowl(chef)
    cutting_board = Cutting_Board(chef, bowl)
 
    print 'Actions are take, chop, open, close, and eat.'

    kitchen.look()

  
    basket_items = []
    kitchen_items = ['knife']
    refrigerator_items = ['bell pepper',
                          'lettuce',
                          'onion'
                          'dressing']

 
    inventory = Inventory()
    inventory.add("bell pepper")
    inventory.view()

"""
