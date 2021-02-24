#!/usr/bin/env python
# coding: utf-8

import sys
import argparse
import numpy as np

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

