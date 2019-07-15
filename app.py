
//Rex Godbout- Le Team (developer)


import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
PIN5= 5
GPIO.setup(PIN5, GPIO.OUT)

PIN12= 12
GPIO.setup(PIN12, GPIO.OUT)

PIN16= 16
GPIO.setup(PIN16, GPIO.OUT)

PIN22= 22
GPIO.setup(PIN22, GPIO.OUT)


#work
from flask import *

app = Flask(__name__)

@app.route("/forward", methods=["POST"])
def forward():
    GPIO.output(PIN5, True)
    GPIO.output(PIN12, False)

    GPIO.output(PIN16, True)
    GPIO.output(PIN22, False)
    return "ok"


@app.route("/STOP", methods=["POST"])
def STOP():
    GPIO.output(PIN5, False)
    GPIO.output(PIN12 , False)

    GPIO.output(PIN16, False)
    GPIO.output(PIN22, False)
    return "ok"




@app.route("/reverse", methods=["POST"])
def reverse():
    GPIO.output(PIN5, False)
    GPIO.output(PIN12, True)

    GPIO.output(PIN16, False)
    GPIO.output(PIN22, True)
    return "ok"

@app.route("/left", methods=["POST"])
def left():
    GPIO.output(PIN5, True)
    GPIO.output(PIN12 , False)

    GPIO.output(PIN22, True)
    GPIO.output(PIN16, False)
    return "ok"

@app.route("/right", methods=["POST"])
def right():
    GPIO.output(PIN5, False)
    GPIO.output(PIN12, True)

    GPIO.output(PIN22, False)
    GPIO.output(PIN16, True)
    return "ok"



@app.route("/", methods=["GET"])
def home():
    return render_template("button.html", title="Button", name="L’TEAM")


