#!/usr/bin/env python
# coding: utf-8
# Roxanne Berthin <roxanne.berthin@sorbonne-universite.fr>, version 24/02/2021


import sys
import argparse
import numpy as np
from func.temperature import cat_temperature
from func.trajectories import cat_xyz, cat_traj
from func.read_inputs import read_data, read_runtime
from func.polarization import cat_pol
from func.charges import cat_charges, cat_tot_charges
from func.dipoles import cat_dip
from func.stress import cat_stress

def main():
    print('\n**********************************************')
    print('*******   PYTHON SCRIPT MW CAT FILEs   *******')
    print('**********************************************\n')
    print(' I can cat :')
    print('  - temperature.out    (temperature)')
    print('  - trajectories.xyz   (xyz)')
    print('  - trajectories.out   (trajectories)')
    print('  - polarization.out   (polarization)') 
    print('  - charges.out        (charges)')
    print('  - total_charges.out  (total_charges)')
    print('  - dipoles.out        (dipoles)')
    print('  - stress_tensor.out  (stess_tensor)\n')

    parser = argparse.ArgumentParser(
        description = '  ')
    parser.add_argument('-f', '--propertie', default = '', help = 'types of '\
                        'files you want to cat')
    parser.add_argument('-d', '--directory', default = '', help = 'directories '\
                        'containing files you want to cat')
    args = parser.parse_args()
    
    if len(args.directory) < 2:
        print('ERROR : I can cat a single file, I need at least two files ...')
        sys.exit(1)
    else:
       dir_list = args.directory.split(',')
    
    if len(args.propertie) == 0:
        print('ERROR : I need at least a type of file to cat')
        sys.exit(1)
    else:
        prop_list = args.propertie.split(',')

    print('I will cat '+str(len(prop_list))+' types of files '\
                'from '+str(len(dir_list))+' directories')

        
    print('Reading runtime.inpt ...')
    step, write_output = read_runtime(dir_list, prop_list)
    for prop in range (len(prop_list)):
        if prop_list[prop] == 'temperature':
            print('** Starting files temperature.out **')
            cat_temperature(dir_list, step, write_output[prop])   
            print('temperature :  DONE\n')

        if prop_list[prop] == 'xyz':
            print('** Starting files trajectories.xyz **')
            nat = read_data(str(dir_list[0])+'/data.inpt', 'all')
            cat_xyz(dir_list, step, nat, write_output[prop])
            print('xyz :  DONE')

        if prop_list[prop] == 'trajectories':
            print('** Starting files trajectories.out **')
            nat = read_data(str(dir_list[0])+'/data.inpt','all')
            cat_traj(dir_list, step, nat, write_output[prop])
            print('traj :  DONE')

        if prop_list[prop] == 'polarization':
            print('** Starting files polarization.out **')
            cat_pol(dir_list, step, write_output[prop])
            print('polarization :  DONE\n')

        if prop_list[prop] == 'charges':
            print('** Starting files charges.out **')
            nat = read_data(str(dir_list[0])+'/data.inpt', 'elec')
            cat_charges(dir_list, step, nat, write_output[prop])
            print('charges :  DONE\n')
        
        if prop_list[prop] == 'total_charges':
            print('** Starting files total_charges.out **')
            cat_tot_charges(dir_list, step, write_output[prop])
            print('total_charges :  DONE\n')

        if prop_list[prop] == 'dipoles':
            print('** Starting files dipoles.out **')
            n1 = read_data(str(dir_list[0])+'/data.inpt', 'all')
            n2 = read_data(str(dir_list[0])+'/data.inpt', 'elec')
            cat_dip(dir_list, step, n1-n2, write_output[prop])
            print('dipoles :  DONE')

        if prop_list[prop] == 'stress_tensor':
             print('** Starting files stress_tensor.out **')
             cat_stress(dir_list, step, write_output[prop])
             print('stress_tensor :  DONE\n')


    print('**********************************************')
    print('*********    !!   ALL  DONE   !!     *********')
    print('**********************************************\n')

    
if __name__ == '__main__':
    main()
                           
