#!/usr/bin/env python
'''
Generate HTML from CSV using Python

Run this like:

  python script.py my-data.csv > index.html
'''
import os
import csv
import sys

csv_filename = sys.argv[1]
#csv_filename = ICARUS_PMT_Data
rows = list(csv.reader(open(csv_filename)))

# column holding a file name, used to generate a link to a similarly
# named PDF file assumed to be in the same directory.

# needs work (!)
filename_column = 1

# header
title = "ICARUS PMT CALIBRATION DATA TABLE"
print('''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>%s</title>
</head>
''' %title)

# Start body
print('''
<body>
<h1>%s</h1>
</body>
''' % title)
#print('</body>')

print('''
<hr size="4" noshade>''')

print('''
<body>
<h3><u> 
"Calibration of photomultiplier tubes for the ICARUS experiment"</u></h3>
</body>
''')

print('''
<body>
<h4>
Kees Benkendorfer, Physics Department, Reed College, Portland, OR 97202
</p>
Amelia Camino, Department of Physics and Astronomy, Stony Brook University, Stony Brook, NY 11790
</p>
Hannah Kim, Department of Physics, University of Virginia, Charlottesville, VA 22904
</p>
Milind Diwan and Aiwu Zhang, Physics Department, Brookhaven National Laboratory, Upton, NY 11973
</p>
</h4>
</body>
''')


print('''
<body>
<h4> 
The ICARUS detector is currently being installed and commissioned; as part of this commissioning work, we have calibrated and characterized the electronic response of the photomultiplier tubes (PMTs) at room temperature. For each PMT, we recorded digitized pulses both with and without injected light from a semiconductor laser. We took these data at several voltage settings for the entire array of 360 PMTs. Here are our results from the statistical fits of charge distributions we performed in order to obtain the intensity of the light pulses, the PMT gain as a function of voltage, and a preliminary measurement of their dark rate. This database was made so that these results may be compared to the data that will be obtained when the detector is cooled down to liquid argon temperature (87K) in the coming months.</h4>
</body>
''')

print('''
<body>
<h4>
For more information, please see the following link to our technical note:https://sbn-docdb.fnal.gov/cgi-bin/private/ShowDocument?docid=14169.
</h4>
</body>
''')

print('''
<body>
<h4>
All our code can be found within the git repository here: https://github.com/zhangaw325/ICARUS_PMT_calibration.
</h4>
</body>
''')

# start table
print ('''
<table style = "width:100%">
<caption align = "center">ICARUS PMT Calibration Data</caption>

<tr>
<table border = "3">
''')

print('''
<button ondblclick="A4alert()" style ="background-color:#F5B7B1">Show Alert Message for PMT 4 in chimney A4</button>''')
print('''
<script>
function A4alert(){
alert("PMT 9 in Chimney A4 is dead and therefore no data was taken.");
}
</script>''')

print('''
<button ondblclick="B4alert()" style ="background-color:#F5CBA7">Show Alert Message for PMTs 1-8 in chimney B4</button>''')
print('''
<script>
function B4alert(){
alert("There was a broken fiber cable to the light source for PMTs 1-8 in Chimney B4.");
}
</script>''')

print('''
<button ondblclick="B42alert()" style ="background-color:#F9E79F">Show Alert Message for PMTs 9,10,--, and -- in chimney B4</button>''')
print('''
<script>
function B42alert(){
alert("There was no data taken for PMTs 9,10,--, and -- in Chimney B4.");
}
</script>''')

print('''
<button ondblclick="B16alert()" style ="background-color:#A2D9CE">Show Alert Message for PMT 8 in chimney B16</button>''')
print('''
<script>
function B16alert(){
alert("PMT 8 in Chimney B16 is dead and therefore no data was taken.");
}
</script>''')

print('''
<button ondblclick="C8alert()" style ="background-color:#A9CCE3">Show Alert Message for PMT 9 in chimney C8</button>''')
print('''
<script>
function C8alert(){
alert("The status of PMT 9 in Chimney C8 is unclear as the fiber cable appears to be dead.");
}
</script>''')

for colname in rows[0]:
    if colname == 'Result':
        print('<th colspan="1">%s</th>' % colname)
    elif colname == 'Waveform window':
        print('<th colspan="3">%s</th>' % colname)
    elif colname == 'Dark rate':
        print('<th colspan ="4">%s</th>' % colname)
    elif colname == '':
        print('<th colspan="2">%s</th>' % colname)
    elif colname == 'Gain Calibration':
        print('<th colspan="13">%s</th>' % colname)
    elif colname == 'Gain vs. Voltage':
        print('<th colspan="13">%s</th>' % colname)
    elif colname == 'Afterpulse':
        print('<th colspan="1">%s</th>' % colname)
    else:
        print('<th>%s</th>' % colname)    
print ('</tr>')

print ('<tr>')
for colname in rows[1]:
    if colname == 'chimney':
        print('<th>%s</th>' % colname)
    elif colname == 'PMTch':
        #print('''
         #        <th>waveform window</th>
          #     ''')
        print('<th>%s</th>' % colname)
    elif colname == "voltage":
        print('<th>%s (Volts)</th>' % colname)     
    else:
        print('<th>%s</th>' % colname)
print ('</tr>')
        
# special column for link to PDF
# print ('<th> Charge Distributions (fitted)</th>')
# print ('</tr>')

# Generate table rows.
for count, row in enumerate(rows[2:1310]):
    try:
         pmt = int(row[1])
         chimney = str(row[0])
    except ValueError:
         continue
    if int(count/3)== 0:
        print ('<tr bgcolor="#E0FFFF">')
    elif (int(count/3) % 2) == 0:
        print ('<tr bgcolor="#E0FFFF">')
    else:
        print ('<tr>')
    if chimney == 'B4':
        if pmt in range(1,9):
            print ('<tr bgcolor="#F5CBA7">')
        else:
            print ('<tr bgcolor="#FAD7A0">')
    if chimney == 'B16':
        if pmt == 8:
            print ('<tr bgcolor="#A2D9CE">')
    if chimney == 'C8':
        if pmt == 9:
            print ('<tr bgcolor="#A9CCE3">') 
    for col in row[:-1]:
        print ('<td>%.5s</td>'%col)
    print ('<td><a href="HistofChargeDist/%s">%s</a></td>'%(row[-1], row[-1]))
print ('</tr>')


# end table, body and document
print ('</table>')
print ('</body>')
print ('</html>')
