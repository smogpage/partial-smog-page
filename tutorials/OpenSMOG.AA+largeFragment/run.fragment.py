# import OpenSMOG
from OpenSMOG import SBM

#Choose some basic runtime settings.  We will call our system fragment
SMOGrun = SBM(name='fragment', time_step=0.002, collision_rate=1.0, r_cutoff=0.65, temperature=0.5)

#Select a platform and GPU IDs (if needed)
#We will use opencl.  If you want to perform CPU-only calculations, set platform to 'CPU'.
SMOGrun.setup_openmm(platform='opencl',GPUindex='default')

#Decide where to save your data (here, output_fragment)
SMOGrun.saveFolder('output_fragment')

#You may optionally set some input file names to variables
SMOG_grofile = 'ribosome.fragment.gro'
SMOG_topfile = 'ribosome.fragment.top'
SMOG_xmlfile = 'ribosome.fragment.xml'

#Load your force field data
SMOGrun.loadSystem(Grofile=SMOG_grofile, Topfile=SMOG_topfile, Xmlfile=SMOG_xmlfile)

#Create the context, and prepare the simulation to run
SMOGrun.createSimulation()

#Perform L-BFGS energy minimization
SMOGrun.minimize(tolerance=1)

#Decide how frequently to save data
SMOGrun.createReporters(trajectory=True, energies=True, energy_components=True, interval=10**3)

#Launch the simulation
SMOGrun.run(nsteps=10**5, report=True, interval=10**3)

#Note: One can also run for clock time, rather than number of timesteps. For example, to run for 10 hours, you could use: SMOGrun.runForClockTime(time=10)

