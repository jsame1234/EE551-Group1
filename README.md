# EE551-Group1
For EE551 Engineering Python, group consisting of Sam Fishman, Bryan Jimenez, Peter Brine

To run:
	For the eye tracking software run the eyeDetect.py program. You will be prompted to enter 1 to run the main program, 2 to run the training program, or 3 to run eye detection calibration.
	Main program:
		This will load the saved training data from the csv file and estimate where you are looking on the screen. The coordinates of these gaze estimations are being saved to a text file (collectedData.txt), along with a timestamp for each recording.	
	Training program:
		You click where you're looking, and, after around 10-20 such clicks, the program will learn the correspondence and start drawing a blue blur where you look. It's important to keep your head still (in position AND angle) or it won't work. Training data will be saved to a csv file.
	Eye Detection calibration:
		You should do this first. There should be a green line from your forehead to one pupil; the end of the line is the estimate of pupil position. The blue circles should generally track your pupils, though less reliably than the green line. If performance is bad, you can tweak the "TUNABLE PARAMETER" lines. (This is a big area where improvement is needed; probably some learning of parameters.)
