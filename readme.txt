Administration:
	Creators:
		Andrew Farley
		Joseph Grosso
		Kyle Singer
		Andrew Fryer

	Emails:
		andrew.farley@gmail.com
		Joe.grosso.cogeco@gmail.com
		kylesinger@rogers.com
		andrewtfryer@gmail.com

	Group:
		Team Carnation

	Project Title:
		Saving Ontario Energy

Code Location: 
	OEC_2020 ->
		venv -> (contains virtual environment)
			bin
			include
			lib
			pyvenv.cfg
		given-files -> (contains all given data)
			inputFile1.csv
			inputFile1.xlsx 
			inputFile2.csv
			inputFile2.xlsx
			inputFile3.csv
			inputFile3.xlsx
			OEC 2020 Programming Competition Package.pdf
			OEC_sample_format.xlsx
			OEC_sample_input.csv
			OEC_sample_ouput.csv
			System Volume Information ->
						IndexerVolumeGuid
						WPSettings.dat
		_pycache_ -> (pycharm IDE added info)
			GreedyAlgorithm.cpython-36.pyc
			helpers.cpython-36.pyc
			Input.cpython-36.pyc
			Output.cpython-36.pyc
		src -> (all source code for product)
			get_list_rankings.py
			GreedyAlgorithm.py
			helpers.py
			Input.py
			main.py
			Output.py
			test.csv (outputted data)
			Test.py
		outputs (will show excel outputs after running)
Compile & Run:
	To compile and run, follow the following commands below:
		git clone https://github.com/Andrew-Fryer/OEC_2020.git
		cd OEC_2020
		pip install pandas matplotlib
		cd src
		python main.py
	Go to outputs folder to see the outputted files.


External sources/libraries:
	We used Pandas and Matplotlib libraries to read and graph data respectively. Note 
	that these are large libraries that do not fit on a USB key.
