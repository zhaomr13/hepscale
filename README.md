# A simple tool to create scale plot in high energy physics

## Usage
+ Please put your data file in the ~/.hepscale
+ ''hepscale ls .'' will list your datafiles
+ If you have a data file named ''mass.dat'', you can plot with ''hepscale plot mass.dat''

## Example of data file:
(mass.dat)
LinePlot
Mass
4 13 MassUnit
l red 1       TeV $$
l red 1       GeV $$
l red 1       MeV $$
l red 100     MeV $$
p red 125.5   GeV $H^0$
p red 0.5     MeV $e$
p red 80.377  GeV $W$
p red 91.18   GeV $Z$
p red 1776.86 MeV $\tau$
p red 105.65  MeV $\mu$
p red 134.98  MeV $\pi^0$
p red 497.6   MeV $K^0$
p red 3097    MeV $J/\psi$
p red 9460.3  MeV $\Upsilon(1S)$%

+ Explanations:
+ l1: LinePlot: For future extension
+ l2: Mass: title of the plot
+ l3: 4 13: plot the scale from 1e4 to 1e13, the unit varying, so please just try these two number
+ l3: MassUnit: use mass as unit, other option: TimeUnit, LengthUnit
+ l4-...: the first symbol l,p or i means the point style. l means to draw a verticle line, p mean to draw the physics quantity, i mean to draw the quantity as 1/x.
