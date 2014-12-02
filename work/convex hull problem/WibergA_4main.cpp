

using namespace std;

int matcher(vector<xypoints> theone, xypoints checked)
{
    //A function to check if the point that fits in the convex hull is already in the vector containing the points of the convex hull
    //Precondition: A vector of points for the convex hull containing at least one point and a point to check
    //Postcondition: An integer,  a -1 if the point is already in the convexhull vector a 0 if it is not
    cout<<checked.x<<checked.y<<endl;
    for(int veccheck = 0; veccheck<theone.size(); veccheck++)
    {
        if(theone[veccheck].x  == checked.x && theone[veccheck].y == checked.y)
        {
            return -1;
        }
    }
    return 0;
}

Convexhull::Convexhull(string thename)
{
    //Copy constructor for Convexhull
    //Precondition: Creation of the Convexhull object and setting it equal to a string
    //Postcondition: The object has a filename to look for
    filename = thename;//the file name of the file to be read in
}

Convexhull::~Convexhull()
{
    //Destructor for the Convexhull object
    //Precondition: Convexhull object exists
    //Postcondition: Convexhull object is destroyed

}


void Convexhull::readin()
{
    //A method to readin the sets of points into an array of structs
    //Precondition: A Convexhull object exists and has a filename to check for
    //Postcondition: A full list containing all the points from the file



    int tempcontain; //an integer to contain the data while it is transfer from the file to the different variables

    string infile = filename;

    ifstream fin;

    fin.open(infile.c_str());

    if (fin.fail())
    {
        //A catch if the filename is incorrect or the program can't find it
        cout<<"FATAL ERROR! "<< filename<<" did not open."<<endl;
        exit(-1);
    }

    fin>>tempcontain;

    first = tempcontain; // the length of the list of points


    Allthepoints = new xypoints[first];



    for(int i = 0; i<first; i++)
    {

        fin>>tempcontain;

        Allthepoints[i].x = tempcontain;//inputing the x coordinate of the point

        fin>>tempcontain;

        Allthepoints[i].y =tempcontain;//inputing the y coordinate of the point

    }


    fin.close();


}



void Convexhull::findthehull()
{

    //A method to find all the points in the convex hull of the set of points from the read in file using the brute force algorithm
    //Precondition: The points have been stored in the array
    //Postcondition: The convex hull of the points has been found

    double A;//the A of the equation Ax + By = C
    double B;//the B of the equation Ax + By = C
    double C;//the C of the equation Ax + By = C

    int hullcounter = 0; //iterates through the array the hull to store the info
    int negatory = 0;//counter for the negitives
    int positive = 0;//counts the number of positives
    int itsbeenchecked; // an


    double total;

    for(int h = 0; h<first; h++)
    {

        //first loop pointing to the point to be checked

        for(int r = 0; r<first; r++)
        {

            //loop pointing to the points to be checked against

            if(h != r)
            {
                //if the point is not the same point

              A = Allthepoints[r].y - Allthepoints[h].y;//A for the equation Ax + By = C

              B = Allthepoints[h].x - Allthepoints[r].x;//B for the equation Ax + By = C

              C = Allthepoints[h].x * Allthepoints[r].y - Allthepoints[h].y * Allthepoints[r].x;//C for the equation Ax + By = C
             negatory = 0;//counter for the negitives
            positive = 0;//counts the number of positives
             for(int q = 0; q<first; q++)
             {


                 //For loop to run all the other points given against the line the two points make to see if the line is part of the convex hull

                 if(q != h && q != r)
                 {
                     //A check to make sure that q is not the same point as either r or h

                 int p = 0;
                total = (A*Allthepoints[q].x + B*Allthepoints[q].y) - C;//checking each point against the line
                 }
                if(total < 0)
                {
                    negatory++;//counting the total number of negative results
                }
                else if(total > 0)
                {
                    positive++;//counting the total number of positive results

                }
             }

             if(positive == 0 || negatory == 0)//if statement to check if all the results were positive or negative if they were they are part of the convex hull
             {


                 if(thehull.size()<= 0)
                 {

                     //conditional to check if the vector is empty to avoid checking the list for duplicates
                     thehull.push_back(Allthepoints[h]);
                     hullcounter++;

                     thehull.push_back(Allthepoints[r]);
                     hullcounter++;
                 }

                 itsbeenchecked = matcher(thehull, Allthepoints[h]);//function to check if the point is already in the vector
                 if(itsbeenchecked == 0)
                 {
                     cout<<"gothere"<<endl;
                     thehull.push_back(Allthepoints[h]);
                     hullcounter++;
                 }

                 itsbeenchecked = matcher(thehull, Allthepoints[r]);//checking the point at the other end of the line segment
                 if(itsbeenchecked == 0)
                 {
                     cout<<"gothere"<<endl;
                     thehull.push_back(Allthepoints[r]);
                     hullcounter++;
                 }
                }



             }


            }


        }
    }




void Convexhull::printthehull()
{
    //A method to print the points in the convex hull
    //Precondition: A vector of points in the convex hull
    //Postcondition: Those points in the vector printed to the screen
    for(int printthis = 0; printthis<thehull.size(); printthis++)
    {
        cout<<thehull[printthis].x<<", "<<thehull[printthis].y<<endl;
    }

}
