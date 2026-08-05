import sys
import os


def print_and_exit(message):
    print(message)
    sys.exit(1)


def check_argument_file(filepath):
    if not os.path.exists(filepath):
        print_and_exit(f"Error: '{filepath}' does not exist")
    if not os.path.isfile(filepath):
        print_and_exit(f"Error: '{filepath}' is not a file")
    if not os.access(filepath, os.R_OK):
        print_and_exit(f"Error: '{filepath}' is not readable")


def read_entries(filepath):
    entries = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            origin, destination, distance = line.split(",")
            entries.append((origin, destination, int(distance)))
    return entries


def do_option_a(entries):
    if len(entries) == 0:
        print("No city distance information in this file")
        return
    print("Origin and destination cities:")
    for origin, destination, _ in entries:
        print(f"{origin} >> {destination}")


def do_option_o(entries, origin):
    matches = [(d, dist) for (o, d, dist) in entries if o == origin]
    if len(matches) == 0:
        print(f"No known destinations from {origin}")
        return
    print(f"Destinations from {origin}:")
    for i, (dest, dist) in enumerate(matches, start=1):
        print(f"{i}. {dest} ({dist} km)")


def do_option_d(entries, max_distance):
    matches = [(o, d, dist) for (o, d, dist) in entries if dist <= max_distance]
    if len(matches) == 0:
        print(f"No cities within {max_distance} Km")
        return
    print(f"Cities within {max_distance} Km distance:")
    for origin, destination, dist in matches:
        print(f"Distance: {dist}")
        print(f"{origin} >> {destination}")


def do_option_v():
    print("Name: Jinkyeong")
    print("Surname: Kim")
    print("Student ID: 14657314")
    print("Date of completion: 17 May 2026")


def main():
    argv = sys.argv

    if len(argv) < 3:
        print_and_exit(
            "Usage: python travelhelper.py {-a | -v | -o origin | -d distance} argument_file"
        )

    option = argv[1]

    if option == "-a":
        if len(argv) != 3:
            print_and_exit("Usage: python travelhelper.py -a argument_file")
        argument_file = argv[2]
        check_argument_file(argument_file)
        entries = read_entries(argument_file)
        do_option_a(entries)

    elif option == "-v":
        if len(argv) != 3:
            print_and_exit("Usage: python travelhelper.py -v argument_file")
        argument_file = argv[2]
        check_argument_file(argument_file)
        do_option_v()

    elif option == "-o":
        if len(argv) != 4:
            print_and_exit("Usage: python travelhelper.py -o origin argument_file")
        origin = argv[2]
        argument_file = argv[3]
        check_argument_file(argument_file)
        entries = read_entries(argument_file)
        do_option_o(entries, origin)

    elif option == "-d":
        if len(argv) != 4:
            print_and_exit("Usage: python travelhelper.py -d distance argument_file")
        try:
            distance = int(argv[2])
        except ValueError:
            print_and_exit("Error: distance must be a non-negative integer")
        argument_file = argv[3]
        check_argument_file(argument_file)
        entries = read_entries(argument_file)
        do_option_d(entries, distance)

    else:
        print_and_exit(f"Error: unknown option '{option}'")


if __name__ == "__main__":
    main()
