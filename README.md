# ResumeIQ — AI Resume Analyzer & Job Match Assistant

ResumeIQ is an AI-powered resume analysis application that helps job seekers understand how well their resume aligns with a target job description. It extracts information from PDF resumes, identifies technical skills, calculates skill-match and text-similarity scores, generates a transformer-based resume summary, and provides actionable improvement insights.

The project combines Natural Language Processing (NLP), machine learning techniques, a React frontend, a FastAPI backend, and Docker containerization in one application.

## Features

- **PDF Resume Upload:** Upload a text-based PDF resume for analysis.
- **Resume Text Extraction:** Extract readable text from PDF documents.
- **Skill Extraction:** Identify technical skills using a configurable skill dictionary and alias matching.
- **Job Skill Matching:** Compare resume skills with the requirements detected in a job description.
- **Skill Match Score:** Calculate the percentage of detected job skills also present in the resume.
- **Text Similarity:** Use TF-IDF vectorization and cosine similarity to measure textual alignment between the resume and job description.
- **AI Resume Summary:** Generate a concise summary using the Hugging Face T5-small sequence-to-sequence model.
- **Actionable Insights:** Present an overall match assessment, matched skills, missing skills, and improvement recommendations.
- **Interactive Web Interface:** Display analysis results in a React-based dashboard.
- **REST API:** Expose resume analysis functionality through FastAPI.
- **Docker Support:** Run the frontend and backend together using Docker Compose.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | React, JavaScript, Vite, CSS |
| Backend | Python, FastAPI, Uvicorn |
| PDF Processing | PyMuPDF |
| NLP and Machine Learning | scikit-learn, TF-IDF, cosine similarity |
| Transformer Model | Hugging Face Transformers, T5-small |
| Model Runtime | PyTorch |
| API Validation | FastAPI, Python Multipart |
| Containerization | Docker, Docker Compose |
| Version Control | Git, GitHub |

## System Architecture

```text
                 User
                  |
                  v
          React Frontend
                  |
                  | PDF Resume + Job Description
                  v
           FastAPI Backend
                  |
                  v
           PDF Text Extraction
                  |
                  v
             Text Cleaning
                  |
          +-------+--------+
          |                |
          v                v
    Skill Extraction   TF-IDF Vectorization
          |                |
          v                v
    Skill Comparison   Cosine Similarity
          |                |
          +-------+--------+
                  |
                  v
         T5 Resume Summarization
                  |
                  v
          Insights Generation
                  |
                  v
        JSON Analysis Response
                  |
                  v
          React Results UI
```

## How It Works

1. The user uploads a PDF resume and enters a job description.
2. The frontend sends both inputs to the FastAPI `/analyze` endpoint.
3. PyMuPDF extracts readable text from the uploaded PDF.
4. The backend cleans the extracted resume text and job description.
5. The skill extractor detects supported skills and their aliases.
6. The job matcher identifies overlapping and missing skills and calculates the skill-match percentage.
7. TF-IDF vectorization and cosine similarity calculate textual similarity.
8. The T5-small transformer generates a resume summary from recognized resume sections.
9. The insights module creates an assessment and recommendations based on the analysis scores and detected skills.
10. The backend returns a JSON response, which the React frontend displays.

## Understanding the Scores

### Skill Match Percentage

The skill-match percentage measures the proportion of detected job-description skills that are also detected in the resume.

**Formula:**

`Skill Match = (Matched Job Skills / Detected Job Skills) × 100`

The score is based on the skills recognized by the configured dictionary. It is not a hiring probability.

### Text Similarity Percentage

Text similarity uses TF-IDF representations of the resume and job description, followed by cosine similarity. It measures lexical overlap and textual alignment; it does not establish that two documents have the same meaning.

### Missing Skills

Missing skills are detected requirements that the skill extractor did not find in the resume. A missing skill is not proof that the candidate lacks that ability.

## Project Structure

```text
ResumeIQ/
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── models/
│   │   └── summarizer.py
│   ├── nlp/
│   │   ├── insights.py
│   │   ├── job_matcher.py
│   │   ├── skill_extractor.py
│   │   └── text_matcher.py
│   ├── services/
│   │   └── resume_service.py
│   ├── utils/
│   │   ├── pdf_parser.py
│   │   ├── resume_sections.py
│   │   └── text_cleaner.py
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── Dockerfile
├── data/
│   └── sample_job_descriptions/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

Additional utility modules and tests may also be present in the repository.

## Requirements

- Windows, Linux, or macOS
- Docker Desktop with Docker Compose, or a compatible Docker Engine installation
- Git for version control
- An internet connection for the initial transformer model download

The backend uses PyTorch and Transformers, so the backend Docker image can be large. The first startup may take longer while model files are downloaded and loaded.

## Run with Docker Compose

Docker Compose is the recommended way to run the complete application.

### 1. Clone the repository

```bash
git clone https://github.com/ghawatesiddharth/ResumeIQ_Analyser.git
cd ResumeIQ_Analyser
```

### 2. Start the application

```bash
docker compose up -d --build
```

### 3. Check the services

```bash
docker compose ps
```

Both the backend and frontend should show a running status.

### 4. Open the application

- **ResumeIQ Frontend:** http://localhost:5173
- **Backend API:** http://localhost:8000
- **Swagger API Documentation:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health

### 5. Stop the application

```bash
docker compose down
```

This stops and removes the Compose containers and network while keeping the built images.

## Run the Backend Locally

If you prefer to run the backend without Docker, use Python and install the dependencies.

Activate your existing virtual environment if you already have one. Otherwise, create a suitable Python environment.

Install the backend dependencies:

```bash
pip install -r requirements.txt
```

Start the API from the project root:

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000.

## Run the Frontend Locally

Open a second terminal:

```bash
cd frontend
npm ci
npm run dev
```

Vite normally serves the development frontend at http://localhost:5173.

For local development, ensure the frontend API URL and backend CORS configuration match your local setup.

## API Reference

### `GET /health`

Checks whether the API is responding.

Example response:

```json
{
  "status": "ok",
  "service": "ResumeIQ API"
}
```

### `POST /analyze`

Accepts multipart form data containing:

- `resume`: a PDF resume file
- `job_description`: the target job description

The response contains the uploaded filename and an analysis object with detected skills, matched skills, missing skills, skill-match percentage, text-similarity percentage, resume summary, and insights.

The current API accepts PDF files up to 5 MB and requires a meaningful job description. Scanned PDFs without an extractable text layer may not work.

## Testing

The project includes Python test scripts for several components, such as PDF extraction, text cleaning, skill extraction, job matching, summarization, and resume analysis.

Run an individual test script from the project root, for example:

```bash
python test_skill_extractor.py
```

Other test scripts can be run in the same way. Ensure the required Python dependencies and model files are available.

## Current Limitations

- Skill extraction relies on a manually configured dictionary of skills and aliases; it may miss skills that are not included.
- TF-IDF cosine similarity measures textual overlap, not deep semantic equivalence.
- The T5-small summary may omit details or produce imperfect wording and should be reviewed.
- PDF text extraction works best with text-based PDFs; scanned documents may require OCR.
- Analysis results are decision-support information, not a guarantee of interview selection or employment.
- The current application is an MVP and should undergo additional security, privacy, accessibility, and deployment testing before public production use.

## Privacy and Security

Resume documents can contain sensitive personal information. Use only documents you are authorized to process. Uploaded files are processed through the backend, and the current API removes its temporary uploaded PDF after analysis. Do not commit personal resumes, access tokens, passwords, environment files, or other confidential data to a public repository.

## Future Enhancements

- Expand the skill taxonomy and improve context-aware extraction.
- Add OCR support for scanned resumes.
- Improve summary quality and evaluation.
- Add exportable analysis reports.
- Introduce configurable API URLs and production deployment settings.
- Add automated tests and continuous integration.
- Optimize Docker image size and model-loading performance.

## Author

**Siddharth Ghawate**

B.Tech — Information Technology

GitHub: https://github.com/ghawatesiddharth

### Academic Disclaimer

ResumeIQ is an educational project and is not intended to make hiring decisions or guarantee employment outcomes. Its scores and recommendations are generated using the implemented algorithms and configured skill dictionary and should be interpreted as indicative results rather than definitive assessments of a candidate.

### License and Usage

No open-source license has been assigned to this repository. Unless a license is added, the project's code remains subject to applicable copyright laws. Public visibility on GitHub does not by itself grant permission to copy, modify, redistribute, or commercially use the code.

Third-party libraries and pretrained models remain subject to their respective licenses and terms.
