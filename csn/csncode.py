import socket
import sys
import RPi.GPIO as GPIO
from gpiozero import Button,Servo,LED
from time import sleep


server = {'serverIp' : '192.168.42.1', 'serverPort' :12345}

def makeSocket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')
    except socket.error:
        print(socket.error)
        sys.exit()

    return s

def sendRequest(s):
    sleep(1)

    s.send('request'.encode('utf-8'))

    while True:
        try :
            reply = s.recv(4096)
            strCode = str(reply).split(':')[1] #Split the reply, and thake the first element (The reply will be returnRquest:0000)

            if strCode is not None:
                return strCode
        except IndexError:
            print('Ga normale indexes gebruiken')
        except:
            print('Ontvangen ging helemaal naar de tievus')


#Specify the correct pin on the RPi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.OUT)

#Servo frequency and start point
servo=GPIO.PWM(13,50)
servo.start(2.5)

#Gives stringvalue on the buttons
buttonNumber = [
    [4,'0'],
    [17,'1'],
    [12,'2'],
    [20,'3']
]
#Some variables
password=""
tries=0
alarmOn=True



#Declare pin number with correct color
Red=LED(22)
Green=LED(5)
Yellow=LED(27)

Red.on()

"""
@def Start
Starts the program
"""
def Start(tries, soc):
    print("START FUNCTIE")
    Red.on()
    sleep(0.4)
    Invoer(password, tries, soc)

"""
@def Invoer
Makes sure the GPIO pins keep the right string values.
"""
def Invoer(password,tries, soc):
    Red.off()
    Yellow.on()
    while len(password) != 4:
        if GPIO.input(4):
            password += buttonNumber[0][1]
            sleep(0.4)
            print(password)
        if GPIO.input(17):
            password+= buttonNumber[1][1]
            sleep(0.4)
            print(password)
        if GPIO.input(12):
            password+= buttonNumber[2][1]
            sleep(0.4)
            print(password)
        if GPIO.input(20):
            password+= buttonNumber[3][1]
            sleep(0.4)
            print(password)
        if len(password) == 4:
            control(password, tries, soc)

"""
@def control
-password:The password entered with Invoer
-Code:standard 0123
-while: If zero is entered close Control and go back to start to re-use the code
-soc: The socket for the server

Checks if entered password is the same as the given password
"""
def control(password, tries, soc):
    # Socket for checking the code
    soc.send(('check:' + str(password)).encode('utf-8')) #Check the code on the serverside

    # Wait for response of the check
    while True:
        try :
            reply = s.recv(4096).decode("utf-8")
            Code = int(reply.split(':')[1]) #Split the reply, and thake the first element (The reply will be returnCheck:false/true)
            print(reply.split(":"))
            if Code is not None:
                break
        except IndexError:
            print('Waarom ga je van een index uit als je het niet controleerd?')
        except:
            print('Ontvangen ging helemaal naar de tievus')
    print(bool(Code))
    if bool(Code) == True:
        Green.on()
        Yellow.off()
        Unlock(servo)
        print("OPEN")
        tries = 0
        while True:
            if GPIO.input(4):
                Green.off()
                Lock(servo)
                print("DICHT")
                Red.on()
                sleep(0.4)
                break
    elif tries == 2:
        print("je hebt te vaak geprobeerd")
        Blink()
        Blocked(password, tries, soc)
    elif bool(Code) == False:
        print("verkeerd probeer opnieuw")
        password=''
        tries += 1
        Red.on()
        Yellow.off()
        sleep(2)
        print(str(tries)+ ",Dit zijn alle tries")
        Invoer(password, tries, soc)


"""
@def Lock
Locks the lock
"""
def Lock(servo):
    servo.ChangeDutyCycle(2.5)
    return
"""
@def Unlock
Unlocks the lock 
"""
def Unlock(servo):

    servo.ChangeDutyCycle(11)
    return


"""
@def Blocked
If you have tried too many times you have to enter a certain password which is given via mail to unlock it.
"""
def Blocked(password, tries, soc):
    # Socket for checking the code
    soc.send(('alarm').encode('utf-8')) #Check the code on the serverside

    # Wait for response of the send alarm
    while True:
        try :
            reply = s.recv(4096)
            print(reply)#alarm has started
            alarmOn = False
            break
        except:
            print('Ontvangen ging helemaal naar de tievus')

    # Wait for the server to allow the alarm to be off
    while True:
        try :
            reply = s.recv(4096).decode("utf-8")
            print(reply)
            if str(reply) == 'alarmStop':
                break
        except:
            print('Ontvangen ging helemaal naar de tievus')



"""
@def Blink
Make all LED's blink three times. 
"""
def Blink():
    Red.blink(0.5,0.5,3)
    Green.blink(0.5,0.5,3)
    Yellow.blink(0.5,0.5,3)

def deadline():
    if

# Connection with the server
s = makeSocket()

try:

    s.connect((server['serverIp'], server['serverPort']))
    while True:
        reply = s.recv(4096)
        print(reply)
        break

except socket.error:
    print('Connection not found : ')
    print(socket.error)
    sys.exit()
except:
    print('Iets anders ging mis')

"""
@while True
Keeps the code running
"""
while True:
    if alarmOn == True and GPIO.input(19):
        alarmOn = False
        print("ALARM OFF")
        Red.off()
        sleep(0.4)
    elif alarmOn == False and GPIO.input(19):
        alarmOn = True
        print("ALARM ON")
        Red.on()
        sleep(0.4)
    elif alarmOn and GPIO.input(4):
        Red.on()
        s.send("request".encode("utf-8"))
        while True:
            reply = s.recv(4096).decode("utf-8")
            print (reply)
            break

        sleep(0.4)
        print("ALARM ON 4")
        Start(tries, s)
