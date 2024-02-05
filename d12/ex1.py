enemies = 1

def increase_enemies():
    global enemies 
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside the function: {enemies}")


player_health = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion()


print(player_health)