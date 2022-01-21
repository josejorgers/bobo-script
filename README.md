# Robobo explorer

A solution for a Robobo explorer robot.

## Installation

This solution is written with Python3. Besides that, the only dependency is the Robobo.py library, you can read about it [here](https://pypi.org/project/robobopy/).

Nevertheless, the recommended way to use this project is to have [conda](https://docs.conda.io/en/latest/) installed and running ```conda env create -f environment.yml``` in the root directory of this project. After that, you can activate the environment with ```conda activate bobo-script```. And run the project with ```python src/main.py```.

But if you already have the required dependencies installed, you can run the project with ```python src/main.py``` directly.

## Execution specifications

Make sure you are using the correct IP address of the Robobo. You can check the file ```src/constants/connections.py``` and change the variable ```LOCAL``` to the desired IP address. Keep in mind that the code in the branch ```simulator``` of this repository is intended to be ran on the Robobo Simulator while the code in the branch ```real-life``` is intended to be ran on the real Robobo.

If you want to tune some sensors of the Robobo, you can do it in the files inside de ```src/constants``` module.

## Documentation

Refer to the ```doc``` folder for the documentation (in Spanish).
