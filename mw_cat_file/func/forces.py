#!/usr/bin/env python
# coding: utf-8


def cat_forces(dir_list, step, nat, freq):
    fout = open('forces_cat_1-'+str(len(dir_list))+'.xyz', 'w')
    header = '# Forces on mobile particles in atomic unit\n'\
             '# -----------------------------------------\n'\
             '# Force:   1 au = 8.2387225e-8 N = 51.421 eV/angstrom\n'\
             '#      fx_total                fy_total                fz_total'\
             '               fx_coulomb              fy_coulomb              fz_coulomb'\
             '           fx_intermolecular       fy_intermolecular       fz_intermolecular'\
             '       fx_intramolecular       fy_intramolecular       fz_intramolecular\n'
    fout.write(header)
    for i in range (len(dir_list)):
        print('    directory '+str(i+1)+'/'+str(len(dir_list)))
        fin = open(str(dir_list[i])+'/forces.out','r')
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
                    fout.write('{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}'\
                               '{10} {11}\n'.format(line.split()[0], line.split()[1], 
                               line.split()[2], line.split()[3], line.split()[4], 
                               line.split()[5],line.split()[6], line.split()[7],
                               line.split()[8], line.split()[9],line.split()[10],
                               line.split()[11]))
        else :
            for j in range(int(step[i]/freq)+1):
                l = fin.readline()
                fout.write(l)
                for k in range (nat):
                    line = fin.readline()
                    fout.write('{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}'\
                               '{10} {11}\n'.format(line.split()[0], line.split()[1], 
                               line.split()[2], line.split()[3], line.split()[4], 
                               line.split()[5],line.split()[6], line.split()[7],
                               line.split()[8], line.split()[9],line.split()[10], 
                               line.split()[11]))


