import pygaps.characterisation as pgc
import pygaps.parsing as pgp
import matplotlib.pyplot as plt

# create the path
path = r'case.csv'

# import the isotherm
isotherm = pgp.isotherm_from_csv(path)
#isotherm.print_info()

# fitting on DFT kernel
result_dict_dft = pgc.psd_dft(
    isotherm,
    #kernel='DFT-N2-77K-carbon-slit',
    #kernel='./NLDFT-H2-77K-carbon-slit_2006.csv',
    #kernel='./kernel/H2_77K/NLDFT-H2-77K-carbon-slit_1nm_2006.csv',
    kernel='./kernel/H2_77K/NLDFT-H2-77K-carbon-slit_2nm_2006.csv',
    #branch='des',
    #bspline_order=5,
    verbose=True)

# plot
fig1 = plt.figure(1)
fig1.savefig('./plot/H2_77K_2nm_Fit.jpg')
fig2 = plt.figure(2)
fig2.savefig('./plot/H2_77K_2nm_PSD.jpg')
#plt.show()

#import pprint
#pprint.pprint(result_dict_dft)

import pandas as pd
# method 1
#d2={}
#for k,v in result_dict_dft.items():
#    d2[k]=pd.Series(v)
#df = pd.DataFrame(d2)
#
# method 2
df = pd.DataFrame.from_dict(result_dict_dft, orient='index').T
#
# method 3
#d = result_dict_dft
#df = pd.DataFrame(d.values(), index=d.keys()).T
#df.to_csv("result_dft_ads.csv", index=False)

# set init of ds
dfds = df.assign(ds=0.0e0)

import numpy as np

# convert pandas to numpy array
ndfds = dfds.to_numpy()

# calculate ds
ndfds[0,5] = (ndfds[0,5] - 0.0)/ndfds[0,0]*1000.0
for num in range(1,len(ndfds)):
  ndfds[num,5] = (ndfds[num,2] - ndfds[num-1,2])/ndfds[num,0]*1000.0

# set name of columns
ndf = pd.DataFrame(ndfds)
ndf.columns = ['pore_widths_nm', 'pore_distribution', 'pore_volume_cumulative_cm^3g^-1', 'kernel_loading', 'limits','ds_m^2g^-1']

# output window and excel file
import pprint
pprint.pprint(ndf)
ndf.to_csv("result_dft_ads.csv", index=False)
