class Food:
    base_hearts = 1
    def __init__(self, ingredience):
        self.ingredience = ingredience
        self.hearts = Food.calculate_hearts(ingredience)

    @classmethod
    def calculate_hearts(cls, ingredience):
        hearts = cls.base_hearts
        for ingredient in ingredience:
            if "apple" in ingredient:
                hearts += 2
            else:
                hearts += 1
        return hearts

    @classmethod
    def from_nothing(cls, heart):
        food = cls(ingredience=[])
        food.hearts = heart
        return food


        

def main():
    mushroom_skewer = Food(ingredience=["apple", "banana", "melon", "watermelon"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")

    mushroom_skewer = Food.from_nothing(heart = 4)
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")
if __name__ == "__main__":
    main()

