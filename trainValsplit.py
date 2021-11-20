import os

train = open('filelists/train.txt', 'w')
test = open('filelists/val.txt', 'w')

base = None # Path to processed dataset folder 

folders = None # Name of a dataset folder

for folder in folders:
    videos = os.listdir(os.path.join(base, folder))
    for i in range(len(videos)):
        thingToWrite = os.path.join(folder, videos[i]) + '\n'
        if i % 10 == 0:
            test.write(thingToWrite)
        else:
            train.write(thingToWrite)

train.close()
test.close()