class Football:
    @staticmethod
    def initializeData():
        Football.table = (("Man Utd", 6), 
                          ("Chelsea", 4),
                          ("Everton", 2),
                          ("Spurs",   0))

    @staticmethod
    def readData():
        return Football.table
    
