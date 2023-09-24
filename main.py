import openai, os
from distributions.distro import Distro
from schedulers.scheduler import scheduler

class Agent:
    def __init__(self, api_key, debug = False, cls = False):
        self.api_key = api_key
        openai.api_key = api_key
        self.debug = debug
        self.cls = cls
        if self.cls == 'cls': os.system('cls')
        if self.cls == 'clear': os.system('clear')
        if self.debug: print("Agent Initalized")

    def _generate(self):
        self.person = Distro()
        self.data = self.person.generate()
        if self.debug: print("Generated Person Data")
        self.data.update({"schedule" : scheduler(str(self.data))})
        if self.debug: print("Generated Schedule")
        return self.data
