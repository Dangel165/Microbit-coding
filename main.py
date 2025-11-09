robot.df_robot_maqueen.start()

def on_forever():
    if robot.detect_line(RobotLineDetector.LEFT) and robot.detect_line(RobotLineDetector.RIGHT):
        robot.motor_steer(0, 100)
    elif robot.detect_line(RobotLineDetector.LEFT) and robot.detect_line(RobotLineDetector.RIGHT):
        robot.motor_steer(-100, 50)
    elif not (robot.detect_line(RobotLineDetector.LEFT)) and robot.detect_line(RobotLineDetector.RIGHT):
        robot.motor_steer(100, 50)
basic.forever(on_forever)
