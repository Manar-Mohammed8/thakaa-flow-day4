```skills = ["Python", "Git", "SQL"]
skills.append("Pandas")
skills.insert(1, "Excel")
print(skills, len(skills))
print(skills[1], skills[-1], skills[1:3])
ids = {101, 102, 101, 103}
print(len(ids), 104 in ids)
emp = {"name": "Sara", "role": "AI Engineer"}
print(emp.get("team", "Not set"))
emp["team"] = "R&D"
print(len(emp), list(emp.keys()))
```

 
# 2. قراءة الكود وتوقع الناتج

| السطر | توقعي | الناتج الفعلي | سبب الاختلاف|
|---|---|---|---|
| `print(skills, len(skills))`|`["Python", "Excel", "Pandas", "SQL", "Git"]` و 5 | `['Python', 'Excel', 'Git', 'SQL', 'Pandas'] 5` | توقعي غلط في ترتيب Git وSQL وPandas بعد Excel والعناصر صح |
| `print(skills[1], skills[-1], skills[1:3])` | Python Excel Pandas Git | `Excel Pandas ['Excel', 'Git']` | توقعي بيطبع العناصر بالترتيب، لكن طلع مختلف لأن الأقواس المربعة فيها أرقام تحدد أماكن معينة من القائمه `skills[1]` تجيب العنصر الثاني مو الأول`skills[-1]` تجيب آخر عنصر و`skills[1:3]` تجيب جزء من القائمة من 1 إلى قبل 3 |
| `print(len(ids), 104 in ids)` | `3 False` | `3 False` | لا يوجد اختلاف. الـ set ما يتكرر فحذف 101 وصارت 3 فقط، وطلعت False لأن 104 غير موجود |
| `print(emp.get("team", "Not set"))` | `id` | `Not set` | توقعت id وصار Not set، لأن team مو موجود |
| `print(len(emp), list(emp.keys()))` | `3 ['name', 'id', 'role']` | `3 ['name', 'role', 'team']` | توقعت id وصار team، لأن انضاف team بدل id |

## 4. أي هيكل أستخدم؟

| الحالة | الهيكل | السبب |
|---|---|---|
| إحداثيات فرع الشركة على الخريطة | `tuple` | لأن الإحداثيات ثابتة |
| مهام اليوم بالترتيب | `list` | لأن المهام تتغير |
| أسماء الشركات العميلة بدون تكرار | `set` | لأن ما فيه تكرار |
| بيانات موظف | `dict` | لأن البيانات لها مفاتيح |

## 1. جدول الهياكل

| الهيكل | مرتّب؟ | قابل للتعديل؟ | يسمح بالتكرار؟ | كيف أصل لعنصر؟ |
|---|---|---|---|---|
| list | نعم | نعم | نعم | بالفهرس |
| tuple | نعم | لا | نعم | بالفهرس |
| set | لا | نعم | لا | ما أقدر بالفهرس |
| dict | نعم | نعم | لا | بالمفتاح |





