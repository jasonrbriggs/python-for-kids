def spaceship_building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print(f'Week {week} = {total_cans} cans')

spaceship_building(2)