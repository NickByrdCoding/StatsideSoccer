class Pass:
    def __init__(self, direction, distance, type, x_completion, x_threat, receiving_player, frame):
        self.direction = direction
        self.distance = distance
        self.type = type
        self.receiving_player = receiving_player
        self.x_completion = x_completion
        self.x_threat = x_threat
        self.frame = frame