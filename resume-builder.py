import json

def generate_resume(json_file, output_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Initialize the resume markdown string
    resume_md = ''
    
    # Personal Information section
    personal_info = data.get('Personal Information')
    if personal_info:
        resume_md += '## Personal Information\n\n'
        for key, value in personal_info.items():
            resume_md += f"- **{key}:** {value}\n"
        resume_md += '\n'
    
    # Education section
    education = data.get('Education')
    if education:
        resume_md += '## Education\n\n'
        for key, value in education.items():
            resume_md += f"### {key.capitalize()}\n\n"
            for field, field_value in value.items():
                if field == 'Relevant Courses':
                    resume_md += f"- **{field}:**\n"
                    for course in field_value:
                        resume_md += f"  - {course}\n"
                else:
                    resume_md += f"- **{field}:** {field_value}\n"
            resume_md += '\n'
    
    # Work Experience section
    work_experience = data.get('Work Experience')
    if work_experience:
        resume_md += '## Work Experience\n\n'
        for key, value in work_experience.items():
            resume_md += f"### {value['Job Title']}\n\n"
            resume_md += f"- **Company:** {value['Company']}\n"
            resume_md += f"- **Address:** {value['Address']}\n"
            resume_md += f"- **Dates:** {value['Dates']}\n"
            resume_md += '- **Skills:**\n'
            for skill in value['Skills']:
                resume_md += f"  - {skill}\n"
            resume_md += '- **Responsibilities:**\n'
            for bullet in value['Bullets']:
                resume_md += f"  - {bullet}\n"
            resume_md += '\n'
    
    # Skills section
    skills = data.get('Skills')
    if skills:
        resume_md += '## Skills\n\n'
        for category, category_skills in skills.items():
            resume_md += f"### {category}\n\n"
            for skill in category_skills:
                resume_md += f"- {skill}\n"
            resume_md += '\n'
    
    # Projects section
    projects = data.get('Projects')
    if projects:
        resume_md += '## Projects\n\n'
        for key, value in projects.items():
            resume_md += f"### {value['Name']}\n\n"
            resume_md += f"- **Organization:** {value['Organization']}\n"
            resume_md += f"- **Dates:** {value['Dates']}\n"
            resume_md += f"- **GitHub:** [{value['GitHub']}]({value['GitHub']})\n"
            resume_md += '- **Skills:**\n'
            for skill in value['Skills']:
                resume_md += f"  - {skill}\n"
            resume_md += '- **Responsibilities:**\n'
            for bullet in value['Bullets']:
                resume_md += f"  - {bullet}\n"
            resume_md += '\n'
    
    # Save the resume to a file
    with open(output_file, 'w') as file:
        file.write(resume_md)

# Usage example
json_file = 'resume_data.json'
output_file = 'resume.md'
generate_resume(json_file, output_file)
print(f"Resume saved to {output_file}")
