import os, logging, subprocess

if not os.path.exists("crash.txt"):
    subprocess.run(["touch", "crash.txt"])
    with open("crash.txt", "r+") as a:
        a.truncate(0)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("crash.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

UPSTREAM_REPO_URL = os.getenv("UPSTREAM_REPO_URL", "https://github.com/BianSepang/WeebProject")
BRANCH = os.getenv("UPSTREAM_BRANCH", "master")

if UPSTREAM_REPO_URL is not None:
    if os.path.exists(".git"):
        subprocess.run(["rm", "-rf", ".git"])
    start = subprocess.run(
        [
          f"git init -q \
                   && git config --global user.email jiz@linuxmail.com \
                   && git config --global user.name cokwibu \
                   && git add . \
                   && git commit -sm start -q \
                   && git remote add origin {UPSTREAM_REPO_URL} \
                   && git fetch origin -q \
                   && git reset --hard origin/{BRANCH} -q"
        ],
        shell=True,
    )
    if start.returncode == 0:
        logging.info(f"Successfully update from upstream repo with > {UPSTREAM_REPO_URL} {BRANCH}")
    else:
        logging.error("Something gonna wrong!")