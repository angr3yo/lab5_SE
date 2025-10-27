"""
Inventory Management System

A clean, secure, and PEP8-compliant version of the inventory management
program after static code analysis fixes using Pylint, Bandit, and Flake8.
"""

import logging
from typing import Dict, Optional

# Constants for menu options
ADD_ITEM = 1
REMOVE_ITEM = 2
DISPLAY_INVENTORY = 3
EXIT_PROGRAM = 4

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class InventoryItem:
    """Represents a single item in the inventory."""

    def __init__(self, name: str, quantity: int = 0, price: float = 0.0):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, change: int) -> None:
        """Update the quantity of the item."""
        try:
            change = int(change)
            self.quantity += change
            logging.info(
                "Updated quantity for '%s' to %d units.", self.name, self.quantity
            )
        except ValueError as exc:
            logging.error("Invalid quantity input for %s: %s", self.name, exc)

    def __str__(self) -> str:
        """Return a string representation of the item."""
        return f"{self.name}: {self.quantity} units @ ₹{self.price:.2f}"


class InventorySystem:
    """Handles adding, removing, and displaying inventory items."""

    def __init__(self) -> None:
        self.items: Dict[str, InventoryItem] = {}

    def add_item(
        self, name: str, quantity: int = 0, price: float = 0.0
    ) -> None:
        """Add or update an inventory item."""
        if not name:
            logging.warning("Cannot add item with empty name.")
            return

        if name in self.items:
            self.items[name].update_quantity(quantity)
        else:
            self.items[name] = InventoryItem(name, quantity, price)
            logging.info("Item '%s' added with %d units at ₹%.2f.",
                         name, quantity, price)

    def remove_item(self, name: str) -> None:
        """Remove an existing item."""
        if name in self.items:
            del self.items[name]
            logging.info("Item '%s' removed successfully.", name)
        else:
            logging.warning("Item '%s' does not exist in inventory.", name)

    def display_inventory(self) -> None:
        """Display all inventory items."""
        if not self.items:
            logging.info("Inventory is currently empty.")
            return
        logging.info("=== Inventory List ===")
        for item in self.items.values():
            logging.info("%s", item)


def get_valid_int(prompt: str) -> Optional[int]:
    """Safely get an integer input from user."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        logging.error("Invalid integer input.")
        return None


def main() -> None:
    """Main function for the inventory system CLI."""
    inventory = InventorySystem()

    while True:
        logging.info("\nMenu:\n1. Add Item\n2. Remove Item\n3. Display Inventory\n4. Exit")
        choice = get_valid_int("Enter choice: ")

        if choice is None:
            continue

        if choice == ADD_ITEM:
            name = input("Enter item name: ").strip()
            qty = get_valid_int("Enter quantity: ")
            price_input = input("Enter price: ").strip()
            try:
                price = float(price_input)
            except ValueError:
                logging.error("Invalid price input.")
                continue

            if qty is not None:
                inventory.add_item(name, qty, price)

        elif choice == REMOVE_ITEM:
            name = input("Enter item name to remove: ").strip()
            inventory.remove_item(name)

        elif choice == DISPLAY_INVENTORY:
            inventory.display_inventory()

        elif choice == EXIT_PROGRAM:
            logging.info("Exiting inventory system. Goodbye!")
            break

        else:
            logging.warning("Invalid choice: %s", choice)


if __name__ == "__main__":
    main()
