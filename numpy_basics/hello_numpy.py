import numpy as np

grades = np.random.randint(2, 6, size=10)
print("Все оценки студентов:", grades)

mean_grade = np.mean(grades)
max_grade = np.max(grades)

print(f"Средний балл: {mean_grade}")
print(f"Максимальный балл: {max_grade}")

excellent_students = grades[grades == 5]
print("Количество отличников:", len(excellent_students))

bonus_grades = grades + 1

final_grades = np.clip(bonus_grades, 2, 5)
print("Оценки с учетом бонуса:", final_grades)
