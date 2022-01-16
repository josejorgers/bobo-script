from robobopy.utils.IR import IR

def distance_based_turn(robot, speed=30, time=0.5):
    left_distance = robot.readIRSensor(IR.FrontLL)
    right_distance = robot.readIRSensor(IR.FrontRR)

    if left_distance > right_distance:
        robot.moveWheelsByTime(-speed, speed, time)
        return
    
    robot.moveWheelsByTime(speed, -speed, time)
    