#
# OpenBTS/TransceiverRAD1/CMakeLists.txt
#

add_compile_options(-march=native)

set_source_files_properties(../apps/GetConfigurationKeys.cpp PROPERTIES COMPILE_FLAGS -fno-var-tracking-assignments)

include_directories(${CMAKE_CURRENT_SOURCE_DIR})
add_library(openbts-transceiverrad1 STATIC
	DummyLoad.cpp
	FactoryCalibration.cpp
	RAD1Device.cpp
	Transceiver.cpp
	radioInterface.cpp
	rnrad1Core.cpp
	sigProcLib.cpp
        fusb.cpp
        rnrad1Rx.cpp
        rnrad1Tx.cpp
)
target_link_libraries(openbts-transceiverrad1 openbts-common usb-1.0)

add_executable(PowerScanner PowerScanner.cpp ../apps/GetConfigurationKeys.cpp)
add_executable(RAD1Cmd RAD1Cmd.cpp)
add_executable(RAD1RxRawPower RAD1RxRawPower.cpp)
add_executable(RAD1RxRawPowerSweep RAD1RxRawPowerSweep.cpp)
add_executable(RAD1SN RAD1SN.cpp)
add_executable(RAD1ping RAD1ping.cpp)
add_executable(openbts-transceiver-rad1 runTransceiver.cpp)
add_executable(sigProcLibTest sigProcLibTest.cpp)

target_link_libraries(PowerScanner openbts-scanning openbts-transceiverrad1 openbts-gsm)
target_link_libraries(RAD1Cmd openbts-transceiverrad1)
target_link_libraries(RAD1RxRawPower openbts-transceiverrad1)
target_link_libraries(RAD1RxRawPowerSweep openbts-transceiverrad1)
target_link_libraries(RAD1SN openbts-transceiverrad1)
target_link_libraries(RAD1ping openbts-transceiverrad1)
target_link_libraries(openbts-transceiver-rad1 openbts-transceiverrad1 openbts-gsm)
target_link_libraries(sigProcLibTest openbts-transceiverrad1 openbts-gsm)

install(TARGETS openbts-transceiver-rad1
	RUNTIME DESTINATION bin
)

# install(README)
# install(README.Talgorithm)
