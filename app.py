from typing import Any
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.datetime import TimeField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired
from apscheduler.schedulers.background import BackgroundScheduler
from functions.helpers import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'A7xc5poOYNA7J8Xenv8v0CqWhL66Do2b'

Bootstrap(app)

scheduler = BackgroundScheduler()
scheduler.start()

downSchedule = None
upSchedule = None

downTime = None
upTime = None

class ControlForm(FlaskForm):
    value = IntegerField('Value')
    submitUp = SubmitField('Up')
    submitDown = SubmitField('Down')

class InitForm(FlaskForm):
    submitMin = SubmitField('Min')
    submitMax = SubmitField('Max')
    submitRst = SubmitField('Reset')

class ScheduleForm(FlaskForm):
    downTime = TimeField(downTime)
    upTime = TimeField(upTime)
    submitTime = SubmitField("Set Time")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/control", methods=["GET", "POST"])
def control():
    controlForm = ControlForm()

    if request.method == "POST":
        if controlForm.submitUp.data and controlForm.value.data:
            print("UP")
            value = controlForm.value.data
            blindsUp(value)
            controlForm.submitUp.data = False
            controlForm.submitDown.data = False
        elif controlForm.submitDown.data and controlForm.value.data:
            print("DOWN")
            value = controlForm.value.data
            blindsDown(value)
            controlForm.submitUp.data = False
            controlForm.submitDown.data = False

    return render_template("control.html", controlForm=controlForm)

@app.route("/initialize", methods=['GET', 'POST'])
def initialize():
    controlForm = ControlForm()
    initForm = InitForm()
    error = None

    if request.method == "POST":
        if controlForm.submitUp.data and controlForm.value.data:
            print("UP")
            value = controlForm.value.data
            blindsUp(value)
            controlForm.submitUp.data = False
            controlForm.submitDown.data = False
        elif controlForm.submitDown.data and controlForm.value.data:
            print("DOWN")
            value = controlForm.value.data
            blindsDown(value)
            controlForm.submitUp.data = False
            controlForm.submitDown.data = False

        if initForm.submitMin.data:
            if setMin():
                error = False
            else:
                error = True

            print("MIN")
        elif initForm.submitMax.data:
            if setMax():
                error = False
            else:
                error = True

            print("MAX")
        elif initForm.submitRst.data:
            reset()

            print("RST")

    return render_template("initialize.html", controlForm=controlForm, initForm=initForm)

@app.route("/timer", methods=['GET', 'POST'])
def timer():
    global downSchedule, upSchedule, downTime, upTime

    scheduleForm = ScheduleForm()

    if request.method == 'POST':
        if scheduleForm.downTime.data:
            downTime = scheduleForm.downTime.data
            print("DT: " + str(downTime))
        
        if scheduleForm.upTime.data:
            upTime = scheduleForm.upTime.data
            print("UT: " + str(upTime))

        if scheduleForm.downTime.data and scheduleForm.upTime.data and scheduleForm.submitTime.data: 
            print("SCHEDULED_UT")

            if downSchedule:           
                downSchedule.remove()
                downSchedule = None
                print("REMOVED_UT")

            downSchedule = scheduler.add_job(blindsDown, 'cron', hour=downTime.hour, minute=downTime.minute)

            scheduleForm.submitTime.data = False
        
        if scheduleForm.upTime.data and scheduleForm.submitTime.data:
            print("SCHEDULED_DT")

            if upSchedule:
                upSchedule.remove()
                upSchedule = None
                print("REMOVED")

            upSchedule = scheduler.add_job(blindsUp, 'cron', hour=upTime.hour, minute=upTime.minute)

            scheduleForm.submitTime.data = False


    return render_template("timer.html", scheduleForm=scheduleForm, downTime=downTime, upTime=upTime)
    
if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')