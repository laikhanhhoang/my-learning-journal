import os
import re

course_folder = "courses"

def make_anchor(text: str) -> str:
    # Chuyển heading thành anchor GitHub style
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = text.replace(' ', '-')
    return text

with open("README.md", "w", encoding="utf-8") as readme:
    readme.write("# All My Courses\n\n")

    # ===== PHẦN 1: Tạo Mục lục =====
    for filename in sorted(os.listdir(course_folder)):
        if filename.endswith(".md"):
            filepath = os.path.join(course_folder, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()

            # Tìm heading đầu tiên bắt đầu bằng ##
            title = filename.replace(".md", "").replace("_", " ")

            for line in lines:
                if line.startswith("## "):
                    title = line.replace("## ", "").strip()
                    break

            anchor = make_anchor(title)
            readme.write(f"- [{title}](#{anchor})\n")

    readme.write("\n---\n\n")

    # ===== PHẦN 2: Ghi toàn bộ nội dung file =====
    for filename in sorted(os.listdir(course_folder)):
        if filename.endswith(".md"):
            filepath = os.path.join(course_folder, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            readme.write(content + "\n\n")
