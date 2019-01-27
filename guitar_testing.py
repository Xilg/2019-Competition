import wpilib
import time
from wpilib.interfaces import GenericHID

class Guitar:
    def __init__(self, operator): #, controllerNumber):
        self.operator = operator

        self.LEFT = GenericHID.Hand.kLeft
        self.RIGHT = GenericHID.Hand.kRight

        self.wammy_count = 0

    def is_wammy_pushed(self):
        return self.operator.getTriggerAxis(self.LEFT) > -0.9 and not (self.operator.getTriggerAxis(self.LEFT) == 0)

    def get_buttons_pushed(self):
        inputs = {
            1: "A", 
            2: "B", 
            3: "Y", 
            4: "X"
            # 5: ["Bumper", self.LEFT]
        }

        returned = inputs.copy()

        for input in inputs:
            if(type(inputs[input]) == type("")):
                string_executable = "self.operator.get" + inputs[input] + "Button()"
                returned[input] = exec(string_executable)
                print(string_executable)
            elif(type(inputs[input]) == type([])):
                returns[input] = exec("self.operator.get" + inputs[input][0] + "(" + str(inputs[input][1]) + ")")

        return returned


    def get_input(self):
        pressed = []
        print(self.get_buttons_pushed())
        if(self.operator.getAButton()):
            pressed.append("1")
            # print("A button pressed")
        
        if(self.is_wammy_pushed()):
            pressed.append("wammy")
            self.wammy_count += 1
            # print("Wammy count is: " + str(self.wammy_count))

        return pressed