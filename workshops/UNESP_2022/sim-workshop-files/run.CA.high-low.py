from OpenSMOG import SBM

#Choose some basic runtime settings.  We will call our system 2ci2
SMOGhot = SBM(name='2ci2', time_step=0.0005, collision_rate=1.0, r_cutoff=1.1, temperature=2.0)

#Select a platform and GPU IDs (if needed)
SMOGhot.setup_openmm(platform='cpu',GPUindex='default')

#Decide where to save your data (here, output_2ci2)
SMOGhot.saveFolder('output_2ci2.CA.hot')

#You may optionally set some input file names to variables
SMOG_grofile = '2ci2.CA.gro'
SMOG_topfile = '2ci2.CA.top'
SMOG_xmlfile = '2ci2.CA.xml'

#Load your force field data
SMOGhot.loadSystem(Grofile=SMOG_grofile, Topfile=SMOG_topfile, Xmlfile=SMOG_xmlfile)

#Create the context, and prepare the simulation to run
SMOGhot.createSimulation()

#Perform energy minimization
SMOGhot.minimize(tolerance=1)

#Decide how frequently to save data
SMOGhot.createReporters(trajectory=True, energies=True, energy_components=True, interval=10**3)

#Launch the simulation
SMOGhot.run(nsteps=10**5, report=True, interval=10**3)

#Save the state of the system
statefilename='smog.state'
SMOGhot.simulation.saveState(statefilename)


# Now run it at a lower temperature, starting from the unfolded conformation

#Choose some basic runtime settings.  We will call our system 2ci2
SMOGcold = SBM(name='2ci2', time_step=0.0005, collision_rate=1.0, r_cutoff=1.1, temperature=0.8)

#Select a platform and GPU IDs (if needed)
SMOGcold.setup_openmm(platform='cpu',GPUindex='default')

#Decide where to save your data (here, output_2ci2)
SMOGcold.saveFolder('output_2ci2.CA.cold')

#You may optionally set some input file names to variables
SMOG_grofile = '2ci2.CA.gro'
SMOG_topfile = '2ci2.CA.top'
SMOG_xmlfile = '2ci2.CA.xml'

#Load your force field data
SMOGcold.loadSystem(Grofile=SMOG_grofile, Topfile=SMOG_topfile, Xmlfile=SMOG_xmlfile)

#Create the context, and prepare the simulation to run
SMOGcold.createSimulation()

#Perform energy minimization
SMOGcold.minimize(tolerance=1)

#Decide how frequently to save data
SMOGcold.createReporters(trajectory=True, energies=True, energy_components=True, interval=10**3)

# load in the last frame of the last run
SMOGcold.simulation.loadState(statefilename)

#Launch the simulation
SMOGcold.run(nsteps=4*10**5, report=True, interval=10**3)


