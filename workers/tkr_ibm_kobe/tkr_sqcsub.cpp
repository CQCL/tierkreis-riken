#include <cstdlib>
#include <iostream>

#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/tuple.h>

#include "sqc_api.h"
#include "sqc_ecode.h"

#define MAX_QASM_LEN (1024 * 1024)

std::tuple<std::string, std::string>
get_transpile_info()
{
    std::string props = "dummyprops";
    std::string config = "dummyconfig";

    sqcInitOptions *init_options = sqcMallocInitOptions();
    init_options->use_qiskit = 0;
    sqcInitialize(init_options);

    sqcQC *qcir = sqcQuantumCircuit(1);
    sqcIbmdTranspileInfo(qcir, SQC_RPC_SCHED_QC_TYPE_IBM_DACC);

    props = str(qcir->backend_config_json);
    config = str(qcir->backend_props_json);

    return std::tuple<std::string, std::string>(props, config);
}

NB_MODULE(tkr_sqcsub, m)
{
    m.def("get_transpile_info", &get_transpile_info);
}

// int main(int argc, char *argv[])
//{
//   char *config = "";
//   char *props = "s";
//   get_transpile_info(&config, &props);
//
//   return 0;
// }
