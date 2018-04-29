#!/bin/bash
echo "Starting emotion recognition..."
python emotion_recognition.py poc &
echo "Starting eye detection..."
python eyeDetect.py 1 &
