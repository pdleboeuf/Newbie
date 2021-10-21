# Paul LeBoeuf Planetary Assignment

# Ask user to enter name and weight
sName =(input("What is your name? "))
nEarth =(input("What is your weight? "))

#Convert weight to float
nEarthWeight = float(nEarth)

#Assign planets their gravity factor
MercuryGravity = 0.38
VenusGravity = 0.91
MoonGravity = 0.165
MarsGravity = 0.38
JupiterGravity = 2.34
SaturnGravity = 0.93
UranusGravity = 0.92
NeptuneGravity = 1.12
PlutoGravity = 0.066

#Calculate earth weight by gravity factor to find that planet's weight equivalent

nMercuryWeight = nEarthWeight * MercuryGravity
nVenusWeight = nEarthWeight * VenusGravity
nMoonWeight = nEarthWeight * MoonGravity
nMarsWeight = nEarthWeight * MarsGravity

#Display results of the weight equivalents
print(sName,("Here are your weights on our Solar System's Planets:"))
print("Weight on Mercury is:" + format(nMercuryWeight, '.2f'))
print("Weight on Mars is:" + format(nMarsWeight, '.2f'))
print("Weight on Venus is:" + format(nVenusWeight, '.2f'))
