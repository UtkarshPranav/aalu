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
          
          
def ascii_offset(string1, string2):                                                                                                                                                                                                            
    # Offset between ascii strings                                                                                                                                                                                                             
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
    bin_str1 = binascii.hexlify(string1.encode()).decode()
    bin_str2 = binascii.hexlify(string2.encode()).decode()
    offset = eval("0x"+bin_str1) - eval("0x"+bin_str2)
    return offset
  
  def ascii_comapre_verbose(string1, string2):
    #verbose output for ascii compare
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
    string1_length = len(string1)
    string2_length = len(string2)
    length_boolen = string1_length - string2_length # 0 if equals
    if(string1 == string2):
        print(colored(string1, "green"))
        print("Same String!")
        return 0
    print(string1)
    max_length = max(string1_length, string2_length)
    if(len(string1) > len(string2)):
        max_len_string = string1
    else:
        max_len_string = string2
    i = 0
    # Check whether string1 is max or string2
    if(max_len_string == string1):
        while(i != max_length):
            try: # for the out of index in string
                if(string1[i] == string2[i]):
                    # print(string1[i], end='')
                    print(colored(string2[i], "green"), end='')
                else:
                    print(colored(string2[i],  "yellow"), end='')
            except Exception as e:
                print(colored("×", "red"), end='')
            i+=1
    else:
        while(i != len(string2)):
            try: # for the out of index in string
                if(string1[i] == string2[i]):
                    # print(string1[i], end='')
                    print(colored(string2[i], "green"), end='')
                else:
                    print(colored(string2[i],  "yellow"), end='')
            except Exception as e:
                print(colored(string2[i], "blue"), end='')
            i+=1

            
            def hex_offset_check(hex_string1:bytes, hex_string2:bytes): 
    #offset cal 0x41414141 - 0x42424242 = -16843009
    bin_hex_string1 = int(binascii.hexlify(hex_string1), 16)
    bin_hex_string2 = int(binascii.hexlify(hex_string2), 16)
    return (bin_hex_string1 - bin_hex_string2)
def hex_dump_verbose(hex_string1:bytes, hex_string2:bytes):
    #verbose output for hex compare
    bin_hex_string1 = binascii.hexlify(hex_string1)
    bin_hex_string2 = binascii.hexlify(hex_string2)
    if(bin_hex_string1 == bin_hex_string2):
        print(colored("Twin", "green"))
        return 0
    print(bin_hex_string1.decode())
    max_length = max(len(bin_hex_string1), len(bin_hex_string2))/2
    if(len(bin_hex_string1) > len(bin_hex_string2)):
        max_bin_hex_string = bin_hex_string1
    else:
        max_bin_hex_string = bin_hex_string2
    i = 0
    if(max_bin_hex_string == hex_string1):
        while(i != max_length):
            try: # for the out of index in string
                if(hex_string1[i] == hex_string2[i]):
                    print(colored(hex(hex_string2[i])[2:], "green"), end='')
                else:
                    print(colored(hex(hex_string2[i])[2:], "yellow"), end='')
            except Exception as e:
                print(colored("×", "red"), end='')

            i+=1
    else:
        while(i != len(hex_string2)):
            try: # for the out of index in string
                if(hex_string1[i] == hex_string2[i]):
                    print(colored(hex(hex_string2[i])[2:], "green"), end='')
                else:
                    print(colored(hex(hex_string2[i])[2:], "yellow"), end='')
            except:
                print(colored(hex(hex_string2[i])[2:], "blue"), end='')

            i+=1


          
 
