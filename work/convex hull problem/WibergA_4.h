/*WibergA_5
*
*A program to find the convex hull of a set of points using the brute force algorithm
*
*Description: A program that allows the user to input a file containing a set of points and find the convex hull of those points
*
*Input:  The user can input the name of a file of points
*
*Output: The output of this program is a list of the points from the file that make up the convex hull in counter-clockwise order
*
*My partner for this project was Aimee Avila
*/
#include <iostream>
#include <string.h>
#include <fstream>
#include <stdlib.h>
#include <iomanip>
#include <time.h>
#include <vector>


using namespace std;

struct xypoints
 {
     //A datastructure to contain the xy points as a pair
      double x;//the x coordinate
      double y;//the y coordinate
};

class Convexhull
{
public:


    Convexhull(){string filename = "";};//Inline default constructor

    Convexhull(string);

    ~Convexhull();


    void readin();

    void findthehull();

    void printthehull();


   protected:
      string filename;//the name of the file
      long first; //The first number in the read in file contains how many points the file contains
      xypoints* Allthepoints; //an array to contain all the xypoint structs
      vector<xypoints> thehull;//The array to contain all the points in the hull
};
