resume_data = {
    "Personal Information": {
        "Name": "Jon Doe",
        "Email": "email@domain.com",
        "Phone": "(123) 456-7890",
        "Address": "City, ST",
        "LinkedIn": "linkedin.com/in/jondoe",
        "GitHub": "github.com/jondoe"
    },
    "Education": {
        "grad": {
            "School": "Some University",
            "Address": "City, ST",
            "Dates": "September 2021 - Expected May 2023",
            "Degree": "Master of Science",
            "Major": "Computer Science",
            "GPA": "4.0",
            "Relevant Courses": [
                "Data Structures and Algorithms",
                "Copmputer Architecture",
                "Operating Systems"
            ]
        },
        "undergrad": {
            "School": "",
            "Address": "",
            "Dates": "",
            "Degree": "",
            "Major": "",
            "GPA": "",
            "Relevant Courses": [
                "",
                "",
                ""
            ]
        }
    },
    "Work Experience": {
        "company1": {
            "Company": "Company 1",
            "Address": "City, ST",
            "Dates": "May 2021 - August 2021",
            "Job Title": "Software Development Intern",
            "Skills": [
                "Python",
                "React",
                "Django",
                "PostgreSQL",
                "Docker",
                "Jenkins"
            ],
            "Bullets": [
                "Developed a web application using React, Django, and PostgreSQL to display data from a REST API",
                "Created a Python script to automate the process of generating a report from a database",
                "Implemented a Docker container to run a Jenkins pipeline to build and deploy the web application"
            ]
        },
        "company2": {
            "Company": "",
            "Address": "",
            "Dates": "",
            "Job Title": "",
            "Skills": [
                "",
                "",
                ""
            ],
            "Bullets": [
                "",
                "",
                ""
            ]
        }
    },
    "Skills": {
        "Programming Languages": [
            "Javascript",
            "Python",
            "Java",
            "SQL",
            "C#"
        ],
        "Frontend Development": [
            "React",
            "Angular",
            "Vue.js",
            "jQuery"
        ],
        "Backend Development": [
            "Node.js",
            "Express.js",
            "ASP.NET",
            "Flask",
            "Django"
        ],
        "Databases": [
            "Oracle",
            "MySQL",
            "MongoDB",
            "PostgreSQL"
        ],
        "Tools": [
            "Git",
            "Docker",
            "Jenkins",
            "Jira",
            "Confluence"
        ],
        "Operating Systems": [
            "Windows",
            "Linux",
            "MacOS"
        ]
    },
    "Projects": {
        "project1": {
            "Name": "Resume Builder",
            "Organization": "some organization",
            "Dates": "October 2018 - December 2019",
            "GitHub": "https://github.com/jondoe/test-project",
            "Bullets": [
                "Developed a web application using React, Node.js, and MongoDB to generate a resume",
                "Implemented a REST API to store and retrieve resume data from a database",
                "Created a Python script to automate the process of generating a report from a database"
            ],
            "Skills": [
                "React",
                "Node.js",
                "MongoDB",
                "Python"
            ]
        },
        "project2": {
            "Name": "",
            "Organization": "",
            "Dates": "",
            "GitHub": "",
            "Bullets": [],
            "Skills": []
        }
    }
}

# Generate a Mardown file from the resume data that is formatted so that it looks like a typical resume
# Path: resume-builder.py

def generate_resume(resume_data):
    # Create a new Markdown file
    resume_file = open("resume.md", "w")

    # Write the resume header
    resume_file.write("# " + resume_data["Personal Information"]["Name"] + "\n")
    resume_file.write(resume_data["Personal Information"]["Email"] + " | " + resume_data["Personal Information"]["Phone"] + " | " + resume_data["Personal Information"]["Address"] + "\n")
    resume_file.write("[LinkedIn](" + resume_data["Personal Information"]["LinkedIn"] + ") | [GitHub](" + resume_data["Personal Information"]["GitHub"] + ")\n\n")

    # Write the education section
    resume_file.write("## Education\n\n")
    resume_file.write("### " + resume_data["Education"]["grad"]["School"] + "\n")
    resume_file.write(resume_data["Education"]["grad"]["Address"] + " | " + resume_data["Education"]["grad"]["Dates"] + "\n")
    resume_file.write(resume_data["Education"]["grad"]["Degree"] + " in " + resume_data["Education"]["grad"]["Major"] + " | GPA: " + resume_data["Education"]["grad"]["GPA"] + "\n")
    resume_file.write("Relevant Courses: " + ", ".join(resume_data["Education"]["grad"]["Relevant Courses"]) + "\n\n")

    resume_file.write("### " + resume_data["Education"]["undergrad"]["School"] + "\n")
    resume_file.write(resume_data["Education"]["undergrad"]["Address"] + " | " + resume_data["Education"]["undergrad"]["Dates"] + "\n")
    resume_file.write(resume_data["Education"]["undergrad"]["Degree"] + " in " + resume_data["Education"]["undergrad"]["Major"] + " | GPA: " + resume_data["Education"]["undergrad"]["GPA"] + "\n")
    resume_file.write("Relevant Courses: " + ", ".join(resume_data["Education"]["undergrad"]["Relevant Courses"]) + "\n\n")

    # Write the work experience section
    resume_file.write("## Work Experience\n\n")
    resume_file.write("### " + resume_data["Work Experience"]["company1"]["Company"] + "\n")
    resume_file.write(resume_data["Work Experience"]["company1"]["Address"] + " | " + resume_data["Work Experience"]["company1"]["Dates"] + "\n")
    resume_file.write(resume_data["Work Experience"]["company1"]["Job Title"] + "\n")
    resume_file.write("Skills: " + ", ".join(resume_data["Work Experience"]["company1"]["Skills"]) + "\n")
    resume_file.write("Bullets:\n")
    for bullet in resume_data["Work Experience"]["company1"]["Bullets"]:
        resume_file.write("* " + bullet + "\n")
    resume_file.write("\n")
    
    resume_file.write("### " + resume_data["Work Experience"]["company2"]["Company"] + "\n")
    resume_file.write(resume_data["Work Experience"]["company2"]["Address"] + " | " + resume_data["Work Experience"]["company2"]["Dates"] + "\n")
    resume_file.write(resume_data["Work Experience"]["company2"]["Job Title"] + "\n")
    resume_file.write("Skills: " + ", ".join(resume_data["Work Experience"]["company2"]["Skills"]) + "\n")
    resume_file.write("Bullets:\n")
    for bullet in resume_data["Work Experience"]["company2"]["Bullets"]:
        resume_file.write("* " + bullet + "\n")
    resume_file.write("\n")
    
    # Write the skills section
    resume_file.write("## Skills\n\n")
    for skill in resume_data["Skills"]:
        resume_file.write("### " + skill + "\n")
        resume_file.write(", ".join(resume_data["Skills"][skill]) + "\n\n")
        
    # Write the projects section
    resume_file.write("## Projects\n\n")
    resume_file.write("### " + resume_data["Projects"]["project1"]["Name"] + "\n")
    resume_file.write(resume_data["Projects"]["project1"]["Organization"] + " | " + resume_data["Projects"]["project1"]["Dates"] + "\n")
    resume_file.write("Skills: " + ", ".join(resume_data["Projects"]["project1"]["Skills"]) + "\n")
    resume_file.write("Bullets:\n")
    for bullet in resume_data["Projects"]["project1"]["Bullets"]:
        resume_file.write("* " + bullet + "\n")
    resume_file.write("\n")
    
    resume_file.write("### " + resume_data["Projects"]["project2"]["Name"] + "\n")
    resume_file.write(resume_data["Projects"]["project2"]["Organization"] + " | " + resume_data["Projects"]["project2"]["Dates"] + "\n")
    resume_file.write("Skills: " + ", ".join(resume_data["Projects"]["project2"]["Skills"]) + "\n")
    resume_file.write("Bullets:\n")
    for bullet in resume_data["Projects"]["project2"]["Bullets"]:
        resume_file.write("* " + bullet + "\n")
    resume_file.write("\n")
    
    # Close the file
    resume_file.close()
    
generate_resume(resume_data)