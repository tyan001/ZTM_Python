# %%
import utility
# import shopping.shopping_cart
from shopping.shopping_util.shopping_util import buy
# %%

if __name__ == "__main__":
    # Example usage
    print("Addition:", utility.add(1, 2))
    print("Subtraction:", utility.subtract(5, 3))
    print("Multiplication:", utility.multiply(4, 7))
    print("Division:", utility.divide(20, 4))
    
    test = buy("apple")
    print("Shopping Cart:", test)
    print(__name__)
    print(utility.__name__)