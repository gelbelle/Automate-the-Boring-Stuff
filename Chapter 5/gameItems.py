class Items:
    def __init__(self, name, is_magical, durability):
        self.name = name
        self.is_magical = is_magical
        self.durability = durability

    @property
    def durability(self):
        return self._durability

    @durability.setter
    def durability(self, value):
        if not isinstance(value, int | float) or value < 0:
            raise ValueError("Positive number expected")
        self._durability = value

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


class Treasure(Items):
    def __init__(self, name, is_magical, value):
        super().__init__(name, is_magical, 100)
        self.value = value

        def spend(self):
            return -self.value
