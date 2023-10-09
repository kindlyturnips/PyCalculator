#----------------------------------------------------------------------------------
#                 SOUNDING OBJECT TO READ AND FIND SOUNDING DATA
#----------------------------------------------------------------------------------
class Sounding():
    def __init__(self,filename=None):
        #Initialize Sounding Variables
        #Optional filename argument with default
        self.filename = filename if filename is not None else r"./Data.txt"
        self.range    = None
        self.depth    = None
        self.grid     = None

        #Read Sounding Variables
        self.readData(self.filename)
    
    #Method to Read Data
    def readData(self,filename):
        with open(filename,"r") as data_file:
            data = data_file.readlines()
        data_file.close()

        #Cast Range & Depth into Arrays
        self.range = np.array( [int(i) for i in data[0].split(',')])
        self.depth = np.array( [int(i) for i in data[1].split(',')])

        #Cast Grid Data into Matrix
        grid_raw  = np.array( [int(i) for i in data[2].split(',')])
        self.grid = np.zeros((self.depth.size,self.range.size))

        #Iterate through array and populate matrix
        i , j = 0 , 0
        for k in range(grid_raw.size):
            self.grid[i,j] = grid_raw[k]
            i += 1
            if i % self.depth.size == 0:
                i = 0
                j+=1

    #Method to Find Sounding Value
    def findData(self,query_range,query_depth):

        #Create Absolute Distance arrays
        dist_range = abs( self.range - np.ones(self.range.size) * query_range )
        dist_depth = abs( self.depth - np.ones(self.depth.size) * query_depth )

        #Find closest depth and range
        min_range_j = np.argmin(dist_range)
        min_depth_i = np.argmin(dist_depth)

        return self.grid[min_depth_i, min_range_j]
    
    #Method to Test n Number of Random Queries
    def testFind(self,n):
        print(f"TESTING FIND\n\
              Range: {self.range}\n\
              Depth: {self.depth}\n\
              Grid: {self.grid[0]}\n\
                    {self.grid[1]}\n\
                    {self.grid[2]}\n")
                    
        #Generate Random Querys & Subsuquent Arrays n times
        for i in range(0,n):       
            test_range  = randint( 0  , max(self.range)  ) + random()
            test_depth  = randint( 0  , max(self.depth)  ) + random()
            test_answer = self.findData( test_range, test_depth )
            print(f"\
                  Test:        {i}\n\
                  Test Range:  {test_range}\n\
                  Test Depth:  {test_depth}\n\
                  Test Answer: {test_answer}\n")



