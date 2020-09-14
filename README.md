# My framework with smoke GUI tests for Pronet

##### This reporsitory includes the python framework for simple smoke test.
##### As a testrunner the PyTest framework was used.

## Instalation
##### For packages instalattion the next command should be ruuned in terminal:
*pip3 install -r requirements.txt*


## How to run
##### The runner accepts the path to .csv file as a parameter "--path_to_csv_file". This file should include the next columns:
###### *- name of the trader that should be tested*  - as string
###### *- URL path to the trader's desktop page* - as string
###### *- URL path to the trader's mobile page* - as string
###### *- username for basic authentication* - as string
###### *- password for basic authentication* - as string

##### Also the name of the tested trader should be specified as the "-trader" parameter.
##### The framework uses the pytest-html plugin for report generation and pytest-xdist plugin for multithreading test running.
###### (For more information about these and other pytest plugins, these were used in the framework, see the correspond documentation.)
