from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.uix.button import Button
#from kivy.uix.popup import Popup
from kivy.uix.label import Label
import glob
import json
from theta_REF1 import *


from UMLspaces_v1 import *
from theta_REF1 import *

# 2016-06-05 WORKING!
# DONE ok via csv reader: need to add rooms, better data structure/list definition
# DONE though we can neaten up with "uiClean" function ...and ... can we delete a button? We'd want to kill lower level buttons when we change
# higher level buttons
# and ... can we package with a __main__ and deploy on qpyton?
# or ... package to apk with buildozer or the cloud solution?

# list of our 4 campuses
campuses = []
# Dictionary of all buildings, with campus keys
campBldgs = {}
# Dictionary of floors; buildings are the keys
bFlrs = {}
#Dictionary of roooms, 'BLDGID'-'FLOOR' is the key
rooms = {}
    
initUMLspaces(campuses, campBldgs, bFlrs, rooms)
    
def campusHandler(campusSpn, text):
    #print('The spinner', campusSpn, 'have text', text)
    bldgSpn.values = campBldgs[text]
    if (bldgSpn.text != "Building"):
        bldgSpn.text = "Building"
    # reset other spinners, if nec
    if (flrSpn.text != "Floor"):
        flrSpn.text = "Floor"
    if (rmSpn.text != "Room"):
        rmSpn.text = "Room"
    if (takePhoto.text != "Take Photo"):
        takePhoto.text = "Take Photo"
    
def bldgHandler(bldgSpn, text):
    print (text + "-" + campusSpn.text)
    if (text != "Building"):
        flrSpn.values = bFlrs[text]
    if (flrSpn.text != "Floor"):
        flrSpn.text = "Floor"
    if (rmSpn.text != "Room"):
        rmSpn.text = "Room"
    if (takePhoto.text != "Take Photo"):
        takePhoto.text = "Take Photo"
        
def flrHandler(flrSpn, text):
    if (text != "Floor"):
        print (text + "-" + bldgSpn.text)
        rmSpn.values = rooms[(bldgSpn.text+'-'+flrSpn.text)]    
    if (rmSpn.text != "Room"):
        rmSpn.text = "Room"
    if (takePhoto.text != "Take Photo"):
        takePhoto.text = "Take Photo"

def rmHandler(rmSpn, text):
    # What directory??
    takePhoto.text = (bldgSpn.text + '-' + rmSpn.text)
    # REMEMBER: we need to add Callback and theta library
    # and, we should check if this room/photo exists and, if it does,
    # ask to confirm taking a 2nd photosphere. Append number to end also

def takePhotoHandler(instance):
    outFile = "C:\\Theta\\" + instance.text + ".JPG"
    print "Take Theta: ", outFile
    #Check for file existence
    if (os.path.isfile(outFile) == True):
        print "FILE ALREADY EXISTS", instance.text + ".JPG"
        #we should list all files with the base filename plus hyphen
        #use length of that list to get new filename, change button
        # log into log are, diff color text?
        status1.text = (status1.text + "\nFile already exists: " + outFile)
    else:
        print "Doesn't exist yet: ", (outFile)
        #NO status = takeTheta(instance.text + ".JPG")
        sid = startSession()
        takePicture(sid)
        getImage(latestFileUri(),outFile)
        print "Photo complete"
        #print status
        status1.text = (status1.text + " COMPLETE")
def checkForFile(fname):
    retVal = glob.glob(fname + "*.JPG")
root = Widget()


campusSpn = Spinner (
    # default value shown
    text='Campus',
    values = campuses,
    # just for positioning in our example
    size_hint=(None, None),
    size=(100, 44),
    pos_hint={'center_x': .5, 'center_y': .5}
)
campusSpn.bind(text=campusHandler)

bldgSpn = Spinner(
    # default value shown
    text='Building',
    values = ['Pick Campus first'],
    #values = bldgs
    # just for positioning in our example
    size_hint=(None, None),
    size=(100, 44),
    pos=(100,0)
    )
bldgSpn.bind(text=bldgHandler)

flrSpn = Spinner(
    # default value shown
    text='Floor',
    # available values
    values=['Pick Building first'],
    # just for positioning in our example
    size_hint=(None, None),
    size=(100, 44),
    pos=(200,0)
    )
flrSpn.bind(text=flrHandler)


rmSpn = Spinner(
    # default value shown
    text='Room',
    # available values
    values=['PickFloorFirst'],
    # just for positioning in our example
    size_hint=(None, None),
    size=(100, 44),
    pos=(300,0)
    )
rmSpn.bind(text=rmHandler)

takePhoto = Button (
    text='Take Photo',
    size_hint=(None,None),
    size=(200,44),
    pos=(400,0)
    )
takePhoto.bind(on_press=takePhotoHandler)

status1 = Label (
    text="Status reports here",
    padding_x=10,
    padding_y=10,
    pos=(50,400)
    )

root.add_widget(campusSpn)
root.add_widget(bldgSpn)
root.add_widget(flrSpn)
root.add_widget(rmSpn)
root.add_widget(takePhoto)
root.add_widget(status1)

runTouchApp(root)
