#!/usr/bin/env python3

# Created by Brian Musembi
# Created on June 2021
# This program finds the average of a list of marks


def average_of_marks(marks):
    # This function finds the average of all the marks
    total = 0

    for loop_counter in marks:
        total += loop_counter
    average = (total / len(marks))

    return average


def main():
    # This function handles input and calls a function

    print("This program accepts a list of marks and"
          " calculates the average. Enter -1 to calculate"
          " the average.")
    print("")

    marks = []
    temp_mark = 0

    # input
    while True:
        try:
            temp_mark = input("Enter a mark (%): ")
            mark_int = int(temp_mark)
            marks.append(mark_int)

            while mark_int != -1:
                temp_mark = input("Enter a mark (%): ")
                mark_int = int(temp_mark)
                marks.append(mark_int)

            marks.pop()
            print("")

            average_of_list = average_of_marks(marks)
            average_rounded = '{0:.4g}'.format(average_of_list)

            print("")
            print("The average of all the numbers is: {0}"
                  .format(average_rounded))

            break

        except Exception:
            # output
            print("Enter a number for all values, try again.")


if __name__ == "__main__":
    main()
