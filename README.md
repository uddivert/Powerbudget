## Input: 
Power Verification Engine takes in one input, a formatted .csv timeline of possible satellite operations including information on time, anticipated submode, solar intensity, and power generation. An example of the correct formatting can be found in the home directory as example.csv. Also the initial state of the satellite (including initial battery level are enumerated at the top of the engine.py and genCsv() respectively and should be changed as necessary for each test). I plan to make a second input as either a json string or another .csv file to set the initial satellite state but for now just change those values.

## Processing:
The engine runs through the csv row by row after doing some formatting and calls a function for each component with the submode and time interval (time spent in a certain submode). The component functions return the power consumed in Watts during that time in that submode by calculating the interval under the curve (the curve represents the change in Watts/hr power consumed by the component and is derived by interpolating data points gathered through empirical testing).

## Output:
The power consumed by each component, the sum of that power consumption, and the battery power remaining after the gain and loss had been combines with the previous battery power are all written to the output.csv. Furthermore the "pass or fail" of the timeline will be printed to the command line. A timeline is said to "fail" if the power level ever drops below 5W. Else it "Passes".

## Running the engine:
- Ensure the engine imports all of the component files and that each component file has accurate functions for each of the satellites possible submodes. This is subject to change since the submodes and components haven't been nailed down yet.
- Name your timeline powertestdata.csv
- Run $ python engine.py
- Check for output
