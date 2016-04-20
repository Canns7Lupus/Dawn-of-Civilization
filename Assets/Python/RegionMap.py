from Consts import *

(iNone, iMinority, iPeriphery, iHistorical, iCore) = range(5)

def getMapValue(x, y):
	return tRegionMap[iWorldY-1-y][x]
	
def getSpreadFactor(iReligion, x, y):
	iRegion = gc.getMap().plot(x, y).getRegionID()
	if iRegion < 0: return -1
	
	for iFactor in tSpreadFactors[iReligion].keys():
		if iRegion in tSpreadFactors[iReligion][iFactor]:
			return iFactor
	
	return iNone
	
def updateRegionMap():
	for x in range(iWorldX):
		for y in range(iWorldY):
			gc.getMap().plot(x, y).setRegionID(getMapValue(x, y))
			
def updateReligionSpread():
	for x in range(iWorldX):
		for y in range(iWorldY):
			for iReligion in range(iNumReligions):
				gc.getMap().plot(x, y).setSpreadFactor(iReligion, getSpreadFactor(iReligion, x, y))
				
def init():
	updateRegionMap()
	updateReligionSpread()
				

tRegionMap = (
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	29,	-1,	29,	29,	29,	29,	29,	-1,	29,	-1,	29,	29,	29,	29,	29,	-1,	-1,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	6,	6,	6,	6,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	29,	29,	-1,	-1,	-1,	29,	-1,	-1,	29,	-1,	-1,	29,	29,	-1,	-1,	-1,	-1,	-1,	5,	5,	5,	5,	5,	5,	5,	5,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	6,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	23,	23,	23,	23,	23,	23,	23,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	30,	30,	-1,	-1,	-1,	29,	29,	29,	29,	-1,	-1,	29,	29,	-1,	-1,	29,	-1,	29,	-1,	-1,	-1,	-1,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	5,	5,	5,	5,	5,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	5,	5,	5,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	6,	6,	-1,	-1,	-1,	-1,	-1,	-1,	23,	-1,	23,	23,	23,	23,	23,	23,	23,	23,	23,	-1,	-1,	-1,	-1,	23,	23,	23,	-1,	-1,	-1,	23,	23,	23,	23,	-1,	23,	23,	23,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	30,	30,	30,	30,	29,	-1,	-1,	29,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	29,	-1,	-1,	-1,	-1,	29,	29,	29,	29,	-1,	-1,	-1,	5,	5,	5,	5,	5,	-1,	5,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	5,	5,	5,	5,	5,	5,	5,	-1,	-1,	-1,	-1,	-1,	-1,	6,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	23,	-1,	23,	23,	23,	23,	23,	23,	-1,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	-1,	-1,	-1,	-1),
(	23,	-1,	-1,	-1,	-1,	-1,	-1,	30,	30,	30,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	-1,	-1,	29,	29,	-1,	-1,	-1,	-1,	29,	29,	-1,	29,	-1,	-1,	-1,	5,	5,	5,	5,	5,	-1,	-1,	5,	5,	5,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	6,	-1,	6,	6,	6,	-1,	23,	-1,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23),
(	23,	23,	-1,	-1,	30,	30,	30,	30,	30,	30,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	-1,	-1,	29,	29,	29,	-1,	-1,	-1,	-1,	-1,	-1,	5,	5,	5,	-1,	-1,	-1,	5,	5,	5,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	5,	5,	5,	5,	5,	5,	5,	5,	5,	-1,	-1,	-1,	6,	6,	-1,	6,	6,	6,	6,	6,	6,	6,	6,	6,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23),
(	-1,	-1,	-1,	-1,	-1,	30,	30,	30,	30,	30,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	29,	-1,	-1,	-1,	-1,	29,	29,	-1,	-1,	-1,	-1,	-1,	5,	5,	5,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	5,	5,	5,	5,	5,	5,	5,	-1,	5,	5,	5,	6,	6,	-1,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	-1,	23,	23,	23,	23,	-1),
(	-1,	-1,	-1,	30,	30,	30,	30,	30,	30,	30,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	29,	29,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	5,	5,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	0,	0,	-1,	-1,	-1,	-1,	-1,	5,	5,	5,	5,	5,	5,	-1,	-1,	5,	-1,	5,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	-1,	23,	23,	23,	23,	23),
(	-1,	-1,	-1,	-1,	30,	30,	30,	30,	30,	30,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	-1,	29,	29,	-1,	29,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	0,	0,	0,	-1,	-1,	-1,	-1,	5,	5,	5,	5,	5,	5,	-1,	-1,	5,	5,	5,	6,	6,	-1,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	-1,	-1,	-1,	23,	23,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	30,	-1,	30,	-1,	-1,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	-1,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	0,	-1,	0,	0,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	5,	-1,	5,	-1,	-1,	-1,	-1,	-1,	6,	-1,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	-1,	-1,	-1,	-1,	-1,	-1,	23,	23,	-1,	-1,	-1,	23),
(	-1,	30,	-1,	30,	30,	-1,	-1,	-1,	-1,	-1,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	-1,	29,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	0,	0,	-1,	-1,	0,	0,	-1,	-1,	-1,	-1,	-1,	5,	-1,	-1,	5,	5,	-1,	-1,	4,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	23,	23,	23,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	29,	29,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	0,	0,	-1,	-1,	0,	0,	-1,	-1,	-1,	-1,	-1,	5,	5,	-1,	5,	-1,	-1,	4,	4,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	-1,	-1,	19,	-1,	-1,	-1,	-1,	23,	23,	23,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	29,	29,	29,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	0,	-1,	-1,	0,	0,	0,	0,	-1,	-1,	-1,	-1,	5,	-1,	-1,	-1,	-1,	-1,	4,	4,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	-1,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	23,	-1,	19,	-1,	-1,	-1,	-1,	23,	23,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	29,	29,	29,	29,	29,	-1,	-1,	29,	29,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	0,	0,	0,	-1,	-1,	-1,	-1,	4,	4,	4,	4,	4,	4,	4,	4,	4,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	-1,	22,	22,	20,	20,	20,	20,	20,	20,	20,	20,	23,	23,	-1,	19,	-1,	-1,	-1,	-1,	23,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	29,	29,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	29,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	0,	0,	0,	0,	0,	-1,	-1,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	-1,	-1,	22,	22,	20,	20,	20,	20,	20,	20,	20,	20,	23,	23,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	29,	-1,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	-1,	29,	29,	29,	29,	29,	29,	29,	29,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	22,	22,	22,	22,	22,	22,	-1,	22,	22,	22,	22,	22,	22,	-1,	22,	22,	22,	22,	22,	20,	20,	20,	20,	20,	20,	20,	20,	23,	23,	-1,	19,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	-1,	-1,	29,	29,	29,	29,	29,	31,	29,	-1,	29,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	-1,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	20,	20,	20,	20,	20,	20,	20,	20,	23,	-1,	-1,	19,	19,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	-1,	31,	-1,	29,	-1,	31,	29,	31,	31,	-1,	29,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	22,	22,	22,	22,	22,	22,	22,	-1,	-1,	-1,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	20,	20,	20,	20,	18,	18,	18,	-1,	-1,	-1,	-1,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	-1,	31,	31,	-1,	31,	31,	31,	31,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	6,	6,	-1,	6,	-1,	6,	6,	6,	6,	6,	-1,	-1,	22,	22,	-1,	-1,	12,	12,	12,	12,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	17,	17,	17,	17,	18,	18,	-1,	-1,	-1,	-1,	-1,	-1,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	31,	31,	31,	-1,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	6,	-1,	-1,	-1,	6,	-1,	6,	6,	6,	6,	-1,	22,	22,	22,	-1,	-1,	12,	12,	12,	12,	-1,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	17,	17,	17,	17,	17,	18,	18,	18,	-1,	-1,	-1,	-1,	-1,	19,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	4,	4,	4,	4,	2,	2,	2,	2,	2,	3,	3,	4,	4,	4,	4,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	6,	6,	6,	-1,	-1,	12,	12,	12,	12,	12,	12,	12,	12,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	22,	17,	17,	17,	17,	17,	-1,	-1,	17,	-1,	18,	18,	18,	-1,	-1,	-1,	19,	19,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	1,	1,	1,	1,	4,	4,	4,	4,	2,	2,	2,	2,	-1,	-1,	3,	3,	3,	3,	3,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	6,	6,	-1,	-1,	-1,	12,	12,	12,	12,	12,	12,	12,	22,	22,	22,	22,	22,	22,	21,	21,	21,	21,	21,	17,	17,	17,	17,	17,	17,	-1,	-1,	-1,	-1,	18,	18,	-1,	-1,	-1,	19,	19,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	1,	1,	1,	1,	1,	1,	1,	-1,	-1,	-1,	2,	2,	2,	-1,	-1,	3,	3,	3,	3,	3,	-1,	-1,	7,	7,	7,	-1,	-1,	7,	7,	-1,	-1,	12,	12,	12,	12,	12,	12,	12,	12,	22,	22,	22,	22,	21,	21,	21,	21,	21,	21,	21,	17,	17,	17,	17,	17,	17,	17,	17,	-1,	-1,	18,	18,	-1,	19,	19,	19,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	1,	1,	1,	1,	1,	1,	1,	-1,	-1,	-1,	-1,	2,	2,	-1,	-1,	3,	3,	3,	3,	-1,	7,	7,	7,	7,	7,	7,	7,	7,	7,	12,	-1,	-1,	12,	12,	12,	12,	12,	12,	12,	22,	22,	22,	21,	21,	21,	21,	21,	21,	21,	21,	17,	17,	17,	17,	17,	17,	17,	17,	-1,	-1,	-1,	-1,	-1,	19,	-1,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	31,	-1,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	31,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	1,	-1,	-1,	-1,	-1,	1,	1,	1,	1,	1,	1,	-1,	-1,	-1,	2,	-1,	-1,	2,	2,	-1,	-1,	3,	3,	-1,	-1,	7,	7,	7,	7,	7,	7,	7,	8,	-1,	12,	12,	12,	12,	12,	12,	12,	12,	12,	12,	13,	22,	22,	21,	21,	21,	21,	21,	21,	21,	21,	17,	17,	17,	17,	17,	17,	17,	17,	17,	-1,	-1,	-1,	19,	19,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	33,	-1,	33,	33,	31,	31,	31,	31,	31,	-1,	31,	-1,	31,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	1,	1,	1,	1,	1,	1,	-1,	-1,	-1,	2,	-1,	-1,	-1,	2,	2,	-1,	3,	3,	3,	-1,	7,	7,	7,	7,	7,	7,	8,	8,	8,	8,	12,	12,	12,	12,	12,	12,	12,	12,	12,	13,	13,	13,	13,	13,	21,	21,	21,	21,	21,	21,	17,	17,	17,	17,	17,	17,	17,	17,	17,	-1,	-1,	-1,	19,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	33,	33,	-1,	33,	33,	33,	33,	31,	31,	-1,	-1,	-1,	-1,	31,	31,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	1,	1,	1,	1,	1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	2,	-1,	-1,	-1,	-1,	3,	-1,	-1,	-1,	-1,	-1,	8,	8,	8,	8,	8,	8,	12,	12,	12,	12,	12,	12,	12,	12,	13,	13,	13,	13,	13,	13,	13,	13,	13,	13,	15,	15,	17,	17,	17,	17,	17,	17,	17,	17,	17,	-1,	-1,	-1,	-1,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	33,	-1,	33,	33,	33,	33,	33,	-1,	-1,	-1,	-1,	-1,	-1,	31,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	2,	2,	-1,	-1,	-1,	3,	3,	-1,	-1,	-1,	-1,	7,	-1,	8,	8,	8,	8,	8,	8,	12,	12,	12,	12,	12,	12,	12,	12,	13,	13,	13,	13,	13,	13,	13,	13,	13,	13,	15,	15,	15,	17,	17,	17,	17,	17,	17,	17,	-1,	-1,	-1,	19,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	33,	-1,	-1,	33,	33,	33,	33,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	32,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	11,	11,	11,	11,	11,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	3,	3,	-1,	-1,	-1,	8,	8,	8,	8,	8,	8,	12,	12,	12,	12,	12,	12,	12,	13,	13,	13,	13,	13,	13,	13,	13,	13,	13,	13,	15,	15,	15,	15,	17,	17,	17,	17,	17,	-1,	-1,	17,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	33,	33,	33,	33,	-1,	-1,	-1,	-1,	-1,	32,	32,	32,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	1,	-1,	-1,	-1,	11,	11,	11,	11,	11,	11,	11,	11,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	8,	8,	8,	8,	8,	-1,	-1,	-1,	12,	12,	12,	12,	13,	13,	13,	13,	13,	13,	13,	13,	13,	13,	13,	13,	15,	15,	15,	15,	17,	17,	17,	-1,	-1,	-1,	-1,	17,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	33,	33,	33,	33,	-1,	-1,	33,	33,	-1,	-1,	-1,	-1,	-1,	32,	32,	-1,	32,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	-1,	-1,	-1,	10,	10,	-1,	-1,	-1,	-1,	-1,	8,	8,	9,	9,	9,	9,	9,	-1,	-1,	-1,	12,	12,	12,	13,	13,	13,	13,	13,	13,	13,	13,	13,	13,	13,	-1,	-1,	15,	15,	15,	15,	-1,	-1,	17,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	33,	33,	33,	-1,	33,	33,	33,	-1,	-1,	-1,	32,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	1,	-1,	-1,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	10,	10,	10,	10,	10,	10,	10,	-1,	9,	9,	9,	9,	9,	9,	-1,	-1,	-1,	-1,	-1,	-1,	13,	13,	13,	14,	14,	14,	14,	14,	14,	14,	-1,	-1,	-1,	15,	15,	15,	15,	15,	-1,	-1,	-1,	-1,	-1,	16,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	33,	33,	33,	33,	33,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	32,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	10,	10,	10,	10,	10,	10,	-1,	-1,	9,	9,	9,	9,	9,	9,	9,	-1,	9,	-1,	-1,	-1,	-1,	13,	-1,	14,	14,	14,	14,	14,	14,	14,	-1,	-1,	-1,	15,	-1,	15,	15,	15,	15,	-1,	-1,	-1,	-1,	16,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	33,	33,	33,	33,	33,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	10,	10,	10,	10,	10,	10,	10,	-1,	-1,	9,	9,	9,	9,	9,	9,	9,	9,	9,	-1,	-1,	-1,	-1,	-1,	14,	14,	14,	14,	14,	14,	14,	-1,	-1,	-1,	-1,	-1,	15,	15,	15,	15,	15,	-1,	-1,	-1,	16,	16,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	33,	33,	33,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	32,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	1,	-1,	-1,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	10,	10,	10,	10,	10,	10,	10,	-1,	-1,	-1,	9,	9,	9,	9,	9,	9,	9,	-1,	-1,	-1,	-1,	-1,	-1,	14,	14,	14,	14,	14,	14,	-1,	-1,	-1,	-1,	-1,	-1,	15,	15,	15,	15,	15,	-1,	-1,	-1,	-1,	16,	16,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	33,	-1,	33,	-1,	-1,	37,	37,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	10,	10,	10,	10,	10,	10,	10,	10,	-1,	-1,	9,	9,	9,	9,	9,	9,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	14,	14,	14,	14,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	15,	-1,	-1,	15,	-1,	-1,	-1,	-1,	16,	16,	16,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	25,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	33,	-1,	37,	37,	37,	37,	37,	37,	37,	37,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	26,	26,	26,	26,	26,	26,	-1,	-1,	-1,	9,	9,	9,	9,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	14,	14,	14,	14,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	15,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	16,	16,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	37,	37,	37,	37,	37,	37,	37,	37,	37,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	26,	26,	26,	26,	26,	26,	26,	-1,	-1,	9,	9,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	14,	14,	14,	-1,	-1,	-1,	-1,	-1,	16,	-1,	16,	16,	-1,	-1,	-1,	-1,	16,	-1,	16,	-1,	16,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	37,	37,	37,	37,	37,	37,	37,	37,	37,	37,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	-1,	-1,	27,	27,	27,	26,	26,	26,	26,	-1,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	9,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	14,	14,	-1,	-1,	-1,	-1,	-1,	-1,	16,	-1,	-1,	16,	-1,	-1,	-1,	16,	16,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	37,	37,	37,	37,	37,	37,	37,	37,	37,	37,	37,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	27,	27,	27,	27,	27,	-1,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	26,	26,	26,	26,	26,	26,	26,	26,	26,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	14,	-1,	14,	-1,	-1,	-1,	-1,	16,	16,	-1,	-1,	-1,	-1,	16,	16,	16,	-1,	16,	16,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	37,	37,	37,	37,	37,	34,	34,	34,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	27,	26,	26,	26,	26,	26,	26,	26,	26,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	14,	-1,	-1,	-1,	-1,	-1,	16,	16,	-1,	-1,	-1,	16,	16,	16,	-1,	16,	-1,	-1,	25,	-1,	25,	25,	-1,	-1,	-1,	25,	25,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	37,	37,	37,	37,	37,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	27,	27,	27,	-1,	-1,	-1,	27,	27,	27,	27,	27,	27,	27,	27,	27,	26,	26,	26,	26,	-1,	26,	26,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	16,	16,	-1,	-1,	-1,	-1,	-1,	-1,	16,	16,	-1,	25,	25,	25,	25,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	36,	36,	36,	36,	37,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	28,	-1,	26,	26,	26,	26,	26,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	16,	16,	16,	16,	-1,	-1,	-1,	-1,	-1,	-1,	25,	25,	25,	25,	-1,	-1,	-1,	25,	-1,	-1,	-1),
(	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	36,	36,	36,	36,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	28,	28,	28,	-1,	-1,	26,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	16,	-1,	16,	-1,	-1,	-1,	25,	25,	-1,	25,	25,	-1,	-1,	-1,	25,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	36,	36,	36,	36,	36,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	28,	-1,	28,	28,	-1,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	36,	36,	36,	36,	36,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	28,	-1,	28,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	-1,	-1,	24,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	36,	36,	-1,	36,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	28,	-1,	28,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	-1,	24,	24,	-1,	-1,	24,	24,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	25),
(	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	36,	36,	36,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	28,	26,	-1,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	24,	24,	24,	24,	-1,	24,	24,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	36,	36,	36,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	-1,	28,	26,	-1,	26,	26,	-1,	-1,	-1,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	-1,	-1,	-1,	-1,	-1,	25,	-1),
(	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	36,	36,	34,	34,	34,	34,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	28,	26,	-1,	26,	26,	-1,	-1,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	-1,	-1,	-1,	-1,	-1,	25),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	36,	36,	34,	34,	34,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	28,	28,	28,	26,	26,	26,	-1,	26,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	25,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	35,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	28,	28,	28,	26,	26,	-1,	-1,	26,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	35,	34,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	28,	28,	28,	26,	-1,	-1,	26,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	35,	34,	34,	34,	34,	34,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	28,	28,	26,	-1,	-1,	26,	26,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	24,	24,	24,	24,	24,	24,	24,	-1,	24,	24,	24,	24,	24,	24,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	35,	35,	35,	35,	35,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	28,	28,	-1,	-1,	-1,	-1,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	24,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	35,	35,	35,	35,	35,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	28,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	24,	24,	24,	-1,	-1,	-1,	-1,	24,	24,	24,	24,	24,	24,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	35,	35,	35,	35,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	24,	24,	24,	-1,	-1,	-1,	-1,	25,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	35,	35,	35,	35,	35,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	28,	28,	28,	28,	28,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	24,	-1,	-1,	-1,	-1,	-1,	25,	25),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	35,	35,	35,	35,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	25),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	35,	35,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	24,	24,	-1,	-1,	-1,	-1,	-1,	25,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	35,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	-1,	-1,	-1,	-1,	-1,	25,	25,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	35,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	26,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	25,	25,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	35,	35,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	25,	25,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	35,	-1,	-1,	-1,	35,	35,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	35,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1),
(	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1))

tSpreadFactors = (
# Judaism
{
	iMinority :	[rEgypt, rMesopotamia, rPersia, rAnatolia, rBalkans, rItaly, rIberia, rEurope, rRussia, rBritain, rUnitedStates],
},
# Orthodoxy
{
	iCore :		[rRussia, rEthiopia],
	iHistorical : 	[rBalkans, rAnatolia, rMesopotamia, rEgypt, rSiberia],
	iPeriphery : 	[rMaghreb, rItaly, rPersia, rAlaska],
	iMinority :	[rCentralAsia],
},
# Catholicism
{
	iCore :		[rEurope, rItaly, rIberia],
	iHistorical :	[rBritain, rScandinavia, rCanada, rAlaska, rUnitedStates, rCaribbean, rMesoamerica, rColombia, rPeru, rBrazil, rArgentina, rSouthAfrica],
	iPeriphery :	[rBalkans, rAustralia, rOceania, rWestAfrica],
},
# Protestantism
{
	iCore :		[rEurope, rScandinavia, rUnitedStates],
	iHistorical :	[rBritain, rCanada, rAlaska, rAustralia],
	iPeriphery :	[rOceania, rSouthAfrica],
},
# Islam
{
	iCore : 	[rArabia, rMesopotamia, rEgypt],
	iHistorical : 	[rPersia, rMaghreb, rCentralAsia, rIndia, rIndonesia, rWestAfrica],
	iPeriphery : 	[rEthiopia, rItaly, rIberia, rAnatolia, rBalkans],
	iMinority : 	[rRussia, rSiberia],
},
# Hinduism
{
	iCore : 	[rIndia, rDeccan],
	iHistorical : 	[rIndochina, rIndonesia],
},
# Buddhism
{
	iCore : 	[rIndia, rTibet, rIndochina],
	iHistorical : 	[rCentralAsia, rChina, rManchuria, rKorea, rJapan, rIndonesia],
	iMinority :	[rPersia],
},
# Confucianism
{
	iCore : 	[rChina, rManchuria],
	iHistorical :	[rKorea],
	iPeriphery : 	[rCentralAsia, rTibet],
	iMinority : 	[rJapan, rIndonesia, rIndochina, rAustralia],
},
# Taoism
{
	iCore : 	[rChina],
	iHistorical : 	[rManchuria],
	iPeriphery : 	[rTibet, rCentralAsia],
},
# Zoroastrianism
{
	iHistorical :	[rPersia],
	iMinority : 	[rIndia],
},
)