import os
import uuid
import requests
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

print("🟢 Flask app loaded")

os.makedirs('data', exist_ok=True)

print("✅ Ensured 'data' directory exists:", os.path.abspath("data"))
print("📄 Files in /app/data:", os.listdir("data") if os.path.exists("data") else "MISSING")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app/data/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    token = db.Column(db.String(64), unique=True)

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY", "test-key")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN", "test-domain")

def send_verification_email(email, token):
    verify_link = f"http://localhost:5000/verify?token={token}"
    print(f"📧 Mock verification email for {email}")
    print(f"🔗 Visit this URL to verify: {verify_link}")

@app.route('/')
def home():
    print("🟢 Home page hit")
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        if User.query.filter_by(email=email).first():
            return render_template('signup.html', error="Email already registered")
        token = str(uuid.uuid4())
        user = User(email=email, password_hash=generate_password_hash(password), token=token)
        db.session.add(user)
        db.session.commit()
        print("📨 About to send mock email...")
        print("token: ", token)
        send_verification_email(email, token)
        return render_template('message.html', message="Signup successful. Check email to verify.")
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            return render_template('login.html', error="Invalid credentials")
        if not user.verified:
            return render_template('login.html', error="Please verify your email first")
        return render_template('message.html', message="Login successful!")
    return render_template('login.html')

@app.route('/verify')
def verify():
    token = request.args.get("token")
    user = User.query.filter_by(token=token).first()
    if user:
        user.verified = True
        user.token = None
        db.session.commit()
        return render_template('message.html', message="Email verified successfully.")
    return render_template('message.html', message="Invalid or expired token.")

if __name__ == '__main__':
    with app.app_context():
        print("📦 Creating DB at:", app.config['SQLALCHEMY_DATABASE_URI'])
        db.create_all()
    app.run(debug=True, host="0.0.0.0")