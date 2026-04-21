import os
print(os.getcwd())


import json
import os

file_name = "finance_tracker.json"


def load_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return {"shifts": []}


def save_data(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def add_shift(data):
    date = input("date (yyyy-mm-dd): ")
    shift_type = input("shift type: ")
    hours = float(input("hours: "))
    rate = float(input("hourly rate: "))
    tips = float(input("tips: "))

    total = hours * rate + tips

    shift = {
        "date": date,
        "shift_type": shift_type,
        "hours": hours,
        "rate": rate,
        "tips": tips,
        "total": total
    }

    data["shifts"].append(shift)
    save_data(data)

    print(f"saved - you made ${total:.2f}\n")


def view_shifts(data):
    if not data["shifts"]:
        print("no shifts saved\n")
        return

    print("\nall shifts")
    print("-" * 60)
    for shift in data["shifts"]:
        print(f"{shift['date']} | {shift['shift_type']} | {shift['hours']} hrs | ${shift['rate']}/hr | tips: ${shift['tips']:.2f} | total: ${shift['total']:.2f}")
    print()


def total_money(data):
    total = sum(shift["total"] for shift in data["shifts"])
    print(f"\ntotal made from all shifts: ${total:.2f}\n")


def month_total(data):
    month = input("enter month (yyyy-mm): ")
    total = 0

    for shift in data["shifts"]:
        if shift["date"].startswith(month):
            total += shift["total"]

    print(f"\ntotal for {month}: ${total:.2f}\n")


def week_total(data):
    start = input("week start date (yyyy-mm-dd): ")
    end = input("week end date (yyyy-mm-dd): ")
    total = 0

    for shift in data["shifts"]:
        if start <= shift["date"] <= end:
            total += shift["total"]

    print(f"\ntotal from {start} to {end}: ${total:.2f}\n")


def main():
    data = load_data()

    while True:
        print("1. add shift")
        print("2. view shifts")
        print("3. total money")
        print("4. month total")
        print("5. week total")
        print("6. quit")

        choice = input("pick: ")

        if choice == "1":
            add_shift(data)
            data = load_data()
        elif choice == "2":
            view_shifts(data)
        elif choice == "3":
            total_money(data)
        elif choice == "4":
            month_total(data)
        elif choice == "5":
            week_total(data)
        elif choice == "6":
            break
        else:
            print("invalid choice\n")


main()
