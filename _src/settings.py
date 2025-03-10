"""
Application Settings
"""

from pathlib import Path

# base directory for application
BASE_DIR = Path(__file__).resolve().parent.parent

# dev/prod mode (if needed)
APP_VERSION = "1.0.0"
DEBUG = False

# database path
DATABASE_PATH = BASE_DIR / "youtube_tutorials.db"

# py template directory
PY_TEMPLATES_DIR = BASE_DIR / "py_templates"

# reserved name
CONTRIBUTOR_RESERVED_USERNAMES = ["admin", "superuser", "administrator", "root"]
MAX_NUM_CONTRIBUTOR = 50

# tutorials
MAX_NUM_TUTORIALS = 250

# admin user name
ADMIN_USER = "endangismaya"

# messages
WELCOME_MESSAGES = {
    "English": "Welcome",
    "Spanish": "Bienvenido",
    "French": "Bienvenue",
    "German": "Willkommen",
    "Japanese": "ようこそ (Yōkoso)",
    "Chinese (Simplified)": "欢迎 (Huānyíng)",
    "Arabic": "أهلاً وسهلاً (ʾahlan wa-sahlan)",
    "Hindi": "स्वागत (Svāgat)",
    "Russian": "Добро пожаловать (Dobro pozhalovat')",
    "Portuguese": "Bem-vindo",
    "Italian": "Benvenuto",
    "Korean": "환영합니다 (Hwan-yeonghamnida)",
    "Swahili": "Karibu",
    "Dutch": "Welkom",
    "Swedish": "Välkommen",
    "Turkish": "Hoş geldiniz",
    "Vietnamese": "Chào mừng",
    "Indonesian": "Selamat datang",
}

THANK_YOU_MESSAGES = {
    "English": "Thank You",
    "Spanish": "Gracias",
    "French": "Merci",
    "German": "Danke",
    "Japanese": "ありがとうございます (Arigatō gozaimasu)",
    "Chinese (Simplified)": "谢谢 (Xièxie)",
    "Arabic": "شكراً (Shukran)",
    "Hindi": "धन्यवाद (Dhanyavād)",
    "Russian": "Спасибо (Spasibo)",
    "Portuguese": "Obrigado",
    "Italian": "Grazie",
    "Korean": "감사합니다 (Gamsahamnida)",
    "Swahili": "Asante",
    "Dutch": "Dank u",
    "Swedish": "Tack",
    "Turkish": "Teşekkür ederim",
    "Vietnamese": "Cảm ơn",
    "Indonesian": "Terima kasih",
}
