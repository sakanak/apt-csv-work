# apt-csv-work
Analyzing/modifying CSV proxigram data

Application package requirements:
    matplotlib
    numpy
    pandas
    tkinter
    struct

## Use:
Download applet folder
Run ManipulationInterface.py
    ![alt](https://i.postimg.cc/Kv0k7Tgn/manipinterface.png)

    Enter filepaths in the necessary fields, then click "Load Entered Filepaths"
    To run any other tasks after loading filepaths, click the button corresponding to that task and follow the prompts in your terminal.

### For project description, see Mentorship Deliverables/pdf_versions/CARM Kanigicherla Vishal Final Powerpoint 2020.pptx.pdf

## To-do list and tentative additions for applet:
    - Add whole sample calculations using lattice parameter to *VolumeRadCalc.py*
    - Cluster detection and colocation algorithm
    - Basic proxigram generation
    - Cut *ProxigramPeakDecomp.py* into substituent methods
    
    - POS file handlilng
        - Parse .pos for file length
        - Make graphing software plot >1,000,000 data points
        - Make *MassSpectrum.py* handle more data
    
    - Tentative
        - Integrate SQL to handle larger file sizes
        - Use ML to optimize maximum separation algorithm for dmax/Nmin
        - Optimize calculation for Gibbsian interfacial excess of solute