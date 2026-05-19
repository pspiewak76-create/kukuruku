import random

WORLD_MIN = -10
WORLD_MAX = 10
MAX_STEPS = 30


def get_number(message, min_val=-100, max_val=100):
    while True:
        try:
            value = int(input(message))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Podaj liczbę z zakresu od {min_val} do {max_val}!")
        except ValueError:
            print("Podaj poprawną liczbę całkowitą!")


def move_rover(x, y, direction):
    old_x, old_y = x, y

    if direction == "W":
        y += 1
    elif direction == "S":
        y -= 1
    elif direction == "D":
        x += 1
    elif direction == "A":
        x -= 1

    x = max(WORLD_MIN, min(WORLD_MAX, x))
    y = max(WORLD_MIN, min(WORLD_MAX, y))

    return old_x, old_y, x, y


def random_event(energy):
    event = random.randint(1, 4)

    if event == 1:
        print("Łazik znalazł baterię! +5 energii")
        energy += 5
    elif event == 2:
        print(" Burza piaskowa! -4 energii")
        energy -= 4
    elif event == 3:
        print(" Kamienie uszkodziły łazik! -2 energii")
        energy -= 2
    else:
        print("Spokojny teren. Nic się nie stało.")

    return energy


def print_report(name, start_x, start_y, x, y, energy, steps, history, reason):
    print("\n==============================")
    print("RAPORT KOŃCOWY")
    print("==============================")

    print(f"Nazwa łazika: {name}")
    print(f"Pozycja startowa: ({start_x}, {start_y})")
    print(f"Pozycja końcowa: ({x}, {y})")
    print(f"Liczba kroków: {steps}")
    print(f"Pozostała energia: {energy}")
    print(f"Powód zakończenia: {reason}")

    print("\nNajważniejsze zdarzenia:")
    for item in history:
        print("-", item)

    score = energy + (MAX_STEPS - steps)

    print(f"\nWynik końcowy: {score}")

    if energy > 0:
        print("Misja zakończona sukcesem!")
    else:
        print("Misja zakończona porażką!")


def game():
    print("==============================")
    print("SYMULATOR ŁAZIKA MARSA")
    print("==============================")

    name = input("Podaj nazwę łazika: ")

    start_x = get_number("Podaj startowe X (-100 do 100): ")
    start_y = get_number("Podaj startowe Y (-100 do 100): ")

    x = start_x
    y = start_y

    energy = get_number("Podaj ilość energii (0 do 100): ", min_val=0, max_val=100)

    print("\nSterowanie:")
    print("W - góra")
    print("S - dół")
    print("A - lewo")
    print("D - prawo")

    print(f"\nGranice świata gry: {WORLD_MIN} do {WORLD_MAX}")
    print(f"Maksymalna liczba kroków: {MAX_STEPS}")

    history = []
    steps = 0

    while True:
        if energy <= 0:
            reason = "Brak energii"
            break

        if steps >= MAX_STEPS:
            reason = "Osiągnięto limit kroków"
            break

        print("\n----------------------")
        print(f"Krok: {steps + 1}")
        print(f"Pozycja: ({x}, {y})")
        print(f"Energia: {energy}")

        direction = input("Wybierz ruch (W/A/S/D): ").upper()

        if direction not in ["W", "A", "S", "D"]:
            print("Niepoprawny ruch!")
            continue

        old_x, old_y, x, y = move_rover(x, y, direction)

        print(f"Pozycja przed ruchem: ({old_x}, {old_y})")
        print(f"Pozycja po ruchu: ({x}, {y})")

        energy_before = energy
        energy -= 1

        print(f"Energia przed ruchem: {energy_before}")
        print(f"Energia po ruchu: {energy}")

        energy = random_event(energy)

        history.append(f"Ruch na ({x}, {y})")

        if x == 5 and y == 5:
            print(" Łazik dotarł do celu!")
            reason = "Odnaleziono bazę"
            break

        steps += 1

    print_report(
        name,
        start_x,
        start_y,
        x,
        y,
        energy,
        steps,
        history,
        reason
    )


while True:
    game()

    again = input("\nCzy chcesz zagrać ponownie? (t/n): ").lower()
    if again != "t":
        print("Koniec programu.")
        break
