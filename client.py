import socket, select, string, sys

# Function to show the input prompt to the user
def prompt() :
    sys.stdout.write('> ')
    sys.stdout.flush()          # Clear the stream before the next input
 
 # Main Method
if __name__ == "__main__":
     
    if(len(sys.argv) < 5) :
        print 'Usage : python client.py -sip server-ip -sp port'
        sys.exit()
     
    host = sys.argv[2]
    try:
        port = int(sys.argv[4])
    except:
        print 'Please enter proper port'
        sys.exit()
     
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(2)
    
    RECV_BUFFER = 4096          # Advisable to keep it as an exponent of 2 
     
    # Send greeting to server
    try :
        s.sendto('GREETING', (host,port))        
    except :
        print 'Unable to connect to server'
        sys.exit()
     
    print 'Connected to server. Start sending messages'
    # Show the prompt to the user so that he can start sending messages.
    prompt()

    while 1:
        socket_list = [sys.stdin, s]            # Get all sockects for the client
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from server
            if sock == s:
                data = sock.recvfrom(RECV_BUFFER)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    # print the incoming data(message) and display the prompt again
                    sys.stdout.write(data[0])
                    prompt()
             
            #user typed a message and is sending it accross
            else :
                msg = sys.stdin.readline()
                s.sendto(msg, (host,port))
                prompt()