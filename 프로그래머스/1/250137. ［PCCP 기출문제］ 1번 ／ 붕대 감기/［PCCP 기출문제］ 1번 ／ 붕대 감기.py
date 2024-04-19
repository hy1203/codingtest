def solution(bandage, health, attacks):
    max_time = attacks[-1][0]
    max_heal = health
    attack_dict={}
    for i in attacks:
        attack_dict[i[0]] = i[1]
    t = 0
    continue_suss = 0

    while t <= max_time:
        if t in attack_dict:
            health -= attack_dict[t]
            continue_suss = 0

            if health <= 0:
                return -1
        else:
            continue_suss += 1
            if continue_suss < bandage[0]:
                health += bandage[1]
                if health > max_heal:
                    health = max_heal
            else:
                health = health + bandage[1]+bandage[2]
                if health > max_heal:
                    health = max_heal
                continue_suss = 0
        t += 1
    return health