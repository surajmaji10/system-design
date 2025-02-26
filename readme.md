#### Install these:
```bash
sudo apt update && sudo apt upgrade
git clone <url> sys-des
cd sys-des
sudo apt install python3 python3-venv python3-pip
python3 -m venv .myvenv
source .myvenv/bin/activate
pip3 install -r requirements
```

Run it on the cmd line: (not backgrouded)\
`
uvicorn file:app --reload --host=0.0.0.0
`