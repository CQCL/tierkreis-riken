cmake_minimum_required(VERSION 3.15...3.27)
project(tkr_sqcsub)

if (CMAKE_VERSION VERSION_LESS 3.18)
  set(DEV_MODULE Development)
else()
  set(DEV_MODULE Development.Module)
endif()

find_package(Python 3.8 COMPONENTS Interpreter ${DEV_MODULE} REQUIRED)

if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

# Detect the installed nanobind package and import it into CMake
execute_process(
  COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
  OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE nanobind_ROOT)
find_package(nanobind CONFIG REQUIRED)


set(CMAKE_THREAD_PREFER_PTHREAD TRUE)
set(THREADS_PREFER_PTHREAD_FLAG TRUE)
find_package(Threads REQUIRED)


nanobind_add_module(tkr_sqcsub tkr_sqcsub.cpp)
target_include_directories(tkr_sqcsub PRIVATE /vol0300/share/ra010014/jhpcq_modules/x86/SDK/SQC_library_0.9/include /vol0300/share/ra010014/jhpcq_modules/x86/SDK/SQC_library_0.9/include/)
target_link_directories(tkr_sqcsub PRIVATE /vol0300/share/ra010014/jhpcq_modules/x86/SDK/SQC_library_0.9/include /vol0300/share/ra010014/jhpcq_modules/x86/SDK/SQC_library_0.9/lib /vol0300/share/ra010014/jhpcq_modules/x86/SDK/SQC_library_0.9/lib64)
target_link_libraries(tkr_sqcsub PRIVATE sqc_api sqc_rpc sqc_reqsched sqc_reqinvoker qtmd_sim_invoker sqc_dbmgr sqc_util sqc_rpccommon uuid sqlite3 protobuf absl_leak_check absl_die_if_null absl_log_initialize utf8_validity utf8_range grpc++ grpc address_sorting upb_textformat_lib upb_json_lib upb_wire_lib upb_message_lib utf8_range_lib upb_mini_descriptor_lib upb_mem_lib upb_base_lib absl_statusor gpr absl_log_internal_check_op absl_flags_internal absl_flags_reflection absl_flags_private_handle_accessor absl_flags_commandlineflag absl_flags_commandlineflag_internal absl_flags_config absl_flags_program_name absl_raw_hash_set absl_hashtablez_sampler absl_flags_marshalling absl_log_internal_conditions absl_log_internal_message absl_examine_stack absl_log_internal_format absl_log_internal_proto absl_log_internal_nullguard absl_log_internal_log_sink_set absl_log_internal_globals absl_log_sink absl_log_entry absl_log_globals absl_hash absl_city absl_low_level_hash absl_vlog_config_internal absl_log_internal_fnmatch absl_random_distributions absl_random_seed_sequences absl_random_internal_pool_urbg absl_random_internal_randen absl_random_internal_randen_hwaes absl_random_internal_randen_hwaes_impl absl_random_internal_randen_slow absl_random_internal_platform absl_random_internal_seed_material absl_random_seed_gen_exception absl_status absl_cord absl_cordz_info absl_cord_internal absl_cordz_functions absl_exponential_biased absl_cordz_handle absl_crc_cord_state absl_crc32c absl_crc_internal absl_crc_cpu_detect absl_bad_optional_access absl_strerror absl_str_format_internal absl_synchronization absl_graphcycles_internal absl_kernel_timeout_internal absl_stacktrace absl_symbolize absl_debugging_internal absl_demangle_internal absl_malloc_internal absl_time absl_civil_time absl_strings absl_strings_internal absl_string_view absl_base absl_spinlock_wait absl_int128 absl_throw_delegate absl_time_zone absl_bad_variant_access absl_raw_logging_internal absl_log_severity cares ssl re2 z munge crypto sqc_rpccommon protobuf-c rt pthread dl numa Threads::Threads)
