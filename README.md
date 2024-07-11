<h1>To run this Python script on a Raspberry Pi, follow these steps:</h1>
<br>
Set up your Raspberry Pi:
<br>
Ensure your Raspberry Pi is properly set up with Raspbian OS installed.
<br>
Connect your Raspberry Pi to a monitor, keyboard, and mouse, or use SSH to access it remotely.
<br>
Install the RPi.GPIO library (if it's not already installed):
  <br>
<h4>Open a terminal on your Raspberry Pi and run:<h4>
<br>
sudo apt-get update
<br>
sudo apt-get install python3-rpi.gpio
<h3>Save the script:<h3>

Open a text editor (like nano or vim) on your Raspberry Pi.
Copy the provided code into the text editor.
Save the file with a .py extension, for example, frequency_generator.py.
Run the script:

Open a terminal and navigate to the directory where you saved the script.
Run the script using Python 3 by typing:
<br>
python main.py
<h3>Enter the frequency:</h3>
<br>
When prompted, enter a frequency value between 1 and 80 Hz.
<br>
The script will generate the specified frequency using GPIO pin 12.
<br>
To stop the frequency generation, press Ctrl + C.
<br>
<br>
<br>

<h1>Here’s a step-by-step example using nano as the text editor:</h1>
Open a terminal.
<br>
Create and edit the script:
<br>
nano frequency_generator.py
<br>
<h4>Copy and paste the code into nano, then save and exit:</h4>
<br>
Paste the code using right-click or Ctrl + Shift + V.
<br>
Save the file by pressing Ctrl + O, then Enter.
<br>
Exit nano by pressing Ctrl + X.

<br>
<h4>Run the script:</h4>
<br>
Run the script:
<br>
python main.py
