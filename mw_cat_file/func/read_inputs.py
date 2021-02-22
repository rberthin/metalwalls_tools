#!/usr/bin/env python
# coding: utf-8
# Roxanne Berthin <roxanne.berthin@sorbonne-universite.fr>, version 16/02/2021


def read_data(file):
    with open(file) as dat:
        for line in dat:
            if (line.lstrip()).startswith("num_atoms"):
                nbatoms = float(line.split()[1])
    return int(nbatoms)



def read_runtime(directory, propertie):
    step = []
    default = 0
    write_output = []
    for i in range (len(directory)):
        with open(str(directory[i])+'/runtime.inpt') as run:
            for line in run:
                if (line.lstrip()).startswith("num_steps"):
                    step.append(int(line.split()[1]))

                if i == 0:
                    if (line.lstrip()).startswith("output"):
                        temp = run.readlines()
                        for j in range (len(temp)):
                            if 'default' in temp[j]:
                                default = int(temp[j].split()[1])
                        for p in range (len(propertie)):
                            write_output.append(default)
                            for m in range (len(temp)):
                                if propertie[p] in temp[m]:
                                    write_output[p] = int(temp[m].split()[1])

    return step, write_output

