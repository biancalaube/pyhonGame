from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene does not exsist yet."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n-------------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    def enter(self):
        print "Sorry you won't able to find your grandpapa's killer."
        print "Thanks for playing my game, Bye!"
        exit(1)

class entryWay(Scene):

    def enter(self):
        print "You've just walked into the grand entry way of your Grandpapa's estate."
        print "Except, instead of being greeted by the bulter per usual you're met with silence."
        print "Right there infront of you is the body of your Grandpapa. Dead of the ground."
        print "With a singular bullet wound right in the middle of his forhead."
        print "Now you have two options to head 'right' or 'left' into the next room."

        while True:
            action = raw_input("> ")

            if action == "right":
                return 'kitchen'
            elif action == "left":
                return 'library'
            else:
                print "does not compute, please write 'right' or 'left'"


class library(Scene):

    def enter(self):
        print "You've just entered the library. You take a look around but no one seems to be here."
        print "But them something catches your eye and you walk towards it."
        print "It's a key pad you haven't seen before beside the bookshelf."
        print "When you walk towards the keypad you start to hear noises behind the bookshelf."
        print "They password is three digits long. You have five guesses."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print "the code starts wiht %s _ _ " % code[0]
        guess = raw_input("> ")
        guesses = 0



        while guesses < 5:
            if guess == code:
                print "You have guessed the code correctly. The bookshelf swings open."
                print "You see just a staircase going downwards and you start walking."
                return 'secretRoom'
            else:
                print "Incorrect code: code starts with %s _" %code[0:2]
                guess = raw_input("> ")
                guesses += 1


        print "The code was: %s" % code
        print "You fail to guess the code and in turn who killed your grand papa."
        print "Since he creeps up behind you while you're guessing shoots you in the head"
        print "just like your grand papa"
        return 'death'


class kitchen(Scene):

    def enter(self):
        print "You casuaslly enter the kitchen. They're two people in the room the cook and the maid."
        print "Either one could be the killer but you arent sure yet."
        print "You declare 'I know one of is the killer so just bring yourself forward'"
        print "As you finish your sentence you hear a loud bang and grab the"
        print "the closes frying pan near you. You dont have enough time to attack them both"
        print "you either can attack the 'maid' or the 'cook'"

        check = True

        while check == True:
            action = raw_input("> ")

            if action == "maid":
                print "You lift up the frying pan and go to smack the back of the head of the maid."
                print "Right as you finish smack the maid though you hear a bang."
                print "The cook has shot you in the back and when you turn around he is already gone."
                return 'death'
            elif action == "cook":
                print "\n"
                print "As you raise your frying pan to go to attack the cook he suddenly jumps and dissapears."
                print "You rush to see where he just was and you see that there was a trapped door"
                print "You look behind you to see if the maid is okay and she's in shock but okay"
                print "You look to the wall right next to where the cook was standing and you see a keypad"
                check = False
            else:
                print "does not compute, please write 'maid' or 'cook'"

        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print "They password is three digits long. You have five guesses."
        print "the code starts wiht %s _ _ " % code[0]
        guess = raw_input("> ")
        guesses = 0

        while guesses < 5:
            if guess == code:
                print "You have guessed the code correct and the trap door opens."
                print "You look behind you and tell the maid to stay where she is."
                print "You then take a deep breath and jump down the shoot."
                return 'secretRoom'
            else:
                print "Incorrect code: code starts with %s _" %code[0:2]
                guess = raw_input("> ")
                guesses += 1

        print "You fail to guess the code."
        print "the code was: %s" %code
        print "And in turn getting revenge on your grandpapa's killer."
        print "All of a sudden you feel a sharp pain in your side and you blackout."
        return 'death'



class secretRoom(Scene):

    def enter(self):
        print "You have entered a secret Room and infront of you there is three people."
        print "You then realize it's the cook cloned so there is three of them."
        print "He is stealing the family jewels and looks at you and laughs."
        print "He yells 'You'll never catch me -'. You dont let him finish his sentence "
        print "You grab the closest sharp object and attack."
        print "\n"
        print "You have one chance to attack the correct clone. 1,2 or 3."

        clone = randint(1,3)
        action = raw_input("> ")

        if int(action) == clone:
            print "You attacked th right clone! You stab him and he is currently on the ground."
            print "You we're able to solve the case!"
            return 'finish'
        else:
            print "You swing the object you're holding and it goes right through the clone."
            print "You chose the wrong cook and from behind he hits you with something in the back"
            print "of your head and you pass out."
            return 'death'

class finish(Scene):

    def enter(self):
        print "You found and caught your grandpapa's killer."
        print "Good for you. You inherited your fortune and won the game"
        print "Thanks for playing!"
        exit(1)

class Map(object):
    #dictionary
    scenes = {
        'entryWay': entryWay(),
        'kitchen': kitchen(),
        'library': library(),
        'secretRoom': secretRoom(),
        'death': Death(),
        'finish': finish()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


#main
a_map = Map('entryWay')
a_game = Engine(a_map)
a_game.play()
