# Module 3
#   Programming Assignment 4
#     Prob-5.py

# <Grant Parkinson>


def main():
    try:
        x = eval(2)
        print("x:", x)
    except TypeError:
        print("\n\nThere was a Type Error... exiting\n\n")
        exit
    except:
        print("\n\nThere was an unknown error... exiting\n\n")
        exit


main()
