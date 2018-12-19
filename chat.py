import sys

import server
import client

if len(sys.argv) > 1:
    client = client.Client(sys.argv[1])
else:
    server = server.Server()
    print('\nserver created...')
    server.run()





















