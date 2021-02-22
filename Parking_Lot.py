import Vehicle
import argparse
import sys

if sys.version_info[0] == 2:
    input = input()


class Parking:
    def __init__(self):
        self.capacity = 0
        self.Slot_ID = 0
        self.Occupied_slots = 0

    def Create_New_Slot(self, capacity):
        self.slots = [-1] * capacity
        self.capacity = capacity
        return self.capacity

    def Empty_Slots(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park(self, Reg_no, color):
        if self.Occupied_slots < self.capacity:
            Slot_ID = self.Empty_Slots()
            self.slots[Slot_ID] = Vehicle.Car(Reg_no, color)
            self.Slot_ID = self.Slot_ID+1
            self.Occupied_slots = self.Occupied_slots + 1
            return Slot_ID+1
        else:
            return -1

    def leave(self, Slot_ID):

        if self.Occupied_slots > 0 and self.slots[Slot_ID-1] != -1:
            self.slots[Slot_ID-1] = -1
            self.Occupied_slots = self.Occupied_slots - 1
            return True
        else:
            return False

    def status(self):
        print("Slot No.\tRegistration No.\tColour")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i+1) + "\t\t" +
                      str(self.slots[i].Reg_no) + "\t\t" + str(self.slots[i].color))
            else:
                continue

    def getRegNoFromColor(self, color):

        Registration_Nos = []
        for i in self.slots:

            if i == -1:
                continue
            if i.color == color:
                Registration_Nos.append(i.Reg_no)
        return Registration_Nos

    def getSlotNoFromRegNo(self, Reg_no):

        for i in range(len(self.slots)):
            if self.slots[i].Reg_no == Reg_no:
                return i+1
            else:
                continue
        return -1

    def getSlotNoFromColor(self, color):

        slotnos = []

        for i in range(len(self.slots)):

            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                slotnos.append(str(i+1))
        return slotnos

    def show(self, line):
        if line.startswith('create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.Create_New_Slot(n)
            print('Created a parking lot with '+str(res)+' slots')

        elif line.startswith('park'):
            Reg_no = line.split(' ')[1]
            color = line.split(' ')[2]
            res = self.park(Reg_no, color)
            if res == -1:
                print("Sorry, parking lot is full")
            else:
                print('Allocated slot number: '+str(res))

        elif line.startswith('leave'):
            leave_slotid = int(line.split(' ')[1])
            status = self.leave(leave_slotid)
            if status:
                print('Slot number '+str(leave_slotid)+' is free')

        elif line.startswith('status'):
            self.status()

        elif line.startswith('registration_numbers_for_cars_with_colour'):
            color = line.split(' ')[1]
            Registration_Nos = self.getRegNoFromColor(color)
            print(', '.join(Registration_Nos))

        elif line.startswith('slot_numbers_for_cars_with_colour'):
            color = line.split(' ')[1]
            slotnos = self.getSlotNoFromColor(color)
            print(', '.join(slotnos))

        elif line.startswith('slot_number_for_registration_number'):
            Reg_no = line.split(' ')[1]
            slotno = self.getSlotNoFromRegNo(Reg_no)
            if slotno == -1:
                print("Not found")
            else:
                print(slotno)
        elif line.startswith('exit'):
            exit(0)


def main():

    parkinglot = Parking()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=False,
                        dest='src_file', help="Input File")
    args = parser.parse_args()

    if args.src_file:
        with open(args.src_file) as f:
            for line in f:
                line = line.rstrip('\n')
                parkinglot.show(line)
    else:
        while True:
            line = input("$ ")
            parkinglot.show(line)


if __name__ == '__main__':
    main()
