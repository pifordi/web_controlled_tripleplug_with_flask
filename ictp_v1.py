__author__ = 'Semih YILDIRIM'

from flask import Flask, request, render_template, redirect
import time
from wiringx86 import GPIOGalileo as Galileo
from threading import Timer


plug_status = {'a':'off', 'b':'off', 'c':'off'}

gpio = Galileo(debug = False)

plug_a_ctrl = 9
plug_b_ctrl = 10
plug_c_ctrl = 11

gpio.pinMode(plug_a_ctrl, gpio.OUTPUT)
gpio.pinMode(plug_b_ctrl, gpio.OUTPUT)
gpio.pinMode(plug_c_ctrl, gpio.OUTPUT)

gpio.digitalWrite(plug_a_ctrl, gpio.HIGH)
gpio.digitalWrite(plug_b_ctrl, gpio.HIGH)
gpio.digitalWrite(plug_c_ctrl, gpio.HIGH)

class parse_command:
    global plug_a_ctrl
    global plug_b_ctrl
    global plug_c_ctrl


    @staticmethod
    def parse_name(name):
        if name == "a":
            plug = plug_a_ctrl
        elif name == "b":
            plug =  plug_b_ctrl
        elif name == "c":
            plug = plug_c_ctrl
        return plug

    @staticmethod
    def parse_turn_mode(turn_mode):
        if turn_mode == "on":
            level = gpio.LOW #normally we need to use gpio.HIGH but our relay module is low trigger
        elif turn_mode == "off":
            level = gpio.HIGH #normally we need to use gpio.LOW but our relay module is low trigger
        return level

    @staticmethod
    def parse_interval(number, smh):
        number = float(number)

        if smh == "second":
            interval = number*1
        if smh == "minute":
            interval = number*60
        elif smh == "hour":
            interval = number*3600
        return interval


def control(name, turn_mode):
    gpio.digitalWrite(parse_command.parse_name(name), parse_command.parse_turn_mode(turn_mode))
    
    plug_status[name] = turn_mode
        
def rule(name, turn_mode, number, smh, then):
    plug_status.get
    control(name, turn_mode)
    start = time.time()
    future_time = parse_command.parse_interval(number, smh) + start
    name = Timer(parse_command.parse_interval(number, smh), control, [name, then])
    name.start()




app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
    return redirect('home')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', a=plug_status.get('a'), b=plug_status.get('b'), c=plug_status.get('c'))

@app.route('/plugs', methods=['GET', 'POST'])
def plugs():
    return render_template('plugs.html', a=plug_status.get('a'), b=plug_status.get('b'), c=plug_status.get('c'))


@app.route('/home/turnall', methods=['POST'])
def home_turnall():
    turn_mode = request.form['turnall']

    control('a', turn_mode)
    control('b', turn_mode)
    control('c', turn_mode)

    return render_template('home.html', a=plug_status.get('a'), b=plug_status.get('b'), c=plug_status.get('c'))
   

@app.route('/plugs/control', methods=['POST'])
def plugs_control():
    plug = request.form['plug']
    turn_mode = request.form['turn']
    
    control(plug, turn_mode)

    return render_template('plugs.html', a=plug_status.get('a'), b=plug_status.get('b'), c=plug_status.get('c'))

@app.route('/plugs/rule', methods=['POST'])
def plugs_rule():
    plug = request.form['plug']
    turn_mode = request.form['turn']
    smh = request.form['smh']
    number = request.form['number']
    then = request.form['then']

    rule(plug, turn_mode, number, smh, then)

    return render_template('plugs.html', a=plug_status.get('a'), b=plug_status.get('b'), c=plug_status.get('c'))


if __name__ == '__main__':
    app.run(host='192.168.1.29' , threaded=True, port=3936) #app.run(host='0.0.0.0') This tells your operating system to listen on all public IPs

