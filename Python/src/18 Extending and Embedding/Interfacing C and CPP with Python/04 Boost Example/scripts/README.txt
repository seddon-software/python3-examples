Notes:

1. These scripts build for 'i386' by default (don't know why) and I need x86_64
   Therefore I have to set:
   		os.environ["ARCHFLAGS"] = "-arch x86_64"
   		
2. To find the Boost shared libraries on MacOS you must set DYLD_LIBRARY_PATH:
		DYLD_LIBRARY_PATH=/Users/seddon/work/boost_1_57_0/stage/lib

    However, Eclipse only works if you set DYLD_LIBRARY_PATH in Eclipse preferences (Python Interpreter/Environment)
    and doesn't work if you try to set this environment variable in the Python script.
    