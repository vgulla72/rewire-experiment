
from crewai import Task
from agents import (resume_parser_agent, query_classifier_agent,
                    jobrole_industry_researcher_agent, work_culture_researcher_agent,
                    career_transition_agent, people_like_me_agent)
from models import (ResumeData, RoleRecommendations,
                    WorkCultureRecommendations, CareerTransitionRecommendations, PeopleLikeMeRecommendations)


resume_extraction = Task(
description=(
        "Extract and structure key details from {profile}, ensuring completeness and accuracy.\n"
        "The extracted information should include Work Experience, Education, Skills, Certifications, "
        "Projects, and relevant metadata such as industry classification and job seniority levels.\n"
        "Enhance the structured resume profile by:\n"
        "1️⃣ **Verifying accuracy** of extracted details.\n"
        "2️⃣ **Adding missing details** if contextually inferrable (without assumptions) and well reasoned.\n"
        "3️⃣ **Categorizing** extracted skills and experience into appropriate industries.\n"
        "4️⃣ **Incorporating additional insights**, such as employer ratings, career trajectory, and industry trends.\n"
        "5️⃣ **Ensuring consistency and readability** for downstream applications.\n"
        "5️6 **Ensure the inferred details are well reasoned"
    ),
    expected_output=(
        "A fully structured and enriched resume profile in the prescribed output format, ready for further analysis.\n"
        "This output should:\n"
        "Be **validated and free of errors**.\n"
        "Include additional insights**, such as employer reputation, industry , manager vs individual contributor etc.\n"
        "Utilize web search and scraping tools to fetch compensation range for latest role from reliable sources.\n"
        "Maintain proper categorization** of roles, skills, and industries.\n"
        "Provide well reasoned justification wherever requested explicitly for the inferences"
    ),
    output_pydantic=ResumeData,
    agent=resume_parser_agent
)

query_classification_task = Task(
    description=(
        "Analyze the user's input **{query}** and determine whether it relates to **work culture preferences** "
        "or **job roles/industry**.\n"
        "If the query concerns work-life balance, company culture, team dynamics, or leadership style, classify it as **Work Culture**.\n"
        "If the query pertains to job positions, career paths, industries, or required skills, classify it as **Job Role/Industry**.\n"
        "Ensure the classification is **precise and unambiguous**."
    ),
    expected_output=(
        "A classification label: either **Work Culture** or **Job Role/Industry**, depending on the nature of the query.\n"
        "This classification will be used to dynamically trigger the appropriate research agent."
    ),
    agent=query_classifier_agent
)

jobrole_industry_research_task = Task(
    description=(
        "Analyze the user's **{query}** and **{profile}** to identify suitable job roles and industries.\n"
        "Leverage industry trends and data to recommend positions aligning with the user's background.\n"
        "If available, refine recommendations using the companies suggested by `work_culture_researcher_agent`.\n"
        "Suggest any necessary **training or skills** required to qualify for these roles.\n"
        "Ensure recommendations are **accurate, well-supported, and aligned with industry standards**."
    ),
    expected_output=(
        "A structured response with:\n"
        "- **Recommended job roles** based on the user's skills & experience.\n"
        "- **Potential companies** where these roles exist (optionally filtered from previous agent output).\n"
        "- **Suggested training/certifications** if needed.\n"
        "- **Clear reasoning** behind each recommendation."
    ),
    output_pydantic=RoleRecommendations,
    agent=jobrole_industry_researcher_agent
)

work_culture_research_task = Task(
    description=(
        "Analyze the user's **{query}** to identify companies that match their work culture preferences and suitable for {profile}.\n"
        "Research work environments, company values, employee reviews, and other relevant factors.\n"
        "Utilize web search and scraping tools to fetch real-time insights from reliable sources.\n"
        "Ensure that recommendations are **structured, well-reasoned, and free from assumptions**."
    ),
    expected_output=(
        "A structured response with:\n"
        "- **Recommended companies** matching the user's cultural preferences.\n"
        "- **Key cultural factors** considered (e.g., remote work policies, work-life balance, diversity, etc.).\n"
        "- **Category of the company** (e.g., non-profit, for-profit, govt, academia, etc.).\n"
        "- **Well-reasoned justification** for each recommendation.\n"
        "- **Additional insights** (if available)."
    ),
    output_pydantic=WorkCultureRecommendations,
    agent=work_culture_researcher_agent
)

career_transition_research_task = Task(
    description=(
        "Analyse the user's ** {query} ** for reason for career change and career preferences set in {profile}"
        "Use knowledge of working professionals from linkedin who have transitioned from user's current role in {profile} matching the {query} and preferences"
        "Ensure the recommendations are well reasoned"
    ),
    expected_output=(
        "A structured response with: "
        "** Recommended Role** where people from user's current role in {profile} moved to matching the preferences in {profile}"
        "** List of LInkedin profiles** matching this transition from user's current role"
        "** Well-reasoned justification** for each recommendation"
    ),
    output_pydantic=CareerTransitionRecommendations,
    agent=career_transition_agent
)

people_like_me_task = Task(
    description=(
        "Identify individuals who were in similar jobs in the past as in  user's **{profile}** and currently in jobs similar to **{jobs}**.\n"
        "Leverage professional networking platforms to find potential connections.\n"
        "Recommend relevant profiles based on **{profile}**, location, and other criteria.\n"
        "Ensure that the recommendations are **relevant, accurate, and respectful of privacy**."
    ),
    expected_output=(
        "A list of **recommended profiles** that closely match the user's background and recommended jobs.\n"
        "Each recommendation should include:\n"
        "- **Name, previous and current designation** of the individual.\n"
        "- **Profile summary** highlighting previous and current designation and key attributes.\n"
        "- **Reasoning** behind the recommendation.\n"
        "- **Links to their linkedin profiles** (if available).\n"
    ),
    output_pydantic=PeopleLikeMeRecommendations,
    agent=people_like_me_agent
)
career_transition_research_task = Task(
    description=(
        "Analyse the user's ** {query} ** for reason for career change and career preferences set in {profile}"
        "Use knowledge of working professionals from linkedin who have transitioned from user's current role in {profile} matching the {query} and preferences"
        "Ensure the recommendations are well reasoned"
    ),
    expected_output=(
        "A structured response with: "
        "** Recommended Role** where people from user's current role in {profile} moved to matching the preferences in {profile}"
        "** List of LInkedin profiles** matching this transition from user's current role"
        "** Well-reasoned justification** for each recommendation"
    ),
    output_pydantic=CareerTransitionRecommendations,
    agent=career_transition_agent
)






