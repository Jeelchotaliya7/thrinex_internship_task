@echo off

echo ==========================
echo DATA PIPELINE STARTING
echo ==========================

cd /d %~dp0scripts

echo Running Data Cleaning...
python data_cleaning.py

echo Running Report Generation...
python report_generation.py

echo ==========================
echo PIPELINE COMPLETED
echo ==========================

pause