#! /usr/bin/env python

import os
import sys
import glob
import math
import time
import shutil
import datetime
import argparse
import susyhitutils
from progressbar import ProgressBar

is_py3 = (sys.version_info > (3, 0))


def main():

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('-c', dest='configfile', required=True, help='Configfile')
    parser.add_argument('-o', dest='outputdir', help='Output directory')

    parser.add_argument('--count', action='store_true', help='Count number of jobs')
    parser.add_argument('--scan', action='store_true', help='Do parameters scan')

    parser.add_argument('--debug', action='store_true', help='Debug output')

    global args
    args = parser.parse_args()

    try:
        if is_py3:
            exec(open(args.configfile).read(), globals())
        else:
            execfile(args.configfile, globals())

        # check needed vectors
        v_mu, v_m1, v_m2, v_m3, v_at, v_gmass, v_msq, v_tanb

    except:
        print('Error in the configile. exit...')
        print('Configfile must have the following vectors: v_m1, v_m2, v_m3, v_mu, v_msq, v_tanb, v_at, v_gmass')
        raise

    def default_filter_par_fn(m1, m2, m3, mu, tanb, msq, at, gmass):
        pass

    def default_filter_slha_fn(slha_path):
        pass

    global filter_fn_par_copy
    try:
        filter_fn_par_copy = filter_par_fn
    except:
        print('No parameter filter function defined in config file')
        filter_fn_par_copy = default_filter_par_fn

    global filter_fn_slha_copy
    try:
        filter_fn_slha_copy = filter_slha_fn
    except:
        print('No filter function defined in config file')
        filter_fn_slha_copy = default_filter_slha_fn

    # Count total jobs
    njobs = 0
    for at in v_at:
        for tanb in v_tanb:
            for msq in v_msq:
                for m3 in v_m3:
                    for m2 in v_m2:
                        for m1 in v_m1:
                            for mu in v_mu:
                                for Gmass in v_gmass:
                                    if filter_fn_par_copy(m1, m2, m3, mu, tanb, msq, at, Gmass):
                                        continue
                                    njobs += 1

    if args.count:
        print('Number of jobs: %i' % njobs)
        return

    # Run directory
    if args.outputdir is None:
        t = datetime.datetime.now()
        datestr = '%s-%s-%s_%s.%s.%s' % (t.year, t.month, t.day, t.hour, t.minute, t.second)
        run_dir = 'SusyGridRun_%s' % datestr
    else:
        run_dir = args.outputdir

    susyhitutils.create_run_directory(run_dir)

    if args.scan:

        # Check scan status
        slha_files = glob.glob('at*.slha')
        if len(slha_files) > 0:
            done_files = [ f for f in slha_files if os.path.isfile(f) ]
            #done_files.sort(key=lambda x: os.path.getmtime(x))
            done_files = done_files[:-1] # FIX: check for errors in done_files
            print('Found %i slha files already done. Continue with the remaining jobs...' % len(done_files))
        else:
            done_files = []

        try:
            bar = ProgressBar(njobs, len(done_files))

            rm_files = 0

            progress = len(done_files) + 1
            for at in v_at:
                for tanb in v_tanb:
                    for msq in v_msq:
                        for m3 in v_m3:
                            for m2 in v_m2:
                                for m1 in v_m1:
                                    for mu in v_mu:
                                        for Gmass in v_gmass:
                                            if filter_fn_par_copy(m1, m2, m3, mu, tanb, msq, at, Gmass):
                                                continue

                                            outfile = 'm1_%s_m2_%s_m3_%s_mu_%s_tanb_%s_msq_%s_at_%s_Gmass_%s.slha' % (m1, m2, m3, mu, tanb, msq, at, Gmass)

                                            if outfile in done_files:
                                                continue

                                            if args.debug:
                                                print (outfile)

                                            susyhitutils.generate_slha(m1, m2, m3, mu, tanb, msq, at, Gmass, outfile, args.debug)


                                            ## Check that the n1 mass is below gluino mass, otherwise remove slha file
                                            if filter_fn_slha_copy(outfile):
                                                rm_files += 1
                                                os.system('rm %s' % outfile)

                                            # if progress%10 == 0:
                                            #     time.sleep(2)

                                            if not args.debug:
                                                bar.print_bar(progress)
                                            progress += 1


            # end of loops
            print('%i files removed beacuse slha filter' % rm_files)

        except KeyboardInterrupt:
            pass


    # Clean directory
    susyhitutils.clean_run_directory()



if __name__ == '__main__':
    main()
