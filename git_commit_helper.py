import pyperclip
import os
from datetime import datetime

def get_commit_message():
    print("Masukkan pesan commit (gunakan enter untuk baris baru, ketik 'DONE' untuk selesai):")
    
    # Menampung pesan commit dalam list
    commit_message_lines = []
    
    while True:
        line = input()  # Membaca baris input
        if line.strip().upper() == 'DONE':  # Mengakhiri input jika pengguna mengetik 'DONE'
            break
        commit_message_lines.append(line)
    
    # Gabungkan baris-baris input menjadi satu string dengan baris baru di antaranya
    commit_message = "\n".join(commit_message_lines)
    return commit_message

def save_log_to_file(commit_message):
    # Membuat folder logs jika belum ada
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Menentukan nama file log berdasarkan waktu saat commit
    now = datetime.now()
    log_filename = now.strftime("logs/commit_log_%Y-%m-%d_%H-%M-%S.txt")
    
    # Menulis pesan commit dan perintah Git ke file log dengan encoding utf-8
    with open(log_filename, 'w', encoding='utf-8') as log_file:
        log_file.write(f"Pesan Commit yang Anda Masukkan:\n{commit_message}\n\n")
        log_file.write("Template Perintah Git untuk Commit dan Push:\n")
        log_file.write(f"git add .\n")
        log_file.write(f"git commit -m \"{commit_message}\"\n")
        log_file.write(f"git remote -v\n")
        log_file.write(f"git push origin main\n")
    
    print(f"Log telah disimpan di: {log_filename}")

def display_commit_commands(commit_message):
    # Menyusun template perintah Git
    git_commands = f"""
git add .
git commit -m "{commit_message}"
git remote -v
git push origin main
"""
    
    # Menampilkan pesan commit dan perintah git
    print(f"\nPesan Commit yang Anda Masukkan:")
    print(commit_message)

    print("\nTemplate Perintah Git untuk Commit dan Push:")
    print(git_commands)
    
    # Menyalin perintah Git ke clipboard
    pyperclip.copy(git_commands)
    print("\nPerintah Git telah disalin ke clipboard!")

def main():
    # Meminta pesan commit dari pengguna
    commit_message = get_commit_message()

    # Menyimpan log ke file
    save_log_to_file(commit_message)

    # Menampilkan pesan commit dan perintah Git
    display_commit_commands(commit_message)

if __name__ == "__main__":
    main()
import pyperclip
import os
from datetime import datetime

def get_commit_message():
    print("Masukkan pesan commit (gunakan enter untuk baris baru, ketik 'DONE' untuk selesai):")
    
    commit_message_lines = []
    
    while True:
        line = input()
        if line.strip().upper() == 'DONE':
            break
        commit_message_lines.append(line)
    
    commit_message = "\n".join(commit_message_lines)
    return commit_message

def save_log_to_file(commit_message):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    now = datetime.now()
    log_filename = now.strftime("logs/commit_log_%Y-%m-%d_%H-%M-%S.txt")
    
    with open(log_filename, 'w', encoding='utf-8') as log_file:
        log_file.write(f"Pesan Commit yang Anda Masukkan:\n{commit_message}\n\n")
        log_file.write("Template Perintah Git untuk Commit dan Push:\n")
        log_file.write(f"git add .\n")
        log_file.write(f"git commit -m \"{commit_message}\"\n")
        log_file.write(f"git remote -v\n")
        log_file.write(f"git push origin main\n")
    
    print(f"Log telah disimpan di: {log_filename}")
    return log_filename

def display_commit_commands(commit_message, log_filename):
    git_commands = f"""
git add .
git commit -m "{commit_message}"
git remote -v
git push origin main
"""
    
    print(f"\nPesan Commit yang Anda Masukkan:")
    print(commit_message)

    print("\nTemplate Perintah Git untuk Commit dan Push:")
    print(git_commands)
    
    pyperclip.copy(git_commands)
    print("\nPerintah Git telah disalin ke clipboard!")
    print(f"Log telah disimpan di: {log_filename}")

def main():
    commit_message = get_commit_message()
    log_filename = save_log_to_file(commit_message)
    display_commit_commands(commit_message, log_filename)

if __name__ == "__main__":
    main()