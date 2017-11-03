#
# OpenBTS/Control/CMakeLists.txt
#

# TODO - move CollectMSInfo.cpp and RRLPQueryController.cpp to RRLP directory.

add_library(openbts-control STATIC
	CBS.cpp
	ControlTransfer.cpp
	DCCHDispatch.cpp
	L3CallControl.cpp
	L3Handover.cpp
	L3LogicalChannel.cpp
	L3MMLayer.cpp
	L3MobilityManagement.cpp
	L3SMSControl.cpp
	L3StateMachine.cpp
	L3SupServ.cpp
	L3TermCause.cpp
	L3TranEntry.cpp
	L3Utils.cpp
	PagingEntry.cpp
	RRLPServer.cpp
	TMSITable.cpp
)

# install(README.Control)
