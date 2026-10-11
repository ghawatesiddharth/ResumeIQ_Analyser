import re


# Canonical skill -> possible aliases found in resumes
# and job descriptions.
SKILL_ALIASES = {

    # ==========================================
    # PROGRAMMING LANGUAGES
    # ==========================================

    "Python": [
        "python",
    ],

    "Java": [
        "java",
    ],

    "JavaScript": [
        "javascript",
        "js",
    ],

    "C++": [
        "c++",
    ],

    "C": [
        "c",
    ],

    "SQL": [
        "sql",
    ],


    # ==========================================
    # MACHINE LEARNING / AI
    # ==========================================

    "Machine Learning": [
        "machine learning",
        "ml",
    ],

    "Deep Learning": [
        "deep learning",
        "dl",
    ],

    "Natural Language Processing": [
        "natural language processing",
        "nlp",
    ],

    "Generative AI": [
        "generative ai",
        "genai",
        "gen ai",
    ],

    "Large Language Models": [
        "large language models",
        "large language model",
        "llm",
        "llms",
    ],

    "Prompt Engineering": [
        "prompt engineering",
        "prompt design",
    ],

    "Supervised Learning": [
        "supervised learning",
    ],

    "Unsupervised Learning": [
        "unsupervised learning",
    ],

    "Random Forest": [
        "random forest",
    ],

    "Linear Regression": [
        "linear regression",
    ],

    "Model Evaluation": [
        "model evaluation",
    ],

    "Hyperparameter Tuning": [
        "hyperparameter tuning",
        "hyperparameter optimization",
    ],

    "Computer Vision": [
        "computer vision",
        "cv",
    ],


    # ==========================================
    # DATA SCIENCE LIBRARIES
    # ==========================================

    "Pandas": [
        "pandas",
    ],

    "NumPy": [
        "numpy",
    ],

    "scikit-learn": [
        "scikit-learn",
        "sklearn",
    ],

    "Matplotlib": [
        "matplotlib",
    ],

    "Seaborn": [
        "seaborn",
    ],

    "BeautifulSoup": [
        "beautifulsoup",
        "beautifulsoup4",
    ],

    "TensorFlow": [
        "tensorflow",
    ],

    "PyTorch": [
        "pytorch",
    ],


    # ==========================================
    # WEB / FRONTEND
    # ==========================================

    "HTML": [
        "html",
    ],

    "CSS": [
        "css",
    ],

    "Tailwind CSS": [
        "tailwind css",
        "tailwindcss",
    ],

    "React": [
        "react",
        "react.js",
        "reactjs",
    ],

    "Node.js": [
        "node.js",
        "nodejs",
    ],


    # ==========================================
    # BACKEND / APIs
    # ==========================================

    "FastAPI": [
        "fastapi",
    ],

    "Flask": [
        "flask",
    ],

    "REST API": [
        "rest api",
        "restful api",
        "restful apis",
    ],

    "API Integration": [
        "api integration",
        "api integrations",
    ],


    # ==========================================
    # DATABASES
    # ==========================================

    "PostgreSQL": [
        "postgresql",
        "postgres",
    ],

    "MySQL": [
        "mysql",
    ],

    "MongoDB": [
        "mongodb",
        "mongo",
    ],

    "DBMS": [
        "dbms",
        "database management system",
    ],


    # ==========================================
    # DATA ENGINEERING / ANALYTICS
    # ==========================================

    "Data Preprocessing": [
        "data preprocessing",
        "data pre-processing",
    ],

    "Feature Engineering": [
        "feature engineering",
    ],

    "Exploratory Data Analysis": [
        "exploratory data analysis",
        "eda",
    ],

    "Data Scraping": [
        "data scraping",
        "web scraping",
    ],

    "Data Visualization": [
        "data visualization",
        "data visualisation",
    ],


    # ==========================================
    # VISUALIZATION / BI
    # ==========================================

    "Power BI": [
        "power bi",
        "powerbi",
    ],

    "Tableau": [
        "tableau",
    ],

    "MS Excel": [
        "ms excel",
        "microsoft excel",
        "excel",
    ],


    # ==========================================
    # SOFTWARE DEVELOPMENT
    # ==========================================

    "Object-Oriented Programming": [
        "object-oriented programming",
        "object oriented programming",
        "oop",
    ],

    "Git": [
        "git",
    ],

    "GitHub": [
        "github",
    ],

    "Jupyter Notebook": [
        "jupyter notebook",
        "jupyter",
    ],

    "VS Code": [
        "vs code",
        "visual studio code",
    ],


    # ==========================================
    # DEVOPS / CLOUD
    # ==========================================

    "Docker": [
        "docker",
    ],

    "AWS": [
        "aws",
        "amazon web services",
    ],


    # ==========================================
    # KNOWLEDGE GRAPHS / SEMANTIC WEB
    # ==========================================

    "OWL-RL": [
        "owl-rl",
        "owl rl",
    ],

    "Knowledge Graphs": [
        "knowledge graph",
        "knowledge graphs",
    ],

    "RDF": [
        "rdf",
        "resource description framework",
    ],

    "SPARQL": [
        "sparql",
    ],
}


def normalize_text(text: str) -> str:
    """
    Normalize text for skill matching.
    """

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text,
    )

    return text.strip()


def contains_skill(
    text: str,
    skill_alias: str,
) -> bool:
    """
    Check whether a skill alias exists as a
    complete term in the text.
    """

    pattern = (
        r"(?<!\w)"
        + re.escape(skill_alias)
        + r"(?!\w)"
    )

    return re.search(
        pattern,
        text,
    ) is not None


def extract_skills(
    text: str,
) -> list[str]:
    """
    Extract canonical technical skills from
    resume or job-description text.
    """

    normalized_text = normalize_text(
        text
    )

    found_skills = []

    for (
        canonical_skill,
        aliases,
    ) in SKILL_ALIASES.items():

        for alias in aliases:

            if contains_skill(
                normalized_text,
                alias,
            ):

                found_skills.append(
                    canonical_skill
                )

                break

    return found_skills