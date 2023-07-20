# Imports audio and os and time libraries. 
from replit import audio
import os, time

print("🎵 MyPOD Music Player")

# The subroutine to play the music. 
def play():
  source = audio.play_file('audio.wav')
  
  # unpause the music playing. 
  source.paused = False 
  while True:
    # User input to stop the music. 
    stopPlay = int(input("Press 2 to stop the music and return to the Main Menu."))
    if stopPlay == 2:
      # This will pause the file
      source.paused = True
      # Return the subroutine so it's useful outside of the sub. 
      return
    else:
      continue
while True:
  # Clear the screen.
  os.system("clear")
  print("🎵 MyPOD Music Player")
  time.sleep(3)
  print("Press 1 to play music")
  time.sleep(3)
  print("Print 2 to exit the player.")
  time.sleep(3)
  print("Press any other key to return to the Main Menu")

  userReply = int(input())
  if userReply == 1:
    print("Let's play some music!")
    play()
  elif userReply == 2:
    exit()
  else:
    continue
  
  
  # clear the screen 
  # Show the menu
  # take user's input
  # check whether you should call the play() subroutine depending on user's input
