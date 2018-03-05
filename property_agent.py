def get_valid_input(input_string, valid_options):
    """
    Function which check if input information is correct
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    # input information
    response = input(input_string)
    # check if information is correct
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    """
    Class which represent property in total
    """

    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Print information about the property
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        Input information about the property
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    Class which represent apartments, use class Property
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Print information about apartments
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        """
        Read information about the apartments
        """
        parent_init = Property.prompt_init()
        # get_valid_input check if information is correct
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ",
            Apartment.valid_laundries)
        # get_valid_input check if information is correct

        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        # add new information
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    Class which represent houses
    """
    # correct values to check
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Print information about the house
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        Read information about the house
        """
        parent_init = Property.prompt_init()
        # check if information is correct
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Print information about the house
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        Read information about the house
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Class which represent type of payment - rent
    """

    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        Print information about the rent
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        Read information about rent
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """
    Class for renting house
    """

    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    Class for renting apartments
    """

    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    Class for buying apartments
    """

    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    Class for buying house
    """

    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Class which represent agent, to manage information
    """

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        """
        Print information about the property
        """
        for property in self.property_list:
            property.display()

    # map to manage property
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        """
        Method to add new property
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def property_price_purchasing(self, flag="min"):
        """
        Function return cheapest or most expansive property for purchasing
        """
        # list with all prices
        prices = []
        for property in self.property_list:
            # check if property is for purchasing
            if issubclass(type(property), Purchase):
                try:
                    # add new price of property
                    prices.append(int(property.price))
                except:
                    pass
        # choose mod of function
        if flag == "min":
            price = min(prices)
        else:
            price = max(prices)
        # print information about property
        for property in self.property_list:
            if issubclass(type(property), Purchase):
                try:
                    if int(property.price) == price:
                        property.display()
                except:
                    pass

    def property_price_renting(self, flag="min"):
        """
        Function return cheapest or most expansive property for renting
        """
        # list with rents
        prices = []
        for property in self.property_list:
            # check if property is for renting
            if issubclass(type(property), Rental):
                try:
                    # add new rent of property
                    prices.append(int(property.rent))
                except:
                    pass
        # choose mod of function
        if flag == "min":
            price = min(prices)
        else:
            price = max(prices)
        # print information about property
        for property in self.property_list:
            if issubclass(type(property), Rental):
                try:
                    if int(property.rent) == price:
                        property.display()
                except:
                    pass
