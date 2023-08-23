

class myFruit():
    """
    Basic class of a fruit

    :type kind = str
    :type weight = double
    """
    kind = ""
    weight = 0

    def __init__(self, kind = "airfruit", weight=0):
        self.kind = kind
        self.weight = weight
    
    def weight(self):
        """
        Returns weight of a fruit
        """
        return self.weight 
    
    def kind(self):
        """
        Returns kind of a fruit
        """
        return self.kind
