from robobopy.utils.LED import LED
from robobopy.utils.Color import Color
from robobopy.utils.Emotions import Emotions
from robobopy.utils.Sounds import Sounds

def danger_appears(robot):

    robot.setLedColorTo(LED.All, Color.RED)
    robot.setEmotionTo(Emotions.SURPRISED)
    robot.playSound(Sounds.DISCOMFORT)
    robot.moveTiltTo(50, 15)

    robot.moveWheelsByTime(-10, -10, 2)

    robot.sayText("Ups, that was close!")
    robot.setEmotionTo(Emotions.NORMAL)
    robot.moveTiltTo(75, 15)
