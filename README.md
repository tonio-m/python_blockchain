# python_blockchain

Extremely simplified Blockchain implemented in python.

5 line functions, no classes (only dictionaries), less than 60 lines of code.

All payloads are json serializable.

This is meant to exemplify hands-on the basic concepts of a blockchain.


### List of compromises:
Since this is a project meant for learning and not for actual hosting, 
there were some compromises made for the sake of simplicity:

* No Client separation
* No Miner identity (no miner hash)
* No rewards based on PoW
* No wallet balance (balance achieved by tallying up the transaction history)
* No nakamoto consensus, since there is no client server and its not a distributed system.


Apart from these, all the functions implemented are really similar to something you would find on the bitcoin source code.
