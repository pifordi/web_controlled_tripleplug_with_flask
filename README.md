# internet Controlled TriplePlug with_flask
Web-controlled triple plug with flask and wiring-x86. Intel Galileo Gen1 used to evaluate the project. 

<p>
Firstly you need to install ubilinux is based on Debian Wheezy(ehttp://www.emutexlabs.com/ubilinux) and also instructions about installing and booting the board with ubilinux is available on my blog in Turkish(https://yildirimsemih.wordpress.com/2015/07/02/ubilinux-kurulumu-wiringx86-moduluyle-led-kontrolu-intel-galileo-python/)
</p>

<p>
And, then you need to install required software packages on the board. Use the following commands respectively;

<p>
<strong>apt-get update</strong> //update package versions
</p>
<p>
<strong>apt-get install python-pip</strong> //install python package manager. it will be used to install some python modules
</p>
<p>
<strong>pip install wiring-x86</strong>  //install wiring module for Galileo based on i386 (http://wiring-x86.readthedocs.org/)
</p>
<p>
<strong>pip install Flask</strong>  //install python microweb frame work is main module for us (http://flask.pocoo.org/)
</p>
<p>
<strong>apt-get install tmux</strong>  //tmus is a terminal managing tool for linux. you can create one more than terminal. localtunnel and flask                         //has debug console and we need to use 2 terminal window for each one
</p>
    <p>(Ctrl-b) + n : Move to next window</p>
    <p>
    (Ctrl-b) + p : Move to previous window
    </p>
    <p>(Ctrl-b) + w : Interactively choose the window (useful if you have more than 2 window)
    </p>
    <p>
    (Ctrl-b) + & : Close a window, simply press
    </p>
<p>
<strong>apt-get install --yes nodejs</strong> // install nodejs to use localtunnel is used for sharing local server globally. i.e. your server has                              //global ip and it is accesable globally on all over the world
</p>
<p>
<strong>apt-get install npm</strong>  // install node pas-ckage manager to install localtunnel
</p>
<p>
    <strong>npm install --save localtunnel //install localtunnel (http://localtunnel.me/) </strong>
</p>    
<p>
Fianlly, Galileo is ready for evaluate our icto_v1.py(main script) and galileotoworld.js(localtunnel)
The circuit part of the project is easy and not required improved skills for construct them. We use a relay module which works with 5V and some jumpers to connect it on Galileo pins.
You need to be careful for high voltages. And you know I am not responsible damages on you. 
Constructing the circuit and other documents is avalilable on my blog(https://yildirimsemih.wordpress.com/) in Turkish. 
</p>

