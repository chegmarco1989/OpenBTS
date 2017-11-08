#
# OpenBTS/Transceiver52M/CMakeLists.txt
#

add_compile_options(-march=native)

include_directories(${CMAKE_CURRENT_SOURCE_DIR})
add_library(openbts-transceiver52m STATIC
	DummyLoad.cpp
	Transceiver.cpp
	convert.c
	convolve.c
	radioClock.cpp
	radioInterface.cpp
	radioVector.cpp
	sigProcLib.cpp

	Resampler.cpp
	radioInterfaceResamp.cpp

	# if UHD
	UHDDevice.cpp

	# if USRP1
	#USRPDevice.cpp
)

add_executable(openbts-transceiver-uhd
	runTransceiver.cpp
)

target_link_libraries(openbts-transceiver-uhd
	openbts-transceiver52m
	openbts-gsm
	openbts-common
	uhd
	Boost::system

)

install(TARGETS openbts-transceiver-uhd
	RUNTIME DESTINATION bin
)

# install(README)
# install(README.Talgorithm)
