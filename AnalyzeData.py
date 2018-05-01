#Analyze data from eye tracker and emotion tracker, plot to heatmap

#imports
import matplotlib.pyplot as plt
import matplotlib.colors as col
import numpy as np

#import eyetracker data
eyetracker = [line.rstrip("\n").split(',') for line in open("CollectedData.txt")]
xCoord = [float(eyetracker[i][0]) for i in range(len(eyetracker)) if float(eyetracker[i][0])>0 and float(eyetracker[i][1])>0 and float(eyetracker[i][0])<1920 and float(eyetracker[i][1])<1080]
yCoord = [float(eyetracker[i][1]) for i in range(len(eyetracker)) if float(eyetracker[i][0])>0 and float(eyetracker[i][1])>0 and float(eyetracker[i][0])<1920 and float(eyetracker[i][1])<1080]
timeEye = [float(eyetracker[i][2].split(':', 2)[2]) for i in range(len(eyetracker)) if float(eyetracker[i][0])>0 and float(eyetracker[i][1])>0 and float(eyetracker[i][0])<1920 and float(eyetracker[i][1])<1080]

#import emotion tracker data
emotion = [line.rstrip("\n").split(',') for line in open("collectedDataEmo.txt")]
j = 0
emote = []
timeEmo = []
for i in range(len(timeEye)):
    while float(emotion[j][1].split(':', 2)[2]) < timeEye[i]:
        j = j + 1;
    emote.append(emotion[j][0])
    timeEmo.append(float(emotion[j][1].split(':', 2)[2]))

#set up color map
#0 - neutral - white - FFFFFF
#1 - disgusted - green - 00FF00
#2 - fearful - purple - 800080
#3 - happy - yellow - FFFF00
#4 - angry - red - FF0000
#5 - sad - blue - 0000FF
#6 - surprised - orange - FFA500
for i in range(len(emote)):
    if emote[i] == "neutral":
        emote[i] = 0
    elif emote[i] == "disgusted":
        emote[i] = 1
    elif emote[i] == "fearful":
        emote[i] = 2
    elif emote[i] == "happy":
        emote[i] = 3
    elif emote[i] == "angry":
        emote[i] = 4
    elif emote[i] == "sad":
        emote[i] = 5
    elif emote[i] == "surprised":
        emote[i] = 6

N=6
cpool = [ '#ffffff','#00ff00','#800080','#ffff00','#ff0000','#0000ff','#ffa500']
cmapEmo = col.ListedColormap(cpool[0:N], 'indexed')

#initialize plot
plt.clf()
heatmap = plt.figure(figsize=(16,9))
#plt.subplot(121)

#plt.xlim(0,1920)
#plt.xticks(np.linspace(0,1920,16,endpoint=True))
#plt.ylim(0,1080)
#plt.yticks(np.linspace(0,1080,9,endpoint=True))

plt.hexbin(xCoord, yCoord, gridsize=30, bins=None)
cb1 = plt.colorbar()
cb1.set_label('frequency')
#plt.subplot(122)

heatmapEmo = plt.figure(figsize=(16,9))
plt.hexbin(xCoord, yCoord, C=emote, cmap=cmapEmo, gridsize=30, bins=None)
cb2 = plt.colorbar()
cb2.set_clim(0,6)
cb2.set_label('emotion')

plt.show()
