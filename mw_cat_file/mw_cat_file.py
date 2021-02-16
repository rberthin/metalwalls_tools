#!/usr/bin/env python
# coding: utf-8
# Roxanne Berthin <roxanne.berthin@sorbonne-universite.fr>, version 16/02/2021


import sys
import argparse
import numpy as np

#******************************************************************************************
#******************************************************************************************
def read_data(file):
    with open(file) as dat:
        for line in dat:
            if (line.lstrip()).startswith("num_atoms"):
                nbatoms = float(line.split()[1])
    return int(nbatoms)

#******************************************************************************************
#******************************************************************************************

def cat_temperature(dir_list, step, freq):
    fout = open('temperature_cat_1-'+str(len(dir_list))+'.out', 'w')
    header = '# Temperature in K\n# ----------------\n# step temperature (K)\n'
    fout.write(header)
    count = 0
    for i in range (len(dir_list)):
        fin = open(str(dir_list[i])+'/temperature.out','r')
        print('    directory '+str(i+1)+'/'+str(len(dir_list)))
        line = fin.readline()
        line = fin.readline()
        line = fin.readline()

        if i < (len(dir_list)-1):
            for j in range(int(step[i]/freq)):
                line = fin.readline()
                fout.write('{0:8s}    {1}\n'.format(
                          str(int(line.split()[0])+count), line.split()[1]))
        else : 
            for j in range(int(step[i]/freq)+1):
                line = fin.readline()
                fout.write('{0:8s}    {1}\n'.format(
                           str(int(line.split()[0])+count), float(line.split()[1])))

        count = count + step[i]

#******************************************************************************************
#******************************************************************************************

def cat_xyz(dir_list, step, nat, freq):
    fout = open('trajectories_cat_1-'+str(len(dir_list))+'.xyz', 'w')
    for i in range (len(dir_list)):
        print('    directory '+str(i+1)+'/'+str(len(dir_list)))
        fin = open(str(dir_list[i])+'/trajectories.xyz','r')

        if i < (len(dir_list)-1):
            for j in range(int(step[i]/freq)):
                l = fin.readline()
                fout.write(l)
                l = fin.readline()
                fout.write(l)
                for k in range(nat):   
                    line = fin.readline()
                    fout.write('{0:5s}   {1}   {2}   {3}\n'.format(
                           line.split()[0], line.split()[1], line.split()[2], line.split()[3]))
        else :
            for j in range(int(step[i]/freq)+1):
                l = fin.readline()
                fout.write(l)
                l = fin.readline()
                fout.write(l)
                for k in range (nat):
                    line = fin.readline()
                    fout.write('{0:5s}   {1}   {2}   {3}\n'.format(
                           line.split()[0], line.split()[1], line.split()[2], line.split()[3]))


#******************************************************************************************
#******************************************************************************************

def cat_traj(dir_list, step, nat, freq):
    fout = open('trajectories_cat_1-'+str(len(dir_list))+'.out', 'w')
    header = '# Trajectories of mobile particles in atomic unit\n # ----------------------'\
             '-------------------------\n# Length:   1 au = 0.052917721067 nm\n# Velocity:'\
             ' 1 au = 2.1876912633e6 m.s^-1\n#         x                    y             '\
             '       z                    vx                   vy                   vz\n'
    fout.write(header)

    for i in range (len(dir_list)):
        print('    directory '+str(i+1)+'/'+str(len(dir_list)))
        fin = open(str(dir_list[i])+'/trajectories.out','r')
        fin.readline()
        fin.readline()
        fin.readline()
        fin.readline()
        fin.readline()
        if i < (len(dir_list)-1):
            for j in range(int(step[i]/freq)):
                l = fin.readline()
                fout.write(l)
                for k in range(nat):
                    line = fin.readline()
                    fout.write('{0}   {1}   {2}   {3}   {4}   {5}\n'.format(
                           line.split()[0], line.split()[1], line.split()[2], line.split()[3],
                           line.split()[4], line.split()[5]))
        else :
            for j in range(int(step[i]/freq)+1):
                l = fin.readline()
                fout.write(l)
                for k in range (nat):
                    line = fin.readline()
                    fout.write('{0}    {1}   {2}   {3}   {4}   {5}\n'.format(
                           (line.split()[0]), line.split()[1], line.split()[2], line.split()[3],
                           line.split()[4], line.split()[5]))


#******************************************************************************************
#******************************************************************************************


def main():
    print('\n**********************************************')
    print('*******   PYTHON SCRIPT MW CAT FILEs   *******')
    print('**********************************************\n')
    print(' I can cat :')
    print('  - temperature.out   (temperature)')
    print('  - trajectories.xyz  (xyz)\n') 
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
    print('I will cat '+str(len(prop_list))+' types of files from '+str(len(dir_list))+' directories')

    
    # ***** RUNTIME.INPT *****
    step = []
    default = 0
    write_output = []
    print('Reading runtime.inpt ...\n')
    for i in range (len(dir_list)):
        with open(str(dir_list[i])+'/runtime.inpt') as run: 
            for line in run:
                if (line.lstrip()).startswith("num_steps"):
                    step.append(int(line.split()[1]))

                if i == 0:   
                    if (line.lstrip()).startswith("output"):
                        temp = run.readlines()
                        for j in range (len(temp)): 
                            if 'default' in temp[j]:
                                default = int(temp[j].split()[1])
                        for p in range (len(prop_list)):
                            write_output.append(default) 
                            for m in range (len(temp)):
                                if prop_list[p] in temp[m]:
                                    write_output[p] = int(temp[m].split()[1])
                                        
    for prop in range (len(prop_list)):
        if prop_list[prop] == 'temperature':
            print('** Starting files temperature.out **')
            cat_temperature(dir_list, step, write_output[prop])   
            print('temperature :  DONE\n')

        if prop_list[prop] == 'xyz':
            print('** Starting files trajectories.xyz **')
            nat = read_data(str(dir_list[0])+'/data.inpt')
            cat_xyz(dir_list, step, nat, write_output[prop])
            print('xyz :  DONE')

        if prop_list[prop] == 'traj':
            print('** Starting files trajectories.out **')
            nat = read_data(str(dir_list[0])+'/data.inpt')
            cat_traj(dir_list, step, nat, write_output[prop])
            print('traj :  DONE')


    print('**********************************************')
    print('*********    !!   ALL  DONE   !!     *********')
    print('**********************************************\n')

    
if __name__ == '__main__':
    main()
                           
