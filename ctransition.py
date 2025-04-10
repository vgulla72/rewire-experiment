from crewai import Crew

from models import ResumeData, CareerTransitionRecommendation
from agents import career_transition_agent, people_like_me_agent, role_researcher_agent
from tasks import career_transition_research_task, people_like_me_task, role_research_task
from resume_extractor import get_structured_data_from_resume_path

def start_ctransition_app(profile: ResumeData):


    career_change_reason = input("Reason for Career Change: ")
    preferred_industry_input = input(f"What Is your preferred Industry of choice ?: ")
   # if preferred_industry_input == "Y":
   #     preferred_industry_input = profile.career_preferences.preferred_industry
    preferred_domain_input = input("What Is your preferred Domain of choice ?:")

    #if preferred_domain_input == "Y":
    #    preferred_domain_input = profile.career_preferences.preferred_domain

    workplace_likes_input = input("What are your some of the aspects you like about a workplace you want to work ?:")
    #if workplace_likes_input == "Y":
    #    workplace_likes_input = profile.career_preferences.workplace_likes

    workplace_dislikes_input = input(
        "What Are some of the dislikes at a workplace you want to work ?: ")
    #if workplace_dislikes_input == "Y":
    #    workplace_dislikes_input = profile.career_preferences.workplace_dislikes

    crew = Crew(agents=[role_researcher_agent ],
                tasks=[role_research_task],
                verbose=True)
    result = crew.kickoff(inputs={"career_change_reason": career_change_reason,
                                  "preferred_domain_input": preferred_domain_input,
                                  "workplace_likes_input": workplace_likes_input,
                                  "workplace_dislikes_input": workplace_dislikes_input,
                                  "profile": profile.model_dump()
                                  }
                          )
    role_recommendations = result.raw
    print(result.raw, type(result.raw))

    crew = Crew(agents=[people_like_me_agent], tasks=[people_like_me_task],
                verbose=True)
    result = crew.kickoff(inputs={"profile": profile.model_dump(),
                                  "role_recommendations": role_recommendations})

    print(result.raw)



if __name__ == "__main__":
    resume_data = get_structured_data_from_resume_path("/Users/vasanthagullapalli/Documents/Vasantha Gullapalli Resume.pdf")
    start_ctransition_app(resume_data)