class ProductOfNumbers:

    def __init__(self):
        self.stream = []

    def add(self, num: int) -> None:
        self.stream.append(num)

    def getProduct(self, k: int) -> int:
        # print("hi")
        # print(self.stream)
        stream_copy = []
        for i in range(len(self.stream)):
            stream_copy.append(self.stream[i])
        prod = 1
        for i in range(k):
            num = stream_copy.pop()
            prod *= num
            # print(f"adding {num}")
        return prod

# This runs in O(n) time complexity! 

# to run in O(1) time complexity, we need to use prefix sums: class ProductOfNumbers:
    # def __init__(self):
    #     self.prefix = [1]  # Initialize prefix with 1 to handle division
    #     self.last_zero_index = -1  # Tracks the last index where 0 was added

    # def add(self, num: int) -> None:
    #     if num == 0:
    #         self.prefix = [1]  # Reset prefix list
    #         self.last_zero_index = len(self.prefix) - 1  # Track zero index
    #     else:
    #         self.prefix.append(self.prefix[-1] * num)  # Store cumulative product

    # def getProduct(self, k: int) -> int:
    #     if k >= len(self.prefix):  
    #         return 0  # If k is larger than the available non-zero numbers, return 0
    #     return self.prefix[-1] // self.prefix[-(k + 1)]  # Compute product

# Your ProductOfNumbers object will be instantiated and called as such:

productOfNumbers =  ProductOfNumbers();
productOfNumbers.add(3);        # [3]
productOfNumbers.add(0);        # [3,0]
productOfNumbers.add(2);        # [3,0,2]
productOfNumbers.add(5);        # [3,0,2,5]
productOfNumbers.add(4);        # [3,0,2,5,4]
print(productOfNumbers.getProduct(2)); # return 20. The product of the last 2 numbers is 5 * 4 = 20
print(productOfNumbers.getProduct(3)); # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
print(productOfNumbers.getProduct(4)); # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        # [3,0,2,5,4,8]
print(productOfNumbers.getProduct(2)); # return 32. The product of the last 2 numbers is 4 * 8 = 32 