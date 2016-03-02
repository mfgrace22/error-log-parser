"""Script to strip out test errors and failures so they can be rerun."""

# first, open up the test.log file located at /home/matt/test.log

# next, for each line in file, if the line begins with "ERROR: " or "FAIL: ",
# copy the ENTIRE LINE, and write it to a new file.

# for each line in the NEW file, replace "ERROR: " with "" and replace "FAIL: "
# with ""

# replace ") " with "."

# for each line from the BOL to the "(", copy the text and past it at EOL after
# the "."

# replace "(" with ""

# make sure to trim off any spaces at BOL or EOL

# construct a string of all of the lines formatted as:

"""
'line 1\n
 line 2\n
 line 3\n
 ...
 line n\n'
"""

# construct the variable for rerunning the test failures
test_failures='clinic_portal.tests.seltest_clinic_selenium.BankAccountFormTests.test_IWI_custom_requirements'
