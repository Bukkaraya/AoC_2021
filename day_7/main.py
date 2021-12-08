if __name__ == "__main__":
    with open("input.txt", "r") as f:
        crab_positions = f.read().split("\n")[0].split(",")

    crab_positions = sorted(list(map(int, crab_positions)))

    best_fuel_cost = 100000000
    best_altered_fuel_cost = 100000000
    for i in range(len(crab_positions)):
        current_alignment = i
        fuel_cost = 0
        altered_fuel_cost = 0

        for pos in crab_positions:
            n = abs(pos - current_alignment)
            altered_fuel_cost += n * (n+1) / 2

            fuel_cost += n
        
        if fuel_cost < best_fuel_cost:
            best_fuel_cost = fuel_cost
        
        if altered_fuel_cost < best_altered_fuel_cost:
            best_altered_fuel_cost = altered_fuel_cost
    
    print(f"Answer for Part 1: {best_fuel_cost}")
    print(f"Answer for Part 2: {best_altered_fuel_cost}")

