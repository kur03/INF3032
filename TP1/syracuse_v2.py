class Syracuse :
    
    def __init__(self, filename) :
        self.filename = filename
        self.nbr = 0
        self.file = None
        
    def load_value(self):
        self.file = open(self.filename, "r+") 
        self.nbr = int(self.file.read())

    def calculate(self):
        self.load_value()
        count = 0
        while (self.nbr != 1) :
            if (self.nbr % 2 == 0) :
                self.nbr = int(self.nbr/2)
                count += 1

            else :
                self.nbr = int(self.nbr*3+1)
                count += 1
            self.file.write(str(self.nbr) + "\n")


        self.file.write("There were "+ str(count)+ " iteration until we reached 1.\n")
        self.file.close()
    
    def get_result(self):
        self.file = open(self.filename, 'r')
        print(self.file.read())
        self.file.close()
        
        
        
syracuse = Syracuse('syracuse.txt')
syracuse.calculate()
syracuse.get_result()