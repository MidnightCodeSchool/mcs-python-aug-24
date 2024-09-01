"""
Program a rock, paper, scissor.
If the player wins, print "You win!"
If the player loses, print "You lose!"
If it's a draw, print "It's a draw!"
If invalid input, raise "Invalid input"
use random.choice to generate the computer's hand
---
ให้เขียนโปรแกรมเกม rock, paper, scissor โดยมี function ดังนี้
ถ้าผู้เล่นชนะ ให้ print "You win!"
ถ้าผู้เล่นแพ้ ให้ print "You lose!"
ถ้าเสมอ ให้ print "It's a draw!"
ถ้า input ไม่ถูกต้อง ให้ raise "Invalid input"
ใช้ random.choice ในการสุ่มมือของคอมพิวเตอร์
"""
def play(player_hand: str, computer_hand: str) -> str:
    """
    Play a round of paper scissor rock
    Args:
        player_hand: Literal["paper", "scissor", "rock"]: The player's hand
        computer_hand: Literal["paper", "scissor", "rock"]: The computer's hand
    Returns:
        str: win, lose or draw
    """
    ...

def main():
    player_hand = ...
    computer_hand = ...
    game_result = play(player_hand, computer_hand)
    ...

if __name__ == "__main__":
    main()