class DVD:
    def __init__(self, name:str, releaseYear:int, director:str):
        self.name = name
        self.releaseYear = releaseYear
        self.director = director
    
    def __str__(self):
        return self.name+", directed by "+self.director+", released in "+str(self.releaseYear)

dvdCollection = [None]*15
avengerDVD = DVD("The Avengers", 2012, "Joss Whedon")
incrediblesDVD = DVD("The Incredibles", 2004, "Brad Bird")
findingDoryDVD = DVD("Finding Dory", 2016, "Andrew Stanton")
lionKingDVD = DVD("The Lion King", 2019, "Jon Favreau")
starWarsDVD = DVD("Star Wars", 1977, "George Lucas")

dvdCollection[7] = avengerDVD
dvdCollection[3] = incrediblesDVD
dvdCollection[9] = findingDoryDVD
dvdCollection[2] = lionKingDVD
dvdCollection[3] = starWarsDVD

for dvd in dvdCollection:
    print(dvd)

squaresArray = []

for i in range(10):
    squaresArray.append((i+1)**2)

print(squaresArray)