import pgzrun, random, time

TITLE = "recycling"
WIDTH = 600
HEIGHT = 600
ITEMS = ["plasticbag", "battery", "chips", "bottleimg"]
gameover = False
items = []
level = 1
animations = []
def draw():
    screen.blit("recyclebg", (0,0))
def update():
    if len(items) == 0:
        make_items(level)
        

# def make_items(numberofitems):
    
    
def items_to_create(numberofitems):
    create = ["paperbag"]
    for i in range(numberofitems):
        # create.append(ITEMS[random.randint(0,3)])
        create.append(random.choice(ITEMS))
    return create

def create_items(create):
    actors = []
    for i in create:
        actors.append(Actor(i))
    return actors

def layout_items(actors):
    number_of_gaps = len(actors) + 1
    gapsize = WIDTH / number_of_gaps
    random.shuffle(actors)
    for i,v in enumerate(actors):
        pos = (i + 1) * gapsize
        v.x = pos
        

pgzrun.go()