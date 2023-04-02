class Item:
    def __init__(self, **kwargs):
        self.name = kwargs['name'] # recommended string with 32 char
        self.desc = kwargs['desc'] # recommended string with 256 char
        self.price = kwargs['price'] # recommended int
        self.seller = kwargs['seller'] # recommended string with 32 char
        self.image = kwargs['image'] # The url of image should given

class Snack(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Clothing(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = kwargs['size'] # recommended string with 4 char
        self.color = kwargs['color'] # recommended string with 16 char

class ComputerPart(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spec_identifier = kwargs['ident'] # recommended string with 16 char
        self.spec_amount = kwargs['amount'] # recommended int
        self.spec_unit = kwargs['unit'] # recommended string with 4 char