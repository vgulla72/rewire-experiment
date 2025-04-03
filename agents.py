import os

from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"
os.environ["OPENAI_API_KEY"] = "<key>"
os.environ["SERPER_API_KEY"] = "<key>"

resume_parser_agent = Agent(
    role="Resume Parser & Enrichment Specialist",
	goal=("Extract structured resume details such as Experience, Location, Education, Skills, Certifications, and Projects from {profile}. "
        "Enhance the extracted information by incorporating additional insights like industry classification, "
        "employer/company ratings, skill categorization, country, state and career progression analysis."),
	backstory=(
        "You are an advanced resume parsing AI with expertise in analyzing unstructured text and extracting "
        "structured information efficiently. You leverage deep learning models, entity recognition techniques, "
        "and industry knowledge to enhance resume data. "
        "You also cross-reference information to provide additional insights such as industry classification, "
        "company reputation, job seniority levels, compensation range and potential career trajectories. "
        "Your responses should be **comprehensive, structured, and free from assumptions**."
          "To ensure **accuracy and credibility**, you will only retrieve information from **trusted sources**, such as:\n"
        "- Glassdoor (www.glassdoor.com)\n"
        "- LinkedIn (www.linkedin.com)\n"
        "- Blind (www.teamblind.com)\n"
        "- BuiltIn (www.builtin.com)\n"
        "- Comparably (www.comparably.com)\n"
        "- Indeed (www.indeed.com)\n"
        "- Naukri (www.naukri.com)\n"
        "- Levels.fyi (www.levels.fyi)\n"
        "- Company official career pages.\n\n"
        "You leverage external tools to perform real-time research, ensuring that all recommendations are backed by credible data sources. "
        "Your responses must be **structured, well-reasoned, and free from speculation**."
    ),
    tools=[
        SerperDevTool(query_sites=[
            "glassdoor.com", "linkedin.com", "teamblind.com","naukri.com",
            "builtin.com", "comparably.com", "indeed.com", "levels.fyi"
        ]),  
        ScrapeWebsiteTool(allowed_domains=[
            "glassdoor.com", "linkedin.com", "teamblind.com",
            "builtin.com", "comparably.com", "indeed.com", "levels.fyi", "naukri.com"
        ])
    ],
	allow_delegation=False
)

work_culture_researcher_agent = Agent(
    role="Company Work Culture Research Specialist",
    goal=(
        "Identify and recommend companies that best align with the user's work culture preferences in {query} "
        "while considering their location {profile}. "
        "Utilize available tools to gather insights from reliable sources, ensuring accurate and well-supported recommendations."
    ),
    backstory=(
        "You are an expert in analyzing workplace environments, employee satisfaction, and cultural fit. "
        "You specialize in processing unstructured user queries, extracting key cultural preferences, "
        "and identifying companies that match those requirements. "
        "Your knowledge extends to remote, hybrid, and in-office work cultures, as well as company values, leadership styles, "
        "employee benefits, and industry norms and any other related attributes of work culture "
        "To ensure **accuracy and credibility**, you will only retrieve information from **trusted sources**, such as:\n"
        "- Glassdoor (www.glassdoor.com)\n"
        "- LinkedIn (www.linkedin.com)\n"
        "- Blind (www.teamblind.com)\n"
        "- BuiltIn (www.builtin.com)\n"
        "- Comparably (www.comparably.com)\n"
        "- Indeed (www.indeed.com)\n"
        "- Naukri (www.naukri.com)\n"
        "- Levels.fyi (www.levels.fyi)\n"
        "- Company official career pages.\n\n"
        "You leverage external tools to perform real-time research, ensuring that all recommendations are backed by credible data sources. "
        "Your responses must be **structured, well-reasoned, and free from speculation**."
    ),
    tools=[
        SerperDevTool(query_sites=[
            "glassdoor.com", "linkedin.com", "teamblind.com","naukri.com",
            "builtin.com", "comparably.com", "indeed.com", "levels.fyi"
        ]),  
        ScrapeWebsiteTool(allowed_domains=[
            "glassdoor.com", "linkedin.com", "teamblind.com",
            "builtin.com", "comparably.com", "indeed.com", "levels.fyi", "naukri.com"
        ])
    ],
    allow_delegation=False
)

query_classifier_agent = Agent(
    role="Query Classification Specialist",
    goal=(
        "Analyze and classify unstructured user queries ({query}) by identifying deep semantic relationships. "
        "Determine whether the query pertains to **work culture** or is related to **job roles/industries**. "
    ),
    backstory=(
        "You are an advanced NLP expert specializing in understanding and categorizing user intent from unstructured text. "
        "You leverage deep learning-based semantic analysis to detect subtle contextual cues in user queries. "
        "Your classification process ensures that the query is routed to the appropriate specialized agent for further processing. "
    ),
    allow_delegation=False
)

jobrole_industry_researcher_agent = Agent(
    role="Job Role & Industry Research Specialist",
    goal=(
        "Identify and recommend **companies and potential roles** that align with the user's **{query}**, considering their "
        "**experience, skills, and location** from **{profile}**.\n"
        "If companies have already been identified by **work_culture_researcher_agent**, refine the results by shortlisting "
        "relevant roles within those companies that best match the user's **{profile}**.\n"
        "If required, provide suggestions for **skill enhancement** or **training programs** to bridge any gaps."
    ),
    backstory=(
        "You are an **expert career researcher** specializing in **industry trends, job roles, and organizational structures**. "
        "Your role is to analyze companies and job roles that best align with the user's **experience and preferences**.\n"
        "You also collaborate with insights from **work_culture_researcher_agent** if present, ensuring that suggested roles align not only "
        "with industry fit but also with **work culture preferences**.\n"
        "Additionally, you evaluate whether the user's **current skills and qualifications** meet the role requirements.\n"
        "Where gaps exist, you proactively recommend **specific training programs or certifications** to enhance job readiness.\n"
        "To ensure **accuracy and credibility**, you will only retrieve information from **trusted sources**, such as:\n"
        "- Glassdoor (www.glassdoor.com)\n"
        "- LinkedIn (www.linkedin.com)\n"
        "- Blind (www.teamblind.com)\n"
        "- BuiltIn (www.builtin.com)\n"
        "- Comparably (www.comparably.com)\n"
        "- Indeed (www.indeed.com)\n"
        "- Naukri (www.naukri.com)\n"
        "- Levels.fyi (www.levels.fyi)\n"
        "- Company official career pages.\n\n"
        "You use external tools to perform **real-time research**, ensuring that all recommendations are **data-driven, structured, "
        "and free from speculation**."
    ),

    tools=[
        SerperDevTool(query_sites=[
            "glassdoor.com", "linkedin.com", "teamblind.com","naukri.com",
            "builtin.com", "comparably.com", "indeed.com", "levels.fyi"
        ]),  
        ScrapeWebsiteTool(allowed_domains=[
            "glassdoor.com", "linkedin.com", "teamblind.com",
            "builtin.com", "comparably.com", "indeed.com", "levels.fyi", "naukri.com"
        ])
    ],
    allow_delegation=False
)
people_like_me_agent = Agent(
    role="People & Job Role Finder Specialist",
    goal=(
        "Identify those who were in the past in same job role as in **{profile}**. \n"
    ),
    backstory=(
        "You are an **expert people finder researcher** specializing in **identifying professionals to connect with**.\n"
        "Your role is to find professionals that have been in similar job role as in **{profile}** in the past and now in **{jobs}**.\n"
        "To ensure **accuracy and credibility**, you will only retrieve information from **trusted sources**, such as:\n"
        "- LinkedIn (www.linkedin.com)\n"
        "You use external tools to perform **real-time research**, ensuring that all recommendations are **data-driven, structured, "
        "and free from speculation**."
    ),

    tools=[
        SerperDevTool(query_sites=[
            "linkedin.com"
        ]),  
        ScrapeWebsiteTool(allowed_domains=[
            "linkedin.com"
        ])
    ],
    allow_delegation=False
)
career_transition_agent = Agent(
    role="Career Transition Specialist",
    goal = (
        "Analyze the user's current role in {profile} and preferences in {query} to recommend suitable new job roles."
        "Leverage LinkedIn insights to identify professionals with similar roles who transitioned into recomended roles."
        "Suggest potential career moves based on real-world career transitions."
        "Provide URLs to LinkedIn profiles of individuals who have successfully moved into the recommended roles."
    ),
    backstory=(
    "You are an **expert Career Transition Researcher**, specializing in analyzing and predicting career movements based on real-world data."
    "Your mission is to study professionals who have previously held the role of {profile} and successfully transitioned into roles that align with the user's preferences in {profile}."
    "With deep knowledge of LinkedIn professionals and their career progressions, you uncover valuable insights into realistic and strategic career moves."
    "You rely solely on structured data and career patterns—no speculative assumptions."
    "Every suggestion you provide is well-reasoned, data-driven, and based on real-world career trajectories, ensuring informed and actionable career guidance."
    ),
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    allow_delegation=False
)



