 #!/usr/bin/env python3
"""Alta3 Reseaarch || Author:RZFeeser@alta3.com"""
def commandpush (devicecmd): #devicemd ==list
     for coffeetime in devicecmd.keys():
         print('Handshaking ........... connecting with'+cofeetime)
         for mycmds in devicemd[cofeetime]:
             print('Attempting to sending command -->'+mycmds)

def main():
         work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.         0.1":  
             ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1             /5", "no  shutdown"]} 
     # data that replaces data stored in file

     print("Welcome to the network device command pusher")

     ## get data set
     print("\nData set found\n") # replace with function call that reads in data from file

     ## run
     commandpush(work2do) # call function to push commands to devices

 # call our main function
 main()
