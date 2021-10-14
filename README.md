# Ant Colony Optimization Problem
This project is used to simulate the behaviour of an edge server that has to assign tasks to devices based on pheromone levels, it used the ant colony optimization algorithm base idea that the path with the most pheromone level is used.

## Setting up project
To get the project up and running, you need to setup a virtual environment using pipenv 

Ensure you have pipenv installed on your system. If you do not have it, run `pip instal pipenv`.

After cloning the project, cd into the ubiquitous-enigma directory.

In the ubiquitous-enigma directory, run:
`pipenv install` to create and install packages used in this project followed by `pipenv shell` to activate the virtual environment.

## Running project
If all the above was done successfully, run the program by using  `python ant.py`.


## Packages used in this project
* [Pynput](https://pynput.readthedocs.io/en/latest/, "Pynput") - This library allows you to control and monitor input devices. I used this package to detect keyboard inputs.

* [Rich](https://github.com/willmcgugan/rich, "Rich") - Rich is a Python library for rich text and beautiful formatting in the terminal.

## Project Images