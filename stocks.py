
def stock_purchases():
    amazon = 3000
    apple = 100
    fb = 250
    google = 1400
    msft = 200
    
    name = input("What is your name? ")
    amount_invest = input("How much would you like to invest? $")
    amount_invest = int(amount_invest)
    
    # Given the prices above and a client's investment budget, how much stock can they buy?
    # 1.1 TODO: Ask the client's name (use the string: "What is your name? ") and save it into a variable

    # 1.2 TODO: Ask the client how many dollars they would like to invest (use the string: "How much would you like to invest? $")
    # and save it into a variable
    # NOTE: When you use the `input` function to get user input, what do numbers get saved as?

    # 1.3 TODO: Uncomment the line below to ask the client which stock they're interested in.
    # NOTE: Take a look at how this input string prints out
    stock_name = input("\nWhich stock are you interested in? Enter the full name:\nAmazon\nApple\nFacebook\nGoogle\nMicrosoft\nStock Name: ")
    
    # Now that you have all of the client info, you can check how much they can purchase of the stock
    # they're interested in.

    # 1.4 TODO: Use `if/elif/else` conditional logic to determine how much stock the client can buy,
    # and save it in a variable
    
    if apple:
        amount_shares = amount_invest//apple
        print(f"{name} has ${amount_invest} to invest and can buy {amount_shares} shares of Apple at the current price of $100.")
    # elif apple:
        # amount_shares = amount_invest//apple
        # print(f"{name} has ${amount_invest} to invest and can buy {amount_shares} shares of Apple at the current price of $100.")
    # elif stock_name == Facebook:
        # amount_shares = amount_invest//fb
        # print(f"{name} has ${amount_invest} to invest and can buy {amount_shares} shares of Facebook at the current price of $250.")
    # elif stock_name == Google:
        # amount_shares = amount_invest//google
        # print(f"{name} has ${amount_invest} to invest and can buy {amount_shares} shares of Google at the current price of $1400.")
    # elif stock_name == Microsoft:
        # amount_shares = amount_invest//msft
        # print(f"{name} has ${amount_invest} to invest and can buy {amount_shares} shares of Microsoft at the current price of $200.")
    # 1.5 TODO: Once you've calculated the number of stocks that can be purchased,
    # Use an f-string to print the result for the client, ala:
    # Alex has $5000 to invest and can buy 50 shares of Apple at the current price of $100.
stock_purchases()