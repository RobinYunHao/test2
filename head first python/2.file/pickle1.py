man = []
other = []
try:
    file = open("juben2.txt")
    for line in file :
        try:
            (person,said) = line.split(':',1)
            said = said.strip()
            if person == 'Man':
                man.append(said)
            elif said == 'Otherman':
                other.append(said)
        except(ValueError):
            pass
    file.close
except(IOError):
    print('datafile is missing')
print man
print other


