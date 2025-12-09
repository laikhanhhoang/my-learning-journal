import os

course_folder = "courses"

with open("README.md", "w", encoding="utf-8") as readme:
    readme.write("# All My Courses\n\n")

    for filename in sorted(os.listdir(course_folder)):
        if filename.endswith(".md"):
            filepath = os.path.join(course_folder, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Chỉ ghi nội dung, KHÔNG ghi tên file
            readme.write(content + "\n\n")
