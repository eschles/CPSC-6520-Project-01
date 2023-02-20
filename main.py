# Your game should have a main script that ties everything together and starts the game loop.

from Stuff import FrameViewer
from Stuff import GameLoop

sw = FrameViewer.screenColor
print(sw)
GameLoop.gameLoop(FrameViewer.screen, FrameViewer.screenColor)

