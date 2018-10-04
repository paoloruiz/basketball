// data from https://hashtagbasketball.com/fantasy-basketball-projections

// R#	PLAYER	POS	TEAM	GP	MPG	FG%	FT%	3PM	PTS	TREB	AST	STL	BLK	TO	TOTAL	$AV
const inputPlayers = '1	Anthony Davis	PF/C	NOR	72	36.0	0.52 (10.5/20.3)	0.83 (6.8/8.2)	0.7	28.5	11.3	2.6	1.4	2.4	2.3	15.93	71\n2	Stephen Curry	PG/SG	GSW	72	32.0	0.49 (8.2/16.7)	0.92 (5.1/5.6)	4.4	25.9	4.8	6.2	1.6	0.2	2.9	14.42	65\n3	James Harden	PG/SG	HOU	80	35.4	0.45 (8.8/19.8)	0.85 (8.3/9.7)	3.7	29.6	5.8	8.7	1.6	0.6	4.7	14.26	69\n4	Kevin Durant	SF/PF	GSW	67	34.0	0.51 (8.6/16.8)	0.89 (4.7/5.4)	2.6	24.6	6.7	5.2	0.8	1.6	2.8	13.76	59\n5	Karl-Anthony Towns	C	MIN	80	36.0	0.54 (9.0/16.6)	0.85 (4.5/5.3)	1.4	24.0	12.4	2.8	0.9	1.4	2.2	13.17	57\n6	Giannis Antetokounmpo	SF/PF	MIL	78	36.0	0.52 (9.9/19.0)	0.78 (6.6/8.4)	0.7	27.1	9.6	5.6	1.5	1.5	3.0	13.09	62\n7	Kawhi Leonard	SG/SF	TOR	70	34.0	0.48 (8.6/18.0)	0.87 (5.9/6.8)	2.0	25.1	6.5	3.6	1.7	0.9	2.1	11.67	54\n8	Nikola Jokic	PF/C	DEN	75	32.0	0.51 (7.0/13.8)	0.86 (3.8/4.4)	1.5	19.3	10.9	6.2	1.2	0.9	2.6	11.22	51\n9	LeBron James	SF/PF	LAL	75	36.0	0.52 (10.2/19.5)	0.71 (4.6/6.5)	1.7	26.7	8.6	9.2	1.3	0.7	4.2	10.83	55\n10	Damian Lillard	PG	POR	74	36.0	0.44 (8.5/19.3)	0.91 (6.6/7.2)	3.1	26.6	4.5	6.4	1.0	0.3	2.7	10.24	46\n11	Joel Embiid	PF/C	PHI	58	31.0	0.48 (8.4/17.4)	0.78 (6.7/8.5)	1.4	24.8	11.1	3.5	0.8	2.0	4.0	9.67	47\n12	Chris Paul	PG	HOU	63	31.5	0.46 (5.8/12.7)	0.91 (3.5/3.8)	2.4	17.5	5.4	7.7	1.7	0.2	2.2	9.41	43\n13	Kyrie Irving	PG/SG	BOS	60	32.0	0.48 (8.9/18.3)	0.91 (4.0/4.4)	2.8	24.6	3.5	5.4	1.0	0.3	2.3	9.23	41';

const formattedPlayers = inputPlayers.split('\n').map((row) => {
	const cols = row.split('\t');
  return {
  	player: cols[1],
    position: cols[2],
    fgp: cols[6].split(' ')[0],
    fgma: cols[6].split(' ')[1],
    ftp: cols[7].split(' ')[0],
    ftma: cols[7].split(' ')[1],
    tpm: cols[8],
    pts: cols[9],
    reb: cols[10],
    ast: cols[11],
    stl: cols[12],
    blk: cols[13],
    tos: cols[14]
  };
});



document.getElementById('out').innerHTML = formattedPlayers.reduce((a, p) => a + p.fgma, '');
