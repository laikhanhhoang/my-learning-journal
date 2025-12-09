import os

header = "# All Courses I Take\n\n"

course_folder = "courses"

with open("README.md", "w", encoding="utf-8") as readme:
    readme.write(header)
    
    for filename in sorted(os.listdir(course_folder)):
        if filename.endswith(".md"):
            with open(os.path.join(course_folder, filename), "r", encoding="utf-8") as f:
                content = f.read()
                readme.write(content + "\n\n")
