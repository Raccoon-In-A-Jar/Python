import json

dicofichier = open("E:\dicoville.txt", "w", encoding="utf-8")





with open('E:\city.list.json', encoding="utf-8") as json_file:
    data = json.load(json_file)

    dicofichier.write("IDictionary<string, string> MyCities = new Dictionary<string, string>();\n")
    dicofichier.write("\n")
    # dicofichier.writelines("MyCities.Add(machin, bidule);")

    for p in data['cities']:

        cityID = "\"" + str(p['id']) + "\""
        cityName = "\"" + p['name'] + ',' + p['country'] + "\""
        print(cityName + "," + cityID)
        dicofichier.write("MyCities.Add(" + cityName + "," + cityID + ");\n")

        # dicofichier.write(("\"" + p['name'] + ',' + p['country'] + "\""))
        # print("\"" + str(p['id']) + "\"")
        # print("\"" + p['name'] + ',' + p['country'] + "\"")
dicofichier.close()
print("done")
