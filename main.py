# Your game should have a main script that ties everything together and starts the game loop.
#scp -r <folder>/ cmurmu@access.computing.clemson.edu <folder location>

from Stuff import FrameViewer
from Stuff import GameLoop
from Stuff import paddle

#assigning python files to variable for easy future modification
f = FrameViewer
p = paddle

#calling Game loop from the main
GameLoop.gameLoop(f.screen, f.screenColor, p.paddle_surface)
