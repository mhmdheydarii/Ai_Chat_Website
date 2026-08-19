<section style="max-width:700px; margin:auto; font-family:Arial, sans-serif; line-height:1.7; color:#333;">
  <h1 style="text-align:center; color:#2c3e50;">Django Ai Chat</h1>
  

  <p align="center">
  <img src="./docs/chat.png" width="700"/>
  </p>
</section>

<h2>About</h2>
<p>A web-based AI chat application built with Python, Django, and the OpenAI API.
Users can chat with AI, view their chat history, and delete previous conversations.</p>


<h2>Features</h2>
<ul>
  <li> Session Authentication</li>
  <li> Role-Based Permissions</li>
  <li> Admin Dashboard</li>
  <li> Chat History</li>
</ul>


<h2>Technologies</h2>
<ul>
  <li> Python</li>
  <li> Django</li>
  <li> Postgres</li>
  <li> OpenAI API</li>
  <li> HTML, CSS, JavaScript</li>
</ul>


<h2>⚙️ Installation (Windows)</h2>

<p>Follow these steps to set up and run the project locally.</p>

<hr>

<h3>1. Clone the repository</h3>

```bash
git clone https://github.com/mhmdheydarii/Ai_Chat_Website.git
```

<br>

<h3>2. Navigate to the project directory</h3>

```bash
cd Ai_Chat_Website
```

<br>

<h3>3. Create a virtual environment</h3>

```bash
python -m venv .venv
```

<br>

<h3>4. Activate the virtual environment</h3>

<p><b>CMD</b></p>

```cmd
.venv\Scripts\activate
```

<p><b>PowerShell</b></p>

```powershell
.\.venv\Scripts\Activate.ps1
```

<p>
After activation, you should see something similar to:
</p>

```bash
(.venv)
```

<p>
at the beginning of your terminal line.
</p>

<br>

<h3>5. Install dependencies</h3>

<p>If the project includes a <code>requirements.txt</code> file:</p>

```bash
pip install -r requirements.txt
```

<br>

<h3>6. Configure environment variables</h3>

<p>Create a .env file in the project root and add the required environment variables.</p>

```bash
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-api-key

DB
NAME=db-name
USER=db-user
PASSWORD-db-password
HOST=db-hose
PORT=db-port

SMTP
EMAIL_USER=your email address
EMAIL_PASSWORD=your email password
```
</br>
<h3>7. Run the project</h3>


```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```

<hr>

<details>
<summary><b>❌ Deactivate Virtual Environment</b></summary>

<br>

To exit the virtual environment:

```bash
deactivate
```

</details>

<br>

<p align="center">
⭐ If you found this project useful, consider giving it a star.
</p>
