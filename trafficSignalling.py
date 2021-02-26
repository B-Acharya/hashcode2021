if __name__=="__main__":
    streets = dict()
    paths = dict()
    junctions = dict()
    with open("./f.txt") as f:
        duration, intersections, noOfStreets, noOfCars, bonus = f.readline().split()
        for _ in range(int(noOfStreets)):
            B, E , streetName , L = f.readline().split()
            streets[streetName]= [B,E,L]
        for _ in range(int(noOfCars)):
            a = f.readline()
            num = a.split()[0]
            paths[int(num)]= a.split()[1:]
    for i in range(int(intersections)):
        junctions[i] = list() 
    for keys in streets.keys():
        value = junctions[int(streets[keys][1])]
        value.append(keys)
        junctions[int(streets[keys][1])]= value
    weight = dict()
    for i in streets.keys():
        weight[i] = 0 
    for keys in paths.keys():
        for street in paths[keys]:
            weight[street] += 1
    total = 0 
    for keys in junctions.keys():
        for str1 in junctions[keys]:
            if weight[str1]> 0 :
                total +=1
                break
    with open("./output_f.txt","w") as f:
        f.write(str(total)+"\n")
        #f.write(str(len(junctions.keys()))+"\n")
        for keys in junctions.keys():
            length = 0
            for street in junctions[keys]:
                if weight[street]>0:
                    length +=1
            if length==0:
                continue
            f.write(str(keys)+"\n")
            f.write(str(length) + "\n")
            #f.write(str(len(junctions[keys]))+"\n")
            for street in junctions[keys]:
                if weight[street]>0:
                    f.write(street+ " " + str(weight[street]//length) + "\n")

