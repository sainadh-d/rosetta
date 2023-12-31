# Merge and aggregate datasets

## Task Link
[Rosetta Code - Merge and aggregate datasets](https://rosettacode.org/wiki/Merge_and_aggregate_datasets)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.DoubleSummaryStatistics;
import java.util.List;

public final class MergeAndAggregateDatasets {

	public static void main(String[] args) {
		List<Patient> patients = Arrays.asList(
			new Patient("1001", "Hopper"),
			new Patient("4004", "Wirth"),
			new Patient("3003", "Kemeny"),
			new Patient("2002", "Gosling"),
			new Patient("5005", "Kurtz") );

		List<Visit> visits = Arrays.asList(				
		    new Visit("2002", "2020-09-10", 6.8),
		    new Visit("1001", "2020-09-17", 5.5),
		    new Visit("4004", "2020-09-24", 8.4),
		    new Visit("2002", "2020-10-08", null),
		    new Visit("1001", ""          , 6.6),
		    new Visit("3003", "2020-11-12", null),
		    new Visit("4004", "2020-11-05", 7.0),
		    new Visit("1001", "2020-11-19", 5.3) );
		
		Collections.sort(patients, Comparator.comparing(Patient::patientID));		
		System.out.println("| PATIENT_ID | LASTNAME | LAST_VISIT | SCORE_SUM | SCORE_AVG |");		
	    for ( Patient patient : patients ) {	    	
	    	List<Visit> patientVisits = visits.stream().filter( v -> v.visitID == patient.patientID() ).toList();
	    	String lastVisit = patientVisits.stream()
	    		.map( v -> v.visitDate ).max(Comparator.naturalOrder()).orElseGet( () -> "   None   " );	    	
	    	DoubleSummaryStatistics statistics = patientVisits.stream()
	    		.filter( v -> v.score != null ).mapToDouble(Visit::score).summaryStatistics();	    		    	
	    	double scoreSum = statistics.getSum();
	    	double scoreAverage = statistics.getAverage();	    	
	    	String patientDetails = String.format("%12s%11s%13s%12.2f%12.2f", 
	    		patient.patientID, patient.lastName, lastVisit, scoreSum, scoreAverage);	    	
	    	System.out.println(patientDetails);
	    }

        private static record Patient(String patientID, String lastName) {};
	    private static record Visit(String visitID, String visitDate, Double score) {};

	} 

}

```

## Python Code
### python_code_1.txt
```python
# to install pandas library go to cmd prompt and type:
# cd %USERPROFILE%\AppData\Local\Programs\Python\Python38-32\Scripts\
# pip install pandas
import pandas as pd

# load data from csv files
df_patients = pd.read_csv (r'patients.csv', sep = ",", decimal=".")
df_visits = pd.read_csv (r'visits.csv', sep = ",", decimal=".")

''' # load data hard coded, create data frames
import io
str_patients = """PATIENT_ID,LASTNAME
1001,Hopper
4004,Wirth
3003,Kemeny
2002,Gosling
5005,Kurtz
"""
df_patients = pd.read_csv(io.StringIO(str_patients), sep = ",", decimal=".")
str_visits = """PATIENT_ID,VISIT_DATE,SCORE
2002,2020-09-10,6.8
1001,2020-09-17,5.5
4004,2020-09-24,8.4
2002,2020-10-08,
1001,,6.6
3003,2020-11-12,
4004,2020-11-05,7.0
1001,2020-11-19,5.3
"""
df_visits = pd.read_csv(io.StringIO(str_visits), sep = ",", decimal=".")
'''

# typecast from string to datetime so .agg can 'max' it
df_visits['VISIT_DATE'] = pd.to_datetime(df_visits['VISIT_DATE'])

# merge on PATIENT_ID
df_merge = df_patients.merge(df_visits, on='PATIENT_ID', how='left')

# groupby is an intermediate object
df_group = df_merge.groupby(['PATIENT_ID','LASTNAME'], as_index=False)

# note: you can use 'sum' instead of the lambda function but that returns NaN as 0 (zero)
df_result = df_group.agg({'VISIT_DATE': 'max', 'SCORE': [lambda x: x.sum(min_count=1),'mean']})

print(df_result)

```

### python_code_2.txt
```python
import csv

fnames = 'patients.csv  patients_visits.csv'.split()

def csv2list(fname):
    with open(fname) as f:
        rows = list(csv.reader(f))
    return rows

patients, visits = data = [csv2list(fname) for fname in fnames]
result = [record.copy() for record in patients]
result[1:] = sorted(result[1:])
#%%
result[0].append('LAST_VISIT')
last = {p: vis for p, vis, *score in visits[1:]}
for record in result[1:]:
    p = record[0]
    record.append(last.get(p, ''))
#%%
result[0] += ['SCORE_SUM', 'SCORE_AVG']
n = {p: 0 for p, *_ in patients[1:]}
tot = n.copy()
for record in visits[1:]:
    p, _, score = record
    if score:
        n[p] += 1
        tot[p] += float(score)
for record in result[1:]:
    p = record[0]
    if n[p]:
        record += [f"{tot[p]:5.1f}", f"{tot[p] / n[p]:5.2f}"]
    else:
        record += ['', '']
#%%
for record in result:
    print(f"| {' | '.join(f'{r:^10}' for r in record)} |")

```

### python_code_3.txt
```python
import sqlite3
import csv


fnames = 'patients.csv  patients_visits.csv'.split()
conn = sqlite3.connect(":memory:")
#%%
    
def create_table_headers(conn):
    curs = conn.cursor()
    curs.execute('''
      CREATE TABLE patients(PATIENT_ID INT, LASTNAME TEXT);
    ''')
    curs.execute('''
      CREATE TABLE patients_visits(PATIENT_ID INT, VISIT_DATE DATE, SCORE NUMERIC(4,1));
    ''')
    conn.commit()

def fill_tables(conn, fnames):
    curs = conn.cursor()
    for fname in fnames:
        with open(fname) as f:
            tablename = fname.replace('.csv', '')
            #
            csvdata = csv.reader(f)
            header = next(csvdata)
            fields = ','.join('?' for _ in header)
            for row in csvdata:
                row = [(None if r == '' else r) for r in row]
                curs.execute(f"INSERT INTO {tablename} VALUES ({fields});", row)
    conn.commit()

def join_tables_and_group(conn):
    curs = conn.cursor()
    curs.execute('''
CREATE TABLE answer AS
    SELECT
    	patients.PATIENT_ID,
    	patients.LASTNAME,
    	MAX(VISIT_DATE) AS LAST_VISIT,
    	SUM(SCORE) AS SCORE_SUM,
    	CAST(AVG(SCORE) AS DECIMAL(10,2)) AS SCORE_AVG
    FROM
    	patients
    	LEFT JOIN patients_visits
    		ON patients_visits.PATIENT_ID = patients.PATIENT_ID
    GROUP BY
    	patients.PATIENT_ID,
    	patients.LASTNAME
    ORDER BY
    	patients.PATIENT_ID;
        ''')
    curs.execute('''
SELECT * FROM answer;
        ''')
    conn.commit()
    rows = list(curs.fetchall())
    headers = tuple(d[0] for d in curs.description)
    return [headers] + rows
                 
create_table_headers(conn)
fill_tables(conn, fnames)
result = join_tables_and_group(conn)
for record in result:
    print(f"| {' | '.join(f'{str(r):^10}' for r in record)} |")

```

