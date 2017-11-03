#
# OpenBTS/GSMShare/CMakeLists.txt
#

add_library(openbts-gsmshare STATIC
	A51.cpp
	AmrCoder.cpp
	GSM503Tables.cpp
	L3Enums.cpp
	ViterbiR204.cpp
)
	
add_executable(A51Test A51Test.cpp)
add_executable(AMRTest AMRTest.cpp)
add_executable(ViterbiTest ViterbiTest.cpp)

target_link_libraries(A51Test
	openbts-globals openbts-gsmshare openbts-gsm openbts-common sqlite3)
target_link_libraries(AMRTest
	openbts-globals openbts-gsmshare openbts-gsm openbts-common sqlite3)
target_link_libraries(ViterbiTest
	openbts-globals openbts-gsmshare openbts-gsm openbts-common sqlite3)

add_test(A51Test A51Test)
add_test(AMRTest AMRTest)
add_test(ViterbiTest ViterbiTest)
