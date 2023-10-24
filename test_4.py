#?????

def make_payment(P):
    limit = 1000
    P = int(input())
    if P < 20 or P > limit:
        print("Повторите попытку")
    else:
        print("Успех")