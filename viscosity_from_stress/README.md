This allows to compute viscosity from stress_tensor.out output from MetalWalls.

Execution : python viscosity.py -d **directories containing stress files** -n **number of frame to skip** -t **time span of the correlation function in steps** (Default value : n = 1 and t = 1000)

1. the script cat all the stress_tensor.out files. 
2. then it built the input file used by the Fortran code stress_corr.f90
3. execution of stress_corr.f90
4. average of the output files scorr.out\*
5. conversion from ua to mPa.s
