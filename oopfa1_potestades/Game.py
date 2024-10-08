from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss
import random

def bossattack():
    attack=random.randint(1,4)
    if attack==1:
        Enemy.basicAttack(Player)
    elif attack==2:
        Enemy.slashAttack(Player)
    elif attack==3:
        Enemy.rangedAttack(Player)
    elif attack==4:
        Enemy.magicAttack(Player)
    else:
        print("The enemy is standing menacingly!")
        
def swordattack(chc):
    if chc==0:
        pass

def archerattack(chc):
    pass

def magicattack(chc):
    pass

while True:
    print("Welcome! For singleplayer please input 0, for pvp please input 1,")
    print("and to exit, please input anything else.")
    choice=int(input("Input: "))
    if choice==0:
        print("Welcome to singleplayer!")
        user=input(str("Please enter your username: "))
        Player=Novice(user)
        Enemy=Boss("Monster")
        wins=0
        while wins<2:
            while Player.getHp()>0 and Enemy.getHp()>0:
                print(f"{Player.getUsername()} HP: {Player.getHp()}")
                print(f"{Enemy.getUsername()} HP: {Enemy.getHp()}")
                Player.basicAttack(Enemy)
                bossattack()
                if Enemy.getHp()<=0:
                    wins+=1
                    print(f"You win! Wins: {Player.wins}")
                    Player.setHp(100)
                elif Player.getHp()<=0:
                    print(f"You lose! Wins: {Player.wins}")
                    print("Try again? 0 - Yes | 1 - No")
                    
            
        
    elif choice==1:
        print("Welcome to PVP!")
        print("Player 1:")
        u1=input(str("Please enter your username: "))
        print("Please enter which class you want to choose!")
        c1=input(int("0 - Swordsman | 1 - Archer | 2 - Magician"))
        if c1==0:
            Player1=Swordsman(u1)
        elif c1==1:
            Player1=Archer(u1)
        elif c1==2:
            Player1=Magician(u1)
        print("Player 2:")
        u2=input(str("Please enter your username: "))
        print("Please enter which class you want to choose!")
        c2=input(int("0 - Swordsman | 1 - Archer | 2 - Magician"))
        if c2==0:
            Player2=Swordsman(u2)
        elif c2==1:
            Player2=Archer(u2)
        elif c2==2:
            Player2=Magician(u2)
        if c1==0 and c2==0:
            pass
        elif c1==1 and c2==1:
            pass
        elif c1==2 and c2==2:
            pass
        elif c1==0 and c2==1:
            pass
        elif c1==0 and c2==2:
            pass
        elif c1==1 and c2==0:
            pass
        elif c1==1 and c2==2:
            pass
        elif c1==2 and c2==0:
            pass
        elif c1==2 and c2==1:
            pass
    else:
        print("Game is exiting, thank you for playing!")
        break