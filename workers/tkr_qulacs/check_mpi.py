import qulacs

if qulacs.check_build_for_mpi():
    from mpi4py import MPI

    print("Qulacs built with MPI enabled.")
else:
    print("Qulacs module was build without USE_MPI.")
    exit()
