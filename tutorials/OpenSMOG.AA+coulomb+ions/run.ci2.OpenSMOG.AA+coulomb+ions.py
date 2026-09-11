# import OpenSMOG
from OpenSMOG import SBM

#Choose some basic runtime settings.  We will call our system 2ci2
# since we are including diffuse ions, it is important to remember to turn on PBC
SMOGrun = SBM(name='2ci2', time_step=0.002, collision_rate=1.0, r_cutoff=2.0, temperature=0.5, pbc=True)

#Select a platform and GPU IDs (if needed)
#We will use opencl.  If you want to perform CPU-only calculations, set platform to 'CPU'.
SMOGrun.setup_openmm(platform='opencl',GPUindex='default')

#Decide where to save your data (here, output_2ci2)
SMOGrun.saveFolder('output_2ci2')

#You may optionally set some input file names to variables
SMOG_grofile = '2ci2.OpenSMOG.AA+coulomb+ions.MGCL.gro'
SMOG_topfile = '2ci2.OpenSMOG.AA+coulomb+ions.MGCL.top'
SMOG_xmlfile = '2ci2.OpenSMOG.AA+coulomb+ions.MGCL.xml'

#Load your force field data
SMOGrun.loadSystem(Grofile=SMOG_grofile, Topfile=SMOG_topfile, Xmlfile=SMOG_xmlfile)

#Create the context, and prepare the simulation to run
SMOGrun.createSimulation()

#Perform L-BFGS energy minimization
SMOGrun.minimize(tolerance=1)

#Decide how frequently to save data
SMOGrun.createReporters(trajectory=True, energies=True, energy_components=True, interval=10**3)

#Launch the simulation
SMOGrun.run(nsteps=10**6, report=True, interval=10**3)

#Note: One can also run for clock time, rather than number of timesteps. For example, to run for 10 hours, you could use: SMOGrun.runForClockTime(time=10)

