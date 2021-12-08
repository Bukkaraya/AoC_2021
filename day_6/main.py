from collections import Counter

if __name__ == "__main__":
    with open("public_input.txt", "r") as f:
        fishes = f.read().split("\n")[0].split(",")
    
    fishes = list(map(int, fishes))
    fish_count = Counter(fishes)

    unqiue_fishes = set(fishes)

    default_days_till_new_fish = 6

    results_for_each_fish = {}
    for fish in unqiue_fishes:
        current_fishes = [fish]
        for _ in range(256):
            for i in range(len(current_fishes)):
                if current_fishes[i] == 0:
                    current_fishes[i] = default_days_till_new_fish
                    current_fishes.append(default_days_till_new_fish + 2)
                else:
                    current_fishes[i] -= 1
        results_for_each_fish[fish] = len(current_fishes)
    
    final_fish_count = 0
    for k, v in results_for_each_fish.items():
        final_fish_count += v * fish_count[k]

    print(f"Result for Part 1: {final_fish_count}")
    print(f"Result for Part 2: {final_fish_count}")