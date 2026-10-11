# Name: Diesta, Macy T.
# Date: October 11, 2026
# Course: PROGCON IT261
# File: wk11d02ex01_compute_average.py
# Description: Asks for up to 10 numbers, stops early when 0 is entered,
#              and computes the average using a separate function.
#              Converted from my Flowgorithm file wk11d02ex01_compute_average.fprg.


# Flowgorithm: ComputeAverage(numbers, count)
# Adds up the first `count` numbers and returns the total divided by count.
def compute_average(numbers, count):
    total = 0
    # Flowgorithm: For i = 0 to count - 1
    for i in range(count):
        total = total + numbers[i]
    result = total / count
    return result


# Flowgorithm: Main
def main():
    numbers = [0] * 10      # Flowgorithm: Real Array numbers[10]
    count = 0
    num = 1                 # any non-zero value so the loop can start

    # Flowgorithm: While count < 10 AND num != 0
    while count < 10 and num != 0:
        num = float(input("Enter a number (0 to stop): "))
        # Flowgorithm: If num != 0 (the zero is not counted or saved)
        if num != 0:
            numbers[count] = num
            count = count + 1

    # Flowgorithm: If count > 0, call the separate function
    if count > 0:
        average = compute_average(numbers, count)
        print("Average:", average)
    else:
        print("No numbers were entered.")


if __name__ == "__main__":
    main()
