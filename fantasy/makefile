clean:
	rm -f predict.txt
	rm -f thisseason.txt
	rm -f eliteseason.txt
	rm -f diff.txt
	rm -f *Stats.txt
	rm -f pg.txt
	rm -f sg.txt
	rm -f sf.txt
	rm -f pf.txt
	rm -f c.txt

predict: 
	python singleNexSeason.py > predict.txt

thisseason:
	python singleSeason.py > thisseason.txt

eliteseason:
	python eliteSingleSeason.py > eliteseason.txt

pg:
	python singlePG.py > pg.txt

sg:
	python singleSG.py > sg.txt

sf:
	python singleSF.py > sf.txt

pf:
	python singlePF.py > pf.txt

c:
	python singleC.py > c.txt

positions:
	python singlePG.py > pg.txt
	python singleSG.py > sg.txt
	python singleSF.py > sf.txt
	python singlePF.py > pf.txt
	python singleC.py > c.txt

compare:
	python compare.py > diff.txt

parse:
	python parseSeason.py

players:
	python calcTeam.py vicki
	python calcTeam.py dan
	python calcTeam.py alex
	python calcTeam.py john
	python calcTeam.py michael
	python calcTeam.py crystal
	python calcTeam.py kason
	python calcTeam.py elynn
	python calcTeam.py irvin
	python calcTeam.py paolo
	python calcTeam.py josh
	python calcTeam.py tomas
