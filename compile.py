version="Aplha 0.1"
print("preparing to compile...")

from sys import argv as args, exit
file = args[1]
with open(file, 'r') as f:
    input = f.read().splitlines()

outfile = file.replace('.stsc', '.stpd')
out=[]
out.append(f'# Stsc2Stpd V.{version}')

def cut(input:str,toRemove:str):
    working=input.strip()
    if working[:len(toRemove)] == toRemove:
        return working[len(toRemove):].strip()
i=0
while i in range(len(input)):
    line=input[i].replace("out","outln").replace("outlnln","outln")
    funcname=line.strip().split(' ')[0].strip()
    
    if funcname=="outln":

        out.append(f"out: {cut(line,'outln')}")
    elif funcname=="var":
        if "label" in line:
            print("Label not supported yet")
            exit()
        name=line.split(' ')[2]
        value=line.split('=')[1].strip().replace('"','')
        out.append(f"var: {name}={value}")
    i+=1
with open(outfile, 'w') as f:
    print("compiling done!")
    out="\n".join(out)
    f.write(out)