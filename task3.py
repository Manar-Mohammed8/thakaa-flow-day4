me = {
    "name": "منار",
    "city": "الرياض",
    "age": 24,
    "skills": ["الاستماع", "التنظيم", "Python"],
    "courses": {
        "Python": "done",
        "AI": "in progress"
    }
}
me["skills"].append("Git")
print(me)
me["courses"]["AI"] = "done"
me["courses"]["Machine Learning"] = "planned"
print(me)
me["github"] = "Manar-Mohammed8"
del me["city"]
print(me)
print(list(me.keys()))
print(len(me["skills"]))
print("SQL" in me["skills"])
print(me["courses"]["AI"])
print(me["courses"].get("Data Science", "Not found"))
print(f"{me['name']} · {len(me['skills'])} skills · {len(me['courses'])} courses · github.com/{me['github']}")
