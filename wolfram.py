import wolframalpha
import socket

def internet_check():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

def wolframQuery(query):
    print("Working...")
    res = wolframalpha.Client("<your key here>").query(query)
    print("This may help:")
    print(next(res.results).text)


if internet_check() == True:
    query = input("What do you want to know?")
    wolframQuery(query)
else:
    print('Network error.')
    print("""Try:
    Checking the connection,
    Cheking the proxy, firewall and DNS settings,
    Running Network Diagnostics.
    """)
