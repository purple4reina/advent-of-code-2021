def part1(inputs):
    player1, player2 = inputs

    class Die(object):
        def __init__(self):
            self.val = 0
            self.rolls = 0
        def roll(self):
            roll = self.val + 1
            self.val = roll % 100
            self.rolls += 1
            return roll

    die = Die()
    player1_score = player2_score = 0
    while True:
        roll1 = die.roll() + die.roll() + die.roll()
        player1 = (player1 + roll1 - 1) % 10 + 1
        player1_score += player1
        if player1_score > 999:
            loser = player2_score
            break

        roll2 = die.roll() + die.roll() + die.roll()
        player2 = (player2 + roll2 - 1) % 10 + 1
        player2_score += player2
        if player2_score > 999:
            loser = player1_score
            break

    return die.rolls * loser

def part2(inputs):
    player1, player2 = inputs

    all_rolls = {r: 0 for r in range(3, 10)}
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                all_rolls[a + b + c] += 1

    player1_wins = player2_wins = 0
    universes, new_universes = {(player1, 0, player2, 0): 1}, {}
    while universes:

        for (player1, player1_score, player2, player2_score), universe_count \
                in universes.items():
            for roll, roll_count in all_rolls.items():
                new_player1 = (player1 + roll - 1) % 10 + 1
                new_player1_score = player1_score + new_player1
                if new_player1_score > 20:
                    player1_wins += universe_count * roll_count
                else:
                    key = (new_player1, new_player1_score, player2,
                            player2_score)
                    new_universes[key] = new_universes.get(key, 0) + \
                            universe_count * roll_count

        universes, new_universes = new_universes, {}

        for (player1, player1_score, player2, player2_score), universe_count \
                in universes.items():
            for roll, roll_count in all_rolls.items():
                new_player2 = (player2 + roll - 1) % 10 + 1
                new_player2_score = player2_score + new_player2
                if new_player2_score > 20:
                    player2_wins += universe_count * roll_count
                else:
                    key = (player1, player1_score, new_player2,
                            new_player2_score)
                    new_universes[key] = new_universes.get(key, 0) + \
                            universe_count * roll_count

        universes, new_universes = new_universes, {}

    return max(player1_wins, player2_wins)

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    player1, player2 = raw.split('\n')
    player1 = int(player1.split(': ')[-1])
    player2 = int(player2.split(': ')[-1])
    return player1, player2

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
