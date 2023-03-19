import os, glob, json

#!!!REWRITE PATH to wherever the repo was cloned or files downloaded!!!
# No need to change any other variable

path = "C:/Programs/Trackman"
dir_list = os.listdir(path)

#going through all files and appending them to a dictionary
dic = {}
for filename in dir_list:
    f = open(path + '/' + filename)

    data = json.load(f)

    lista = []

    try:
        #scraping the query from the 2 kinds of JSON format with list and no list
        if data['query'].get('L') != None:

            string = data['query']['L'][0]['M']['from']['S']

        elif data['query'].get('L') == None:

            string = data['query']['M']['from']['S']

        #splitting the string into two when there is a "join" keyword in it
        #also replacing some of the different writing styles of "join" just to be safe
        string = string.replace('JOIN', 'join')
        string = string.replace('Join', 'join')
        joinstring = string.split('join')
            
        #each segment's first word now should now contain a table name we are looking for
        for x in joinstring:
            spacestring = x.split(' ')
            
            try: 
                spacestring.remove('') #optionally removing empty quote charachters that might get in the way 
            except:
                pass
            
            if spacestring[0] not in lista:
                lista.append(spacestring[0])

        #creating dictionary with file name and assigning the related tables as values to it
        table_name = filename.replace('.json', '')
        dic[table_name] = lista 

    #debug
    except:
        print(filename)

#denormalizing data so we have single values instead of a list if multiple values belong to a key
pairs = []
for key, values in dic.items():
    for value in values:
        pairs.append([key,value])

#creating nested dictionary with the right hierarchy for visualization
hierarchy = {}
root = set()

for child, parent in pairs:

    childitem = hierarchy.get(child, None)
    if not childitem:
        hierarchy[child] = {}
    else:
        root.discard(child)

    parentitem = hierarchy.get(parent, None)
    if not parentitem:
        hierarchy[parent] = {child: childitem}
        root.add(parent)
    else:
        parentitem[child] = childitem

#visualize relationships via built in json library ( also a bit low on time at the moment :) )
print(json.dumps(hierarchy, sort_keys = True, indent = 6))