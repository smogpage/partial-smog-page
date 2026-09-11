# import OpenSMOG
from OpenSMOG import SBM

#Choose some basic runtime settings.  We will call our system 7k00
SMOGrun = SBM(name='7k00', time_step=0.002, collision_rate=1.0, r_cutoff=0.65, temperature=0.5)

#Select a platform and GPU IDs (if needed)
#We will use opencl.  If you want to perform CPU-only calculations, set platform to 'CPU'.
SMOGrun.setup_openmm(platform='opencl',GPUindex='default')

#Decide where to save your data (here, output_7k00)
SMOGrun.saveFolder('output_7k00')

#You may optionally set some input file names to variables
SMOG_grofile = '7k00.OpenSMOG.AA.gro'
SMOG_topfile = '7k00.OpenSMOG.AA.top'
SMOG_xmlfile = '7k00.OpenSMOG.AA.xml'

#Load your force field data
SMOGrun.loadSystem(Grofile=SMOG_grofile, Topfile=SMOG_topfile, Xmlfile=SMOG_xmlfile)

#Create the context, and prepare the simulation to run
SMOGrun.createSimulation()

#Perform L-BFGS energy minimization
SMOGrun.minimize(tolerance=1)

#Decide how frequently to save data
SMOGrun.createReporters(trajectory=True, energies=True, energy_components=True, interval=10**3)

#Launch the simulation
SMOGrun.run(nsteps=10**4, report=True, interval=10)

#Note: One can also run for clock time, rather than number of timesteps. For example, to run for 10 hours, you could use: SMOGrun.runForClockTime(time=10)

