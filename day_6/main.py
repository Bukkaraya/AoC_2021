import copy
from collections import Counter

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        fishes = f.read().split("\n")[0].split(",")
    
    fishes = list(map(int, fishes))
    results_for_each_fish = {}
    current_fishes = Counter(fishes)

    default_days_till_new_fish = 6

    for i in range(256):
        updated_fishes = copy.deepcopy(current_fishes)

        new_fishes = 0
        for j in range(9):
            if j == 0:
                new_fishes = updated_fishes.get(0, 0)
                updated_fishes[0] = 0
                continue
            updated_fishes[j - 1] = current_fishes.get(j, 0)

        updated_fishes[default_days_till_new_fish + 2] = new_fishes
        updated_fishes[default_days_till_new_fish] = updated_fishes.get(default_days_till_new_fish, 0) + new_fishes
        current_fishes = copy.deepcopy(updated_fishes)

        if i == 79:
            part_one_fish_count = sum([v for _, v in current_fishes.items()])

    part_two_fish_count = sum([v for _, v in current_fishes.items()])

    print(f"Result for Part 1: {part_one_fish_count}")
    print(f"Result for Part 1: {part_two_fish_count}")
