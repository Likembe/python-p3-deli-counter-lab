def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently:"
        for i, person in enumerate(katz_deli, start = 1):
            line_str += f"{i}.{person}"
        print(line_str)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving_person = katz_deli.pop(0)
        print(f"Currently serving {serving_person}.")

katz_deli = []
take_a_number(katz_deli, " Ada ")
take_a_number(katz_deli, " Grace ")
take_a_number(katz_deli, " Kent ")

line(katz_deli)
now_serving(katz_deli)
line(katz_deli)
