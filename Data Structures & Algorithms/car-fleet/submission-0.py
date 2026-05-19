class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort()
        fleets = 1
        currCar = cars[-1]
        for i in range(len(position) - 2, -1, -1):
            if ((target - cars[i][0]) / cars[i][1] <= (target - currCar[0]) / currCar[1]):
                continue
            else:
                fleets += 1
                currCar = cars[i]
        return fleets
                