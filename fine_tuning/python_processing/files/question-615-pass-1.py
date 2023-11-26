from collections import defaultdict


def findWinner(votes):
    # Create a dictionary to store the counts of each candidate
    counts = defaultdict(int)
    for vote in votes:
        counts[vote] += 1

    # Find the candidate with the most votes
    winner = max(counts, key=counts.get)

    # Return the winner
    return winner
