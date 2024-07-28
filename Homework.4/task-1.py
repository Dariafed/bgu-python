def read_cities_from_file() -> list[tuple[str, int]]:
    populations = []
    try:
        with open("cities.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                try:
                    city, population = map(str.strip, line.split(":"))
                    populations.append((city, int(population)))
                except ValueError:
                    print(f"Error parsing line: {line.strip()}")
    except FileNotFoundError:
        print("Input file not found.")
    return populations


def write_cities_to_file(populations: list[tuple[str, int]]) -> None:
    with open("filtered_cities.txt", "w") as f:
        for city, population in populations:
            f.write(f"{city}:{population}\n")


def filter_file(min_population: int) -> None:
    try:
        populations = read_cities_from_file()
        filtered_populations = [
            city for city in populations if city[1] > min_population
        ]
        filtered_populations.sort(key=lambda city: city[0])
        write_cities_to_file(filtered_populations)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    while True:
        try:
            min_population = int(input("Please enter the minimum number of population: "))
            break
        except ValueError:
            print('Invalid input, please enter an integer value.')
    filter_file(min_population)


if __name__ == '__main__':
    main()
