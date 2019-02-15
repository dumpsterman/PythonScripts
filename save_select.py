import shutil
import distutils.dir_util
from os import listdir
import time

def loadSave(save):
    try:
        distutils.dir_util.copy_tree(gameLoc + r, gSave + 'Temp Save')
        distutils.dir_util.copy_tree(gSave + save, gameLoc + r)
        print('Load complete.')
        return True

    except distutils.errors.DistutilsFileError:
        print('That save name does not exist')
        return False

    except:
        print('An error occured.')
        return False

def addSave(saveName):
    try:
        shutil.copytree(gameLoc + r, gSave + saveName)
        print('Save added.')
        return True

    except:
        print('An error occured.')
        return False


r = r"/remote"
gameLoc = r""
gSave = r""
saveDir =  listdir(gSave)
time = time.localtime()[1:5]
userInput = ''
state = False


while userInput != 'add' or userInput != 'load':

    userInput = input('Add or Load save?\n').lower()

    if userInput == 'add':
        save = input('Save Name?\n')+ " " + str(time)
        state = addSave(save)

    if userInput == 'load':
        print(saveDir)
        state = loadSave(input('Pick a save name to load.\n'))

    if state:
        break

input('Press enter to exit.')
