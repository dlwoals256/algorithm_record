MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

class Agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

agents = [Agent(codenames[i], scores[i]) for i in range(MAX_N)]

min_agent = min(agents, key=lambda x: x.score)

print(min_agent.name, min_agent.score)