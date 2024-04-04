# Это вы мне? Подсчитываем тёзок на каждом курсе

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
	course_dict = {"title":course, "mentors":mentor, "duration":duration}
	courses_list.append(course_dict)

# С этого момента начинается выполнение задания 4.
# На входе у вас есть только список курсов courses_list. Об исходных данных, на базе которых он был сделан, вы ничего не знаете

# На каждом курсе в отдельности вам необходимо: 1) найти имена, которые встречаются более 1 раза;
# 2) отобрать людей (Имя + Фамилия), для которых совпало Имя. Это и будут наши тёзки

all_list = []
for m in mentors:
	all_list.extend(m)
all_names_list = []
for mentor in all_list:
	name = mentor.split()
	all_names_list.append(name[0])
unique_names = list(set(all_names_list))
for course in courses_list:
  same_name_list = []
  for uname in unique_names:
    count = 0
    for full_name in course['mentors']:
      if uname in full_name:
        count +=1
        if count > 1 and uname not in same_name_list:
          same_name_list.append(uname)
  same_name_list_res = []
  for namesake in same_name_list:
    for full_name in course['mentors']:
      if namesake in full_name:
        same_name_list_res.append(full_name)
  same_name_list_res = sorted(same_name_list_res)
  if same_name_list_res != []:
    print(f"На курсе {course['title']} есть тёзки: {', '.join(same_name_list_res)}")





# for name in course['mentors']: # Для каждого имени
         # count = 0
        # if name in unique_names: # Если имя в списке уникальных 
        #     count += 1              # Прибавляем 1
        #     for name in courses_list:
        #         if name == name:
        #             same_name_list.append(x)
    # if len(same_name_list) > 0:
    #     print(f'На курсе {course} есть тёзки: {", ".join(sorted(same_name_list))}')