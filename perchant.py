from name import Merchant
from hero import Hero
Audrey = Merchant("Audrey", ["Sea-Shell", "Green Sweater", "jarvis", "Soul"])
Hambergs = Hero("Amber", 500, ["Hamburger"])
item =  Audrey.sell("Soul")
Hambergs.buy(item)
