"""
Docstring pulled from Blackboard
You are online shopping at SuperAwesomeCouponDealsAndStuff.com.
They offer two types of discounts, cash-off coupons and percent
discount coupons. You must add tax after applying coupons.
If you have cash-off coupons, those must be applied first,
then apply the percent discount coupons on the pre-tax amount.
The following is the order of calculations:
The first is cash-off coupons, that you earn by shoppings.
You may apply one $5 or $10 cash off per order.
The second is percent discount coupons for 10%, 15%, or 20% off.
The third is tax
The fourth is shipping according to the the following guidelines:
up to $10 dollars, shipping is $5.95
$10 and up to $30 dollars, shipping is $7.95
$30 and up to $50 dollars, shipping is $11.95
Shipping is free for $50 and over
In this program, prompt the user for the amount of the purchase,
the cash coupon, the percent coupon. Then calculate and return the
total order item.
For instance, you have $5 off and 30% coupons and your item is $15.99,
you will first take
$15.99 - $5.00 = $10.99.
30% off $10.99 to get $7.69
Add tax at 6% to get $8.15
Add shipping cost before tax $5.95 to get $14.10
Do not forget to use variables and constants where appropriate.
Using variables, the first line might look like the following:
cash_off_subtotal = price - cash_off
Name your file coupon_calculations.py.
Assignment
Nested if statement Assignment
Submit your .py file.
This is worth 10 points
"""
#TAX_RATE constant
TAX_RATE = 0.06

# get or set price, cash_coupon, and percentage_coupon
price = float(input("Please enter the price of your purchase: "))
cash_coupon = float(input("If you have a cash coupon, enter how much"
                          "\nit's for, otherwise enter 0: "))
percentage_coupon = float(input("If you have a percentage coupon,"
                                "\nPlease enter it as a number out of 100,"
                                "\notherwise, enter 100 if no discount: "))
percentage_coupon /= 100

# part 1, set post cash coupon to subtotal (even if no discount)
subtotal = price - cash_coupon

# part 2, set post percent coupon to variable (even if no discount)
subtotal -= (subtotal * percentage_coupon)

# part 3, calculate shipping BEFORE adding tax, using nested if-else statements
# shipping costs:
# up to $10 dollars, shipping is $5.95
if subtotal < 10:
    shipping = 5.95
# $10 and up to $30 dollars, shipping is $7.95
else:
    if subtotal < 30:
        shipping = 7.95
# $30 and up to $50 dollars, shipping is $11.95
    else:
        if subtotal < 50:
            shipping = 11.95
# Shipping is free for $50 and over
        else:
            shipping = 0.0

# part 4, calculate tax from chosen tax rate, set to subtotal
subtotal += (subtotal * TAX_RATE)

# part 5
# print out subtotal, shipping, and total in a pretty format
print("Subtotal: $" + "{0: >7}".format(str(round(subtotal, 2)))
      + "\nShipping: $" + "{0: >7}".format(str(shipping))
      + "\n   Total: $" + "{0: >7}".format(str(round(subtotal + shipping, 2))))
