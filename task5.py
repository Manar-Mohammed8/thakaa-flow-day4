MISSION_DAYS = 70
crew = ("Nora", "Omar", "Lina", "Yousef")
supplies = {"oxygen_kg": 840, "water_l": 1260, "food_kg": 336}
per_person_daily = {"oxygen_kg": 0.84, "water_l": 3.5, "food_kg": 1.2}
telescope_a = {"Kepler-22b", "Proxima b", "TRAPPIST-1e", "Gliese 667Cc"}
telescope_b = {"Proxima b", "TRAPPIST-1e", "HD 40307g"}

days_left = {
    "oxygen_kg": supplies["oxygen_kg"] / (per_person_daily["oxygen_kg"] * len(crew)),
    "water_l": supplies["water_l"] / (per_person_daily["water_l"] * len(crew)),
    "food_kg": supplies["food_kg"] / (per_person_daily["food_kg"] * len(crew)),
}
print(days_left)

weakest = min(days_left, key=days_left.get)
print(weakest)
# شرح key: تخلي min يقارن القيم مو أسماء المفاتيح، عشان يطلع المورد الأقل.

print(days_left[weakest] >= MISSION_DAYS)
print(MISSION_DAYS - days_left[weakest])

print(telescope_a & telescope_b)
print(telescope_a - telescope_b)
print(len(telescope_a | telescope_b))

mission_log = ["Started mission", "Checked supplies", "Found planet"]
print(mission_log[-1], len(mission_log))


# لماذا crew tuple وليس list:
# لأن أسماء الطاقم ثابتة.
# وإذا تغيرت بتطلع الحسابات غلط.

# بعد ما غيرت MISSION_DAYS إلى 70
# طلعت True والفرق 0.0
# لأن الغذاء يكفي 70 يوم
