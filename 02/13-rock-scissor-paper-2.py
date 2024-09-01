"""
Program a rock, paper, scissor.
If the player wins, print "You win!"
If the player loses, print "You lose!"
If it's a draw, print "It's a draw!"
If invalid input, raise "Invalid input"
The computer always play rock.
"""
def play(hand: str) -> str:
    """
    Play a round of paper scissor rock
    Args:
        hand: Literal["paper", "scissor", "rock"]: The player's hand
    Returns:
        str: win, lose or draw
    """
    if hand != "rock" and hand != "paper" and hand != "scissor":
        raise ValueError("Invalid input")

    computer_hand = "rock"

    if hand == computer_hand:
        return "draw"
    elif hand == "paper":
        return "win"
    elif hand == "scissor":
        return "lose"
    else:
        raise Exception("Something went wrong")

def main():
    hand = input("Enter your hand(rock, scissor, paper): ")
    game_result = play(hand)
    if game_result == "win":
        print("You win!")
    elif game_result == "lose":
        print("You lose!")
    elif game_result == "draw":
        print("It's a draw!")
    else:
        Exception("Something went wrong")


if __name__ == "__main__":
    main()