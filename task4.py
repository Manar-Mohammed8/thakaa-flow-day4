
registered = ["sara@mail.com", "omar@mail.com", "lina@mail.com",
"sara@mail.com", "yousef@mail.com", "nora@mail.com"]

attended = ["omar@mail.com", "lina@mail.com", "khaled@mail.com", "nora@mail.com"]
tickets = ["VIP", "Regular", "Regular", "Student", "VIP", "Regular"]
prices = {"VIP": 450, "Regular": 200, "Student": 100}

# توقعي:
# عدد التسجيلات المكررة: 1، لأن القائمة فيها 6 عناصر وبعد إزالة التكرار يبقى 5
# سجل وحضر: omar@mail.com , lina@mail.com , nora@mail.com
# سجل ولم يحضر: sara@mail.com , yousef@mail.com
# حضر بدون تسجيل: khaled@mail.com
# نسبة الحضور: 50%
# عدد التذاكر: VIP = 2 ، Regular = 3 ، Student = 1
# الإيراد: 1500
reg_set = set(registered)
print(len(registered) - len(reg_set))
att_set = set(attended)

print(reg_set & att_set)

print(reg_set - att_set)

print(att_set - reg_set)

attended_and_registered = len(reg_set & att_set)
rate = (attended_and_registered / len(reg_set)) * 100
print(rate)

counts = {"VIP": tickets.count("VIP"), "Regular": tickets.count("Regular"), "Student": tickets.count("Student")}
print(counts)

revenue = counts["VIP"] * prices["VIP"] + counts["Regular"] * prices["Regular"] + counts["Student"] * prices["Student"]
print(revenue)

# الناتج الفعلي: النسبة 60.0 والإيراد 1600، وباقي توقعاتي طلعت صح
# سبب اختلاف النسبة: توقعت 50% لكن طلع 60% لأن 3 من أصل 5 مسجلين حضروا.
# سبب اختلاف الإيراد: توقعت 1500 لكن طلع 1600 لأني حسبت الإيراد غلط.

print("تقرير الورشة")
print(f"سجل وحضر: {sorted(reg_set & att_set)}")
print(f"سجل ولم يحضر: {sorted(reg_set - att_set)}")
print(f"حضر بدون تسجيل: {sorted(att_set - reg_set)}")
print(f"نسبة الحضور: {rate}%")
print(f"الإيراد: {revenue} ريال")

# لاحظت أن الـ set ما له ترتيب ثابت، لذلك أحيانًا يطلع sara قبل yousef وأحيانًا العكس.
# أما registered فهي list وترتيبها ثابت لأنها تحتفظ بترتيب العناصر كما أُضيفت.




