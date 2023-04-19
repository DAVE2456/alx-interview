#!/usr/bin/python3                                                              
                                                                                
"""UTF-8 Validation"""                                                                                                                                          
                                                                                
def validUTF8(data):                                                            
    """                                                                         
       Determines if given data set                                             
       represents a valid UTF-8 encoding
    """
                                                                         
    def check(num):                                                             
        mask = 0b10000000 # 128
        a = 0                                                                   
        while num & mask: # 11000110(198) & 10000000(128)                       
            mask >>= 1                                                          
            a += 1
        return a                                                                
                                                                                
    a = 0                                                                       
    while a < len(data):                                                        
        b = check(data[a])                                                      
        c = a + b - (b != 0)                                                    
        a += 1                                                                  
        if b == 1 or b > 4 or c >= len(data):                                     
            return False                                                        
        while a < len (data) and a <= c:                                        
            curnt = check(data[a])                                              
            if curnt != 1:                                                      
                return False                                                    
            a += 1                                                              
    return True
