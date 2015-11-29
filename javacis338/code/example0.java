import java.io.FileReader;
import java.io.IOException;
import java.io.StringWriter;
import java.util.List;

import au.com.bytecode.opencsv.CSVReader;
import au.com.bytecode.opencsv.CSVWriter;

/*
CSV library above is used to handle csv files
You can use this code for dataset reading in all your Data Mining Java programs

This program reads the dataset in CSV format (comma separated values)
and displays it line by line. Each value from dataset has a row and attribute.
For instance row2: attr3=No means that for patient 2 (given by row 2), the attribute 3
(which is SwollenGlands) has value No.
*/

public class example0 {
	private static final String datasetfile="diagnoses.csv";
															// put your dataset file name here
	public static void main(String[] args) throws IOException {
		CSVReader reader = new CSVReader(new FileReader(datasetfile));
		String [] nextLine; // this prepares the reading a line from your dataset
		int i=0;
		while ((nextLine = reader.readNext()) != null) {
                            // this reads a new line from your dataset file
                            // while there are unread lines;
                            // for each line it does what follows
			System.out.print("row"+ i+ ":");
			for(int j=0;j<=6;j++) {
				System.out.print(" attr"+j+"=" + nextLine[j]);
			}
			i++;
			System.out.println();
		}
	}
}