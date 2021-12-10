from pprint import pprint

LED_MAPPINGS = [
    "abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf",
    "abcdefg", "abcdfg"
]

UNIQUE_LED_SEGMENTS_LENGTH = [
    len(LED_MAPPINGS[1]),
    len(LED_MAPPINGS[4]),
    len(LED_MAPPINGS[7]),
    len(LED_MAPPINGS[8]),
]

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputs = f.read().split("\n")

    unique_segments = list(map(lambda a: a.split("|")[1].strip(), inputs))
    unique_segments = [ u.split() for u in unique_segments]

    total_unique = 0
    for u in unique_segments:
        for segment in u:
            if len(segment) in UNIQUE_LED_SEGMENTS_LENGTH:
                total_unique += 1
    
    print(f"Result for Part 1: {total_unique}")

