import Pyro4


@Pyro4.expose
class TicketGenerator(object):

    def generate(self):
        global currentTicket
        currentTicket += 1
        return currentTicket


currentTicket = 0
daemon = Pyro4.Daemon()
uri = daemon.register(TicketGenerator)

print("Ready. Object uri =", uri)
daemon.requestLoop()
