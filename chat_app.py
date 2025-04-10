from crewai import Crew

from models import ResumeData
from agents import query_classifier_agent, jobrole_industry_researcher_agent, work_culture_researcher_agent, people_like_me_agent, out_of_box_agent
from tasks import query_classification_task, jobrole_industry_research_task, work_culture_research_task, people_like_me_task, out_of_box_task
from resume_extractor import get_structured_data_from_resume_path

def classify_input(user_input):
    crew = Crew(agents=[query_classifier_agent], tasks=[query_classification_task])
    result = crew.kickoff(inputs={"query": user_input})
    return result

def find_job_roles(user_input, profile, category): 
    if category.raw == "Job Role/Industry":
            crew = Crew(agents=[jobrole_industry_researcher_agent], tasks=[jobrole_industry_research_task])
            result = crew.kickoff(inputs={"query": user_input, "profile": profile.model_dump()})
            return result
    elif category.raw == "Work Culture":
            crew = Crew(agents=[work_culture_researcher_agent, jobrole_industry_researcher_agent],
                        tasks=[work_culture_research_task, jobrole_industry_research_task])
            result = crew.kickoff(inputs={"query": user_input, "profile": profile.model_dump()})
            return result
    else:
            result = "I didn't understand. Please rephrase."
            return result


def start_chat_app(profile: ResumeData):
    print("Welcome to the Career Chatbot! Type 'exit' to quit.")
    print("Welcome "+ profile.name + "!" + "What is your main reason for career change?")
   
    while True:
        user_input = input("You: ")
        hobbies = input("Please list your super-powers or interests that you want me to consider in options? ")
        profile.hobbies = [hobby.strip() for hobby in hobbies.split(",")]
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        category = classify_input(user_input)
        print(f"Classified as: {category.raw}, {type(category.raw)}")

     # jobs = find_job_roles(user_input, profile, category)
     # print(jobs.raw)

        crew = Crew(agents=[out_of_box_agent], tasks=[out_of_box_task])
        result = crew.kickoff(inputs={"query": user_input, "profile": profile.model_dump()}) 
        print(result.raw)

     #   crew = Crew(agents=[people_like_me_agent], tasks=[people_like_me_task])
     #   result = crew.kickoff(inputs={"role_recommendations": jobs.model_dump(), "profile": profile.model_dump()})
    #  print(result.raw)


if __name__ == "__main__":
    resume_data = get_structured_data_from_resume_path("/Users/vasanthagullapalli/Documents/Vasantha Gullapalli Resume.pdf")
    start_chat_app(resume_data)