p1=int(input("Enter Player1 score"))
p2=int(input("Enter Player2 score"))
p3=int(input("Enter Player3 score"))

def strikrt(runs):
    rate=(runs*100)/60
    return rate

def sixes(runs):
    maxim=runs/6

    return int(maxim)

print("Strike Rate of Player1 - " +str(strike_rate(p1)))
print("Strike Rate of Player2 - " +str(strike_rate(p2)))
print("Strike Rate of Player3 - " +str(strike_rate(p3)))

print("Maximun number of sixes by player1 -  " +str(sixes(p1)))
print("Maximun number of sixes by player2 -  " +str(sixes(p2)))
print("Maximun number of sixes by player3 -  " +str(sixes(p3)))