import wpilib
import time
from wpilib.interfaces import GenericHID

class Guitar:
    def __init__(self): #, controllerNumber):
        self.driver = wpilib.XboxController(1)
        self.operator = wpilib.XboxController(0)

        self.LEFT = GenericHID.Hand.kLeft
        self.RIGHT = GenericHID.Hand.kRight

        self.wammy_count = 0
    def get_input(self):
        if(self.operator.getAButtonPressed()):
            print("A button pressed")
        
        # if(self.operator.getTriggerAxis(self.RIGHT) or self.operator.getTriggerAxis(self.LEFT)):
        #     print("Wammy pressed")
        if(self.operator.getTriggerAxis(self.LEFT) > -0.9 and not (self.operator.getTriggerAxis(self.LEFT) == 0)):
            self.wammy_count += 1
            print("Wammy pressed (number", self.wammy_count, ")")

if __name__ == "__main__":
    guitar = Guitar()
    while True:
        guitar.get_input()
        time.sleep(0.5)
