cd /Users/amin/Projects/jalali-year-progress
source $(pipenv --venv | awk '{print $1"/bin/activate"}')
export $(grep -v '^#' .env | xargs)
python main.py
