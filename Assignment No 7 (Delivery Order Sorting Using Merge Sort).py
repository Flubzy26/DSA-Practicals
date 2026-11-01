def merge_sort(arr):
    """
    Merge Sort Algorithm to sort delivery times in ascending order.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i]['delivery_time'] <= right_half[j]['delivery_time']:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def display_orders(orders):
    if not orders:
        print("No orders to display.")
        return
    print("\n--- Online Orders ---")
    for i, order in enumerate(orders, 1):
        print(f"{i}. Order ID: {order['id']}, Delivery Time: {order['delivery_time']} minutes")


def main():
    orders = []

    while True:
        print("\n--- Online Delivery System Menu ---")
        print("1. Add Order")
        print("2. Display Orders")
        print("3. Sort Orders by Delivery Time (Merge Sort)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            order_id = input("Enter Order ID: ").strip()
            try:
                delivery_time = int(input("Enter Delivery Time (in minutes): "))
                orders.append({'id': order_id, 'delivery_time': delivery_time})
                print("Order added successfully.")
            except ValueError:
                print("Invalid delivery time. Please enter an integer.")

        elif choice == '2':
            display_orders(orders)

        elif choice == '3':
            if not orders:
                print("No orders to sort.")
            else:
                merge_sort(orders)
                print("Orders sorted by delivery time successfully.")

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
