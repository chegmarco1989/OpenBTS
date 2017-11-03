#
# OpenBTS/SGSNGGSN/CMakeLists.txt
#

add_library(openbts-sgsnggsn STATIC
	GPRSL3Messages.cpp
	Ggsn.cpp
	LLC.cpp
	Sgsn.cpp
	SgsnCli.cpp
	iputils.cpp
	miniggsn.cpp
)
