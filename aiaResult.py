from matplotlib import pyplot as plt
from sunpy.instr.aia import aiaprep
from sunpy.net import Fido, attrs as a
from astropy.coordinates import SkyCoord
from astropy import units as u

import sunpy.map
import warnings
warnings.filterwarnings("ignore")

result = Fido.search(a.Time('2017-03-21T01:40:00', '2017-03-21T01:41:00'),
a.Instrument("aia"))

file_download = Fido.fetch(result[0, 3], site='ROB')

aia1 = sunpy.map.Map(file_download[0])

aia = aiaprep(aia1)

aia.plot()
plt.colorbar()
plt.savefig('aiaResult.png')