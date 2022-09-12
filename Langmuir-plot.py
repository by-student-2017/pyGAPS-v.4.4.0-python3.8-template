#import pygaps
import pygaps.characterisation as pgc
import pygaps.parsing as pgp
import matplotlib.pyplot as plt

# create the path
path = r'case.csv'

# import the isotherm
isotherm = pgp.isotherm_from_csv(path)
#isotherm.print_info()

pgc.area_langmuir(isotherm, verbose=True)
#pgc.area_langmuir(isotherm, p_limits=(0.05, 0.3), verbose=True)
fig1 = plt.figure(1)
fig1.savefig('./plot/Langmuir-plot.jpg')
#plt.show()
