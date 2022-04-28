
import random


Symbols = ("O","X")
def state(array):
    draw_flag = True
    for each in array:
        if type(each) != str:
            draw_flag = draw_flag * (type(each) == str)
    if array[0] == array[1] == array[2] == "O": return "O"
    elif array[3] == array[4] == array[5] == "O": return "O"
    elif array[6] == array[7] == array[8] == "O": return "O"
    elif array[0] == array[3] == array[6] == "O": return "O"
    elif array[1] == array[4] == array[7] == "O": return "O"
    elif array[2] == array[5] == array[8] == "O": return "O"
    elif array[0] == array[4] == array[8] == "O": return "O"
    elif array[2] == array[4] == array[6] == "O": return "O"
    elif array[0] == array[1] == array[2] == "X": return "X"
    elif array[3] == array[4] == array[5] == "X": return "X"
    elif array[6] == array[7] == array[8] == "X": return "X"
    elif array[0] == array[3] == array[6] == "X": return "X"
    elif array[1] == array[4] == array[7] == "X": return "X"
    elif array[2] == array[5] == array[8] == "X": return "X"
    elif array[0] == array[4] == array[8] == "X": return "X"
    elif array[2] == array[4] == array[6] == "X": return "X"
    elif (draw_flag == True): return "d" 
    else: return "continue"
class AI:  
    def   __init__(self):
        self.first = True
        self.me = "O"
    def return_position(self,array):
        avilable = []
        count_me = 0
        count_other = 0
        inc=0
        return_value = None
        first = self.first
        me = Symbols[(Symbols.index(self.me)+1)%2]
        draw_flag = True
        for each in array:
            if each == me:
                count_me += 1
            if each == Symbols[(Symbols.index(me)+1)%2]:
                count_other += 1
            if type(each) != str:
                draw_flag = draw_flag * (type(each) == str)
        
        
        if(draw_flag == True):return None  
        
        if (first == True) and (count_me != count_other): return None
        elif (first != True) and (count_me == count_other): return None    
        
        for each in array:
            if type(each) == int:
                avilable.append(each)
        
        for i in range(0,3):
            if (array[0+inc] == array[1+inc]) and avilable.__contains__(2+inc) and (array[0+inc] == me):  return 2 +inc
            elif (array[1+inc] == array[2+inc]) and avilable.__contains__(0+inc) and (array[2+inc] == me): return 0 +inc
            elif (array[0+inc] == array[2+inc]) and avilable.__contains__(1+inc) and (array[2+inc] == me): return 1+inc
            if (array[0+inc] == array[1+inc]) and avilable.__contains__(2+inc) and (array[0+inc] != me): return_value = 2 +inc
            elif (array[1+inc] == array[2+inc]) and avilable.__contains__(0+inc) and (array[2+inc] != me): return_value = 0 +inc
            elif (array[0+inc] == array[2+inc]) and avilable.__contains__(1+inc) and (array[2+inc] != me): return_value = 1+inc
            inc += 3
        
     
        inc = 0
        for i in range(0,3):
            if (array[0+inc] == array[3+inc]) and avilable.__contains__(6+inc) and (array[0+inc] == me):  return 6 + inc
            elif (array[0+inc] == array[6+inc]) and avilable.__contains__(3+inc) and (array[6+inc] == me): return 3 + inc
            elif (array[3+inc] == array[6+inc]) and avilable.__contains__(0+inc) and (array[6+inc] == me): return 0 + inc
            if (array[0+inc] == array[3+inc]) and avilable.__contains__(6+inc) and (array[0+inc] != me):  return_value = 6 + inc
            elif (array[0+inc] == array[6+inc]) and avilable.__contains__(3+inc) and (array[6+inc] != me): return_value = 3 + inc
            elif (array[3+inc] == array[6+inc]) and avilable.__contains__(0+inc) and (array[6+inc] != me): return_value = 0 + inc
            inc += 1
        
        

        if (array[0] == array[8]) and avilable.__contains__(4) and (array[0] == me):  return 4  
        elif (array[0] == array[4]) and avilable.__contains__(8) and (array[4] == me): return 8  
        elif (array[4] == array[8]) and avilable.__contains__(0) and (array[4] == me): return 0
        if (array[0] == array[8]) and avilable.__contains__(4) and (array[0] != me):  return_value = 4  
        elif (array[0] == array[4]) and avilable.__contains__(8) and (array[4] != me): return_value = 8  
        elif (array[4] == array[8]) and avilable.__contains__(0) and (array[4] != me): return_value = 0  
          
        
        if (array[2] == array[6]) and avilable.__contains__(4) and (array[2] == me):  return 4  
        elif (array[2] == array[4]) and avilable.__contains__(6) and (array[4] == me): return 6  
        elif (array[4] == array[6]) and avilable.__contains__(2) and (array[4] == me): return 2
        if (array[2] == array[6]) and avilable.__contains__(4) and (array[2] != me):  return_value = 4  
        elif (array[2] == array[4]) and avilable.__contains__(6) and (array[4] != me): return_value = 6  
        elif (array[4] == array[6]) and avilable.__contains__(2) and (array[4] != me): return_value = 2  
         
        
        if return_value != None: return return_value 
    

        return random.choice(avilable)
    


























