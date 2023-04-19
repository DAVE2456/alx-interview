#!/usr/bin/python3                                                              
                                                                                
"""UTF-8 Validation"""                                                                                                                                          
                                                                                
def validUTF8(data):                                                            
    """                                                                         
       Determines if given data set                                             
       represents a valid UTF-8 encoding
    """
                                                                         
    def check(num):                                                             
        mask = 0b10000000 # 128
        i = 0                                                                   
        while num & mask: # 11000110(198) & 10000000(128)                       
            mask >>= 1                                                          
            i += 1
        return i                                                                
                                                                                
    i = 0                                                                       
    while i < len(data):                                                        
        j = check(data[i])                                                      
        a = i + j - (j != 0)                                                    
        i += 1                                                                  
        if j == 1 or j > 4 or a >= len(data):                                     
            return False                                                        
        while i < len (data) and i <= a:                                        
            curnt = check(data[i])                                              
            if curnt != 1:                                                      
                return False                                                    
            i += 1                                                              
    return True