from WineRs.WineRS_app.models import Wine
from datetime import datetime

path = "Datos"


def populateWines():
    print("Loading wines...")
    Wine.objects.all().delete()

    fileobj = open(path + "\\winemag-data_first150k.csv", "r")
    line = fileobj.readline()
    while line:
        data = line.split(',')
        if len(data) > 1:
            country1 =  data[1].strip().decode('utf-8', 'replace')
            description1 = data[2].strip().decode('utf-8', 'replace')
            designation1 = data[3].strip().decode('utf-8', 'replace')
            points1 = data[4].strip().decode('utf-8', 'replace')
            price1 = int(data[5].strip())
            province1 = data[6].strip().decode('utf-8', 'replace')
            region_11 = data[7].strip().decode('utf-8', 'replace')
            region_21 = data[8].strip().decode('utf-8', 'replace')
            variety1 = data[9].strip().decode('utf-8', 'replace')
            winery1 = data[10].strip().decode('utf-8', 'replace')

            Wine.objects.create(country = country1 ,description = description1,designation = designation1,points=points1,price=price1,province=province1,region_1=region_11,region_2=region_21,variety=variety1,winery=winery1)
    fileobj.close()

    print("Wines inserted: " + str(Wine.objects.count()))
    print("---------------------------------------------------------")


def populateDatabase():
    populateWines()
    print("Finished database population")


if __name__ == '__main__':
    populateDatabase()