

map = [ ["00","01","02","03","04"],
        ["01","11","12","13","14"],
        ["20","21","22","23","24"],
        ["30","31","32","33","34"],
        ["40","41","42","43","44"]]

directions =  ["left","right","up","down"]

char_x = 4
char_y = 2

map[char_x][char_y] = "XX"
go = True

def list_to_string():
    for i in map:
        print(" ".join(i))

def movement():
    global char_x
    global char_y
    while go:       
        response = ""
        while response not in directions:
            response = input("Richtung?\n")    
            if response == "left":
                char_y -= 1
            elif response == "right":
                char_y += 1
            elif response == "up":
                char_x -= 1
            elif response == "down":
                char_x += 1
            else:
                print("I did not understand!")
            print("X",char_x)
            print("Y",char_y)


while True:
    list_to_string()
    movement()
