def printStats(t):
    def stats_decorator(func):
        def wrapper(numbers):
            count = len(numbers)
            total = sum(numbers)
            average = total / count
            maximum = max(numbers)

            print("Numbers:", numbers)
            print("Count:", count)
            print("Average:", average)
            print("Maximum:", maximum)

            return func(numbers)

        return wrapper
    @stats_decorator
    def printStats(numbers):
        pass
    with open(t, 'r') as file:
            for line in file:
                line = line.strip()
                split_line = line.split()
                numbers = [float(num) for num in split_line]
                printStats(numbers)

printStats('printStats.txt')
