#----------------------------------------------------------------------------------
#                 Operations Object for Simple Calculator Application
#----------------------------------------------------------------------------------
class Operations():
    def __init__(self) -> None:
        #Initialize Operations
        self.num  = ""
        self.oper = ["+","-","×","÷"]
        self.eq   = "0"
        self.ans  = None
        #Keep a running variable of num1,oper,num2

    def getEq(self):
        return self.eq
    
    def setNum(self,i):
        if self.eq == "Error":
            self.eq = i
        #Cases for leading 0s    
        elif self.eq == "0":
            if i == "0":         pass
            elif "⁻" in self.eq: self.eq = "⁻" + i
            else:                self.eq = i
        #Next 2 elif probably can be combined
        elif any(i in self.oper for i in self.eq) == True and self.eq.split(" ")[-1] == "0":
            if i == "0":                        pass
            elif "⁻" in self.eq.split(" ")[-1]: self.eq = self.eq[:-1] + "⁻" + i
            else:                             self.eq = self.eq[:-1] + i
        elif any(i in self.oper for i in self.eq) == True and i != "0":
            if self.eq.split(" ")[-1] == "0": self.eq = self.eq[:-1] + i

            else: self.eq += i
        #Normal
        else:
            self.eq += i

    def setOper(self,i):
        if self.eq == "" or self.eq == "Error":
            pass
        if any(i in self.oper for i in self.eq) == False:
            self.eq += " " + i + " 0"
        elif any(i in self.oper for i in self.eq[-2]) == True:
            self.eq = self.eq[:-2] + i + " 0"
        else:
            pass

    def setDec(self):
        #Set decimal in 1st num
        if any(i in self.oper for i in self.eq) == False and "." not in self.eq:
            self.eq+="."
        #Set decimal in 2nd num
        elif any(i in self.oper for i in self.eq) and "." not in self.eq.split(" ")[-1]:
            self.eq+="."

    def setPosNeg(self):
        #Switch 1st num to neg/pos
        if any(i in self.oper for i in self.eq) == False and "⁻" not in self.eq:
            self.eq = "⁻" + self.eq
        elif any(i in self.oper for i in self.eq) == False and "⁻" in self.eq:
            self.eq = self.eq[1:]
        #Switch 2nd num to neg/pos
        spliteq = self.eq.split(" ")
        if any(i in self.oper for i in self.eq) and "⁻" not in spliteq[-1]:     
            self.eq = spliteq[0] + " " + spliteq[1] + " "  + "⁻" + spliteq[-1]
            spliteq = self.eq.split(" ")
        elif any(i in self.oper for i in self.eq) and "⁻" in spliteq[-1]:
            self.eq = spliteq[0] + " " + spliteq[1] + " " + spliteq[-1].replace("⁻","")

    def setPer(self):
        if any(i in self.oper for i in self.eq): 
            spliteq = self.eq.split(" ")
            self.eq = spliteq[0] + " " + spliteq[1] " " + str(float(spliteq[2]) / 100)
        else: self.eq = str(float(self.eq) / 100)

    def numClear(self):
        if any(i in self.oper for i in self.eq): self.eq = self.eq[:-3] + "0"
        else: self.eq = "0"
    def fullClear(self):
        self.eq = "0"
    def delChar(self):
        if any(i in self.oper for i in self.eq): 
            if self.eq[-1] == " ": self.eq = self.eq[:-3]
            else:                  self.eq = self.eq[:-1]
        else: self.eq = self.eq[:-1]

    def invNum(self):
        pass
    def sqNum(self):
        pass
    def sqrtNum(self):
        pass


    def solve(self):
        #Define num & oper
        spliteq = self.eq.split(" ")
        num1, oper, num2  = spliteq[0] , spliteq[1] , spliteq[2]

        #Format negatives nums
        if "⁻" in num1: num1 = -1 * float(num1[1:])
        else:           num1 = float(num1)
        if "⁻" in num2: num2 = -1 * float(num2[1:])
        else:           num2 = float(num2)

        #Run Operations
        if oper == "+":
            result = num1 + num2
        if oper == "-":
            result = num1 - num2
        if oper == "×":
            result = num1 * num2
        if oper == "÷" and num2 != 0: 
            result = num1 / num2
        if oper == "÷" and num2 == 0:  #Div 0 Error
            result = "Error"
            self.eq = result
        
        #Format result
        if result != "Error":    
            if result % 1 == 0: result = int(result)
            if result > 0:    self.eq = str(result)
            elif result == 0: self.eq = str(0)
            else:             self.eq = "⁻" + str(-1 * round(result,6))

