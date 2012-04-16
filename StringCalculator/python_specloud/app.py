from String_calculator import *
import sys

class Input(object):
    def __init__(self):
        self.input = ""
    
    def getInput(self):
        temp = raw_input()
        self.input = temp.strip()
        return self.input

class App(object):
    def __init__(self, args, output, input):
        self.args = args
        self.output = output
        self.sc = StringCalculator(output)
        self.input = input
        self.input.input = args
        self.sc.add(self.input.input)
        
    def getNextUserInput(self):
        self.output.printOutput("another input please")
        self.sc.add(self.input.getInput())
        return self.input.input

    def run(self):
        while self.getNextUserInput() != "":
            continue
            
        
if __name__ == "__main__":
    app = App(sys.argv[1], ConsoleOutput(), Input())     
    app.run()