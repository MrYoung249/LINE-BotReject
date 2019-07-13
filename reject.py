from linepy import *
from time import sleep
young = LINE()
int1 = len(young.getGroupIdsInvited())
if int1 == 0:
    print("No groups inviting")
else:
    for groups in young.getGroupIdsInvited():
        print("Reject " + young.getGroup(groups).name)
        sleep(0.7)
        young.rejectGroupInvitation(groups)
    print("\nYou reject" + str(int1) + "groups invitation")
