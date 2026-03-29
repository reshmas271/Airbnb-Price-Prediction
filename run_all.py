import os
import subprocess
import sys

def check_streamlit():
    """Check if Streamlit is installed, else install it."""
    try:
        import streamlit
    except ImportError:
        print("⚡ Streamlit not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])

def main():
    # 1️⃣ Ensure necessary folders exist
    os.makedirs("models", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    # 2️⃣ Check Streamlit is installed
    check_streamlit()

    # 3️⃣ Clean data
    print("\n🧹 Running data cleaning...")
    subprocess.run([sys.executable, "-m", "src.data_cleaning"], check=True)

    # 4️⃣ Train model
    print("\n🧠 Training model...")
    subprocess.run([sys.executable, "-m", "src.train"], check=True)

    # 5️⃣ Launch Streamlit app locally (headless, no login)
    print("\n🚀 Launching Streamlit app...")
    subprocess.run([
        "streamlit", "run", "app/app.py",
        "--server.headless", "true",
        "--browser.gatherUsageStats", "false"
    ])

if __name__ == "__main__":
    main()
