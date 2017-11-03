#
# OpenBTS/CLI/CMakeLists.txt
#

add_library(openbts-cli STATIC
	CLI.cpp
	CLIBase.cpp
	CLICommands.cpp
	CLIServer.cpp
)

# install(README.CLI)
