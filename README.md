# SkillWeaver-X 🧠🎯

**SkillWeaver-X** is an advanced AI Learning & Career Architect that generates **dynamic, adaptive learning roadmaps** based on a user’s current skills, career goals, time availability, and market trends.

It is designed for students, professionals, and career-switchers in **AI, Data Science, and Web Development**.

---

## 🚀 Key Features

- 📌 Personalized skill-to-career mapping  
- 🔁 Adaptive roadmaps that adjust with goals & skill level  
- 📊 Market-trend–aware skill prioritization  
- 🗓️ Weekly learning plans with milestones  
- ⚙️ Config-driven and easily extensible  
- 🤗 Hugging Face–ready inference pipeline  

---

## 🧠 How It Works

1. **Skill Mapping**  
   Identifies missing skills for a target role using a skill graph.

2. **Trend Analysis**  
   Prioritizes skills using weighted market trend signals.

3. **Roadmap Planning**  
   Converts prioritized skills into a structured weekly plan.

---

## 📥 Input Format

```json
{
  "skills": ["HTML", "CSS"],
  "target_role": "frontend developer",
  "time_per_week": 10,
  "difficulty": "beginner"
}
```

---

## 📤 Output Format

```json
{
  "target_role": "frontend developer",
  "difficulty": "beginner",
  "roadmap": {
    "Week 1": ["JavaScript"],
    "Week 2": ["React"]
  }
}
```

---

## 🏷️ Hugging Face Details

- **Model ID:** `skillweaver-x`
- **Pipeline Tag:** `text-generation`
- **Tags:** `education`, `career-ai`, `roadmap`
- **License:** Apache 2.0

---

## 🛠️ Installation & Usage

### Clone the Repository
```bash
git clone https://huggingface.co/<your-username>/skillweaver-x
cd skillweaver-x
```

### Run Inference
```bash
python inference.py
```

---

## 📁 Project Structure

```
skillweaver-x/
├── config/
├── data/
├── src/
├── inference.py
├── model_card.md
├── README.md
├── LICENSE
└── requirements.txt
```

---

## 🔮 Future Improvements

- LLM-powered reasoning (Mistral / LLaMA)
- Real-time job-market trend scraping
- Gradio / Spaces UI
- Multi-role career planning
- Certification-aware roadmaps

---

## 📜 License

This project is licensed under the **Apache License 2.0**.

---

## ⭐ Why SkillWeaver-X?

SkillWeaver-X is:
- Practical
- Original
- Recruiter-attractive
- Production-ready
- Easy to extend with LLMs

---

**If you like this project, give it a ⭐ on Hugging Face!**
