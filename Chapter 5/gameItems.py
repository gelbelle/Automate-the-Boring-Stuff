class Items:
    def __init__(self, name, durability):
        self.name = name
        self.durability = durability

    @property
    def name(self):
        return self._name

    @property
    def is_magical(self):
        self.is_magical = False

    @property
    def durability(self):
        return self._durability

    @durability.setter
    def set_durability(self, value):
        if not isinstance(value, int | float) or value < 0:
            raise ValueError("Positive number expected")
        self.durability = value

    @classmethod
    def repair(self, repair_amount):
        return self.durability + repair_amount

    @classmethod
    def wear_and_tear(self, degrade_amount):
        return self.durability - degrade_amount

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)


class Weapon(Items):
    def __init__(self, name, is_magical, durability, damage_amount, damage_type):
        super().__init__(name, is_magical, durability)
        self.damage_amount = damage_amount
        self.damage_type = damage_type

    def attack(self):
        return self.damage_amount


class Armour(Items):
    def __init__(self, name, is_magical, durability, defense_amount):
        super().__init__(name, is_magical, durability)
        self.defense_amount = defense_amount

    def defend(self):
        return self.defense_amount
