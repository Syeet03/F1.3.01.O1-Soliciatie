print("- - - - - - - -Sollicitatie Circus directeur- - - - - - - -")

# Wat is uw naam?
naam = input('Wat is uw naam? ')
gewicht = int(input('Wat is uw lichaamsgewicht in KG? '))
if gewicht >= 90:
    gewicht = True
else:
    gewicht = False

# Hoe lang bent u in centimeters?
lengte = int(input('Hoe lang bent u in centimeters? '))
if lengte >= 150:
    lengte = True
else:
    lengte = False

# Hoeveel jaar heeft u praktijkervaring met dieren-dressuur?
dierenDressuur = int(input('Hoeveel jaar heeft u praktijkervaring met dieren-dressuur? '))
if dierenDressuur >= 4:
    dierenDressuur = True   
else:
    dierenDressuur = False

# Hoeveel jaar heeft u ervaring met jongleren?
jongleren = int(input('Hoeveel jaar heeft u ervaring met jongleren? '))
if jongleren >= 5:
    jongleren = True
else:
    jongleren = False

# Hoeveel jaar ervaring heeft u met acrobatiek?
acrobatiek = int(input('Hoeveel jaar ervaring heeft u met acrobatiek? '))
if acrobatiek >= 3:
    acrobatiek = True
else:
    acrobatiek = False

# Heeft u een MBO 4 dilpoma ondernemen?
diploma = str(input('Heeft u een MBO 4 dilpoma ondernemen? Ja/Nee '))
if diploma == "Ja":
    diploma = True
else:
    diploma = False

# Bent u in bezit van een geldig vrachtwagen rijbewijs?
vrachtwagenRijbewijs = str(input('Bent u in bezit van een geldig vrachtwagen rijbewijs? Ja/Nee '))
if vrachtwagenRijbewijs == "Ja":
    vrachtwagenRijbewijs = True
else:
    vrachtwagenRijbewijs = False

# Heeft u een hoge hoed?
hogeHoed = str(input('Heeft u een hoge hoed? Ja/Nee '))
if hogeHoed == "Ja":
    hogeHoed = True
else:
    hogeHoed = False

# Heeft u een certificaat in bezit over overleven met gevaarlijk personeel?
certificaat = str(input('Heeft u een certificaat in bezit over overleven met gevaarlijk personeel? Ja/Nee '))
if certificaat == "Ja":
    certificaat = True
else:
    certificaat = False

# Bent u een man of vrouw?
geslacht = input ("Bent u een man of vrouw? Man/Vrouw ")
if geslacht == "Man":
    # Hoe breedt is uw snor in centimeters?
    manSnor = int(input ("Hoe breedt is uw snor in centimeters? "))
    if manSnor >= 10:
        manSnor = True
    else:
        manSnor = False
else:
    # Heeft u rood krullend haar? Zo ja, wat is de lengte in centimeters?
    vrouwHaar = int(input ("Heeft u rood krullend haar? Zo ja, wat is de lengte in centimeters? "))
    if vrouwHaar >= 20:
        vrouwHaar = True
    else:
        vrouwHaar = False

werkervaring = (dierenDressuur, jongleren, acrobatiek)
overig = (gewicht, lengte, diploma, vrachtwagenRijbewijs, hogeHoed, certificaat, geslacht)

werkervaring = all(werkervaring)
overig = any(overig)

y = werkervaring
x = overig

if y == True:
    werkErvaringFinalString = "voldoende"
elif y == False:
    werkErvaringFinalString = "onvoldoende"

if x == True:
    overigFinalString = "voldoende"
elif x == False:
    overigFinalString = "onvoldoende"

# Uitslag van de sollicitatie
print ("Beste,",naam,"u heeft",werkErvaringFinalString,"werkervaring en",overigFinalString, "overige ervaring")