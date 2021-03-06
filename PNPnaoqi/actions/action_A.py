import qi
import argparse
import sys
import time
import threading

import action_base
from action_base import *


actionName = "A"


def actionThread_exec (params):
    t = threading.currentThread()
    memory_service = getattr(t, "mem_serv", None)
    print "Action "+actionName+" started with params "+params
    if params=='':
        params = '3' # default
    # action init
    dt = 0.25
    count = int(float(params) / dt)
    # action init
    while (getattr(t, "do_run", True) and count>0): 
        print "Action "+actionName+" "+params+" exec..."
        #print "DEBUG:: Action thread ",t," run ",getattr(t, "do_run", True)
        # action exec
        count = count-1
        # action exec
        time.sleep(dt)

    # action end
    count = 0
    # action end
    action_termination(actionName,params)
    #action_success(actionName,params)
    #action_failure(actionName,params)


def init(session):
    print actionName+" init"
    action_base.init(session, actionName, actionThread_exec)


def quit():
    print actionName+" quit"
    actionThread_exec.do_run = False


if __name__ == "__main__":

    print('Starting action server for action %s (CTRL-C to quit)' %actionName)

    app = action_base.initApp(actionName)
        
    init(app.session)

    #Program stays at this point until we stop it
    app.run()

    quit()

