import random

def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

unique_sequence = uniqueid()
id1 = next(unique_sequence)
id2 = next(unique_sequence)
id3 = next(unique_sequence)
print(id1, id2, id3)