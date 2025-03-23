class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
    #     self.spaces = {
    #         1: big,
    #         2: medium,
    #         3: small
    #     }

    # def addCar(self, carType: int) -> bool:
    #     if self.spaces[carType] > 0:
    #         self.spaces[carType] -= 1
    #         return True
    #     return False
        self.count = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        i = carType - 1
        if not self.count[i]:
            return False
        self.count[i] -= 1
        return True

        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)