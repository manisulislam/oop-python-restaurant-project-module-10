from Menu import Burger, Drinks, Pizza, Menu
from restaurant import Restaurant
from users import Chef, Customer, Manager, Server
def main():
    menu= Menu()
    # pizza
    pizza_1= Pizza("sutki pizza",600, "large",["sutki", "onion", "oil"])
    menu.add_menu_item("pizza", pizza_1)
    pizza_2= Pizza("alor vorta pizza", 420, "big", ["potato", "oil"])
    menu.add_menu_item("pizza", pizza_2)
    pizza_3= Pizza("dal er pizza", 500, "small",["dal", "oil"])
    menu.add_menu_item("pizza", pizza_3)

    # burger
    burger_1= Burger("naga burger", 520,"chicken",["bread","chili"])
    menu.add_menu_item("burger", burger_1)
    burger_2 = Burger("beef burger", 6520, "beef", ["goro", "haddi"])
    menu.add_menu_item("burger", burger_2)
    
    # drinks
    coke= Drinks("coke", 50, True)
    menu.add_menu_item("drinks", coke)
    coffee = Drinks("mocha coffee", 120, False)
    menu.add_menu_item("drinks",coffee)

    # show menu
    menu.show_menu()

    # restaurant
    restaurant= Restaurant("sai baba restaurant",2000, menu)

    # add employee
    manager= Manager("kala chan","032145","ka@gmail.com", "kala pur",2000, "jan 1 2020","core")

    restaurant.add_employee("manager", manager)

    chef= Chef("rostom", "526156", "ros@gmail.com","india",4000,"february 2 2020","chef","everything")
    restaurant.add_employee("chef",chef)
    
    server=Server("pakhi bai", "41526","paki@gamil.com","pakistan",1450,"june 2 2020","server")
    restaurant.add_employee("server", server)

    # show employee
    restaurant.show_employee()





if __name__ == "__main__":
    main()