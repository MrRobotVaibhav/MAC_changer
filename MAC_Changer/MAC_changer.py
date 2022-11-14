
import subprocess #This Library is used to interact with the CLI
import optparse   # This Library used for parsing command-line options
import re         # Regex
#ASCII ART File Path
f = open("art.txt","r")
print(f.read())

#Function for Handling Arguments
def arguments():
    parse=optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="Interface whose MAC-Address to change.")
    parse.add_option("-m","--mac",dest="new_Mac_add",help="New MAC-Address.")
    (User_input,arguments)=parse.parse_args()
    if not User_input.interface:
        parse.error("[-]Need An Interface. use --help to know more.")
    elif not User_input.new_Mac_add:
        parse.error("[-]Need new MAC address. use --help to know more.")
    return User_input

#This is the function which interact with the CLI to execute Cmmds
def mac_change_function(interface,new_Mac_add):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw","ether", new_Mac_add])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Changing the MAC ADDRESS...")
    # print("[+] MAC Address changed to "+ new_Mac_add + " of Interface " + interface)

#Read the Current MAC Address to print on screen
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    search_result_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result))
    if search_result_mac:
        return search_result_mac.group(0)
    else:
        print("[-] Error : Don't Get MAC ADDRESS.")
   

# ------calling Fuctions-------
# Taking user's Input
User_input = arguments() 
# printing Current MAC Address
current_mac = get_current_mac(User_input.interface)
print("Current MAC : " + str(current_mac))
# Changing MAC Address
mac_change_function(User_input.interface,User_input.new_Mac_add)

#  Again Calling the Current MAC for Comparing Results
current_mac = get_current_mac(User_input.interface)
#  Print Results
if current_mac == User_input.new_Mac_add:
    print("[+] MAC Address Changed Successfully to " + current_mac)
else:
    print("[-] MAC Address not Changed.")



