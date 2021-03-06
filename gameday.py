left_motor = "56692776393860847950432"
right_motor = "56701913640562953935644"

def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(go_forward, 7)

def autonomous_main():
    pass

async def go_forward(time):
    # move left motor forward 
    Robot.set_value(left_motor, 'duty_cycle', .5)
    # move right motor forward
    Robot.set_value(right_motor,'duty_cycle', .5)
    # wait for x (time) number of seconds
    await Actions.sleep(time)
    # tell left motor to stop
    Robot.set_value(left_motor,'duty_cycle', 0)
    # tell right motor to stop 
    Robot.set_value(right_motor,'duty_cycle', 0)

def teleop_setup():
    print("Tele-operated mode has started!")
    # Experimentation with Controller Function. Revert if not functional.
    async def controller_function():
        if Gamepad.get_value("joystick_left_y") != 0.0:
            print("Moving joystick")
            Robot.set_value(left_motor, "duty_cycle", Gamepad.get_value("joystick_left_y"))
        else:
            Robot.set_value(left_motor, "duty_cycle", 0)
            
        if Gamepad.get_value("joystick_right_y") != 0.0:
            print("Moving joystick")
            Robot.set_value(right_motor, "duty_cycle", Gamepad.get_value("joystick_right_y"))
        else:
            Robot.set_value(right_motor, "duty_cycle", 0)

def teleop_main():
    Robot.run(controller_funtion)
