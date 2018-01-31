import numpy as np
import cv2
import os


def readFrames(path):
	flag = 0
	frameCounter=1
	folderCounter = 1
	foldername = "round_"+str(folderCounter)+"/"
	path = path+foldername
	cap = cv2.VideoCapture(0)
	while(True):
	    	ret, frame = cap.read()
	    	cv2.imshow('frame',frame)

		if(flag == 1):
			#resetting flag
			flag = 0
			folderCounter+=1
			os.makedirs(path+"round_"+str(folderCounter))
			frameCounter=1

			foldername = "round_"+str(folderCounter)+"/"
			path = path+foldername


		fname = "frame_"+str(folderCounter)+"_"+str(frameCounter)+".jpg"
		print(path+fname)
		cv2.imwrite(os.path.join(path, fname), frame)
		frameCounter+=1


	    	if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()



if __name__ == "__main__":
	
	path = "images/"
	readFrames(path)

