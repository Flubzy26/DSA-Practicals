def fractional_knapsack(parcels, capacity):
    if not parcels or capacity <= 0:
        return 0, []

    # Calculate profit-to-weight ratio and sort parcels
    parcels = sorted(parcels, key=lambda x: x['profit'] / x['weight'], reverse=True)

    total_profit = 0
    selected = []

    for parcel in parcels:
        if capacity == 0:
            break
        if parcel['weight'] <= capacity:
            # Take full parcel
            selected.append({'id': parcel['id'], 'weight_taken': parcel['weight'], 'profit': parcel['profit']})
            total_profit += parcel['profit']
            capacity -= parcel['weight']
        else:
            # Take fractional part
            fraction = capacity / parcel['weight']
            profit = parcel['profit'] * fraction
            selected.append({'id': parcel['id'], 'weight_taken': capacity, 'profit': round(profit, 2)})
            total_profit += profit
            capacity = 0

    return round(total_profit, 2), selected


def display_parcels(parcels):
    if not parcels:
        print("No parcels available.")
        return
    print("\n--- Parcel List ---")
    for p in parcels:
        print(f"ID: {p['id']}, Weight: {p['weight']}kg, Profit: ₹{p['profit']}")


def main():
    parcels = []
    capacity = None

    while True:
        print("\n--- Shipping Optimization Menu ---")
        print("1. Add Parcel")
        print("2. Set Truck Capacity")
        print("3. View All Parcels")
        print("4. Compute Maximum Profit (Fractional Knapsack)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            pid = input("Enter Parcel ID: ").strip()
            try:
                weight = float(input("Enter Weight (kg): "))
                profit = float(input("Enter Profit (₹): "))
                if weight <= 0 or profit <= 0:
                    print("Weight and profit must be positive.")
                    continue
                parcels.append({'id': pid, 'weight': weight, 'profit': profit})
                print("Parcel added.")
            except ValueError:
                print("Invalid input. Please enter numeric values for weight and profit.")

        elif choice == '2':
            try:
                cap = float(input("Enter Truck Capacity (kg): "))
                if cap <= 0:
                    print("Capacity must be positive.")
                    continue
                capacity = cap
                print(f"Truck capacity set to {capacity} kg.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == '3':
            display_parcels(parcels)

        elif choice == '4':
            if capacity is None:
                print("Please set the truck capacity first.")
            elif not parcels:
                print("No parcels to consider.")
            else:
                profit, selected = fractional_knapsack(parcels, capacity)
                print(f"\n✅ Maximum Profit: ₹{profit}")
                print("Parcels selected (including partials):")
                for s in selected:
                    print(f"  - Parcel {s['id']} | Taken: {s['weight_taken']} kg | Profit: ₹{s['profit']}")

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
