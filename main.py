import hashlib                                                                                                                                                                                                                                 
from termcolor import colored                                                                                                                                                                                                                  
import binascii                                                                                                                                                                                                                                
import argparse                                                                                                                                                                                                                                
import sys                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                               
# First Argument in functions is considered as Primary string which will be compared with secondary string.                                                                                                                                    
                                                                                                                                                                                                                                               
def ascii_compare(string1, string2):                                                                                                                                                                                                           
    # Boolean strings comapre                                                                                                                                                                                                                  
    tmp = ''                                                                                                                                                                                                                                   
    for word in string1:                                                                                                                                                                                                                       
        if ord(word) in range(0x20, 0x7E):                                                                                                                                                                                                     
            tmp+=word                                                                                                                                                                                                                          
    string1 = tmp                                                                                                                                                                                                                              
    tmp = ''                                                                                                                                                                                                                                   
    for word in string2:                                                                                                                                                                                                                       
        if ord(word) in range(0x20, 0x7E):                                                                                                                                                                                                     
            tmp+=word                                                                                                                                                                                                                          
    string2 = tmp                                                                                                                                                                                                                              
    if(string1 == string2):                                                                                                                                                                                                                    
        return 0                                                                                                                                                                                                                               
    else:                                                                                                                                                                                                                                      
        return 1                                                                                                                                                                                                                               
                                                                                                                                                                                                                                               
def ascii_hash(string1, string2, md5 = 1):                                                                                                                                                                                                     
    # Hash Compare for ASCII strings                                                                                                                                                                                                           
    tmp = ''                                                                                                                                                                                                                                   
    for word in string1:                                                                                                                                                                                                                       
        if ord(word) in range(0x20, 0x7E):                                                                                                                                                                                                     
            tmp+=word                                                                                                                                                                                                                          
    string1 = tmp                                                                                                                                                                                                                              
    tmp = ''                                                                                                                                                                                                                                   
    for word in string2:                                                                                                                                                                                                                       
        if ord(word) in range(0x20, 0x7E):                                                                                                                                                                                                     
            tmp+=word                                                                                                                                                                                                                          
    string2 = tmp                                                                                                                                                                                                                              
    if(md5 == 1):                                                                                                                                                                                                                              
        string1_hash = hashlib.md5(string1.encode())                                                                                                                                                                                           
        string2_hash = hashlib.md5(string2.encode())                                                                                                                                                                                           
        if(string1_hash.hexdigest() == string2_hash.hexdigest()):                                                                                                                                                                              
            return True, string1_hash.hexdigest(), None
 
