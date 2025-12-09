import os

course_folder = "courses"

with open("README.md", "w", encoding="utf-8") as readme:
    
    header = "# All My Courses \n"
    readme.write(header) # readme là biến được mở và đang hoạt động

    for filename in sorted(os.listdir(course_folder)):
        
        if filename.endswith(".md"):
            
            filepath = os.path.join(course_folder, filename)
            
            with open(filepath, "r", encoding="utf-8") as f: # Chế độ 'r' để đọc
                content = f.read()
            
            readme.write(content + "\n\n") # Ghi nội dung và thêm dòng mới
            
