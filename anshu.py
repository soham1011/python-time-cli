class Building:
    floors = 6
    stairs = 1
    lift = 1

    def __init__(self, floorToMake):
        self.floors = floorToMake
        print("MAIN BN RAHA HU")

    def MakeNewFloor(self):
        self.floors = self.floors + 1


youthvilleSBR = Building(6)
print(youthvilleSBR.floors)
youthvilleSBR.MakeNewFloor()
print(youthvilleSBR.floors)

SICSR = Building()
print(SICSR.floors, SICSR.lift)
SICSR.MakeNewFloor()
print(SICSR.floors)