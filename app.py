from money import *
from datetime import *
from tourist import *
from tour import *



tour = TourBuilder("Italy","The best parst of Italy",[Tourist("John Doe", 21), Tourist("Jane Doe", 30), Tourist("Jenny", 6)],Period("01.01.2021","02.02.2021")).withEnsurance().withGuide().build()
