#include "sqc_api.h"
#include "sqc_ecode.h"
#include <stdlib.h>
#include <string.h>

#define MAX_QASM_LEN (1024 * 1024)

struct BackendProperties
{
  char *config;
  char *props;
};

struct BackendProperties
get_transpile_info()
{
  sqcInitOptions *init_options = sqcMallocInitOptions();
  init_options->use_qiskit = 0;
  sqcInitialize(init_options);

  sqcQC *qcir = sqcQuantumCircuit(1);
  sqcIbmdTranspileInfo(qcir, SQC_RPC_SCHED_QC_TYPE_IBM_DACC);
  struct BackendProperties props = {
      .config = qcir->backend_config_json,
      .props = qcir->backend_props_json};

  return props;
}

int main(int argc, char *argv[])
{
  struct BackendProperties props = get_transpile_info();
  printf("%s", props.config);
  return 0;
}
