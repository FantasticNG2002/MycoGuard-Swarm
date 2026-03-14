# MycoGuard-Swarm

# 🍄 MycoGuard: Autonomous Fungi Safety Forge (Track B)

## 1. Project Title
**MycoGuard** is an autonomous multi-agent system designed to analyze mushroom toxicity using quantitative machine learning techniques. Developed by a Computer Engineering student from **Universiti Malaysia Perlis (UniMAP)** for the GDG Gemini Nexus event.

---

## 2. System Architecture (A2A Flow)
MycoGuard utilizes a **Swarm Intelligence** approach where specialized agents collaborate to ensure data integrity and botanical safety.



**Workflow:**
1. **User** uploads `mushrooms (1).csv`.
2. **Data Auditor Agent** cleans and encodes raw data.
3. **Classifier Forge Agent** trains a Random Forest model and identifies key features.
4. **Safety Validator Agent** audits the results for "False Negatives" to ensure 100% safety.
5. **Final Report** is generated with a Feature Importance visualization.

---

## 3. Agent Profiles
* **Data Auditor Agent**: Focuses on data preprocessing, handling categorical encoding, and verifying dataset integrity.
* **Classifier Forge Agent**: The "engine" of the swarm. It autonomously writes and executes Python code to build predictive models.
* **Safety Validator Agent**: Acting as a "Safety Guardrail," it audits model performance specifically for high-risk misclassifications (poisonous vs. edible).

---

## 4. Setup Instructions
1. **Clone the Repo**: `git clone https://github.com/[YOUR_USERNAME]/MycoGuard-Swarm.git`
2. **Install Dependencies**: `pip install pandas scikit-learn google-generativeai matplotlib`
3. **API Configuration**: Securely add your `GEMINI_API_KEY` to your environment variables or Google Colab Secrets.
4. **Run**: Execute the main notebook to trigger the autonomous code execution flow.
