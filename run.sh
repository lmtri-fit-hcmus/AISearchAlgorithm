#!/bin/bash

echo Initialize python library

python3 -m pip install --upgrade pip
pip install moviepy.editor
pip install pygame
pip install numpy

python3 source/main.py