1. Need to set machine volume to "50" (otherwise the setting volume in Psychopy won't work..)
2. Open up Psychopy
3. Run Stroop_practice.py  (16 trials) 
4. Run Stroop.py (160 trials/repetition x2 or x4) [a total of 9 mins for x2]
5. Run filler.py (208 trials) [a total of 8 mins]
6. Run memory.py (240 trials) [a total of 12 mins]
7. Run sourceMem.py (160 trials)  [a total of 8 mins]


Notes - 
stroop_practice.py will call \bin\trialGen.py and output 4 files 
"trials_practice.csv"
"trials_stroop.csv."
"trials_memory.csv"
"trials_sourceMem.csv"

After running experiment, each subject will have
(1) stroop_xxx.csv
(2) filler_xxx.csv
(3) memory_xxx.csv
(4) sourceMem_xxx.csv

tone1 = 400Hz.wav (0.01) volume
tone2 = 400Hz.wav (0.00) volume


For stroop task's volume it's set to 0.25 of the machine volume [50% *.25] in the script
For memory task's volume it's set to 0.5 of the machine volume [50% *.5] in the script