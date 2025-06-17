# Email Verification App (Flask + SQLite + Docker)

A minimal, self-contained Python web app for user signup, email verification (mocked for local use), and login — all backed by SQLite and fully Dockerized.

---

## 🚀 Features

- Signup with email + password
- Email verification via token (mocked to console)
- SQLite for persistent storage
- Login disabled until user verifies
- Simple HTML forms (Flask templates)
- No external services required

---

## 🧱 Project Structure

```email_verification_app/
├── app.py # Main Flask app
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build instructions
├── templates/ # HTML templates
├── data/ # SQLite DB is stored here
├── build.sh # Build the Docker image
├── run.sh # Run the Docker container
├── clean.sh # Remove image and volumes
└── README.md
```

## ⚙️ Usage

### 1. Make Shell Scripts Executable (required once)

```bash
chmod +x build.sh run.sh clean.sh
```

###  2. Build the Docker Image

```bash ./build.sh```


###  3. Run the app

```bash ./run.sh```

###  4.Clean Up (Stop + Remove Container & Image)

```bash ./clean.sh```

## 🔐 Email Verification

This app does not send real emails — instead, it prints the verification link to the Docker console:

```📧 Mock verification email for user@example.com```
```🔗 Visit this URL to verify: http://localhost:5000/verify?token=...```

Copy and paste that into your browser to complete verification.

## 📝 License

MIT License

Copyright (c) 2025 Andrew G. Stanton

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...

## 🙏 Credits
Built with 💡 by Abdrew G. Staton w/ help from "Dr. C" (ChatGPT)  — inspired by Flask simplicity and Docker portability.

