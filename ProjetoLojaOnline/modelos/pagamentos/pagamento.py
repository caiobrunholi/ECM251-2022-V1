from abc import ABC, abstractmethod # Abstract Base Class

class Pagamento(ABC): # (ABC -> Pagamento é filha de ABC
    @abstractmethod
    def realizar_pagamento(self):
        pass 
