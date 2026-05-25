def solution(bandage, health, attacks):
    before_time = 0
    time, heal, add_heal = bandage
    answer = health
    for attack_time, damage in attacks:
        check = attack_time - before_time - 1
        answer = min(health, answer + heal * check + add_heal * (check // time))
        answer -= damage
        
        if answer <= 0:
            return -1
        before_time = attack_time
    return answer