import json
import pdfplumber
from crewai import Crew

from agents import resume_parser_agent
from tasks import resume_extraction
from models import ResumeData


def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF resume."""
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return text

def get_structured_data_from_resume(resume_text):
    crew = Crew(agents=[resume_parser_agent], tasks=[resume_extraction])

    result = crew.kickoff(inputs={"profile": resume_text})
    print(result.raw)

    structured_response = ResumeData.model_validate_json(result.raw)
    return structured_response



def get_structured_data_from_resume_path(pdf_path):
    resume_text = extract_text_from_pdf(pdf_path)
    return get_structured_data_from_resume(resume_text)


if __name__ == '__main__':
    #get_structured_data_from_resume_path("/home/karthik/Downloads/Karthik_Jayanthi_Resume.pdf")

    resume_data = get_structured_data_from_resume_path("/home/karthik/Downloads/Karthik_Jayanthi_Resume.pdf")
    print(json.dumps(resume_data.model_dump(), indent=2))