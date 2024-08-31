# """
# Extracting Jobs from Website with LLM
# """

# # Importing Libraries
# import os
# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
# from langchain_core.exceptions import OutputParserException
# from dotenv import load_dotenv

# # Loading .env file
# load_dotenv()

# # Setting Chain Class with LLM
# class Chain:
#     def __init__(self):
#         self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

#     # Extracting Jobs from Website with LLM
#     def extract_jobs(self, cleaned_text):
#         prompt_extract = PromptTemplate.from_template(
#             """
#             ### SCRAPED TEXT FROM WEBSITE:
#             {page_data}
#             ### INSTRUCTION:
#             The scraped text is from the career's page of a website.
#             Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
#             Only return the valid JSON.
#             ### VALID JSON (NO PREAMBLE):
#             """
#         )
#         chain_extract = prompt_extract | self.llm
#         res = chain_extract.invoke(input={"page_data": cleaned_text})
#         try:
#             json_parser = JsonOutputParser()
#             res = json_parser.parse(res.content)
#         except OutputParserException:
#             raise OutputParserException("Context too big. Unable to parse jobs.")
#         return res if isinstance(res, list) else [res]

#     # Writing Email with LLM
#     def write_mail(self, job, links):
#         prompt_email = PromptTemplate.from_template(
#             """
#             ### JOB DESCRIPTION:
#             {job_description}

#             ### INSTRUCTION:
#             You are Raheel, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
#             the seamless integration of business processes through automated tools. 
#             Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
#             process optimization, cost reduction, and heightened overall efficiency. 
#             Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
#             in fulfilling their needs.
#             Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
#             Remember you are Raheel, BDE at AtliQ. 
#             Do not provide a preamble.
#             ### EMAIL (NO PREAMBLE):

#             """
#         )
        
#         chain_email = prompt_email | self.llm
#         res = chain_email.invoke({"job_description": str(job), "link_list": links})
#         return res.content

# # Running Script 
# if __name__ == "__main__":
#     print(os.getenv("GROQ_API_KEY"))


"""
Extracting Jobs from Website with LLM
"""

# Importing Libraries
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

# Loading .env file
load_dotenv()

# Setting Chain Class with LLM
class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    # Extracting Jobs from Website with LLM
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}

            ### TASK:
            You need to analyze the provided text and extract the job listings in JSON format. The JSON should contain the following keys: 
            `role`, `experience`, `skills`, and `description`. Ensure that the output is a valid JSON structure.
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    # Writing Email with LLM
    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DETAILS:
            {job_description}

            ### INSTRUCTION:
            You are Raheel Arshad, a Business Development Executive at Hafazi Tech. Hafazi Tech is an AI & Software Consulting company specializing in providing 
            tailored solutions to optimize business processes, reduce costs, and enhance efficiency. 
            Draft a compelling cold email to the hiring manager regarding the job described above, highlighting how Hafazi Tech can meet their needs. 
            Incorporate the most relevant portfolio links from the following list to strengthen your pitch: {link_list}.
            ### EMAIL TEMPLATE (NO PREAMBLE):
            """
        )
        
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

# Running Script 
if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))

