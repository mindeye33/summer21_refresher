#include <iostream>
#include <fstream> 
#include <vector>
#include <Eigen/Dense>

void parse_xyz(std::string &, std::vector<std::vector<double>> &, std::vector<std::string> &);
void keep_carbons(std::vector<std::vector<double>> &, std::vector<std::string> &);
double find_dist(std::vector<double> &, std::vector<double> &);
void find_adjacency(std::vector<std::vector<double>> &, Eigen::MatrixXd &);
void strip_down(Eigen::MatrixXd &, double = 2.0);
void output_csv(std::string &, Eigen::MatrixXd &);


int main(int argc, char *argv[]) {
    std::string infile, outfile;
    try {
        if (argc != 3)
            throw std::exception();
        infile = argv[1];
        outfile = argv[2];
    }
    catch(...) {
        std::cout << "Please specify input xyz and output csv for adjacency" << std::endl; 
        return 0;
    }

    std::vector<std::vector<double>> xyz;
    std::vector<std::string> atom_type;
    parse_xyz(infile, xyz, atom_type);
    keep_carbons(xyz, atom_type);
    int n_cs = xyz.size();    
    
    Eigen::MatrixXd adjacency(n_cs, n_cs);
    find_adjacency(xyz, adjacency);
    std::cout << adjacency << std::endl;
    strip_down(adjacency);
    std::cout << adjacency << std::endl;
    output_csv(outfile, adjacency);
}


void parse_xyz(std::string &infile, std::vector<std::vector<double>> &xyz, std::vector<std::string> &atom_type) {
    std::ifstream xyzstream (infile, std::ifstream::in);
    
    std::string line;
    //std::getline(xyz,line, '\r'); // first line
    //int natoms = std::stod(line); // contains number of atoms
    int natoms;
    xyzstream >> natoms;
    std::getline(xyzstream,line, '\r'); // removes second line (comment line)
    std::getline(xyzstream,line, '\r'); // removes second line (comment line)
    std::vector<double> coords(3);

    atom_type.resize(natoms);
    xyz.resize(natoms);

    for (size_t i = 0; i < natoms; i++){
        xyzstream >> atom_type[i] >> coords[0] >> coords[1] >> coords[2];
        xyz[i] = coords;
    }
}

void keep_carbons(std::vector<std::vector<double>> &xyz, std::vector<std::string> &atom_type) {
    size_t natoms = atom_type.size();     
    std::vector<std::vector<double>> c_xyz;
    for (size_t i = 0; i < natoms; i++) {
        if (atom_type[i] == std::string("C")) 
            c_xyz.push_back(xyz[i]);
    }
    xyz = c_xyz;
}

double find_dist(std::vector<double> &xyz1, std::vector<double> &xyz2) {
    double dist = 0.0;
    for (auto it1 = xyz1.begin(), it2 = xyz2.begin(); (it1 != xyz1.end() || it2 != xyz2.end()) ; it1++, it2++) {
        dist += std::pow(*it1 - *it2, 2);
    }
    return std::sqrt(dist);
}

void find_adjacency(std::vector<std::vector<double>> &xyz, Eigen::MatrixXd &adjacency) { 
    size_t n_cs = xyz.size();
    for (size_t i = 0; i < n_cs; i++) 
        for (size_t j = 0; j < n_cs; j++) {
            adjacency(i,j) = find_dist(xyz[i], xyz[j]);
        }
}

void strip_down(Eigen::MatrixXd &adjacency, double cutoff) {
    assert(adjacency.rows() == adjacency.cols()); // make sure it is square!
    size_t n = adjacency.rows();
    for (size_t i = 0; i < n; i++) 
        for (size_t j = 0; j < n; j++) {
            if (adjacency(i,j) > cutoff) // if far away
                adjacency(i,j) = 0.0; // zero it out
            else if (adjacency(i,j) > 1e-6) // some positive noise
                adjacency(i,j) = 1.0;
        }
}

void output_csv(std::string &outfile, Eigen::MatrixXd &adjacency){
    std::ofstream outstream(outfile.c_str());
    const static Eigen::IOFormat CSVFormat(Eigen::StreamPrecision, Eigen::DontAlignCols, ", ", "\n");
    outstream << adjacency.format(CSVFormat);
}


