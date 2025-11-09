robot.dfRobotMaqueen.start()
basic.forever(function () {
    if (robot.detectLine(RobotLineDetector.Left) && robot.detectLine(RobotLineDetector.Right)) {
        robot.motorSteer(0, 70)
    } else if (robot.detectLine(RobotLineDetector.Left) && !(robot.detectLine(RobotLineDetector.Right))) {
        robot.motorSteer(-100, 50)
    } else if (!(robot.detectLine(RobotLineDetector.Left)) && robot.detectLine(RobotLineDetector.Right)) {
        robot.motorSteer(100, 50)
    }
})
