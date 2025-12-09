import os

course_folder = "courses"

# Mở file README.md ở chế độ 'w' (ghi đè toàn bộ)
# và giữ file mở cho đến khi tất cả các thao tác ghi hoàn thành.
with open("README.md", "w", encoding="utf-8") as readme:
    
    # 1. Ghi Header
    header = "# Tất cả các khóa học tôi đã học\n"
    readme.write(header) # readme là biến được mở và đang hoạt động

    # 2. Lặp qua các file trong thư mục 'courses'
    for filename in sorted(os.listdir(course_folder)):
        
        # Chỉ xử lý các file Markdown
        if filename.endswith(".md"):
            
            # Tạo đường dẫn đầy đủ đến file khóa học
            filepath = os.path.join(course_folder, filename)
            
            # Đọc nội dung file khóa học
            with open(filepath, "r", encoding="utf-8") as f: # Chế độ 'r' để đọc
                content = f.read()
            
            # 3. Ghi nội dung khóa học vào README.md
            # Thêm tiêu đề (nếu cần) và nội dung
            readme.write(f"\n## {filename.replace('.md', '').replace('_', ' ')}\n")
            readme.write(content + "\n\n") # Ghi nội dung và thêm dòng mới
            
# Khi ra khỏi khối 'with', README.md sẽ tự động được đóng và cập nhật.
