1. Run stroop_practice.py
	stroop_practice.py will call \bin\trialGen.py and output 3 files 
	"trials_stroop.csv."
	"trials_memory.csv"
	"trials_practice.csv"
	"respMapping.txt"
	This file contains subject specific trial sequences.
	But this file will be overwritten each time stroop_practice.py is ran.
	After running Stroop.py, it will output \data\stroop_practice_xx.csv [xx=subject #]
2. Run stroop.py, this will use trials_stroop.csv and respMapping.txt
	It will output \data\stroop_xx.csv [xx = subject #]
3. Run filler.py
	filler.py will call \in\issp_trialGen.py and output a "trials_issp.csv"
	It will output \data\filler_xx.csv
3. Thirdly, run memory.py
	It will use trial sequences generated in "trial_memory.csv"
	It will output \data\memory_xx.csv
	* Right now, each image is presented for 2.5 second and won't disapper even a response is made
4. Finally, run sourceMem.py
	It will use "trials_sourceMem.csv"
	It will output \data\sourceMem_xx.csv

tone1 = 400Hz.wav (0.01) volume
tone2 = 400Hz.wav (0.00) volume