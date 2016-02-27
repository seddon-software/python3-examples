
Hi Sue/Mark,

As promised, a summary of the 3 courses proposed at yesterday's meeting.  Note that this is not final - examples need to be worked out and the latest software to be made available.

1. Software Engineering with Python (3 days)
    Target audience: Technical group with good programming skills
    Day 1: Basic Python including lists, tuples, dict and functions.  Classes, modules and packages, inheritance
    Day 2: More Advanced Python: functional including comprehensions, lambdas, decorators, generators and closures.
    Day 3: Libraries: Numpy, SciSoftPy, Scipy, Matplotlib, Sympy, Pandas, SciKitLearn, SkiKitImage.
    Also included: using GIT, TDD, Eclipse, iPython, but not Jython
    Course Objective: attendees to be able to write high quality Python code following modern programming practice

2. Diamond Data Analysis with Python (3 days)
    Target audience: Beamline Scientists ???
    Day 1: 1st half day: Basic Python including lists, tuples, dict and functions, but not Object Orientation.
                2nd half day: Modules, packages and the Numpy/SciSoftPy libraries
    Days 2 and 3: Examples of using libraries (SciSoftPy, Scipy, Matplotlib, Sympy, Pandas, SciKitLearn, SkiKitImage) with real data from beamlines:
                Cells example from B22: count number of cells
                Pandas: analyses directories containing experiments to generate statistics
                Fitting: fitting with Gaussians
                Splitting large hdf5 files into a large set of text files and tif files
                Plus other (to be decided) examples
    Also included: using GIT, Eclipse, iPython, but not TDD and Jython.  Will advertise the drop-in sessions.
    Course Objective: attendees to be able to write complex Python scripts with emphasis on utilising the most popular Python Scientific libraries.

3. Diamond Data Acquisition with Jython (3 days) - needs some work
    Target audience: Beamline Scientists working with GDA
    Day 1: Basic Python including lists, tuples, dict and functions, but not Object Orientation (at the suggestion of Rob Walton).
    Days 2 and 3: Not finalised, but based around practical work with sans and scripting on the GDA
        The existing course coverage plotting and fitting - this needs to be extended with extra examples such as:
            slit and vacuum pumping example using pid loop
            use of Mandelbrot simulated detector
            maybe create fake pressure and energy detectors
            Rob suggested simulating elliptical bean and using Python to orientate and center the beam using fake motor simulators
    Also included: using GDA with Jython, but not Python. SciSoftPy.  Maybe the macro facility.  Not sure about explaining built in GDA functionality that is not Jython specific.
    Course Objective: attendees to be able to fully use the scripting capabilities of the GDA

Comments welcome,
Chris


