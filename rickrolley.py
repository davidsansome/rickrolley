from waveapi import document
from waveapi import events
from waveapi import model
from waveapi import robot
import logging

GADGET_URL = 'http://rickrolley.appspot.com/gadgets/rickroll.xml'
ROBOT_EMAIL = 'rickrolley@appspot.com'

def OnRobotAdded(properties, context):
  # Add a new rickroll when we're added to a wave
  RickrollBlip(context.GetRootWavelet().CreateBlip())

def OnBlipDeleted(properties, context):
  blip = context.GetBlipById(properties['blipId'])
  if blip.GetCreator() == ROBOT_EMAIL:
    # Someone removed our rickroll!
    RickrollBlip(context.GetRootWavelet().CreateBlip())

def OnBlipSubmitted(properties, context):
  blip = context.GetBlipById(properties['blipId'])
  if blip.GetCreator() == ROBOT_EMAIL:
    # Someone changed our rickroll!
    RickrollBlip(blip)

def RickrollBlip(blip):
  doc = blip.GetDocument()
  doc.Clear()
  doc.AppendElement(document.Gadget(GADGET_URL))

if __name__ == '__main__':
  myRobot = robot.Robot('Rickrolley',
      image_url='http://rickrolley.appspot.com/images/icon.jpg',
      version='27',
      profile_url='http://rickrolley.appspot.com/')
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  myRobot.RegisterHandler(events.BLIP_DELETED, OnBlipDeleted)
  myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
  myRobot.Run()
