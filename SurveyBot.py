import mouse
import keyboard
import time
import random

def moveMouse(posX, posY):
    mouse.move(posX, posY, absolute=True, duration=0.1)
    mouse.click('left')



def delay(x):
    #some delay
    time.sleep(x) 



def randomnum():
    message= ['Great Service', "Very fast", "Cool coffee", "Hot waitress", "fresh", "New Experience", "Fun times"]
    numMsg = len(message) - 1

    randomNum = random.randint(0, numMsg)
    return randomNum, message

def type():
    # G
    moveMouse(2877,827)
    time.sleep(0.5)
    # O
    moveMouse(3034, 762)
    time.sleep(0.5)
    # O
    moveMouse(3032, 755)
    time.sleep(0.5)
    # D
    moveMouse(2790, 821)
    time.sleep(0.5)
    # space
    moveMouse(2851, 944)
    time.sleep(0.5)
    #S
    moveMouse(2743, 823)
    time.sleep(0.5)
    #E
    moveMouse(2771, 761)
    time.sleep(0.5)
    #R
    moveMouse(2807, 762)
    time.sleep(0.5)
    #V
    moveMouse(2888, 875)
    time.sleep(0.5)
    #I
    moveMouse(2984, 760)
    time.sleep(0.5)
    #C
    moveMouse(2842, 882)
    time.sleep(0.5)
    #E
    moveMouse(2770, 762)
    time.sleep(0.5)

def scroll():
    mouse.wheel(-1)

#15' screen
def surveyPt1():
    randomNum, message = randomnum()
    # #Enter Survey
    # moveMouse(2873, 814)
    # delay(6)

    #start Survey
    moveMouse(1102, 646)
    delay(2)


    # Date of feedback
    moveMouse(510, 434)
    delay(0.5)
    #next page
    moveMouse(1106, 710)
    delay(1)


    #Highly satisfied
    moveMouse(479, 431)
    delay(0.5)
    #nextpage
    moveMouse(1106, 593)
    delay(1)


    # text box
    moveMouse(570, 408)
    delay(1)
    # type something
    keyboard.write(message[randomNum], delay=0.5)
    delay(3)

    #nextpage
    moveMouse(1106, 542)
    delay(1)


    #Carry Out
    moveMouse(536, 537)
    delay(0.5)
    #nextpage
    moveMouse(1106, 763)
    delay(1)


    #Front Counter
    moveMouse(629, 478)
    delay(0.5)
    #next
    moveMouse(1106, 690)
    delay(1)


    #beverage only
    moveMouse(694, 478)
    delay(0.5)
    #next
    moveMouse(1098, 687)
    delay(1)


    #Accuracy
    moveMouse(632, 480)
    delay(0.5)
    #taste
    moveMouse(633, 517)
    delay(0.5)
    #speed
    moveMouse(629, 550)
    delay(0.5)
    #friendliness
    moveMouse(630, 589)
    delay(0.5)
    #interior
    moveMouse(629, 632)
    delay(0.5)
    #exterior
    moveMouse(628, 686)
    delay(0.5)
    # Scroll down
    scroll()
    #next
    moveMouse(1106, 742)
    delay(1)  
    #part 1 completed
    moveMouse(1102, 459)
    delay(1)

# 15'
def surveyPt2():
    #visit
    moveMouse(640, 454)
    delay(0.5)
    #recommend
    moveMouse(638, 506)
    delay(0.5)
    #next
    moveMouse(1108, 647)
    delay(1)
    
    #problem?
    moveMouse(643, 481)
    delay(0.5)
    #next
    moveMouse(1110, 621)
    delay(1)

    # Cold Beverage
    moveMouse(600, 470)
    delay(0.5)
    #next
    moveMouse(1104, 686)
    delay(1)

    # Ice Coffee
    moveMouse(620, 750)
    delay(0.5)
    scroll()
    scroll()
    scroll()
    scroll()
    scroll()
    scroll()
    #next
    moveMouse(1104, 734)
    delay(1)

    #Good coffee?
    moveMouse(478, 422)
    delay(0.5)
    #next
    moveMouse(1106, 586)
    delay(1)

    #portion
    moveMouse(642, 459)
    delay(0.5)
    #appearance
    moveMouse(640, 495)
    delay(0.5)
    #packaging
    moveMouse(638, 535)
    delay(0.5)
    #taste
    moveMouse(639, 571)
    delay(0.5)
    #temparature
    moveMouse(641, 609)
    delay(0.5)
    #quality
    moveMouse(638, 642)
    delay(0.5)
    #flavor
    moveMouse(641, 680)
    delay(0.5)
    #valueformoney
    moveMouse(639, 719)
    delay(0.5)
    scroll()
    scroll()
    scroll()
    scroll()
    scroll()
    scroll()
    #next
    moveMouse(1109, 736)
    delay(1)

    #repurchase
    moveMouse(471, 413)
    delay(0.5)
    #next
    moveMouse(1106, 573)
    delay(1)

    #next
    moveMouse(1106, 453)
    delay(1) 

    #no outstanding
    moveMouse(841, 470)
    delay(0.5)
    #next
    moveMouse(1105, 615)
    delay(1)

    #new Survey
    moveMouse(825, 62)
    delay(2)
    keyboard.send('enter')
    delay(5)


def SurveyPart1_22():
    randomNum, message = randomnum()
    # #Enter Survey
    # moveMouse(2873, 814)
    # delay(6)

    #start Survey
    moveMouse(-618, 645)
    delay(5)


    # Date of feedback
    moveMouse(-880, 424)
    delay(1)
    #next page
    moveMouse(-630, 715)
    delay(3)


    #Highly satisfied
    moveMouse(-1232, 442)
    delay(1)
    #nextpage
    moveMouse(-625, 591)
    delay(3)


    # text box
    moveMouse(-905, 400)
    delay(1)
    # type something
    keyboard.write(message[randomNum], delay=1)
    delay(3)

    #nextpage
    moveMouse(-627, 536)
    delay(3)


    #Carry Out
    moveMouse(-939, 535)
    delay(1)
    #nextpage
    moveMouse(-618, 824)
    delay(3)


    #Front Counter
    moveMouse(-1061, 476)
    delay(1)
    #next
    moveMouse(-622, 690)
    delay(3)


    #beverage only
    moveMouse(-857, 479)
    delay(1)
    #next
    moveMouse(-626, 684)
    delay(3)


    #Accuracy
    moveMouse(-1091, 463)
    delay(1)
    #taste
    moveMouse(-1088, 498)
    delay(1)
    #speed
    moveMouse(-1089, 533)
    delay(1)
    #friendliness
    moveMouse(-1090, 573)
    delay(1)
    #interior
    moveMouse(-1090, 621)
    delay(1)
    #exterior
    moveMouse(-1087, 676)
    delay(1)
    # Scroll down
    scroll()
    #next
    moveMouse(-628, 813)
    delay(3)  
    #part 1 completed
    moveMouse(-624, 461)
    delay(3)

def SurveyPart2_22():
    #visit
    moveMouse(-1087, 454)
    delay(1)
    #Problem
    moveMouse(-1085, 509)
    delay(3)
    #next
    moveMouse(-623, 646)
    delay(1)
    
    #Merchandise?
    moveMouse(-977, 479)
    delay(1)
    #next
    moveMouse(-623, 618)
    delay(3)

    # Merchandise
    moveMouse(-969, 479)
    delay(1)
    #next
    moveMouse(-611, 627)
    delay(3)

    # Cold Beverage
    moveMouse(-1118, 467)
    delay(1)
    #next
    moveMouse(-611, 692)
    delay(3)


    # Ice Coffee
    moveMouse(-1137, 673)
    delay(1)
    scroll()
    scroll()
    scroll()
    scroll()
    scroll()
    scroll()
    scroll()
    scroll()
    scroll()
    scroll()
    #next
    moveMouse(-624, 953)
    delay(3)

    #Good coffee?
    moveMouse(-1254, 439)
    delay(1)
    #next
    moveMouse(-616, 590)
    delay(3)

    #portion
    moveMouse(-1088, 465)
    delay(1)
    #appearance
    moveMouse(-1086, 500)
    delay(1)
    #packaging
    moveMouse(-1088, 536)
    delay(1)
    #taste
    moveMouse(-1087, 577)
    delay(1)
    #temparature
    moveMouse(-1087, 611)
    delay(1)
    #quality
    moveMouse(-1087, 646)
    delay(1)
    #flavor
    moveMouse(-1089, 683)
    delay(1)
    #valueformoney
    moveMouse(-1090, 723)
    delay(1)
    scroll()
    scroll()
    scroll()
    scroll()
    scroll()
    scroll()
    #next
    moveMouse(-626, 852)
    delay(3)

    #repurchase
    moveMouse(-1246, 423)
    delay(1)
    #next
    moveMouse(-610, 587)
    delay(3)

    # #next
    # moveMouse(-1015, 485)
    # delay(1) 

    #no outstanding
    moveMouse(-1015, 485)
    delay(1)
    #next
    moveMouse(-625, 625)
    delay(3)

    # #new Survey
    # moveMouse(825, 62)
    # delay(2)
    # keyboard.send('enter')
    # delay(5)


def fillSurvey():
    SurveyPart1_22()
    SurveyPart2_22()
    keyboard.send("ctrl+w")
    #surveyPt2()

if __name__ == '__main__':
    # For 1 time use
    
    fillSurvey()
    
    # for multiple use
    # for i in range(0,8):
    #     fillSurvey()



