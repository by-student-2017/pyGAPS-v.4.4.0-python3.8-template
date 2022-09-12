#import pygaps
import pygaps.characterisation as pgc
import pygaps.parsing as pgp
import matplotlib.pyplot as plt

# create the path
path = r'case.csv'

# import the isotherm
isotherm = pgp.isotherm_from_csv(path)
#isotherm.print_info()

# DR (Dubinin-Radushkevich) plot
result_dict = pgc.dr_plot(isotherm, verbose=True)
#result_dict = pgc.dr_plot(isotherm, p_limits=[0,0.1], verbose=True)

# plot
fig1 = plt.figure(1)
fig1.savefig('./plot/DR-plot.jpg')
#plt.show()

# import pprint
# pprint.pprint(result_dict)
