# apt-csv-work
Analyzing/modifying CSV proxigram data

ManualPeakDecomp.py requires:
    Proxigram CSV file
    Knowledge of unknown peaks (#, constituent elements w/ %s)
    Understanding which columns user wants to retain and discard

ManualPeakDecomp.py uses the pandas library to parse the proxigram CSV file, and matplotlib in order to generate the final scatterplot.

There are three files ManualPeakDecomp.py interacts with. The first is the original CSV file, the examplee in this repository with name steelrntest.csv. From that file, unknown peaks are separated into their constituent elements, and the file is rewritten into an intermediate, in this repository as steelmod.csv. The third file is the final, with percentages instead of atom counts, and data deemed irrelevant to analysis by user discarded. That file is used to generate the scatterplot to visualize concentration distribution, while the intermediate second file will be used after 'core' region identification for further statistics. The third file exists in the repository as steelgraph.csv.


ColumnModCheck.py prints two columns of data from two distinct CSV files that have the same header (Ex. Al %) to check that intermediate files have transferred the correct data.