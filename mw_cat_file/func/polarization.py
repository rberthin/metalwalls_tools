#!/usr/bin/env python
# coding: utf-8
# Roxanne Berthin <roxanne.berthin@sorbonne-universite.fr>, version 16/02/2021


def cat_pol(dir_list, step, freq):
    fout = open('polarization_cat_1-'+str(len(dir_list))+'.out', 'w')
    header = '# Polarization of the simulation cell in atomic unit\n'\
             '# -----------------------------------------\n'\
             '# Polarization:   1 au =  57.214 765 75 C/m2\n'
    fout.write(header)
    count = 0
    for i in range (len(dir_list)):
        fin = open(str(dir_list[i])+'/polarization.out','r')
        print('    directory '+str(i+1)+'/'+str(len(dir_list)))
        line = fin.readline()
        line = fin.readline()
        line = fin.readline()

        if i < (len(dir_list)-1):
            for j in range(int(step[i]/freq)):
                line = fin.readline()
                fout.write('{0:8s} {1} {2} {3}\n'.format(
                          str(int(line.split()[0])+count), line.split()[1], 
                                  line.split()[2], line.split()[3]))
        else : 
            for j in range(int(step[i]/freq)+1):
                line = fin.readline()
                fout.write('{0:8s} {1} {2} {3}\n'.format(
                           str(int(line.split()[0])+count), line.split()[1],
                               line.split()[2], line.split()[3]))

        count = count + step[i]

