from apfel import Apfel
from gras import Gras
from kuh import Kuh
from schwein import Schwein
from stall import Stall




myStall = Stall()
mySchwein = Schwein("mySchweindel")
myKuh = Kuh("myMoohCooh")

mySchwein.fressen([("name", "Apfel"),("proNomen", "der")])
myKuh.fressen(Gras())


