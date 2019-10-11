# Xander Kehoe
import time
maleValues = [1375, 2047, 2233, 2559, 3265]
femaleValues = [945, 2479, 3007, 3398, 4415]


def drawLine(t, x1, y1, x2, y2, colorP="black"):  # Basic method to draw lines
    t.up()
    t.goto(x1, y1)
    t.down()
    t.pencolor(colorP)
    t.goto(x2, y2)


def drawLineWithDots(t, x1, y1, x2, y2, colorP="black"):  # Basic method to draw lines with dots at each end
    t.pencolor(colorP)
    t.up()
    t.goto(x1, y1)
    t.dot(5)
    t.down()
    t.goto(x2, y2)
    t.dot(5)


def drawTickMarks(t):
    for i in range(6):  # Drawing vertical x marks
        drawLine(t, 40*i, 0, 40*i, 10)
    drawLine(t, 0, max(maleValues)/15, 10, max(maleValues)/15)  # Drawing maximum y mark for male
    drawLine(t, 0, max(femaleValues)/15, 10, max(femaleValues)/15)  # Drawing maximum y mark for female
    drawLine(t, 0, min(maleValues)/15, 10, min(maleValues)/15)  # Drawing minimal y mark for male
    drawLine(t, 0, min(femaleValues)/15, 10, min(femaleValues)/15)  # Drawing minimal y mark for female


def displayText(t):
    t.pencolor("black")
    t.up()
    t.goto(-3, (max(maleValues)/15)-10)
    t.write(max(maleValues), align="right")  # Writing maximum y value at max y mark for male
    t.goto(-3, (max(femaleValues)/15) - 10)
    t.write(max(femaleValues), align="right")  # Writing maximum y value at max y mark for female
    t.goto(-3, (min(maleValues)/15)-10)
    t.write(min(maleValues), align="right")  # Writing minimum y value at min y mark for male
    t.goto(-3, (min(femaleValues)/15) - 10)
    t.write(min(femaleValues), align="right")  # Writing minimum y value at min y mark for female
    x = 40
    for i in range(1970, 2011, 10):  # Writing years 1970-2010
        t.goto(x, -20)
        t.write(str(i), align="center")
        x += 40
    t.goto(0, -50)
    t.write("Two-year College Enrollment (in thousands)")  # Writing Title


def main():
    import turtle as t

    t.hideturtle()

    drawLine(t, 0, 0, 200, 0)
    drawLine(t, 0, 0, 0, 400)

    for i in range(1, 5):  # Drawing lines for male
        drawLineWithDots(t, 40*i, maleValues[i-1]/15, 40*(i+1), maleValues[i]/15, "blue")
    for i in range(1, 5):  # Drawing lines for female
        drawLineWithDots(t, 40*i, femaleValues[i-1]/15, 40*(i+1), femaleValues[i]/15, "red")
    drawTickMarks(t)
    displayText(t)
    time.sleep(15)  # Delay to allow user to actually look at chart so it doesn't immediately close


main()
