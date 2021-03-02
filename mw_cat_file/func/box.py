#!/usr/bin/env python
# coding: utf-8

def cat_box(dir_list, step, freq):
    fout = open('box_parameters_cat_1-'+str(len(dir_list))+'.out', 'w')
    header = '# Box parameters of the system\n'\
             '# ----------------------------\n'\
             '# Length:   1 au = 0.052917721067 nm\n'\
             '# Volume:   1 ua = 1.48184711276e-4 nm**3\n'\
             '# step          length(1)               length(2)'\
             '               length(3)                volume\n'      
    fout.write(header)
    count = 0
    for i in range (len(dir_list)):
        fin = open(str(dir_list[i])+'/box_parameters.out','r')
        print('    directory '+str(i+1)+'/'+str(len(dir_list)))
        line = fin.readline()
        line = fin.readline()
        line = fin.readline()
        line = fin.readline()
        line = fin.readline()

        if i < (len(dir_list)-1):
            for j in range(int(step[i]/freq)):
                line = fin.readline()
                fout.write('{0:8s} {1} {2} {3} {4}\n'.format(
                          str(int(line.split()[0])+count), line.split()[1], line.split()[2],
                          line.split()[3], line.split()[4]))
        else : 
            for j in range(int(step[i]/freq)+1):
                line = fin.readline()
                fout.write('{0:8s}    {1} {2} {3} {4}\n'.format(
                           str(int(line.split()[0])+count), line.split()[1], line.split()[2],
                           line.split()[3], line.split()[4]))

        count = count + step[i]

