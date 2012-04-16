class ConsoleOutput(object):
    def printOutput(self, values):
        print values
        
class StringCalculator(object):
    def __init__(self, output = ConsoleOutput()):
        self.output = output
    
    def add(self, values):
        if not values:
            return 0
        sum = 0
        values = self._handle_delimeters(values)
        negatives = []
        for value in values.split(','):
            if int(value) < 0:
                negatives.append(value)
            elif int(value) <= 1000:
                sum += int(value)
        if len(negatives) > 0:
            raise ValueError("negatives not allowed " + " ".join(negatives))
        self.output.printOutput("The result is " + str(sum))
        return sum
    
    def _handle_delimeters(self, values):
        if values.startswith('//'):
            delims = []
            found = 0
            for idx, c in enumerate(values):
                if c == '[':
                    found = idx
                if c == ']':
                    delims.append(values[found+1:idx])
            values = values[values.find('\n')+1:]
            for delim in delims:
                values = values.replace(delim, ',')
        return values.replace('\n', ',')    