#import pygaps
import pygaps as pg

#isotherm = pygaps.PointIsotherm(
isotherm = pg.PointIsotherm(
    pressure=[0.1, 0.2, 0.3, 0.4, 0.5, 0.4, 0.35, 0.25, 0.15, 0.05],
    loading=[0.1, 0.2, 0.3, 0.4, 0.5, 0.45, 0.4, 0.3, 0.15, 0.05],
    material= 'Carbon X1',
    adsorbate = 'N2',
    temperature = 77,
)
print(isotherm)
#isotherm.plot()
