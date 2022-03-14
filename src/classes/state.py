class state:
    reward = 0
    enterable = False

    def __init__(self, reward:int, isEnterable:bool) -> None:
        self.reward = reward
        self.enterable = isEnterable
    
    def reward(self) -> int:
        return self.reward
    def enterable(self) -> bool:
        return self.enterable