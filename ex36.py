def dungeon(inventory):
    print "You are now in the dungeon."

    print "A wild dragon appears!"
    print "He is blocking a pile of gold."

    print "What do you do?"
    cmdlist = ["punch", "fight", "use mace", "use hammer", "back"]
    cmd = getcmd(cmdlist)

    if cmd == "punch" or cmd == "fight":
        print "You try to fight the dragon but he eats you."
        print "The end."
        exit(0)
    elif cmd == "use hammer":
        print "You laughably try to use a hammer to fight a dragon."
        print "He breathes fire and turns you into ash."
        print "The end."
        exit(0)
    elif cmd == "use mace":
        if "mace" in inventory:
            print "You club the dragon with the mace, killing him."
            print "You take some gold and live a happy life."
            exit(0)
        else:
            print "You don't have a mace!"
            dungeon(inventory)
    elif cmd == "back":
        start(inventory) 

def armory(inventory):
    print "You are now in the armory."
    print "Go back or goto the workbench."

    cmdlist = ["back", "workbench"]
    cmd = getcmd(cmdlist)

    if cmd == "back":
        start(inventory)
    elif cmd == "workbench":
        workbench(inventory)
    else:
        print "Something went wrong." # this shouldn't execute
        exit(0)

def workbench(inventory, items=["nails", "bat"]):
    print "You are now at the workbench."
    print "On the workbench you see:"
    if len(items) > 0:
        for item in items:
            print "-> %s" % item
    else:
        print "Nothing."
    print "Try to make something or go back."

    cmdlist = ["use hammer", "take mace", "back"]
    cmd = getcmd(cmdlist)

    if cmd == "use hammer":
        print "You hammer the nails into the bat and create a mace!"
        items = ['mace']
        workbench(inventory, items)
    elif cmd == "take mace" and "mace" in items:
        if "mace" in inventory:
            print "You already have a mace."
        else:
            print "You have acquired a mace!"
            inventory.append("mace")
            items = []
        workbench(inventory, items)
    elif cmd == "back":
        armory(inventory)
    else:
        print "Something went wrong." # this shouldn't execute
        exit(0);

def start(inventory):
    print "You are now in the start room."
    print "Go left to dungeon or right to armory?"
    cmdlist = ["left", "right"]
    cmd = getcmd(cmdlist)

    if cmd == "left":
        dungeon(inventory)
    elif cmd == "right":
        armory(inventory)
    else:
        print "Something went wrong." # this shouldn't execute
        exit(0);

def getcmd(cmdlist):
    cmd = raw_input("> ")
    if cmd in cmdlist:
        return cmd
    elif cmd == "quit":
        print "Thanks for playing."
        exit(0)
    elif cmd == "inventory":
        print "Your inventory contains:"
        for item in inventory:
            print "--> %s" % item
        return getcmd(cmdlist)
    else:
        print "Command not recognized.  Try again."
        print "Type quit to exit or inventory to view items."
        return getcmd(cmdlist)

if __name__ == "__main__":
    inventory = ["hammer"]
    start(inventory)
