def map_skills(user_skills, target_role, skill_graph):
    required = skill_graph.get(target_role.lower(), [])
    return [skill for skill in required if skill not in user_skills]
