
from crewai import Task
from agents import (resume_parser_agent, query_classifier_agent,
                    jobrole_industry_researcher_agent, work_culture_researcher_agent,
                    career_transition_agent, people_like_me_agent, role_researcher_agent, out_of_box_agent)
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
        "If the query pertains to job description, career paths, industries, or required skills, classify it as **Job Role/Industry**.\n"
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
        "Think out of box and recommend roles aligned with user's hobbies and can benefit from user's background and experience.\n"
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

out_of_box_task = Task(
    description=(
        "Analyze the user's **{query}** and **{profile}** to identify suitable job roles and industries.\n"
        "Think out of box and be creative in identifying careers that can use user's hobbies and benefit from user's experience.\n"
        "Suggest any necessary **training or skills** required to qualify for these roles.\n"
        "Ensure recommendations are **accurate, structured and categorized by type of role**."
    ),
    expected_output=(
        "A structured response with:\n"
        "- **Recommended job roles** based on the user's hobbies, skills & experience, listed by category (Full-time, part-time, freelance, etc.,).\n"
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
        "Analyse the user's ** {career_change_reason} ** for career change and preferences in {workplace_likes_input} and domain in {preferred_domain_input} and current role in {profile}"
        "Use knowledge of working professionals from linkedin who in the past was in user's current role in {profile} and transitioned to roles matching preferences in remaining inputs. "
        "Suggest these roles as recommendations"
        "Ensure the recommendations are well reasoned"
    ),
    expected_output=(
        "A structured response with: "
        "** Recommended Role** where people in the past were on the same role as user's current role in {profile} moved to roles matching the preferences in {career_change_reason}"
        "and can accomodate what the users likes in {workplace_likes_input} and avoids the dislikes in {workplace_dislikes_input}. Additionally the role should match the domain in {preferred_domain_input}"
        "** List of Linkedin profiles** matching this transition from user's current role"
        "** Well-reasoned justification** for each recommendation"
    ),
    output_pydantic=CareerTransitionRecommendations,
    agent=career_transition_agent
)

people_like_me_task = Task(
    description=(
        "Identify individuals who were in similar jobs in the past as in  user's **{profile}** current role and location and are currently working in roles mentioned in  **{role_recommendations}**\n"
        "Leverage professional networking platforms to find potential connections.\n"
        "Recommend relevant profiles based on **{profile}**, location, and other criteria.\n"
        "Ensure that the recommendations are **relevant, accurate, and respectful of privacy**."
        "Using 'site:linkedin.com/in', search for professionals who previously held the same role as in **{profile}** current's role and matching location and currently working in roles mentioned in  **{role_recommendations}**"
        "**Only use actual search and scraped data. Do NOT invent URLs or profiles.**"
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
role_research_task = Task(
    description=(
        "Analyse the user's ** {career_change_reason} ** for career change and preferences in {workplace_likes_input}, dislikes in {workplace_dislikes_input} and preference domain in {preferred_domain_input}"
        "Use knowledge of roles acorss industries and domains and taking help of external tools if required, suggest working  roles matching these preferences and which are closest to the experience of user in {profile}"
        "Suggest these roles as recommendations"
        "Ensure the recommendations are well reasoned"
    ),
    expected_output=(
        "A structured response with: "
        "** Recommended Role** "
        "** Well-reasoned justification** for each recommendation"
    ),
    output_pydantic=RoleRecommendations,
    agent=role_researcher_agent
)





