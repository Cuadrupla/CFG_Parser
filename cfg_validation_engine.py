def reading(nonTerminals, terminals, rules, file_name):
    f = open(file_name)
    linie = f.readline()
    global start
    while linie:
        linie = linie[:(len(linie) - 1)]
        if linie[0] == "#":
            linie = f.readline()
            continue

        if linie == "Non-terminals:":
            linie = f.readline()
            while linie.lower() != "end\n" and linie.lower() != "end":
                if linie[0] == '#':
                    linie = f.readline()
                    continue

                nonTerminalLine = linie.strip().split("#")
                nonTerminals.append(nonTerminalLine[0].strip())
                if validate_nonTerminals() != True:
                    raise Exception("non-terminals are not valid")
                linie = f.readline()

        elif linie == "Terminals:":
            linie = f.readline()
            while linie.lower() != "end" and linie.lower() != "end\n":
                if linie[0] == "#":
                    linie = f.readline()
                    continue

                terminalLine = linie.strip().split("#")
                terminals.append(terminalLine[0].strip())
                if validate_terminals() != True:
                    raise Exception("terminals are not valid")
                linie = f.readline()

        elif linie == "Rules:":
            linie = f.readline()
            while linie.lower() != "end" and linie.lower() != "end\n":
                if linie[0] == '#':
                    linie = f.readline()
                    continue

                productionLine = linie.strip().split("#")
                if len(productionLine) > 1:
                    linie = f.readline()
                    continue

                productionLine = productionLine[0].split("/")
                if len(productionLine) == 1:
                    linie = f.readline()
                    continue

                if productionLine[0] in nonTerminals:
                    if productionLine[0] not in rules.keys():
                        if productionLine[1] == "~":
                            rules[productionLine[0]] = [""]
                        else:
                            valid = True
                            for letter in productionLine[1]:
                                if letter not in nonTerminals and letter not in terminals:
                                    valid = False

                            if valid:
                                rules[productionLine[0]] = [productionLine[1]]
                            else:
                                raise Exception("ruleset not valid!")
                    else:
                        if productionLine[1] == "~":
                            rules[productionLine[0]].append("")
                        else:
                            valid = True
                            for letter in productionLine[1]:
                                if letter not in nonTerminals and letter not in terminals:
                                    valid = False
                            if valid:
                                rules[productionLine[0]].append(productionLine[1])
                            else:
                                raise Exception("ruleset not valid!!")
                else:
                    raise Exception("ruleset not valid")
                linie = f.readline()
        elif linie == "Start:":
            linie = f.readline()
            while linie.lower() != "end" and linie.lower() != "end\n":
                if linie[0] == '#':
                    linie = f.readline()
                    continue

                startLine = linie.strip().split("#")
                if len(startLine) > 1:
                    linie = f.readline()
                    continue
                start = linie[0]
                linie = f.readline()

        linie = f.readline()
    f.close()


nonTerminals = []
terminals = []
rules = {}
start = ""
found = True


def validate_nonTerminals():
    valid = True
    for nonTerminal in nonTerminals:
        if len(nonTerminal) != 1 or nonTerminal != nonTerminal.upper():
            valid = False
    return True if start in nonTerminals and valid else False

def validate_terminals():
    valid = True
    for terminal in terminals:
        if len(terminal) != 1 or terminal != terminal.lower():
            valid = False
    return valid

def validate_solution(startNonTerminal, road):
    global found
    global visited
    if startNonTerminal not in road and startNonTerminal in nonTerminals:
        road += startNonTerminal
    elif startNonTerminal in road:
        found = False
        return
    for word in rules[startNonTerminal]:
        for letter in word:
            if letter in nonTerminals:
                validate_solution(letter, road)
                road = road[:len(road)-1]

    return found


if __name__ == "__main__":
    try:
        reading(nonTerminals, terminals, rules, "cfg_config_file.txt")
        if validate_solution(start, ""):
            print("The received config is a valid CFG")
        else:
            print("The received automata config is NOT a valid CFG")
    except Exception as exception:
        print(exception.args[0])
