import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def create_resume(
    name: str,
    target_job_role: str,
    user_description: str,
) -> str:
    """
    Generates a professional LaTeX resume from user-provided details.
    """
    latex_template = """\
\\documentclass[letterpaper,11pt]{article}

\\usepackage{latexsym}
\\usepackage[empty]{fullpage}
\\usepackage{titlesec}
\\usepackage{marvosym}
\\usepackage[usenames,dvipsnames]{color}
\\usepackage{verbatim}
\\usepackage{enumitem}
\\usepackage[hidelinks]{hyperref}
\\usepackage{fancyhdr}
\\usepackage[english]{babel}
\\usepackage{tabularx}
\\usepackage{fontawesome5}
\\usepackage{multicol}
\\setlength{\\multicolsep}{-3.0pt}
\\setlength{\\columnsep}{-1pt}
\\input{glyphtounicode}


%----------FONT OPTIONS----------
% sans-serif
% \\usepackage[sfdefault]{FiraSans}
% \\usepackage[sfdefault]{roboto}
% \\usepackage[sfdefault]{noto-sans}
% \\usepackage[default]{sourcesanspro}

% serif
% \\usepackage{CormorantGaramond}
% \\usepackage{charter}


\\pagestyle{fancy}
\\fancyhf{} % clear all header and footer fields
\\fancyfoot{}
\\renewcommand{\\headrulewidth}{0pt}
\\renewcommand{\\footrulewidth}{0pt}

% Adjust margins
\\addtolength{\\oddsidemargin}{-0.6in}
\\addtolength{\\evensidemargin}{-0.5in}
\\addtolength{\\textwidth}{1.19in}
\\addtolength{\\topmargin}{-.7in}
\\addtolength{\\textheight}{1.4in}

\\urlstyle{same}

\\raggedbottom
\\raggedright
\\setlength{\\tabcolsep}{0in}

% Sections formatting
\\titleformat{\\section}{
  \\vspace{-4pt}\\scshape\\raggedright\\large\\bfseries
}{}{0em}{}[\\color{black}\\titlerule \\vspace{-5pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\\pdfgentounicode=1

%-------------------------
% Custom commands
\\newcommand{\\resumeItem}[1]{
  \\item\\small{
    {#1 \\vspace{-2pt}}
  }
}

\\newcommand{\\classesList}[4]{
    \\item\\small{
        {#1 #2 #3 #4 \\vspace{-2pt}}
  }
}

\\newcommand{\\resumeSubheading}[4]{
  \\vspace{-2pt}\\item
    \\begin{tabular*}{1.0\\textwidth}[t]{l@{\\extracolsep{\\fill}}r}
      \\textbf{#1} & \\textbf{\\small #2} \\\\
      \\textit{\\small#3} & \\textit{\\small #4} \\\\
    \\end{tabular*}\\vspace{-7pt}
}

\\newcommand{\\resumeSubSubheading}[2]{
    \\item
    \\begin{tabular*}{0.97\\textwidth}{l@{\\extracolsep{\\fill}}r}
      \\textit{\\small#1} & \\textit{\\small #2} \\\\
    \\end{tabular*}\\vspace{-7pt}
}

\\newcommand{\\resumeProjectHeading}[2]{
    \\item
    \\begin{tabular*}{1.001\\textwidth}{l@{\\extracolsep{\\fill}}r}
      \\small#1 & \\textbf{\\small #2}\\\\
    \\end{tabular*}\\vspace{-7pt}
}

\\newcommand{\\resumeSubItem}[1]{\\resumeItem{#1}\\vspace{-4pt}}

\\renewcommand\\labelitemi{$\\vcenter{\\hbox{\\tiny$\\bullet$}}$}
\\renewcommand\\labelitemii{$\\vcenter{\\hbox{\\tiny$\\bullet$}}$}

\\newcommand{\\resumeSubHeadingListStart}{\\begin{itemize}[leftmargin=0.0in, label={}]}
\\newcommand{\\resumeSubHeadingListEnd}{\\end{itemize}}
\\newcommand{\\resumeItemListStart}{\\begin{itemize}}
\\newcommand{\\resumeItemListEnd}{\\end{itemize}\\vspace{-5pt}}
\\newcommand\\sbullet[1][.5]{\\mathbin{\\vcenter{\\hbox{\\scalebox{#1}{\\tiny$\\bullet$}}}}}
\\newcommand{\\descript}[1]{\\color{subheadings}\\raggedright\\hspace*{0pt}\\hfill\\vspace{3pt}\\fontsize{11pt}{13pt}\\selectfont {#1 \\\\} \\normalfont}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%


\\begin{document}


% \\end{center}


\\begin{center}

      {\\Huge \\scshape Subham Sahoo} \\\\\\vspace{4pt}
       DOB: 30 May 2006 \\quad Kalinga Nagar, Jajpur, Odisha   \\\\ \\vspace{4pt}

    \\small \\raisebox{-0.1\\height}\\faPhone\\ (+91) 9040900801 ~ \\href{mailto:mail@subhamsahoo.in}{\\raisebox{-0.2\\height}\\faEnvelope\\  \\underline{mail@subhamsahoo.in}} ~
    \\href{https://linkedin.com/in/realsubhamsahoo/}{\\raisebox{-0.2\\height}\\faLinkedin\\ \\underline{Linkedin}}  ~
    \\href{https://github.com/realsubhamsahoo/}{\\raisebox{-0.2\\height}\\faGithub\\ \\underline{Github}}
    %This Section Adds Additional Links like leetcode, codeforce, etc.
    \\href{https://subhamsahoo.in}{\\raisebox{-0.2\\height}\\faGlobe\\ \\underline{subhamsahoo.in }}
    \\href{https://drive.google.com/file/d/1VIyU4aDMDu3AO2dFUM0DMZdhE7cB00uB/view?usp=sharing}{\\raisebox{-0.2\\height}\\faBook\\ \\underline{gradecard}}
    \\vspace{-12pt}
\\end{center}


%-----------EDUCATION-----------
\\section{Education}
  \\resumeSubHeadingListStart
    \\resumeSubheading
      {National Institute of Technology, Rourkela}{Aug 2023 -- Present}
      {Bachelor of Technology in Ceramic Engineering (CGPA - 7.95)}{Rourkela, Odisha}
    \\resumeSubheading
      {Gurukul Public School}{May 2023}
      {CBSE, Science (PCM) (Percentage - 97.2\\%)}{Chandikhol, Odisha}
  \\resumeSubHeadingListEnd

%------RELEVANT COURSEWORK-------
\\section{Relevant Coursework}

        \\begin{multicols}{3}
            \\begin{itemize}[itemsep=-5pt, parsep=3pt]
                \\item\\small Data Analysis and Visualization
                \\item Business Research Methodology
                \\item Neural Networks \& ML
                \\item Machine Learning Operations
                \\item Structured Query Language
                \\item NLP \& Deep Learning



            \\end{itemize}
        \\end{multicols}
        \\vspace*{2.0\\multicolsep}


%-----------Experience-----------%
\\section{Technical Experience}

  \\resumeSubHeadingListStart
\\resumeSubheading
  {Research Internship: Predicting Compressive Strength of Ceramic Waste Concrete}{June 2025}
  {ML Research Intern}{\\href{https://github.com/realsubhamsahoo/Ceramic-Concrete-Strength-ML-Project}{Github}}
  \\resumeItemListStart
    \\resumeItem{Built a \\textbf{supervised Machine Learning pipeline} to model the \\textbf{compressive strength} of sustainable concrete using \\textbf{167 mix designs} with ceramic waste, fly ash, and recycled aggregates from an experimental dataset at \\textbf{IIT Bhubaneswar}.}
    \\resumeItem{Performed in-depth \\textbf{Exploratory Data Analysis (EDA)} using \\textbf{pandas}, \\textbf{matplotlib}, and \\textbf{seaborn} to visualize \\textbf{feature distributions}, \\textbf{correlations}, \\textbf{water-cement ratio} and \\textbf{age–strength trends}.}
    \\resumeItem{Trained and tuned multiple \\textbf{regression models} including \\textbf{CatBoost}, \\textbf{Gradient Boosting}, \\textbf{XGBoost}, and \\textbf{Random Forest}, achieving \\textbf{R² = 0.94} and \\textbf{RMSE = 4.47}.}
   \\resumeItem{Applied \\textbf{MLOps best practices}—built modular \\textbf{ETL pipelines}, tracked experiments using \\textbf{MLflow}, containerized the application with \\textbf{Docker}, and prepared deployment on \\textbf{AWS EC2} with a \\textbf{Streamlit-based UI}.}
  \\resumeItemListEnd

    \\resumeSubHeadingListEnd
\\vspace{-12pt}

%-----------PROJECTS-----------%

\\section{Projects}
\\resumeSubHeadingListStart

  \\resumeSubheading
    {\\textbf{Data Cleaning and EDA using MySQL}}{Jan 2025}
    {\\textit{Structured Query Language (SQL)}}{\\href{https://github.com/realsubhamsahoo/Data-Cleaning-EDA-Project-MySQL}{Github}}
    \\resumeItemListStart
      \\resumeItem{Cleaned and optimized corporate layoff data using \\textbf{advanced SQL}, reducing data processing time by \\textbf{30\\%}.}
      \\resumeItem{Applied \\textbf{Common Table Expressions (CTEs)} and \\textbf{window functions} to compute cumulative layoffs and identify top layoff trends by year.}
    \\resumeItemListEnd

  \\resumeSubheading
    {\\textbf{Revenue Dashboard Project}}{Jan 2025}
    {\\textit{Power BI}}{\\href{https://github.com/realsubhamsahoo/power-bi-projects/}{Github}}
    \\resumeItemListStart
      \\resumeItem{Designed an \\textbf{interactive Power BI dashboard} for the hospitality sector, enabling data-driven decisions through visual insights and KPI tracking.}
      \\resumeItem{Enabled data-driven decision-making by implementing \\textbf{DAX measures} and developing \\textbf{region-level performance insights}, leading to a \\textbf{20\\% improvement in operational visibility}.}
    \\resumeItemListEnd

\\resumeSubHeadingListEnd
\\vspace{-12pt}


%
%-----------PROGRAMMING SKILLS-----------
\\section{Technical Skills}
\\begin{itemize}[leftmargin=0.35in, itemsep=0pt, label={\\tiny$\\bullet$}]
    \\item \\textbf{Programming Languages}{: Python, SQL (MySQL, PostgreSQL), JavaScript}
    \\item \\textbf{Libraries \& Frameworks}{: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, XGBoost, CatBoost, Streamlit, BentoML}
    \\item \\textbf{MLOps \& Deployment Tools}{: Docker, MLflow, AWS (S3, EC2, Beanstalk, ECR), Azure (Containers, Images), Google Cloud Platform (GCP), DagsHub}
    \\item \\textbf{Data Engineering \& Tools}{: ETL Pipelines, Jupyter Notebook, Power BI, MS Excel, MS PowerPoint, MATLAB, VS Code}
\\end{itemize}

\\vspace{-12pt}

%-----------INVOLVEMENT---------------
\\section{Extracurricular Activities}
    \\resumeSubHeadingListStart
     \\resumeSubheading{HackNITR – Largest Hackathon of Eastern India}{May 2025 -- Present}{Core Team Lead}{NIT Rourkela}
\\resumeItemListStart
  \\resumeItem{Led the \\textbf{Community Partners team} to coordinate outreach across universities in India, onboarded partners, and filtered CP data with \\textbf{600+ entries} using \\textbf{MS Excel} to ensure accurate tracking and boost national-level participation.}
\\resumeItemListEnd
\\vspace{-12pt}
\\resumeSubheading{OpenCode Club}{Aug 2023 -- Present}{Web3 Lead}{NIT Rourkela}
\\resumeItemListStart
  \\resumeItem{Conducted educational \\textbf{Web3 sessions} on \\textbf{decentralization}, \\textbf{wallets}, \\textbf{crypto}, and \\textbf{DeFi} with \\textbf{live demos}, enhancing awareness and interest in \\textbf{blockchain} technologies for \\textbf{40+ Students}.}
\\resumeItemListEnd
    \\resumeSubHeadingListEnd


\\end{document}
"""
    prompt = f\"\"\"
You are an expert LaTeX resume generator. Your task is to create a professional resume for a user.
The user's name is '{name}'.
They are targeting the job role of '{target_job_role}'.
Here is a short description from the user: '{user_description}'.

You MUST generate the LaTeX code for the resume by strictly following the format, structure, and commands of the example below.
Adapt the content to the user's details, inventing plausible information for sections like Education, Experience, Projects, etc., based on the target job role.
The final output should be only the full, complete LaTeX code, starting with `\\documentclass` and ending with `\\end{{document}}`.

Here is the example of the LaTeX format you must follow:

```latex
{latex_template}
```

Now, generate the new LaTeX resume for {name}.
Remember to enclose each section in the special comment markers for future updates, for example:
% BEGIN_SECTION: Education
... LaTeX for education section ...
% END_SECTION: Education
\"\"\"

    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text
