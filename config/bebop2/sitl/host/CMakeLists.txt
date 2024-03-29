include(../set-vars.cmake)

add_subdirectory(${PROJECT_SOURCE_DIR}/tools/sitl_gazebo gazebo)
set(GAZEBO_PLUGIN_BUILD_DIR ${CMAKE_CURRENT_BINARY_DIR}/gazebo)
set(GAZEBO_WORLDS_DIR ${PROJECT_SOURCE_DIR}/tools/sitl_gazebo/worlds)
set(GAZEBO_MODELS_DIR ${PROJECT_SOURCE_DIR}/tools/sitl_gazebo/models)
set(JMAVSIM_DIR ${PROJECT_SOURCE_DIR}/tools/jmavsim)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/start-gazebo.in ${CMAKE_CURRENT_BINARY_DIR}/start-gazebo @ONLY)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/start-jmavsim.in ${CMAKE_CURRENT_BINARY_DIR}/start-jmavsim @ONLY)

# Build the 'Ground Node' for CFDP file transfer.
#initialize_airliner_build(
#    PREFIX gndnode-
#    PSP ${HOST_PSP}
#    OSAL ${HOST_OSAL}
#    CONFIG
#        ${CMAKE_CURRENT_SOURCE_DIR}/inc
#        ${CMAKE_CURRENT_SOURCE_DIR}/../../../shared/inc
#    FILESYS
#        /cf/apps
#        /cf/download
#        /cf/log
#        /cf/upload
#        /ram
#    STARTUP_SCRIPT
#        ${CMAKE_CURRENT_SOURCE_DIR}/cfe_es_startup.scr
#    
#    CONFIG_SOURCES
#        ${CMAKE_CURRENT_SOURCE_DIR}/../../../shared/inc/cfe_mission_cfg.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../../../shared/inc/cfe_msgids.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/inc/osconfig.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/inc/cfe_platform_cfg.h
#)
#
#add_airliner_app(
#    px4lib
#    DEFINITION ${PROJECT_SOURCE_DIR}/apps/px4lib/fsw/for_build)
#    
#add_airliner_app(
#    pblib
#    DEFINITION ${PROJECT_SOURCE_DIR}/apps/pblib/fsw/for_build)
#
#add_airliner_app(
#    sch
#    DEFINITION ${PROJECT_SOURCE_DIR}/apps/sch/fsw/for_build
#    CONFIG     ${CMAKE_CURRENT_SOURCE_DIR}/apps/sch
#    CONFIG_SOURCES
#        ${CMAKE_CURRENT_SOURCE_DIR}/apps/sch/sch_custom_rt.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../inc/sch_platform_cfg.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../inc/sch_msgids.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../../../shared/inc/sch_perfids.h
#    )
#
#add_airliner_app(
#    cf
#    DEFINITION ${PROJECT_SOURCE_DIR}/apps/cf/fsw/for_build
#    CONFIG     ${CMAKE_CURRENT_SOURCE_DIR}/apps/cf
#    CONFIG_SOURCES
#        ${CMAKE_CURRENT_SOURCE_DIR}/../inc/cf_platform_cfg.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../inc/cf_msgids.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../../../shared/inc/cf_perfids.h
#    )
#
#add_airliner_app(
#    ci
#    DEFINITION ${PROJECT_SOURCE_DIR}/apps/ci/fsw/for_build
#    CONFIG     ${CMAKE_CURRENT_SOURCE_DIR}/apps/ci
#    CONFIG_SOURCES
#        ${CMAKE_CURRENT_SOURCE_DIR}/apps/ci/ci_custom.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../inc/ci_platform_cfg.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../inc/ci_msgids.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../../../shared/inc/ci_mission_cfg.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../../../shared/inc/ci_perfids.h
#    )
#
#add_airliner_app(
#    to
#    DEFINITION ${PROJECT_SOURCE_DIR}/apps/to/fsw/for_build
#    CONFIG     ${CMAKE_CURRENT_SOURCE_DIR}/apps/to
#    CONFIG_SOURCES
#        ${CMAKE_CURRENT_SOURCE_DIR}/apps/to/to_custom.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/apps/to/to_custom_udp.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../inc/to_platform_cfg.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../inc/to_msgids.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../../../shared/inc/to_mission_cfg.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../../../shared/inc/to_perfids.h
#    )


