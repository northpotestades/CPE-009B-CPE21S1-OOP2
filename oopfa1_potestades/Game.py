from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss
import random

def select_role():
    roles = {"1": Swordsman, "2": Archer, "3": Magician}
    print("Select your role: 1 - Swordsman, 2 - Archer, 3 - Magician") 
    choice = input("Enter the number of your role: ")
    return roles.get(choice, Novice)

def battle(player, opponent):
    while player.getHp() > 0 and opponent.getHp() > 0:
        for current, target in [(player, opponent), (opponent, player)]:
            if current == player:
                action = input(f"{current.getUsername()}'s Turn! Choose action (1 - Basic Attack, 2 - Special Attack): ")
                if action == '1':
                    current.basicAttack(target)
                elif action == '2':
                    if isinstance(current, Swordsman):
                        current.slashAttack(target)
                    elif isinstance(current, Archer):
                        current.rangedAttack(target)
                    elif isinstance(current, Magician):
                        current.magicAttack(target)
                else:
                    print("Invalid action. Turn skipped.")
            else:
                action = random.choice(['basic', 'slash', 'magic'])
                getattr(current, f"{action}Attack")(target)

def player_vs_computer():
    player_wins = 0 
    while True:
        print("\n--- Single Player Mode ---")
        player = Novice(input("Enter username: "))
        monster = Boss("Monster")
        battle(player, monster)
        
        if monster.getHp() <= 0:
            player_wins += 1
            print(f"{monster.getUsername()} has been defeated! Your wins: {player_wins}")
            if player_wins >= 2:
                player = select_role()(player.getUsername())
        
        if input("You have been defeated! Play again? (y/n): ").lower() != 'y':
            break

def player_vs_player():
    wins = {"Player 1": 0, "Player 2": 0}
    while True:
        print("\n--- Player vs Player Mode ---")
        player1 = select_role()(input("Enter Player 1 username: "))
        player2 = select_role()(input("Enter Player 2 username: "))
        battle(player1, player2)

        if player2.getHp() <= 0:
            wins["Player 1"] += 1
            print(f"{player2.getUsername()} has been defeated! Current Wins: Player 1: {wins['Player 1']}, Player 2: {wins['Player 2']}")
        else:
            wins["Player 2"] += 1
            print(f"{player1.getUsername()} has been defeated! Current Wins: Player 1: {wins['Player 1']}, Player 2: {wins['Player 2']}")

        if input("Play again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    mode = input("Select mode (1: Single Player, 2: Player vs Player): ")
    if mode == '1':
        player_vs_computer()
    elif mode == '2':
        player_vs_player()
    else:
        print("Invalid mode selected.")
