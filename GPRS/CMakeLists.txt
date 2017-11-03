#
# OpenBTS/GPRS/CMakeLists.txt
#

add_library(openbts-gprs STATIC
	ByteVector.cpp
	FEC.cpp
	GPRSCLI.cpp
	MAC.cpp
	MSInfo.cpp
	MsgBase.cpp
	RLC.cpp
	RLCEngine.cpp
	RLCEngine.cpp
	RLCMessages.cpp
	TBF.cpp
	#BSSG.cpp
	#BSSGMessages.cpp
)
