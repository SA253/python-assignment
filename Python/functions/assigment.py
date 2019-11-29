"""#using global
x=0
def demo():
    global x
    x+=1
    print(x)
    
demo()
demo()
demo()
demo()

#lexical reference here is hello . This pattern name is "closures"
#using nonlocal scope
def outer():
    
    i=0
    def inner():
        nonlocal i
        i+=1
        print(i)
    return inner
    
hello=outer()
hello()
hello()
hi=outer()
hello()
hello()
hello()
hi()
hi()
hi()"""




#assignment2
def wallet():
    balance=int(input("enter the balance in the wallet"))
    print("balance",balance)
    def deposit():
        cash=int(input("enter the cash "))
        print("deposit cash is",cash)
        nonlocal balance
        balance=balance+cash
        print(balance)
        d={"balance":balance,"cash":cash}
        return d
    #deposit()
    def spent():
        amount=int(input("enter the amount "))
        print("amount spent is:",amount)
        nonlocal balance
        if balance<amount:
            print("negative balance")
        else:
            balance=balance-amount
            print("remaining amount is",balance)
        d1={"balance":balance,"amount":amount}
        return d2
    #spent()
    def savings():
        nonlocal balance
        print("balance available is:",balance)
        
    #savings()
    d2={"deposit":deposit,"spent":spent,"savings":savings}
    return d2
    def transfer():
        transfer=int(input("enter the transfer amount "))
        print("amount transfered is:",transfer)
        nonlocal balance
        if balance<transfer:
            print("insufficent balance")
        else:
            balance=balance-transfer
            print("remaining amount is",balance)
        d1={"balance":balance,"amount":transfer}
        return d2
        
money=wallet()
wallet2=wallet()
money["deposit"]() 
money["spent"]()
money["savings"]()
wallet2["transfer"]()
        






















