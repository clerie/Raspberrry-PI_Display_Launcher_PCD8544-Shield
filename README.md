# Raspberrry-PI_Display_Launcher_PCD8544-Shield
A launcher for the Raspberry PI Display "PCD8544 Shield" from sunfounder.

This Launcher is written in Python.
It's tested with a Raspberry PI 2 B, Raspbian and the Sundfounder Raspberry PI PCD8544 Shield.

## Installation:

### You have to install the python-dev package:

``` sudo apt-get install python-dev ```

### Install the Drivers for the Display (some examples included):

``` git clone https://github.com/adafruit/Adafruit_Nokia_LCD.git ```

``` cd Adafruit_Nokia_LCD ```

``` sudo python setup.py install ```

### Install the Python Imaging:
 
``` sudo apt-get install python-imaging ```

### Download the Launcher:

``` git clone https://github.com/clerie/Raspberrry-PI_Display_Launcher_PCD8544-Shield.git```

You had finished the installation.

## Usage

### Run the launcher

Go to your directory:
``` cd Raspberrry-PI_Display_Launcher_PCD8544-Shield ```

``` sudo python launcher.py ```

### Use the launcher

The commands for the plugins are the filenames without the ending (.py)

All plugins are in the `plugins` directory.

### Write plugins

You can write plugins too. Simply copy theese in the `plugins` directory and enjoy.
