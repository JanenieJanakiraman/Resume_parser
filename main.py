import json

def parse_resume(resume_text):
    # Implement the parsing logic here
    parsed_resume = {
        "contact_information": {
            "name": "John Doe",
            "address": "123 Main St, Anytown, USA",
            "phone": "555-123-4567",
            "email": "johndoe@example.com"
        },
        "professional_summary": "Experienced software engineer with a background in developing scalable applications.",
        "work_experience": [
            {
                "job_title": "Software Engineer",
                "company": "Tech Corp",
                "location": "San Francisco, CA",
                "start_date": "Jan 2018",
                "end_date": "Present",
                "responsibilities": "Developing web applications using Python and JavaScript."
            }
        ],
        "education": [
            {
                "degree": "B.Sc. Computer Science",
                "institution": "University of Somewhere",
                "location": "Somewhere, USA",
                "graduation_year": "2017"
            }
        ],
        "skills": ["Python", "JavaScript", "React"],
        "certifications": ["Certified Kubernetes Administrator"]
    }
    return json.dumps(parsed_resume, indent=4)

resume_text = """
John Doe
123 Main St, Anytown, USA
Phone: 555-123-4567
Email: johndoe@example.com

Professional Summary
Experienced software engineer with a background in developing scalable applications.

Work Experience
Software Engineer
Tech Corp, San Francisco, CA
Jan 2018 - Present
Developing web applications using Python and JavaScript.

Education
B.Sc. Computer Science
University of Somewhere, Somewhere, USA
2017

Skills
- Python
- JavaScript
- React

Certifications
- Certified Kubernetes Administrator
"""

parsed_resume = parse_resume(resume_text)
print(parsed_resume)
