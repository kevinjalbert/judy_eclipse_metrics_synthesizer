#Information

*Author*:    Kevin Jalbert  (blitzbolt@gmail.com)

*Copyright*: Copyright (c) 2011 Kevin Jalbert

*License*:   MIT License

This program will take the output of the [eclipse\_metrics\_xml\_reader](https://github.com/kevinjalbert/eclipse_metrics_xml_reader "Eclipse Metrics XML Reader") and the mutation score output of [Judy](http://www.e-informatyka.pl/sens/Wiki.jsp?page=Projects.Judy "Judy") and synthesies into a working format for [libsvm](http://www.csie.ntu.edu.tw/~cjlin/libsvm/ "libsvm"). More details about the program are found in the [Wiki](https://github.com/kevinjalbert/judy_eclipse_metrics_synthesizer/wiki "Wiki").

#Pre-Requirements
This program takes advantage of [Python 2.7](http://www.python.org/ "Python")

* libsvm output of [eclipse\_metrics\_xml\_reader](https://github.com/kevinjalbert/eclipse_metrics_xml_reader "Eclipse Metrics XML Reader")
* XML output of [Judy](http://www.e-informatyka.pl/sens/Wiki.jsp?page=Projects.Judy "Judy")
* Python [xlrd](http://www.python-excel.org/ "Python Excel - xlrd") library

_The python command is linked to the 2.7 version of Python_

#Execution
1. Download the source code and place it into a directory of choice
2. Execute using the following command ```python judy_eclipse_metrics_synthesizer.py [OPTIONS]```
3. Resulting files will be found in the same directory as the input file

#Options
To see a list of the options run the following command ```python judy_eclipse_metrics_synthesizer.py -h```


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/kevinjalbert/judy_eclipse_metrics_synthesizer/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

