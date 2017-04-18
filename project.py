# This part defines the "fill-in-the-blanks texts and the solution word lists, each for the three different difficulty levels

texteasy = "A common first thing to do in a language is display 'Hello ___1___!' In ___2___ this is particularly easy; all you have to do is type in: \n___3___ 'Hello ___1___!' \nOf course, that isn't a very useful thing to do. However, it is an example of how to output to the user using the ___3___ command, and produces a program which does something, so it is useful in that capacity.\nIt may seem a bit odd to do something in a Turing complete language that can be done even more easily with an ___4___ file in a browser, but it is a step in learning ___2___ syntax, and that's really its purpose."

textmedium ="A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions."

texthard = "When you create a ___1___, certain ___2___s are automatically generated for you if you don't make them manually. These contain multiple underscores before and after the word defining them. When you write a ___1___, you almost always include at least the ___3___ ___2___, defining variables for when ___4___s of the ___1___ get made. Additionally, you generally want to create a ___5___ method, which will allow a string representation of the ___2___ to be viewed by other developers. /nYou can also create binary operators, like ___6___ and ___7___, which allow + and - to be used by ___4___s of the ___1___. Similarly, ___8___, ___9___ and ___10___ allow ___4___s of the class to be compared (with <, > and ==)."

listeasy = ['world', 'Python', 'print', 'html']
listmedium = ['function', 'arguments', 'None', 'list']
listhard = ['class','method', '__init__','instance','__repr__','__add__', '__sub__', '__lt__','__gt__', '__eq__']

# The following part asks for user input to choose the difficulty level of the game and :
print "Please select a game difficulty by typing it in!"
index = 0
while index < 1:
  userinput= raw_input("Possible choices are easy, medium and hard.")
  if userinput == 'easy':
      print "You have chosen easy level"
      text = texteasy
      list = listeasy
      index+=1
  elif userinput == 'medium':
      print "You have chosen medium level"
      text = textmedium
      list = listmedium
      index+=1
  elif userinput == 'hard':
      print "You have chosen hard level"
      text = texthard
      list = listhard
      index+=1
  else:
      print "This is not a valid input. Please try again and choose easy, medium or hard:"


# This part starts the level that has been chosen by the player, prints the according fill-in-the-blanks text and asks them to put in solutions for the blanks:
print
print "The current paragraph reads as such:"
print text
print

def substitution_quiz(solution_list):
    index = 0
    global text #this has to be put in because I get an UnboundLocalError otherwise
    while index< len(solution_list):
        userinput = raw_input("What should be substituted in for ___"+str(index+1)+"___ ?" )
        if userinput == solution_list[index]:
            text = text.replace("___"+str(index+1)+"___", solution_list[index])
            index+=1
            print
            print ("Correct!")
            print ("The current paragraph reads as such:\n"+text)
        else:
            print
            print ("That isn't the correct answer.")
            userinput = raw_input("Do you want to see the correct answer? y/n:")
            if userinput == 'y':
                print ("The correct answer would have been '"+str(solution_list[index])+"'!")

    print
    print ("Congratulations, you've finished the game! Very well done!")

# I need this line for the game to work, but it prints "None" when the game finishes, which isn't intended.
print substitution_quiz(list)

raw_input("Press enter to exit.")
