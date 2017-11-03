#
# OpenBTS/GSM/CMakeLists.txt
#

add_library(openbts-gsm STATIC
	GSM610Tables.cpp
	GSMCCCH.cpp
	GSMChannelHistory.cpp
	GSMCommon.cpp
	GSMConfig.cpp
	GSML1FEC.cpp
	GSML2LAPDm.cpp
	GSML3CCElements.cpp
	GSML3CCMessages.cpp
	GSML3CommonElements.cpp
	GSML3GPRSElements.cpp
	GSML3MMElements.cpp
	GSML3MMMessages.cpp
	GSML3Message.cpp
	GSML3RRElements.cpp
	GSML3RRMessages.cpp
	GSML3SSMessages.cpp
	GSMLogicalChannel.cpp
	GSMRadioResource.cpp
	GSMSMSCBL3Messages.cpp
	GSMTAPDump.cpp
	GSMTDMA.cpp
	GSMTransfer.cpp
	PhysicalStatus.cpp
	PowerManager.cpp
)
