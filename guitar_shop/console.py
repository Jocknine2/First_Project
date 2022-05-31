import pdb
from models.guitar import Guitar
from models.shop import Shop
from models.manufacturer import Manufacturer

import repositories.guitar_repository as guitar_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.shop_repository as shop_repository

shop_repository.delete_all()
manufacturer_repository.delete_all()
guitar_repository.delete_all()

guitar1 = Guitar("X106s", "Axe", 250, 599, "6 string, 24 frets, 2 humbucker")
guitar_repository.save(guitar1)

guitar2 = Guitar("Stratocaster", "Axe", 400, 900, "6 string, 22 frets, 3 single coil")
guitar_repository.save(guitar2)

guitar3 = Guitar(
    "79' Les Paul", "log", 580, 1600, "6 string, 22 frets, redesigned 59' humbuckers"
)
guitar_repository.save(guitar3)

guitar4 = Guitar(
    "Telecaster", "tele", 450, 870, "61, 6 string, 22 frets, 2 single coil, "
)
guitar_repository.save(guitar4)

guitar5 = Guitar("Flying V", "V", 600, 1200, "6 string, iconic body, dual humbucker")
guitar_repository.save(guitar5)

manufacturer1 = Manufacturer("ESP")
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer("Fender")
manufacturer_repository.save(manufacturer2)

manufacturer3 = Manufacturer("Gibson")
manufacturer_repository.save(manufacturer3)

product1 = Shop(guitar1, manufacturer1)
shop_repository.save(product1)

product2 = Shop(guitar2, manufacturer2)
shop_repository.save(product2)

product3 = Shop(guitar3, manufacturer3)
shop_repository.save(product3)

product4 = Shop(guitar4, manufacturer2)
shop_repository.save(product4)

product5 = Shop(guitar5, manufacturer3)
shop_repository.save(product5)


pdb.set_trace()
