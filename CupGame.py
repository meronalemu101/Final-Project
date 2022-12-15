# Import the necessary modules
from psychopy import visual, core, gui, monitors
import random

# Create the monitor object
mon = monitors.Monitor('myMonitor', width=31.4, distance=60)
mon.setSizePix([1280,800])
mon.save()

# Get the size of the monitor
thisSize = mon.getSizePix()
thisWidth = thisSize[0]
thisHeight = thisSize[1]

# Create the window where the images will be displayed
win = visual.Window(monitor=mon, size= (800,800), color = [-1,-1,-1], fullscr=True)

# Load the images of the three cups
cupA = visual.ImageStim(win, "cupA.png")
cupB = visual.ImageStim(win, "cupB.png")
cupC = visual.ImageStim(win, "cupC.png")

# Print a message to the user
print("Can you guess where the ball is hiding from under three cups? You have five trials to guess the correct cup.")

# Shuffle the cups
cups = [cupA, cupB, cupC]
random.shuffle(cups)

# Loop for five trials
for trial in range(5):
  # Display the images of the cups
  for cup in cups:
    cup.draw()
    win.flip()
    core.wait(0.5)

  # Create a dialog box for the user to enter their response
  user_input = gui.Dlg(title="Cup Game").addText("Enter a cup letter (A, B, or C):")
  user_input.show()

  # Check if the user's guess is correct
  if user_input.data == cups[0]:
    print("Congratulations! You have successfully guessed the cup where the ball is hiding.")
    break
  else:
    print("Sorry, that is not the correct cup. Please try again.")
