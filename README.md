

---

🧹 System Housekeeping

Tools for scanning a system for large files, unused files, and general storage housekeeping. These scripts are designed to be lightweight, portable, and executable directly from GitHub without cloning the repository.

---

🚀 Overview

This repository provides two Bash-based diagnostic tools:

• large-files.sh — identifies files larger than a user‑specified size
• unused-files.sh — identifies files not accessed in a user‑specified number of days


These scripts work on:

• Linux
• macOS
• WSL (Windows Subsystem for Linux)
• Git Bash / MSYS2
• Any POSIX‑compatible shell environment


You can run them locally or directly from GitHub using curl.

---

📁 Scripts Included

1. `large-files.sh`

Scan a directory for files larger than a given size (in MB).

Usage

./large-files.sh <size-in-MB> <path>


Example

./large-files.sh 100 /mnt/c


This scans the Windows C: drive (via WSL) for files larger than 100 MB.

---

2. `unused-files.sh`

Scan a directory for files not accessed in a given number of days.

Usage

./unused-files.sh <days> <path>


Example

./unused-files.sh 90 /mnt/c


This finds files not accessed in 90 days.

---

🌐 Running Scripts Directly From GitHub

You do not need to clone this repository.
You can execute the scripts remotely using curl and Bash process substitution.

---

▶️ Run the Large File Scanner

bash <(curl -s https://raw.githubusercontent.com/ProjectLaunchPadLLC/System-housekeeping-/main/scripts/large-files.sh) 100 /mnt/c


This:

• downloads the script directly from GitHub
• runs it immediately
• scans /mnt/c
• finds files larger than 100 MB


---

▶️ Run the Unused File Scanner

bash <(curl -s https://raw.githubusercontent.com/ProjectLaunchPadLLC/System-housekeeping-/main/scripts/unused-files.sh) 90 /mnt/c


This:

• downloads the script
• runs it
• scans /mnt/c
• finds files not accessed in 90 days


---

🔄 Optional: Auto‑Updating Wrapper

You can run both tools at once using a wrapper script:

bash <(curl -s https://raw.githubusercontent.com/ProjectLaunchPadLLC/System-housekeeping-/main/run-storage-tools.sh)


This wrapper:

• fetches the latest versions of both scripts
• runs them with default parameters
• requires no installation
• always stays up to date


---

🛠 Requirements

These scripts rely only on standard POSIX tools:

• bash
• find
• sort
• curl (for remote execution)


All major Linux distros, macOS, WSL, and Git Bash include these by default.

---

📜 License

You may include any license you prefer (MIT recommended for open-source scripts).

---

❓ Support

If you encounter issues or want to request enhancements, open an issue in this repository.

---



Just tell me what you want next — or tap expand README or add more scripts.
