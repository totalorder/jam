# encoding: utf-8
import network

class StubCamera:
    def addDrawable(self, obj):
        pass

class Gamestate(object):
    def __init__(self, clients=None,inputstate=None, camera=None):
        self.camera = camera if camera else StubCamera()
        self.clients = clients
        self.inputstate = inputstate
        self.clientcommandrepo = network.ClientCommandRepository()
        self.servercommandrepo = network.ServerCommandRepository()

    def update(self, dt, packet):
        pass