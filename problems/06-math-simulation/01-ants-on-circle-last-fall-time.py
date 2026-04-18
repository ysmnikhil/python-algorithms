def time_to_fall_off(circumference, positions, directions, speed):
    """
    Calculate the time it will take for the last ant to fall off the circle.
    
    :param circumference: The circumference of the circle.
    :param positions: A list of positions where each ant starts.
    :param directions: A list of directions for each ant (-1 for counterclockwise, 1 for clockwise).
    :param speed: Speed of the ants.
    :return: The time for the last ant to fall off the circle.
    """
    fall_off_times = []
    
    for i in range(len(positions)):
        position = positions[i]
        direction = directions[i]
        
        if direction == 1:  # Clockwise
            time_to_fall = (circumference - position) / speed
        else:  # Counterclockwise
            time_to_fall = position / speed
        
        fall_off_times.append(time_to_fall)
    
    return max(fall_off_times)

def position_at_time(circumference, positions, directions, speed, time):
    pos = []
    
    for i in range(len(positions)):
        position = positions[i]
        direction = directions[i]

        for i in range(time):
            s = direction * speed
            position += s

            if (position in positions):
                position -= s
    
        pos.append(position)
    return pos

# Example usage:
circumference = 10
positions = [2, 3]  # positions of ants on the circle
directions = [1, -1]  # 1 for clockwise, -1 for counterclockwise
speed = 1  # speed of each ant
time = 1

print("Time for the last ant to fall off:", time_to_fall_off(circumference, positions, directions, speed))
print("Posotions at this time:", position_at_time(circumference, positions, directions, speed, time))
