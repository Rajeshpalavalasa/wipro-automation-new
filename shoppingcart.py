# Defining a blueprint for a shopping cart system
class ShoppingCart:

    # Constructor runs automatically when a cart object is created
    def __init__(self, cart_id):
        self.cart_id = cart_id
        self.products = {}

    # Method inserting a product into the cart
    def add_product(self, product, price):
        self.products[product] = price
        print(f"{product} successfully added.")

    # Method to remove a product from the cart
    def remove_product(self, product):
        #check to avoid deleting non-existing products
        if product in self.products:
            # Removes the product-price pair from memory
            del self.products[product]
            
            # Confirms removal operation
            print(f"{product} removed from cart.")
        else:
            # Handles invalid removal attempts gracefully
            print("[WARNING] Product does not exist in cart.")

    # Method for total payable amount
    def calculate_total(self):
        # Aggregates all product prices stored in the cart
        total_amount = sum(self.products.values())
        return total_amount


# Main 

# Creating a ShoppingCart object
cart = ShoppingCart(101)

# Adding products
cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 500)
cart.add_product("Keyboard", 1500)

# Removing an unwanted product from the cart
cart.remove_product("Mouse")

# Calculating the final bill amount
final_total = cart.calculate_total()

# Displaying the total cost of items in the cart
print("Total Cart Price:", final_total)
