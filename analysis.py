
print("===================================================================================================")
print("NLDFT, ADS")
print(" ")
import dft_fit_csv_ads

print("===================================================================================================")
print("NLDFT, DES")
print(" ")
import dft_fit_csv_des

#print("===================================================================================================")
#print("PSD")
#print(" ")
mgs_PSD = __import__('PSD-plot_pygaps_v202')

print("===================================================================================================")
print("BET plot")
print(" ")
mgs_BET = __import__('BET-plot')

print("===================================================================================================")
print("Langmuir plot")
print(" ")
mgs_Lan = __import__('Langmuir-plot')

print("===================================================================================================")
print("t plot Ref_CarbonBlack")
print(" ")
mgs_tR  = __import__('t-plot_Ref_CarbonBlack')

print("===================================================================================================")
print("alpha-s plot")
print(" ")
mgs_alp = __import__('alpha-s-plot')

#print("===================================================================================================")
#print("DH plot")
#print(" ")
mgs_DH  = __import__('DH-plot')

print("===================================================================================================")
print("DR plot")
print(" ")
mgs_DR  = __import__('DR-plot')

print("===================================================================================================")
print("DA plot")
print(" ")
mgs_DA  = __import__('DA-plot')

print("===================================================================================================")