# ЗАДАНИЕ ПО ТЕМЕ "Форматирование строк"

name_team1 = 'Мастера кода'
name_team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 1)
time1_avg = round(team1_time / score_1, 1)  # Среднее время решения одной задачи командой 1
time2_avg = round(team2_time / score_2, 1)  # Среднее время решения одной задачи командой 2


print('В команде %s участников: %d !' % (name_team1, team1_num))
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))

print('Команда {} решила задач: {} !'.format(name_team2, score_2))
print('{} решили задачи за {} с !'.format(name_team2, round(team2_time, 1)))

print(f'Команды решили {score_1} и {score_2} задач.')
if time1_avg < time2_avg:
    challenge_result = f'Результат битвы: победа команды {name_team1}!'
elif time1_avg > time2_avg:
    challenge_result = f'Результат битвы: победа команды {name_team2}!'
else:
    challenge_result = 'Ничья!'
print(challenge_result)
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')