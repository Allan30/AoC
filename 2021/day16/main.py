file = open("input.txt", "r")
lines = file.readlines()

trames = lines[0].replace('\n', '')

VERSION_LENGTH = 3
TYPE_LENGTH = 3

LITERAL_FOUR_BITS_LENGHT = 5

OPERATOR_ID_LENGTH = 1
OPERATOR_SUBPACKETS0_LENGTH_LENGTH = 15
OPERATOR_SUBPACKETS1_LENGTH_LENGTH = 11

trames = ''.join([bin(int(hex, 16))[2:].zfill(4) for hex in trames])

#print(trames)

sumVersion = 0

def decoded(trames, niv=0):
    global sumVersion
    packets = list()
    while len(trames) > 0 and int(trames) > 0:
        print(trames)
        print(niv)
        packet = dict()
        packet["version"] = int(trames[:VERSION_LENGTH], 2)
        packet["type"] = int(trames[VERSION_LENGTH:VERSION_LENGTH+TYPE_LENGTH], 2)

        sumVersion += packet["version"]

        if packet["type"] == 4:
            subpacket = trames[VERSION_LENGTH+TYPE_LENGTH:VERSION_LENGTH+TYPE_LENGTH+LITERAL_FOUR_BITS_LENGHT]
            packet["subpackets"] = [int(subpacket[1:], 2)]

            index = 1
            
            while subpacket[0] != '0' and subpacket == '0':
                subpacket = trames[VERSION_LENGTH+TYPE_LENGTH+LITERAL_FOUR_BITS_LENGHT*index:VERSION_LENGTH+TYPE_LENGTH+LITERAL_FOUR_BITS_LENGHT*(index+1)]
                packet["subpackets"].append(int(subpacket[1:], 2))
                index += 1

            totalLength = VERSION_LENGTH+TYPE_LENGTH+LITERAL_FOUR_BITS_LENGHT*(index)
        
        else:
            packet["ID"] = int(trames[VERSION_LENGTH+TYPE_LENGTH:VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH], 2)

            if packet["ID"] == 0:
                packet["length"] = int(trames[VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH:VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH+OPERATOR_SUBPACKETS0_LENGTH_LENGTH], 2)
                packet["subpackets"] = trames[VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH+OPERATOR_SUBPACKETS0_LENGTH_LENGTH:VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH+OPERATOR_SUBPACKETS0_LENGTH_LENGTH+packet["length"]]
                totalLength = VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH+OPERATOR_SUBPACKETS0_LENGTH_LENGTH+packet["length"]
            else:
                packet["number"] = int(trames[VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH:VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH+OPERATOR_SUBPACKETS1_LENGTH_LENGTH], 2)
                packet["subpackets"] = ""
                sp = 0
                for sp in range(packet["number"]):
                    #print(trames[VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH+(sp+1)*OPERATOR_SUBPACKETS1_LENGTH_LENGTH:VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH+(sp+2)*OPERATOR_SUBPACKETS1_LENGTH_LENGTH])
                    packet["subpackets"] += trames[VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH+(sp+1)*OPERATOR_SUBPACKETS1_LENGTH_LENGTH:VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH+(sp+2)*OPERATOR_SUBPACKETS1_LENGTH_LENGTH]
                totalLength = VERSION_LENGTH+TYPE_LENGTH+OPERATOR_ID_LENGTH+(sp+2)*OPERATOR_SUBPACKETS1_LENGTH_LENGTH

            packet["subpackets"] = decoded(packet["subpackets"], niv+1)
        packets.append(packet)
        
        trames = trames[totalLength:]
    
    return packets


packets = decoded(trames)
print(packets)
answer = sumVersion
print(answer)
    
        



    

