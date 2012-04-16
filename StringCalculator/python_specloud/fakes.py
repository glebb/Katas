class FakeConsoleOutput(object):
    def __init__(self):
        self.output = []
    
    def printOutput(self, output):
        self.output.append(output)
        
class FakeInput(object):
    def __init__(self):
        self.input = ""
        
    def getInput(self):
        return self.input