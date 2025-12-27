def prioritize_skills(skills, trends):
    return sorted(skills, key=lambda s: trends.get(s, 1.0), reverse=True)
