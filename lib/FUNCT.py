#----------------------------------------------------------------------------------
#                 Operations Object for Simple Calculator Application
#----------------------------------------------------------------------------------
class Operations():
    def __init__(self) -> None:
        #Initialize Operations
        self.num1  = "0"
        self.num2  = "0"
        self.oper  = ""
        self.operations = ["+","-","×","÷"]
        self.eq   = "0"
        self.ans  = None
        #Keep a running variable of num1,oper,num2

    def getEq(self):
        return self.eq
    
    #Update the equation parameters
    def updatePar(self):
        #Format Numbers
        def formatNum(num):
            if float(num) % 1 == 0 and num[-1] != ".": 
                num = str(int(float(num)))
                print("hi")
            elif float(num) % 1 != 0:
                num = str(round(float(num),6))
            
            return num

        #Update state variables
        spliteq = self.eq.split(" ") 
        if len(spliteq)   == 1:
            self.num1, self.oper, self.num2 =  formatNum(spliteq[0]) , "" , "0"   
            self.eq = self.num1

        elif len(spliteq) == 2:
            self.num1, self.oper =  formatNum(spliteq[0]), " " + spliteq[1] + " "
            self.eq = self.num1 + self.oper
            
        elif len(spliteq) == 3:
            self.num1, self.oper, self.num2 = formatNum(spliteq[0]), " " + spliteq[1]+ " ", formatNum(spliteq[2])
            self.eq = self.num1 + self.oper + self.num2
 

        print("Num1: ",self.num1, "\nOper: ", self.oper,"\nNum2: ", self.num2, "\n")

    def setNum(self,i):
        if self.eq == "Error":
            self.eq = i
        #Cases for leading 0s    
        elif self.eq == "0":
            if i == "0":          pass
            elif "⁻" in self.eq:  self.eq = "⁻" + i
            else:                 self.eq = i
        #Next 2 elif probably can be combined
        elif self.oper != "" and self.num2 in ["0","⁻0"]:
            if i == "0":           pass
            elif "⁻" in self.num2: self.eq = self.eq[:-2] + "⁻" + i
            else:                  self.eq = self.eq[:-1] + i 
        elif self.oper != "" and i != "0":
            if self.num2  == "0":  self.eq = self.eq[:-1] + i     
            else:                  self.eq += i 
        #Normal
        else: self.eq += i 
        self.updatePar()

    #Set the math operand
    def setOper(self,i):
        if self.eq == "" or self.eq == "Error":
            pass
        if self.oper == "":
            self.oper = " " + i + " "
            self.eq += self.oper + "0"
        elif self.oper != "" and self.num2 != 0:
            self.oper = " " + i + " "
            self.eq = self.eq[:-4] + self.oper + "0"     
        else: pass
        self.updatePar()

    #Set decimals
    def setDec(self):
        if self.oper == "" and "." not in self.num1:
            self.eq+="."
        elif self.oper != "" and "." not in self.num2:
            self.eq+="."
        self.updatePar()

    #Set positive or negative numbers
    def setPosNeg(self):
        if self.oper == "" and "⁻" not in self.eq:
            self.eq = "⁻" + self.eq
        elif self.oper == "" and "⁻" in self.eq:
            self.eq = self.eq[1:]
        if self.oper != "" and "⁻" not in self.num2:
            self.eq = self.num1 + self.oper + "⁻" + self.num2
        elif self.oper != "" and "⁻" in self.num2:
            self.eq = self.num1 + self.oper + self.num2.replace("⁻","")

        self.updatePar()

    #Percentage function
    def setPer(self):
        if self.oper != "": 
            self.eq = self.num1 + self.oper + str(float(self.num2) / 100)
        else: self.eq = str(float(self.num1) / 100)
        self.updatePar()

    #Clear current number
    def numClear(self):
        if self.oper != "": self.eq = self.eq[:-4] + "0"
        else: self.eq = "0"
        self.updatePar()

    #Clear equation
    def fullClear(self):
        self.eq = "0"
        self.updatePar()

    #Backspace
    def delChar(self):
        if self.oper != "": 
            if self.eq[-1] == " ": self.eq = self.eq[:-3]
            else:                  self.eq = self.eq[:-1]
        else: self.eq = self.eq[:-1]
        self.updatePar()

    #Invert num
    def invNum(self):
        if self.oper != "": 
            self.eq = self.num1 + self.oper + str((1 / float(self.num2)))
        else: self.eq = str((1 / float(self.num1)))
        self.updatePar()
    
    #Square num
    def sqNum(self):
        if self.oper != "": 
            if "⁻" not in self.num2: self.eq = self.num1 + self.oper + str(float(self.num2)**2)
            else:                    self.eq = self.num1 + self.oper + str(float(self.num2[1:])**2)
        else:
            if "⁻" not in self.num1: self.eq = str(float(self.num1)**2)
            else:                    self.eq = str(float(self.num1[1:])**2)
        self.updatePar()

    #Square root num
    def sqrtNum(self):
        if self.oper != "" and "⁻" not in self.num2: 
            self.eq = self.num1 + self.oper + str(float(self.num2)**0.5)
        elif self.oper == "" and "⁻" not in self.num1: 
            self.eq = str(float(self.num1)**0.5)
        else:
            self.eq = "Error"
        self.updatePar()

    def solve(self):
        #Define num & oper
        spliteq = self.eq.split(" ")
        self.num1, self.oper, self.num2

        #Format negatives nums
        if "⁻" in self.num1: self.num1 = -1 * float(self.num1[1:])
        else:           self.num1 = float(self.num1)
        if "⁻" in self.num2: self.num2 = -1 * float(self.num2[1:])
        else:           self.num2 = float(self.num2)

        #Run Operations
        if "+" in self.oper:
            result = self.num1 + self.num2
        if "-" in self.oper:
            result = self.num1 - self.num2
        if "×" in self.oper:
            result = self.num1 * self.num2
        if "÷" in self.oper and self.num2 != 0: 
            result = self.num1 / self.num2
        if "÷" in self.oper and self.num2 == 0:  #Div 0 Error
            result = "Error"
            self.eq = result
        
        #Format result
        if result != "Error":    
            if result % 1 == 0: result = int(result)
            if result > 0:    self.eq = str(result)
            elif result == 0: self.eq = str(0)
            else:             self.eq = "⁻" + str(-1 * round(result,5))
        self.updatePar()

