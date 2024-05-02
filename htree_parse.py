import json

def main():
    file = open("pythia_logs")

    enabled_ids = []
    enables = 0
    grouping = False
    result = False

    lines = file.readlines()

    for line in lines:
        if grouping:
            if "Group" not in line:
                grouping = False
                print("Inconclusive results.\n")
            else:
                result = True
                grouping = False

        if result and "matching groups out of" not in line:
            print(line)
        else:
            result = False
            

        if "Making decision" in line:
            grouping = True
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~ NEW RESULT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(line)

        if "Enabling" in line:
            if enables == 0:
                enables += 1
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~ BASE ENABLE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else:
                enables += 1
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~ NEW ENABLE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            for tracepointID in line[9:].split("TracepointID "):
                
                if len(tracepointID.split(',')) > 1:
                    print("----------- NEW TRACEPOINT ID --------------")
                    for i, field in enumerate(tracepointID.split(',')):
                        if i == 0:
                            enabled_ids.append(field.split(' ')[2])
                        print(field)

    print(enabled_ids)

main()