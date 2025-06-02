


# Quickstart Guide

## 1. Set Up the Python Environment

```bash
venv\Scripts\activate
source venv/bin/activate

pip install -r requirements.txt
```

---

## 2. Run Setup

Prepare everything (tables, data, vectorstores):

```bash
python main.py prompter setup
```

---

## 3. Send Prompts

By default, 30 prompts are sent.
To send a custom number, add it at the end:

```bash
# Default (30 prompts):
python main.py prompter run

# Custom (e.g., 5000 prompts):
python main.py prompter run 5000
```

---

## 4. Collect Results

Generate a report of your experiment:

```bash
python main.py result report
```


