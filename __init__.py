#importing .py files into init()

from Stuff import FrameViewer
from Stuff import GameLoop

sw = FrameViewer.screenColor
print(sw)
GameLoop.gameLoop(FrameViewer.screen, FrameViewer.screenColor)