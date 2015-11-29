import java.io.FileReader;
import java.io.IOException;
import java.io.StringWriter;
import java.util.Scanner;
import java.util.List;

import au.com.bytecode.opencsv.CSVReader;
import au.com.bytecode.opencsv.CSVWriter;


// This program reads the dataset, and the new instances.
// Note that an instance is a patient in this example.
// Then the program will compute and display the distances between the new
// instance / patient and all the instances / patients from the dataset, based on symptoms.
// The distance between two instances is defined here as the number of attribute value disparities.
// For instance the distance between two patients is 2 if one has fever and the other doesn't,
// and one has headache and the other doesn't, and all their other symptoms are the same.

public class example1 {

    //here one specifies the file containing the dataset in comma separated values format CSV

	private static final String datasetfile="diagnoses.csv";

	public static void main(String[] args) throws IOException {

        //one declares variables and arrays to be used

		CSVReader reader = new CSVReader(new FileReader(datasetfile)); //this is used to read from CSV file
		String [] nextLine;
		String[][] data= new String[100][7]; //this array will contain the dataset
		String[]  newinstance=new String[7]; //this array will contain a new instance / new patient symptoms
		int[] distance= new int[100];        //this array will contain the distance from the new instance to each instance in the dataset

		String x,y;

		// prepare to read the dataset in array data
		// and then to read a new instance / patient symptos from the keyboard

		int j,i=0;
		while ((nextLine = reader.readNext()) != null) { //while the line inputed is not empty do

			for(j=0;j<=6;j++)
			    data[i][j]=nextLine[j];

			i++;    // this increses i with 1
		}


		//in variable i we counted the number of instances in the dataset plus 1 because
		//the attribute names were also included at the top of the dataset

		int numberOFinstances = i-1;


        //this prepares a loop to input a variable number of new instances and compute thier distances
        //to the dataset instances

		Scanner in =new Scanner(System.in);  // prepare to read new instance from keyboard

		boolean finished=false;   // the next loop should execute until new instances finish

		while (!finished) {

			// Read a new instance (patient symptoms) and put it in an array called newinstance

			System.out.println();
			System.out.println("Input the new patient's 5 symptoms regarding");
			System.out.println("Sore Throat, Fever, Swollen Glands, Congestion, Headache");
			System.out.println("Input Yes or No, ONE PER LINE, CASE SENSITIVE!:");
			System.out.println();

			for(j=1;j<=5;j++)
				newinstance[j]=in.nextLine();

			// Compute the distances from the new instance to each instance in the dataset
			// For example distance[8] should contain the distance from the new instance to instance 8
			// Start with value 0 for all these distances first.

			for(i=1; i<= numberOFinstances; i++)
				distance[i]=0;

			System.out.println();

			for(i=1; i<= numberOFinstances; i++) {
				for(j=1;j<=5;j++) {
					x=newinstance[j];
					y=data[i][j];
					if (x.compareTo(y)!=0)  //if x and y do not coincide
						distance[i]++;      //then add 1 to the distance
				}

           // Now the computed distances are ready, do display them

			System.out.println("The distance between the new patient and patient"+i+" is "+distance[i]);
			}

			// Ask user if new instances are to be inputed.

			System.out.println();
			System.out.print("Any more new patients? y/n: ");
			x=in.nextLine();

			//If the input from user is not "y" (no more new instances) then one should finish the loop.

			if (x.compareTo("y")!=0){
				finished=true;
				System.out.println();
				System.out.println("GOODBYE .........");
			}
		}

	}
}
