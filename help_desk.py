
import json

tickets = []
next_ticket_id = 1


def save_tickets():
    data = {
        "tickets": tickets,
        "next_ticket_id": next_ticket_id
    }

    with open("tickets.json", "w") as file:
        json.dump(data, file, indent=4)


def load_tickets():
    global tickets
    global next_ticket_id

    try:
        with open("tickets.json", "r") as file:
            data = json.load(file)

            tickets = data["tickets"]
            next_ticket_id = data["next_ticket_id"]

    except FileNotFoundError:
        tickets = []
        next_ticket_id = 1


def create_ticket():
    global next_ticket_id

    issue = input("Enter the issue: ")
    description = input("Enter a description: ")

    print("\nChoose priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input("Enter priority: ")

    if priority_choice == "1":
        priority = "Low"
    elif priority_choice == "2":
        priority = "Medium"
    elif priority_choice == "3":
        priority = "High"
    else:
        print("Invalid priority.")
        return

    ticket = {
        "id": next_ticket_id,
        "issue": issue,
        "description": description,
        "priority": priority,
        "status": "Open"
    }

    tickets.append(ticket)
    next_ticket_id += 1

    save_tickets()

    print("Ticket created successfully!")
    print("Ticket ID:", ticket["id"])


def view_tickets():
    if len(tickets) == 0:
        print("No tickets found.")
        return

    print("\n===== ALL TICKETS =====")

    for ticket in tickets:
        print("\nTicket ID:", ticket["id"])
        print("Issue:", ticket["issue"])
        print("Description:", ticket["description"])
        print("Priority:", ticket["priority"])
        print("Status:", ticket["status"])

    print("\n=======================")


def update_ticket():
    if len(tickets) == 0:
        print("No tickets found.")
        return

    view_tickets()

    ticket_number = input("Enter ticket ID to update: ")

    if not ticket_number.isdigit():
        print("Please enter a valid ticket ID.")
        return

    ticket_number = int(ticket_number)

    selected_ticket = None

    for ticket in tickets:
        if ticket["id"] == ticket_number:
            selected_ticket = ticket
            break

    if selected_ticket is None:
        print("Ticket not found.")
        return

    print("\n1. Open")
    print("2. In Progress")
    print("3. Closed")

    status_choice = input("Choose new status: ")

    if status_choice == "1":
        selected_ticket["status"] = "Open"
    elif status_choice == "2":
        selected_ticket["status"] = "In Progress"
    elif status_choice == "3":
        selected_ticket["status"] = "Closed"
    else:
        print("Invalid status choice.")
        return

    save_tickets()

    print("Ticket status updated successfully!")


def main():
    load_tickets()

    while True:
        print("\n===== IT HELP DESK =====")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Update Ticket")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            update_ticket()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()