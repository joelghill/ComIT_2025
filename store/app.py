"""An example of how to create a command line selection process for a fictional storefront."""

from store import inventory
from store import cart
from store import cli

# Prompt user to enter selection
cli.welcome_prompt()

# Print the inventory
cli.print_inventory(inventory.get_inventory())

while True:
    # Get the user's choice
    selection = cli.get_selection(inventory.get_inventory())

    if selection is None:
        break

    cart.add_item_to_cart(selection)

cart_total = cli.print_inventory(cart.get_cart())
cli.goodbye_message(cart_total)
