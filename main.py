# Topic: String Indexing

# Challenge: Show Only First 4 Digits
# Challenge: Print Every Second Character

credit_number = "1234-5678-9012-3456"

# Exercise 1, Mask Credit Card Number or Display Only Last 4 Digits

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# Exercise 2, Reverse Credit Card Number or Backward Credit Numbers

credit_number = credit_number[::-1]
print(credit_number)