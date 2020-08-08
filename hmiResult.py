from sunpy.net import Fido
from sunpy.net import attrs as a
import sunpy.map
import matplotlib.pyplot as plt

result = Fido.search(a.Time('2013/05/17 00:05:00', '2013/05/17 00:10:00'), a.jsoc.Series("hmi.M_720s"),
	a.jsoc.Keys(["T_REC, CROTA2"]), a.jsoc.Notify("fakhouryali@yahoo.com"))

downloaded_file = Fido.fetch(result[0, 0])

hmi_map = sunpy.map.Map(downloaded_file[0])
fig = plt.figure()
hmi_map.plot()

plt.savefig('hmiResult.png')