#----------------------------------------------------------------
# Generated CMake target import file for configuration "BUILD".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "caffe" for configuration "BUILD"
set_property(TARGET caffe APPEND PROPERTY IMPORTED_CONFIGURATIONS BUILD)
set_target_properties(caffe PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_BUILD "proto;proto;/home/jessi12/CNN_local/boost_1_61_0/stage/lib/libboost_system.so;/home/jessi12/CNN_local/boost_1_61_0/stage/lib/libboost_thread.so;/home/jessi12/CNN_local/boost_1_61_0/stage/lib/libboost_filesystem.so;-lpthread;/usr/local/lib/libglog.so;/usr/local/lib/libgflags.a;/usr/local/lib/libprotobuf.so;-lpthread;/usr/lib64/libhdf5_hl.so;/usr/lib64/libhdf5.so;/usr/local/lib/liblmdb.so;/usr/local/lib/libleveldb.so;/usr/lib64/libsnappy.so;/usr/local/cuda-7.5/lib64/libcudart.so;/usr/local/cuda-7.5/lib64/libcurand.so;/usr/local/cuda-7.5/lib64/libcublas.so;opencv_core;opencv_highgui;opencv_imgproc;/usr/lib64/liblapack.so;/usr/lib64/atlas/libptcblas.so;/usr/lib64/atlas/libatlas.so;/usr/local/lib/libpython2.7.so;/home/jessi12/CNN_local/boost_1_61_0/stage/lib/libboost_python.so"
  IMPORTED_LOCATION_BUILD "${_IMPORT_PREFIX}/lib/libcaffe.so.1.0.0-rc3"
  IMPORTED_SONAME_BUILD "libcaffe.so.1.0.0-rc3"
  )

list(APPEND _IMPORT_CHECK_TARGETS caffe )
list(APPEND _IMPORT_CHECK_FILES_FOR_caffe "${_IMPORT_PREFIX}/lib/libcaffe.so.1.0.0-rc3" )

# Import target "proto" for configuration "BUILD"
set_property(TARGET proto APPEND PROPERTY IMPORTED_CONFIGURATIONS BUILD)
set_target_properties(proto PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_BUILD "CXX"
  IMPORTED_LOCATION_BUILD "${_IMPORT_PREFIX}/lib/libproto.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS proto )
list(APPEND _IMPORT_CHECK_FILES_FOR_proto "${_IMPORT_PREFIX}/lib/libproto.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
