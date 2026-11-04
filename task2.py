tasks = ["Update website", "Client meeting", "Code review"]
# ضفت مهمة في النهاية
tasks.append("Write report")
print(tasks)
# ضفت مهمة في البداية
tasks.insert(0, "Fix urgent bug")
print(tasks)
# حذفت Client meeting لانها انتهت
tasks.remove("Client meeting")
print(tasks)
# ضفت مهمة جديدة
tasks.append("Review Sara's code")
print(tasks)
# حذفت اخر مهمة وطبعتها
removed_task = tasks.pop()
print(removed_task)
# طبعت عدد المهام واول واخر مهمة وترتيب Code review
print(len(tasks))
print(tasks[0], tasks[-1])
print(tasks.index("Code review") + 1)
# توقعي:
# عدد المهام: 4
# اول واخر مهمة: Fix urgent bug , Write report
# ترتيب Code review: 3
# الناتج الفعلي :['Code review', 'Fix urgent bug', 'Update website', 'Write report']
# ['Fix urgent bug', 'Update website', 'Code review', 'Write report']
# ['Code review', 'Fix urgent bug', 'Update website', 'Write report']
# طبعت نسخة مرتبة
print(sorted(tasks))
# طبعت القائمة الأصلية
print(tasks)
# رتبت القائمه الأصلية
tasks.sort()
print(tasks)
# الفرق الي لاحظته: (sorted() ما غيرت الأصلية، وsort() غيرت الأصلية )
