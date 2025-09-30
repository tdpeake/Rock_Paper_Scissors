import os, random

PROJECT_NAME = "Rock Paper Scissors"

CHOICES = ("rock","paper","scissors")
ALIASES = {"r":"rock","p":"paper","s":"scissors"}
WIN_MAP = {"rock":"scissors","scissors":"paper","paper":"rock"}

score = {"player":0,"cpu":0,"tie":0}

def clear_console():
    """
    Clears the console screen based on the operating system.
    """
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def parse_choice(raw_text):
    normalized_input = raw_text.strip().lower()
    normalized_input = ALIASES.get(normalized_input,normalized_input)
    return normalized_input if normalized_input in CHOICES else None

def decide_winner(player_choice, cpu_choice):
    if player_choice == cpu_choice:
        return "tie"
    round_result = WIN_MAP[player_choice]
    if round_result == cpu_choice:
        return "player"
    else:
        return "cpu"
    
def needed_wins(total_rounds):
    if total_rounds > 0 and total_rounds % 2 > 0:
        return total_rounds // 2 + 1
    else:
        return None
    
def update_score(score, outcome):
    score_key = {"player":"player","cpu":"cpu","tie":"ties"}
    who_scored = score_key[outcome]
    new_score = {**score, who_scored:score.get(who_scored,0)+1}
    return new_score
    
    
    
def main():
    clear_console()
    print(f'This is {PROJECT_NAME}')


    
    
if __name__ == "__main__":
    main()
