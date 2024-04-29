import gmpy2
from ReedSolomonTransmit import *
from ReedSolomonSend import *
from ReedSolomonReceive import *
from global_variable_setup import *
from GlobalSetup import *

nu=0.2
M=1000000000

while(True):
    print('Enter "EXIT" to quit')
    print('Enter message(integer) lesser than',M,'to send: ',end='')

    message=input()
    if(message.lower()=="exit"):
        break

    message=int(message)
    if(message>=M):
        break

    GlobalSetup(nu,M)

    ReedSolomonSend(message)

    recovered_msg=ReedSolomonReceive()
    if(recovered_msg=="ERROR"):
        print('Recovery Failed')
    else:
        print('Recovery Successful: ', recovered_msg)

    print()
