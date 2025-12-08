# %%
import utility
import shopping.shopping_cart

# %%

if __name__ == "__main__":
    # Example usage
    print("Addition:", utility.add(1, 2))
    print("Subtraction:", utility.subtract(5, 3))
    print("Multiplication:", utility.multiply(4, 7))
    print("Division:", utility.divide(20, 4))
    
    test = shopping.shopping_cart.buy("apple")
    print("Shopping Cart:", test)