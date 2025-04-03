from crewai import Crew

from models import ResumeData, CareerTransitionRecommendation   
from agents import career_transition_agent
from tasks import career_transition_research_task
from resume_extractor import get_structured_data_from_resume_path

def start_ctransition_app(profile: ResumeData):

    career_change_reason = input("Reason for Career Change: ")
    crew = Crew(agents=[career_transition_agent],
                tasks=[career_transition_research_task])
    result = crew.kickoff(inputs={"query": career_change_reason, "profile": profile.model_dump()})
    print(result.raw)



if __name__ == "__main__":
    resume_data = get_structured_data_from_resume_path("/Users/vasanthagullapalli/Documents/Vasantha Gullapalli Resume.pdf")
    start_ctransition_app(resume_data)