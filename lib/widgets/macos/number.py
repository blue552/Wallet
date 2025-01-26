def write_notes_to_txt(file_path, notes):
    """
    Ghi danh sách ghi chú vào tệp .txt, phân loại ghi chú (ví dụ: Public, Private).

    Args:
        file_path (str): Đường dẫn đến file .txt.
        notes (list of tuple): Danh sách các ghi chú, mỗi ghi chú là một tuple (type, content).
                               - type: Loại ghi chú ('Public', 'Private', v.v.)
                               - content: Nội dung ghi chú.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for note_type, note_content in notes:
                file.write(f"[{note_type}] {note_content}\n")
        print(f"Ghi chú đã được lưu vào file: {file_path}")
    except Exception as e:
        print(f"Lỗi: {e}")


# Danh sách ghi chú
notes = [
    ("Public", "This is a public note for everyone to see."),
    ("Private", "47ac4832356f2716eb8cec6a507227cd71bf39291323abcbce0ccddf3131bf01"),
    ("Public", "General information about the project."),
    ("Private", "Sensitive data: Do not share externally."),
]

# Đường dẫn tới file .txt
file_path = "notes.txt"

# Ghi ghi chú vào file
write_notes_to_txt(file_path, notes)
