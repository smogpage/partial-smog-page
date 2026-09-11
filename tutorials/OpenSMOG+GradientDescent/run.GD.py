from OpenSMOG import SBM
from openmm.app import *
from simtk.unit import *
import sys
import argparse

# You will need openmmtools installed to run steepest descent minimization
from openmmtools import integrators

sbm_AA_grofile = 'smog.gro'
sbm_AA_topfile = 'smog.top'
sbm_AA_xmlfile = 'smog.xml'

sbm_AA_4v9d_run1 = SBM(name='SDmin', time_step=0.002, collision_rate=1.0, r_cutoff=0.65, temperature=0.5)

# rather than call an integrator by name, we will create an integrator object and pass it to OpenSMOG
integrator = integrators.GradientDescentMinimizationIntegrator()

# pass the Gradient Descent minimizer to OpenSMOG
sbm_AA_4v9d_run1.setup_openmm(platform='opencl', precision='single', GPUindex='default', integrator=integrator)
sbm_AA_4v9d_run1.saveFolder('output_minimize')
sbm_AA_4v9d_run1.loadSystem(Grofile=sbm_AA_grofile, Topfile=sbm_AA_topfile, Xmlfile=sbm_AA_xmlfile)
sbm_AA_4v9d_run1.createSimulation()
sbm_AA_4v9d_run1.createReporters(trajectory=True, energies=True, energy_components=True, trajectoryFormat='xtc', interval=10**3)
sbm_AA_4v9d_run1.run(nsteps=300000, report=True, interval=10**3)

#get minimized state 
st_min = sbm_AA_4v9d_run1.simulation.context.getState(getPositions=True, getVelocities=True, getEnergy=True)

#New SBM object
sbm_AA_4v9d_run2 = SBM(name='4v9dcl.db.part0001', time_step=0.002, collision_rate=1.0, r_cutoff=0.65, temperature=0.5)
sbm_AA_4v9d_run2.setup_openmm(platform='opencl', precision='single', GPUindex='default', integrator='langevin')
sbm_AA_4v9d_run2.saveFolder('output_cuda_4v9d_run')
sbm_AA_4v9d_run2.loadSystem(Grofile=sbm_AA_grofile, Topfile=sbm_AA_topfile, Xmlfile=sbm_AA_xmlfile)
sbm_AA_4v9d_run2.createSimulation()
sbm_AA_4v9d_run2.createReporters(trajectory=True, energies=True, energy_components=True, trajectoryFormat='xtc', interval=10**3)
#set minimized State
sbm_AA_4v9d_run2.simulation.context.setState(st_min)
sbm_AA_4v9d_run2.run(nsteps=1000000, report=True, interval=10**3)
