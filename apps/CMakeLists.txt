#
# OpenBTS/apps/CMakeLists.txt
#

set_source_files_properties(GetConfigurationKeys.cpp PROPERTIES COMPILE_FLAGS -fno-var-tracking-assignments)

add_executable(OpenBTS
	GetConfigurationKeys.cpp
	OpenBTS.cpp
)

target_link_libraries(OpenBTS
	openbts-cli
	openbts-sip
	openbts-gsm
	openbts-gsmshare
	openbts-gprs
	openbts-sgsnggsn
	openbts-trxmanager
	openbts-control
	openbts-sms
	openbts-peering
	openbts-nodemanager
	openbts-globals
	openbts-common
	a53
	zmq
)


add_executable(OpenBTSCLI
	OpenBTSCLI.cpp
)

target_compile_options(OpenBTSCLI PUBLIC -DBUILD_CLI)

target_link_libraries(OpenBTSCLI openbts-globals readline)


add_executable(JSONEventsClient
	JSONEventsClient.cpp
)

target_link_libraries(JSONEventsClient zmq)

# install(CLI)
# install(OpenBTS.example.sql)
# install(OpenBTSDo)
# install(exportConfigTable.sh)
# install(generateConfigTable.sh)
# install(generateTeX.sh)
# install(importConfigTable.sh)
# install(iptables.rules)
# install(logrotated.OpenBTS)
# install(openbts.conf)
# install(openbtsconfig)
# install(rsyslogd.OpenBTS.conf)
