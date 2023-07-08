class Crypto:
    def trading(self):
        print("You are trading")

class Credit_card:
    def creditcard(self):
        print("You can use credit card to trade bitcoin")

class Bitcoin(Crypto, Credit_card):

    def trading(self):
        print("You are trading bitcoin")
        return self
    
    def crashing(self):
        print("The market crash")
        return self

    def consequences(self):
        print("you are now homeless")
        return self
    
class Popular_Crypto(Bitcoin):
    def unbiased_fact(self):
        print("Crypto ruined graphics cards market")
        return self

bitcoin = Bitcoin()
graphics_card_market = Popular_Crypto()

bitcoin.trading()\
        .crashing()\
        .consequences()\
        .creditcard()

graphics_card_market.trading()\
                    .crashing()\
                    .consequences()\
                    .creditcard()
                    
graphics_card_market.unbiased_fact()