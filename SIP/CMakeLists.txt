#
# OpenBTS/SIP/CMakeLists.txt
#

add_library(openbts-sip STATIC
	SIP2Interface.cpp
	SIPBase.cpp
	SIPDialog.cpp
	SIPMessage.cpp
	SIPParse.cpp
	SIPRtp.cpp
	SIPTransaction.cpp
	SIPUtility.cpp
)
target_link_libraries(openbts-sip ortp osip2)
