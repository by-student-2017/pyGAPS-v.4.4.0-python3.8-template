#import pygaps
import pygaps.characterisation as pgc
import pygaps.parsing as pgp
import matplotlib.pyplot as plt

# create the path
path = r'case.csv'

# import the isotherm
isotherm = pgp.isotherm_from_csv(path)
#isotherm.print_info()

# DH plot
result_dict = pgc.psd_mesoporous(
    isotherm,
    psd_model='DH',
    branch='ads',
    pore_geometry='cylinder',
    thickness_model='Halsey',
    verbose=True,
)

# plot
fig1 = plt.figure(1)
fig1.savefig('./plot/DH-plot.jpg')
#plt.show()

#import pprint
#pprint.pprint(result_dict)

# old version
#import pandas as pd
#df = pd.DataFrame(result_dict)
#df.to_csv("result_DH.csv", index=False)
