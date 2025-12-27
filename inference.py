import json
from src.generator import generate_roadmap

with open("config/model_config.json") as f:
    config = json.load(f)

with open("config/skill_graph.json") as f:
    skill_graph = json.load(f)

with open("config/trend_config.json") as f:
    trends = json.load(f)

def predict(inputs):
    return generate_roadmap(inputs, skill_graph, trends, config)

if __name__ == "__main__":
    sample_input = {
        "skills": ["HTML", "CSS"],
        "target_role": "frontend developer",
        "time_per_week": 10,
        "difficulty": "beginner"
    }

    print(json.dumps(predict(sample_input), indent=2))
