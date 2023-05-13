# Practice

# You have 100 cats.

# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat(cat  # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.

# The first round, you stop at every cat, placing a hat on each one.
# The second round, you only stop at every second cat(  # 2, #4, #6, #8, etc.).
# The third round, you only stop at every third cat(  # 3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats(e.g., you only visit the 100th cat).
# Write a program that simply outputs which cats have hats at the end.
# Optional: Make function that can calculate hat with any amount of rounds and cats.

# Here you should write an algorithm, after that, try to make pseudo code. Only after that start to work. Code is simple here, but you might struggle with algorithm. Therefore don`t try to write a code from the first attempt.

# Homework should be uploaded at GitHub.com Result of this HW should be a link to your GitHub code


cats_with_hats = []


def get_cats_with_hats(number_of_laps, number_of_cats, step):

    for lap in range(1, number_of_laps + 1, step):

        for cat in range(1, number_of_cats + 1):
            pass
            if cat % lap == 0:

                if cat in cats_with_hats:
                    cats_with_hats.remove(cat)
                else:
                    cats_with_hats.append(cat)

    print(cats_with_hats)


get_cats_with_hats(100, 100, 1)
# get_cats_with_hats(100, 100, 2)
# get_cats_with_hats(100, 100, 3)
