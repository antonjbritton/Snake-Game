import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')

args = parser.parse_args()

if os.path.exists(args.input_file):
    with open(args.input_file) as file:
        fileText = str(file.readlines())

    teamScores = list(fileText.strip("[]'\\n"))
    count = 0
    team1Score = 0
    team2Score = 0
    iterations = len(teamScores) // 3
    for i in range(iterations):
        if teamScores[count + 1] == "1":
            if teamScores[count + 2] == "t":
                team1Score += 5
            elif teamScores[count + 2] == "c":
                team1Score += 2
            elif teamScores[count + 2] == "p":
                team1Score += 3
            elif teamScores[count + 2] == "d":
                team1Score += 3

        if teamScores[count + 1] == "2":
            if teamScores[count + 2] == "t":
                team2Score += 5
            elif teamScores[count + 2] == "c":
                team2Score += 2
            elif teamScores[count + 2] == "p":
                team2Score += 3
            elif teamScores[count + 2] == "d":
                team2Score += 3

        count += 3

    if team1Score > team2Score:
        print("Team 1 is the winner!")
    elif team1Score < team2Score:
        print("Team 2 is the winner!")
    else:
        print("It's a draw!")

    with open(args.output_file, "w") as file:
        file.write(str(team1Score) + ":" + str(team2Score))
