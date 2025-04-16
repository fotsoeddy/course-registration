# 🎓 University Course Registration Platform

A Django + Tailwind CSS-based platform that helps universities manage student and teacher accounts, course registrations, result uploads, and academic notifications via email.

🔗 **Repository**: [https://github.com/fotsoeddy/course-registration](https://github.com/fotsoeddy/course-registration)

---

## 🚀 Features

### 👨‍🎓 Student
- Account registration with profile picture upload.
- Login with welcome email notification.
- Register for courses.
- View registered course results (CA + Exam).
- Download result in PDF format.
- View academic structure.
- Receive result publication email.
- Logout triggers goodbye email (with optional goodbye image).

### 👨‍🏫 Teacher
- Created by admin.
- Receives login credentials via email.
- Login and setup account.
- Create and manage courses.
- Upload student marks manually or via Excel file.
- View students registered in their courses.
- Log out.

### 🛡️ Admin
- Created via the terminal using the custom `KiteSuperUser` command.
- Logs in via the normal login form (`/login/`).
- Can create and manage teacher accounts.
- Has access to all student and teacher data.
- Can manage courses and upload marks.

---

## 🧰 Tech Stack

- **Backend**: Python 3.10, Django 4.x
- **Frontend**: Tailwind CSS
- **Database**: PostgreSQL (or SQLite for local testing)
- **Email**: Django Email Backend

---

## ⚙️ Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/fotsoeddy/course-registration.git
cd course-registration
```

### Step 2: Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup the Environment Variables

Create a `.env` file and add the following:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
EMAIL_HOST=email_host
EMAIL_PORT=email_port
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=University Admin <noreply@example.com>
```

> ⚠️ If using SQLite for local testing, you can skip `DATABASE_URL`.

### Step 5: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser via `KiteSuperUser`
```bash
python manage.py KiteSuperUser
```
You'll be prompted to input:
- Username
- Email
- Password

> ✅ After creation, the admin can log in via the normal login form.

### Step 7: Run the Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 👨‍🏫 Teacher Account Flow

1. Admin logs in and navigates to the **teacher creation section**.
2. When a teacher is created, their **login credentials are sent via email**.
3. Teacher logs in using those credentials.
4. Teacher can:
   - Create and manage courses.
   - Upload student marks manually or with an Excel file.
   - View registered students.
   - Update their account.
   - Log out.

> 📬 Students receive email notifications when marks are uploaded.

---

## 👨‍🎓 Student Account Flow

1. Student registers via the platform and uploads a profile picture.
2. Upon login, receives a **welcome email**.
3. Registers for courses.
4. Views CA and Exam results.
5. Downloads results in **PDF format**.
6. When logging out, receives a **goodbye email** (with optional image).
7. Gets email alerts when marks are uploaded by teachers.

---

## 📤 Excel Upload Feature

- Teachers can upload marks using a preformatted **Excel spreadsheet**.
- The system automatically updates the marks for the students.
- Students receive an **email notification** that marks have been published.

---

## 🧪 Run Tests

```bash
python manage.py test
```

---

## 🙋 Author

- **Jaime Josepha Namekong**
- GitHub: (https://github.com/namekongjosepha)

---

## 🙌 Acknowledgements



---

## 📝 License

MIT License – see the [LICENSE](LICENSE) file for details.

---