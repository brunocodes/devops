import uuid

my = uuid.uuid4()
my2 = uuid.uuid4().hex
my3 = uuid.uuid4().hex
my4 = uuid.uuid4().hex
print(my, my2)
# print(my2[0:32])
print("____")
print(my2[0:24])
print("____")
print(my3[0:24])
print("____")
print(my4[0:24])