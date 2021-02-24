#!/usr/bin/env python
# coding: utf-8

def cat_stress(dir_list, step, freq):
    fout = open('stress_tensor_cat_1-'+str(len(dir_list))+'.out', 'w')
    header = '# Stress tensor of the system\n'\
             '# ----------------\n'\
             '# Pressure:   1 bar = 3.3988273773641905e-09 ua\n'\
             '# step        xx component            yy component            zz component'\
             '            xy component            xz component            yz component\n'      
    fout.write(header)
    count = 0
    for i in range (len(dir_list)):
        fin = open(str(dir_list[i])+'/stress_tensor.out','r')
        print('    directory '+str(i+1)+'/'+str(len(dir_list)))
        line = fin.readline()
        line = fin.readline()
        line = fin.readline()
        line = fin.readline()

        if i < (len(dir_list)-1):
            for j in range(int(step[i]/freq)):
                line = fin.readline()
                fout.write('{0:8s} {1} {2} {3} {4} {5} {6}\n'.format(
                          str(int(line.split()[0])+count), line.split()[1], line.split()[2],
                          line.split()[3], line.split()[4], line.split()[5], line.split()[6]))
        else : 
            for j in range(int(step[i]/freq)+1):
                line = fin.readline()
                fout.write('{0:8s}    {1} {2} {3} {4} {5} {6}\n'.format(
                           str(int(line.split()[0])+count), line.split()[1], line.split()[2],
                           line.split()[3], line.split()[4], line.split()[5], line.split()[6]))

        count = count + step[i]

