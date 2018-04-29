#!/bin/bash
echo "Starting emotion recognition"
python emotion_recognition.py poc &
python eyeDetect.py 1 &
