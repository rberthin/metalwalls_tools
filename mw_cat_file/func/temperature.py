#!/usr/bin/env python
# coding: utf-8

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
                           str(int(line.split()[0])+count), line.split()[1]))

        count = count + step[i]

