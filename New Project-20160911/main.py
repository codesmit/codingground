class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)
    def status(self):
        print self.data 
s = Bag()
s.add(34)
s.add('idiot')
s.add('me')
s.status()

