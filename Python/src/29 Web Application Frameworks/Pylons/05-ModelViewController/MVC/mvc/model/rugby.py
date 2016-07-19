class Rugby:
    @staticmethod
    def initializeData():
        Rugby.table = (("Wales",    6), 
                       ("Scotland", 4),
                       ("Ireland",  2),
                       ("England",  0))

    @staticmethod
    def readData():
        return Rugby.table
    
