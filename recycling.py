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
    if not gameover:
        for i in items:
            i.draw()
    elif gameover == True:
        screen.draw.text("Better luck next time! :(", fontsize = 60, color = "Black", center = (WIDTH /2, HEIGHT /2))
    # elif gameover == "start":
    #     screen.draw.text("You have to click on the paper bag each level to pass. \n If the items reach the bottom you lose \n ")
    else: 
        screen.draw.text("Yay you win! :D", fontsize = 60, color = "Black", center = (WIDTH /2, HEIGHT /2))
        
        
        
    
def update():
    global items 
    if len(items) == 0:
        items = make_items(level)
        
        

def make_items(numberofitems):
    create = items_to_create(numberofitems)
    actors = create_items(create)
    layout_items(actors)
    animate_items(actors)
    return actors
    
    
    
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

def animate_items(actors):
    global animations 
    for i in actors:
        duration = 10 - level
        i.anchor = ("center", "bottom")
        animation = animate(i,duration = duration, y = HEIGHT, on_finished = handlegameover)
        animations.append(animation)

def handlegameover():
    global gameover
    gameover = True

def handlegamecomplete():
    global gameover, level, items, animations
    if level == 5:
        gameover = "complete"
    else:
        level += 1
        items = []
        animations = []
        
    
def on_mouse_down(pos):
    for i in items:
        if i.collidepoint(pos):
            if "paper" in i.image:
                handlegamecomplete()
            else:
                handlegameover()
        else: 
            handlegameover()
                
    
    
    

pgzrun.go()