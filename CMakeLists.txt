#
# OpenBTS/CMakeLists.txt
#

cmake_minimum_required(VERSION 3.0)

project(OpenBTS)

option(ORTP_NEW_API "New API of libortp" ON)  # FIXME
option(USE_COREDUMPER "Use libcoredumper" ON)  # FIXME
option(USE_UHD "Use UHD transceiver" ON)  # FIXME
option(USE_UHD_3_9 "Use UHD transceiver (>= v3.9)" ON)  # FIXME
option(USE_RAD1 "Use RAD1 transceiver" ON)  # FIXME

enable_testing()

include(cmake/features.cmake)

find_package(Boost COMPONENTS system)
find_library(ZMQ zmq REQUIRED)

add_compile_options(-g)
add_compile_options(-O2)
add_compile_options(-Wall)
add_compile_options(-Werror)
add_compile_options(-Wno-nonnull-compare)
add_compile_options(-pthread)
add_definitions(-DTIMESTAMP_ISO="unknown")
#add_definitions(-DTIMESTAMP_ISO=`date +'"%Y-%m-%dT%H:%M:%S"'`)
add_definitions(-DREPO_REV="unknown")
#add_definitions(-D'REPO_REV="$(shell ./$(top_builddir)/Globals/GrabRepoInfo.sh $(top_builddir))"')

add_definitions(-DHAVE_CONFIG_H)
configure_file(config-cmake.h.in config.h)

set(OPENBTS_COMMON_LIBRARIES -rdynamic sqlite3 pthread dl)

include_directories(${PROJECT_SOURCE_DIR})  # required in apps/OpenBTS.cpp
include_directories(${PROJECT_BINARY_DIR})  # required for <config.h>
include_directories(CLI)
include_directories(CommonLibs)
include_directories(Control)
include_directories(GPRS)
include_directories(GSM)
include_directories(GSMShare)
include_directories(Globals)
include_directories(NodeManager)
include_directories(NodeManager/JsonBox-0.4.3/include)
include_directories(Peering)
include_directories(SGSNGGSN)
include_directories(SIP)
include_directories(SMS)
include_directories(Scanning)
include_directories(TRXManager)
include_directories(apps)

#COMMON_LA = $(top_builddir)/CommonLibs/libcommon.la
#GSM_LA = $(top_builddir)/GSM/libGSM.la
#GSMSHARE_LA = $(top_builddir)/GSMShare/libGSMShare.la
#GPRS_LA = $(top_builddir)/GPRS/libGPRS.la
#SGSNGGSN_LA = $(top_builddir)/SGSNGGSN/libSGSNGGSN.la
#SIP_LA = $(top_builddir)/SIP/libSIP.la
#SMS_LA = $(top_builddir)/SMS/libSMS.la
#TRX_LA = $(top_builddir)/TRXManager/libtrxmanager.la
#CONTROL_LA = $(top_builddir)/Control/libcontrol.la
#GLOBALS_LA = $(top_builddir)/Globals/libglobals.la
#CLI_LA = $(top_builddir)/CLI/libcli.la
#PEERING_LA = $(top_builddir)/Peering/libpeering.la
#NODEMANAGER_LA = $(top_builddir)/NodeManager/libnodemanager.la -lzmq
#SCANNING_LA = $(top_builddir)/Scanning/libscanning.la

add_subdirectory(CLI)
add_subdirectory(CommonLibs)
add_subdirectory(Control)
add_subdirectory(GPRS)
add_subdirectory(GSM)
add_subdirectory(GSMShare)
add_subdirectory(Globals)
add_subdirectory(NodeManager)
add_subdirectory(Peering)
add_subdirectory(SGSNGGSN)
add_subdirectory(SIP)
add_subdirectory(SMS)
add_subdirectory(Scanning)
add_subdirectory(TRXManager)
add_subdirectory(Transceiver52M)
#add_subdirectory(TransceiverRAD1)
add_subdirectory(apps)
#add_subdirectory(doc)

# install(INSTALLATION)
# install(LEGAL)
# install(COPYING)
# install(README.APIs)
# install(README)
