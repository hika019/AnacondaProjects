import sys
import os
import commands as cmd
import cv2
import time
import copy
from argparse import ArgumentParser

def getHtml(query):
    return cmd.getstatusoutput("wget -O - https://www.bing.com/images/search?q=" + query)[1]
