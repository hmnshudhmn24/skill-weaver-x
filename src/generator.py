from .skill_mapper import map_skills
from .trend_analyzer import prioritize_skills
from .planner import generate_weekly_plan

def generate_roadmap(user_input, skill_graph, trends, config):
    missing_skills = map_skills(
        user_input["skills"],
        user_input["target_role"],
        skill_graph
    )

    prioritized = prioritize_skills(missing_skills, trends)

    roadmap = generate_weekly_plan(
        prioritized,
        config.get("weeks", 8)
    )

    return {
        "target_role": user_input["target_role"],
        "difficulty": user_input.get("difficulty", config["default_difficulty"]),
        "roadmap": roadmap
    }
