from . import Curl

class Cdi:
    
    def __init__(self):
        self.domain = 'finance.yahoo.com'
        self.curl = Curl()
    
    def get_cdi_atual(self):
        pass