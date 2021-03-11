from abc import ABC, abstractmethod


class Dataset(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def fetch(self):
        pass
    
    @abstractmethod
    def unpack(self):
        pass
    
    @abstractmethod
    def push(self):
        pass