class Tier:

    def __init__(self, name):
        self.name = name
        
    

    def fressen(self, futter):
        print("Mmhh, " + futter.proNomen + " " + futter.name + " war aber lecker!")

    
    def gibLaut(self):
        raise NotImplementedError()