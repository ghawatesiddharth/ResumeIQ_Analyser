import { useState } from "react";
import "./App.css";


function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");


  const handleFileChange = (event) => {
    const file = event.target.files[0];

    setSelectedFile(file || null);
    setAnalysis(null);
    setError("");
  };


  const analyzeResume = async () => {
    if (!selectedFile) {
      setError("Please select a PDF resume first.");
      return;
    }


    if (!jobDescription.trim()) {
      setError("Please enter a job description.");
      return;
    }


    setLoading(true);
    setError("");
    setAnalysis(null);


    const formData = new FormData();

    formData.append(
      "resume",
      selectedFile
    );

    formData.append(
      "job_description",
      jobDescription
    );


    try {
      const response = await fetch(
        "http://127.0.0.1:8000/analyze",
        {
          method: "POST",
          body: formData,
        }
      );


      const data = await response.json();


      if (!response.ok) {
        throw new Error(
          data.detail ||
          "Resume analysis failed."
        );
      }


      setAnalysis(
        data.analysis
      );

    } catch (err) {

      setError(
        err.message ||
        "Unable to connect to ResumeIQ API."
      );

    } finally {

      setLoading(false);

    }
  };


  return (
    <div className="app">

      {/* =========================================
          NAVBAR
      ========================================== */}

      <header className="navbar">

        <div className="brand">

          <div className="brand-icon">
            R
          </div>

          <div>
            <h2>
              ResumeIQ
            </h2>

            <span>
              AI Resume Analyzer
            </span>
          </div>

        </div>


        <div className="api-status">

          <span className="status-dot"></span>

          API Online

        </div>

      </header>


      <main className="container">

        {/* =========================================
            HERO / UPLOAD SECTION
        ========================================== */}

        <section className="hero">

          <div className="hero-content">

            <span className="badge">
              AI-Powered Resume Intelligence
            </span>


            <h1>
              Turn your resume into
              <span>
                actionable insights.
              </span>
            </h1>


            <p>
              Upload your resume and provide a job
              description. ResumeIQ analyzes your
              skills, calculates job compatibility,
              and generates AI-powered insights.
            </p>

          </div>


          <div className="upload-card">

            <div className="upload-icon">
              ↑
            </div>


            <h3>
              Upload your resume
            </h3>


            <p>
              PDF files only
            </p>


            <label className="file-input">

              <input
                type="file"
                accept=".pdf"
                onChange={handleFileChange}
              />

              <span>
                {selectedFile
                  ? selectedFile.name
                  : "Choose PDF"}
              </span>

            </label>


            {selectedFile && (

              <div className="selected-file">

                <span>
                  📄
                </span>


                <div>

                  <strong>
                    {selectedFile.name}
                  </strong>


                  <small>
                    {
                      (
                        selectedFile.size /
                        1024
                      ).toFixed(1)
                    }
                    {" "}KB
                  </small>

                </div>

              </div>

            )}


            <div className="job-description">

              <label>
                Job Description
              </label>


              <textarea
                value={jobDescription}
                onChange={(event) =>
                  setJobDescription(
                    event.target.value
                  )
                }
                placeholder="Paste the job description here..."
                rows="7"
              />


              <small>
                Add the job requirements you want
                to compare against your resume.
              </small>

            </div>


            <button
              className="analyze-button"
              onClick={analyzeResume}
              disabled={loading}
            >

              {loading
                ? "Analyzing Resume..."
                : "Analyze Resume"}

            </button>


            {error && (

              <div className="error-message">
                {error}
              </div>

            )}

          </div>

        </section>


        {/* =========================================
            RESULTS
        ========================================== */}

        {analysis && (

          <section className="results">

            <div className="section-heading">

              <div>

                <span className="section-label">
                  ANALYSIS COMPLETE
                </span>


                <h2>
                  Resume Analysis
                </h2>

              </div>

            </div>


            {/* =====================================
                METRICS
            ====================================== */}

            <div className="metrics">

              <div className="metric-card">

                <span className="metric-title">
                  Skill Match
                </span>


                <strong>
                  {
                    analysis.skill_match_percentage
                  }%
                </strong>


                <span className="metric-description">
                  Match with job requirements
                </span>

              </div>


              <div className="metric-card">

                <span className="metric-title">
                  Text Similarity
                </span>


                <strong>
                  {
                    analysis.text_similarity_percentage
                  }%
                </strong>


                <span className="metric-description">
                  Resume vs job description
                </span>

              </div>


              <div className="metric-card">

                <span className="metric-title">
                  Skills Found
                </span>


                <strong>
                  {
                    analysis.resume_skills.length
                  }
                </strong>


                <span className="metric-description">
                  Technical skills detected
                </span>

              </div>


              <div className="metric-card">

                <span className="metric-title">
                  Missing Skills
                </span>


                <strong>
                  {
                    analysis.missing_skills.length
                  }
                </strong>


                <span className="metric-description">
                  Skills to consider improving
                </span>

              </div>

            </div>


            {/* =====================================
                INSIGHTS
            ====================================== */}

            {analysis.insights && (

              <div className="insights-card">

                <div className="insights-header">

                  <div className="insights-icon">
                    AI
                  </div>


                  <div>

                    <span>
                      ANALYSIS INSIGHTS
                    </span>


                    <h3>
                      {
                        analysis.insights
                          .overall_assessment
                      }
                    </h3>

                  </div>

                </div>


                <div className="insights-content">

                  <div className="insight-item">

                    <div className="insight-title">
                      ✓ Strengths
                    </div>


                    <p>
                      {
                        analysis.insights
                          .strength_message
                      }
                    </p>

                  </div>


                  <div className="insight-item">

                    <div className="insight-title">
                      ⚠ Skills to Improve
                    </div>


                    <p>
                      {
                        analysis.insights
                          .missing_message
                      }
                    </p>

                  </div>


                  <div className="insight-item">

                    <div className="insight-title">
                      💡 Recommendation
                    </div>


                    <p>
                      {
                        analysis.insights
                          .recommendation
                      }
                    </p>

                  </div>


                  <div className="insight-item">

                    <div className="insight-title">
                      📊 Text Alignment
                    </div>


                    <p>
                      {
                        analysis.insights
                          .similarity_message
                      }
                    </p>

                  </div>

                </div>

              </div>

            )}


            {/* =====================================
                MATCHED / MISSING SKILLS
            ====================================== */}

            <div className="results-grid">

              <div className="result-card">

                <div className="card-header">

                  <h3>
                    ✓ Matched Skills
                  </h3>


                  <span>
                    {
                      analysis.matched_skills.length
                    }
                  </span>

                </div>


                <div className="skills">

                  {analysis.matched_skills.map(
                    (skill) => (

                      <span
                        className="skill matched"
                        key={skill}
                      >
                        {skill}
                      </span>

                    )
                  )}

                </div>

              </div>


              <div className="result-card">

                <div className="card-header">

                  <h3>
                    ⚠ Missing Skills
                  </h3>


                  <span>
                    {
                      analysis.missing_skills.length
                    }
                  </span>

                </div>


                <div className="skills">

                  {analysis.missing_skills.map(
                    (skill) => (

                      <span
                        className="skill missing"
                        key={skill}
                      >
                        {skill}
                      </span>

                    )
                  )}

                </div>

              </div>

            </div>


            {/* =====================================
                AI SUMMARY
            ====================================== */}

            <div className="summary-card">

              <div className="summary-header">

                <div className="ai-icon">
                  AI
                </div>


                <div>

                  <span>
                    AI INSIGHT
                  </span>


                  <h3>
                    Resume Summary
                  </h3>

                </div>

              </div>


              <p>
                {analysis.summary}
              </p>

            </div>


            {/* =====================================
                ALL DETECTED SKILLS
            ====================================== */}

            <div className="result-card full-width">

              <div className="card-header">

                <h3>
                  Detected Resume Skills
                </h3>


                <span>
                  {
                    analysis.resume_skills.length
                  }
                </span>

              </div>


              <div className="skills">

                {analysis.resume_skills.map(
                  (skill) => (

                    <span
                      className="skill"
                      key={skill}
                    >
                      {skill}
                    </span>

                  )
                )}

              </div>

            </div>

          </section>

        )}

      </main>


      {/* =========================================
          FOOTER
      ========================================== */}

      <footer>

        <span>
          ResumeIQ
        </span>


        <span>
          AI Resume Analysis & Job Matching
        </span>

      </footer>

    </div>
  );
}


export default App;