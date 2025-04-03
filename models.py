from pydantic import BaseModel,  Field
from typing import List, Optional



class WorkExperience(BaseModel):
    company: str = Field(description="Name of the company")
    location: str = Field(description="Location of the company")
    role: str = Field(description="Title/Role at the company")
    duration: str = Field(description="Duration of the role at the company")
    keywords: List[str] = Field(description="Potential skills employed/identified from the description")
    employment_rating: str = Field(description="Ranking of the employer as Top/Medium/Low in their industry")

class Education(BaseModel):
    degree: str = Field(description="Name of the degree at the institute")
    institution: str = Field(description="Name of the institute")
    year: Optional[str] = Field(description="Year of Graduation")
    education_rating: str = Field(description="Ranking of the institute as Top/Medium/Low in their country")

class CareerPreferences(BaseModel):
    preferred_industry: str = Field(description="Candidate's preferred industry of work for future job opportunities. Don't infer if not found")
    preferred_domain: str = Field(description="Candidate's preferred domain of work for future job opportunities. Don't infer if not found")
    preferred_compensation: str = Field(description="Candidate's preferred compensation wrt to current compensation. Expressed in range of current compensation. "
                                                    "Don't infer if not found")
    workplace_likes: List[str] = Field(description="Candidate's preferred workplace aspects based on their work experience. Do not infer if not present")
    workplace_dislikes: List[str] = Field(description="Candidate's workplace dislikes based on their work experience. Do not infer if not present")
    reasoning: str = Field(description="Detailed justification for inferring preferences around likes, dislikes, domain and industry along with compensation")

class ResumeData(BaseModel):
    name: str = Field(description="Full name of the candidate")
    email: str = Field(description="Email of the candidate")
    phone: str = Field(description="Phone number of the candidate")
    skills: List[str] = Field(description="Expertise or skills highlighted by the candidate")
    work_experience: List[WorkExperience] = Field(description="List of experiences of the candidate")
    education: List[Education] = Field(description="List of educations of the candidate")
    total_yoe: int = Field(description="Total years of experience")
    is_manager: bool = Field(description="Field to suggest if the profile's last job was an individual contributor or Manager")
    leadership_yoe: int = Field(description="If manager, the years of experience in leadership")
    major_industry_work: str = Field(description="Inferred from experience as to which Industry the candidate is most employed too")
    current_industry: str = Field(description="Inferred from either current or last experience to which Industry the candidate has been employed at")
    current_domain: str = Field(description="Inferred from the description in either current or last experience ")
    career_preferences: CareerPreferences = Field(description="Various career preferences of the candidate")

class RoleRecommendation(BaseModel):
    recommended_roles: List[str] = Field(description="List of suggested job roles based on the user's profile.")
    recommended_company: List[str] = Field(description="Name of the company where these roles exist.")
    suggested_training: Optional[List[str]] = Field(None, description="If necessary, recommended training to qualify for these roles.")
    reasoning: str = Field(description="Justification for the recommendations based on user's profile and preferences.")

class RoleRecommendations(BaseModel):
    recommendations: List[RoleRecommendation] = Field(description="List of roles and companies for recommendations along with suggested training & reasoning")


class WorkCultureRecommendations(BaseModel):
    recommended_companies: List[str] = Field(description="List of companies that match the user's work culture preferences.")
    reasoning: str = Field(description="Detailed explanation of why these companies align with the user's preferences.")


class CareerTransitionRecommendation(BaseModel):
    recommended_role: str = Field(description="Suggested role based on user's profile and preferences matching with people transitions")
    people_with_transition: List[str] = Field(description="List of linkedin profiles matching the transition suitable for the user")
    suggested_training: Optional[List[str]] = Field(description="If necessary, recommended training to qualify for these roles.")
    reasoning: str = Field(description="Justification for the recommendations.")

class CareerTransitionRecommendations(BaseModel):
    recommendations: List[CareerTransitionRecommendation] = Field(description="Suggested list of carrier transitions")

class PeopleLikeMeRecommendations(BaseModel):
    recommended_people: List[str] = Field(description="List of professionals who have been in similar job roles as the user.")
    reasoning: str = Field(description="Justification for why these professionals are recommended based on the user's profile.")  

  
