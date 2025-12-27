def generate_weekly_plan(skills, weeks):
    plan = {}
    if not skills:
        return plan

    chunk = max(1, len(skills) // weeks)
    for i in range(weeks):
        start = i * chunk
        end = start + chunk
        if start < len(skills):
            plan[f"Week {i+1}"] = skills[start:end]
    return plan
