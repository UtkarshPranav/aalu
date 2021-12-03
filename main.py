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
            

def hex_check(hex_string1:bytes, hex_string2:bytes):
    #bool return
    if(hex_string1 == hex_string2):
        return True
    else:
        return False
            
def hex_hash_check(hex_string1:bytes, hex_string2:bytes, md5=1):

    hex_string1_hash = hashlib.md5(hex_string1).hexdigest() 
    hex_string2_hash = hashlib.md5(hex_string).hexdigest()
    if(md5 == 1):
        if(hex_string1_hash == hex_string2_hash):]
            return True, hex_string1_hash
        else:
            return False, hex_string1_hash, hex_string2_hash

def main():

    first_file = None
    second_file = None
    first_data = None
    second_data = None
    files_count = 0
    parser = argparse.ArgumentParser()


    parser.add_argument(
    "-m",
    "--mode",
    type=str,
    help = "Select mode betweeen a(ascii) / h(hex); default: ASCII ",
    default = 'a',
    required = True
    )
    parser.add_argument("-f", "--files", nargs=2, metavar=("first_file", "second_file"), help="files to add <File> <File>", required=True)
    parser.add_argument("-c", "--check", help = "returns boolean", action = "store_true")
    parser.add_argument("-H", "--hash", help="check md5-hash", action = "store_true")
    parser.add_argument("-v", "--verbose", action = "store_true")
    parser.add_argument("-o", "--offset", help="Check the offset between two strings", action = "store_true")
    args = parser.parse_args()
    first_file, second_file = args.files
    try:
        f = open(first_file, 'rb')
        first_data = f.read()
        files_count +=1
        print(1)
    except:
        first_data = first_file
    try:
        f = open(second_file, 'rb')
        second_data = f.read()
        file_count +=1
    except:
        second_data = second_file
    if(args.mode.lower() == 'a'):
        try:
            first_data = first_data.decode('utf-8')
            second_data = second_data.decode('utf-8')
        except:
            pass
        # print(type(first_data), type(second_data))
        if(args.check):
            if(ascii_compare(first_data, second_data) == 0):
                print("True")
            else:
                print("Flase")
        if(args.verbose):
            ascii_comapre_verbose(first_data, second_data)
        if(args.hash):
            res = ascii_hash(first_data, second_data)
            if(res[0]):
                print("Same md5digest")
                print(res[1])
            else:
                ascii_comapre_verbose(res[1], res[2])
        if(args.offset):
            print("Note: incomparison to first_data")
            print(ascii_offset(first_data, second_data))
    elif(args.mode.lower() == 'h'):
        first_data = first_data.encode()
        second_data = second_data.encode()
        if(args.check):
            if(hex_check(first_data, second_data)):
                print("Twin")
            else:
                print("Individual")
        if(args.verbose):
            hex_dump_verbose(first_data, second_data)
        if(args.offset):
            print(hex_offset_check(first_data, second_data))
        if(args.hash):
            hex_hash_check(first_data, second_data)
    else:
        print("Invalid Mode")
        exit()
main()


 
