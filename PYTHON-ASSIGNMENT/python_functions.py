def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.
  
  Args:
    price: The original price of the item (a float or integer).
    discount_percent: The discount percentage (e.g., 25 for 25%).
    
  Returns:
    The new price after the discount if the discount is 20% or higher,
    otherwise returns the original price.
  """
  # The condition: check if the discount is 20% or higher
  if discount_percent >= 20:
    # Calculate the amount of the discount
    # We divide by 100 to convert the percentage (e.g., 25) to a decimal (0.25)
    discount_amount = price * (discount_percent / 100)
    
    # Calculate the final price by subtracting the discount
    final_price = price - discount_amount
    
    # Return the new, discounted price
    return final_price
  else:
    # If the discount is less than 20%, no action is taken
    # Return the original, unchanged price
    return price